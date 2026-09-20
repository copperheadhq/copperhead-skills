#!/usr/bin/env python3
"""Audit prose against the humanizer's rules and report what changed.

    audit.py after.txt                  check one file
    audit.py --before a.txt after.txt   check, and diff the stats against the draft
    cat draft | audit.py -              read stdin
    audit.py after.txt --json           machine-readable
    audit.py after.txt --strict         exit 1 if any hard rule is still broken

The banned vocabulary is parsed out of SKILL.md rather than copied here, so the
skill stays the only place the list lives. Everything else is stdlib.
"""

import argparse
import json
import re
import statistics
import sys
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent / "SKILL.md"

# Hard rules: these fail --strict. Soft findings are reported but don't fail.
HARD = {"banned_words", "em_dashes", "oxford_commas", "typographic_artifacts",
        "comma_splices"}


# ---------------------------------------------------------------- parsing

# Real technical uses of words that are slop everywhere else. A checker that
# rejects "dynamic programming" or "test harness" gets switched off, and a
# checker nobody runs is worth nothing.
COLLOCATIONS = [
    "dynamic programming", "dynamic typing", "dynamic range", "dynamic import",
    "dynamic linking", "test harness", "wiring harness", "cable harness",
    "landscape orientation", "robust statistics", "robust regression",
]


def banned_words(skill_md=SKILL, tier="all"):
    """Pull the ban list out of 'Cut these words' in SKILL.md, keeping its tiers.

    The section has three paragraphs and the distinction between them matters.
    The first is never-ship vocabulary and the third is pure filler, so both
    gate. The second is the softer tier, where the word is sometimes the right
    one, so it reports without failing --strict.
    """
    try:
        text = skill_md.read_text(encoding="utf-8")
    except OSError:
        return []
    m = re.search(r"^## Cut these words\s*$(.*?)^## ", text, re.S | re.M)
    if not m:
        return []

    tiers = []
    for para in m.group(1).split("\n\n"):
        para = " ".join(para.split())
        if not para or para.startswith(("`", "-", "|", "**")):
            continue
        softer = para.lower().startswith("also drop the softer tier")
        if ":" in para:
            para = para.split(":", 1)[1]
        para = re.sub(r"\([^)]*\)", " ", para)
        words = set()
        for chunk in re.split(r"[,.]", para):
            chunk = chunk.strip().strip('"\u201c\u201d').lower()
            if not chunk or len(chunk) > 40 or len(chunk.split()) > 7:
                continue
            if re.fullmatch(r"[a-z][a-z '-]*", chunk):
                words.add(chunk)
        if words:
            tiers.append(("soft" if softer else "hard", words))

    hard = sorted(set().union(*[w for t, w in tiers if t == "hard"]) if tiers else set())
    soft = sorted(set().union(*[w for t, w in tiers if t == "soft"]) if tiers else set())
    soft = [w for w in soft if w not in hard]
    if tier == "hard":
        return hard
    if tier == "soft":
        return soft
    return sorted(set(hard) | set(soft))


def count_banned(body_low, words):
    """Count banned terms, skipping ones inside a legitimate technical phrase."""
    found = {}
    for w in words:
        n = len(re.findall(r"\b" + re.escape(w) + r"\w{0,3}\b", body_low))
        if not n:
            continue
        for phrase in COLLOCATIONS:
            if w in phrase:
                n -= body_low.count(phrase)
        if n > 0:
            found[w] = n
    return found


def sentences(text):
    text = re.sub(r"\s+", " ", strip_markup(text))
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z0-9\"'(])", text)
    return [p.strip() for p in parts if p.strip()]


def strip_markup(text):
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = re.sub(r"`[^`]*`", " ", text)
    text = re.sub(r"^\s*[|#>].*$", " ", text, flags=re.M)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    return re.sub(r"[*_]{1,3}", "", text)


def paragraphs(text):
    return [p for p in re.split(r"\n\s*\n", text.strip()) if p.strip()]


# ---------------------------------------------------------------- checks

IRREGULAR = ("done born given taken seen made held kept left told sent built "
             "found shown known written spoken driven chosen").split()
PASSIVE = re.compile(
    r"\b(?:am|is|are|was|were|be|been|being)\b\s+(?:\w+ly\s+)?"
    r"(?:\w+ed|" + "|".join(IRREGULAR) + r")\b", re.I)
CONTRACTION = re.compile(r"\b\w+'(?:s|t|re|ve|ll|d|m)\b", re.I)
TRAILING_ING = re.compile(r",\s+(?:ensuring|allowing|making|enabling|providing|"
                          r"helping|creating|offering|delivering|driving)\b", re.I)
NEGATION_TRAP = re.compile(r"\b(?:not just|isn't just|it's not|it isn't|rather than just)\b"
                           r"[^.!?]{0,60}\b(?:but|it's)\b", re.I)
OXFORD = re.compile(r"\w+,\s+(\w[\w\s]*?),\s+(?:and|or)\s+\w")
# A middle segment opening with a determiner is an appositive, not a list item.
DETERMINER = re.compile(r"^(?:the|a|an|my|our|your|his|her|its|their)\b", re.I)


def oxford_commas(body):
    return sum(1 for m in OXFORD.finditer(body) if not DETERMINER.match(m.group(1)))
SUBJECT = r"(?:it|he|she|they|we|you|i|there|this|that)"
# After a subject pronoun the next word is normally the verb, so a comma
# followed by pronoun + word is a splice. The exclusions are the cases where
# the pronoun is not starting a new clause.
NOT_A_VERB = {"and", "or", "but", "nor", "so", "yet", "who", "which", "that",
              "whom", "whose", "too", "also", "as", "then", "either", "neither"}
COMMA_SPLICE = re.compile(r",\s+" + SUBJECT + r"\s+([a-z']+)(\s*,)?", re.I)
# A sentence opening with one of these has a leading dependent clause, so the
# comma is doing its job rather than splicing two independent statements.
SUBORDINATOR = re.compile(
    r"^\W*(?:if|when|whenever|because|although|though|while|since|after|before|"
    r"unless|until|whereas|as|once|given|assuming|where|yes|no|well|sure|right|"
    r"okay|ok|first|second|then|still|instead|otherwise)\b", re.I)


def comma_splices(sents):
    n = 0
    for sent in sents:
        if SUBORDINATOR.match(sent):
            continue
        for m in COMMA_SPLICE.finditer(sent):
            word, trailing_comma = m.group(1).lower(), m.group(2)
            # ", they say," is a parenthetical, not a splice.
            if trailing_comma:
                continue
            if word in NOT_A_VERB:
                continue
            n += 1
            break
    return n
ARTIFACTS = {"curly apostrophe": "’", "curly quote": "“",
             "curly quote close": "”", "ellipsis char": "…",
             "non-breaking space": " "}
HEDGES = ["it's important to note", "it's worth mentioning", "it should be noted",
          "in today's", "at the end of the day", "when it comes to", "in order to",
          "the fact that", "needless to say", "that being said", "let's dive",
          "let's explore", "in conclusion", "look no further"]
STOCK_HEADERS = ["key takeaways", "final thoughts", "the road ahead", "wrapping up",
                 "challenges and opportunities", "the bottom line", "what's next"]


def analyse(text, bans):
    body = strip_markup(text)
    sents = sentences(text)
    lens = [len(s.split()) for s in sents]
    words = len(body.split())
    low = body.lower()

    hard_list = banned_words(tier="hard")
    found = count_banned(low, [w for w in bans if w in hard_list])
    found_soft = count_banned(low, [w for w in bans if w not in hard_list])

    arts = {name: body.count(ch) for name, ch in ARTIFACTS.items() if ch in body}
    hedge_hits = {h: low.count(h) for h in HEDGES if h in low}
    header_hits = [h for h in STOCK_HEADERS if h in low]
    commas_per = [s.count(",") for s in sents]

    return {
        "words": words,
        "sentences": len(sents),
        "paragraphs": len(paragraphs(text)),
        "mean_sentence": round(statistics.mean(lens), 1) if lens else 0,
        "sentence_stdev": round(statistics.pstdev(lens), 1) if len(lens) > 1 else 0.0,
        "shortest": min(lens) if lens else 0,
        "longest": max(lens) if lens else 0,
        "lengths": lens,
        "para_lengths": [len(sentences(p)) for p in paragraphs(text)],
        "banned_words": found,
        "softer_tier": found_soft,
        "em_dashes": body.count("—"),
        "oxford_commas": oxford_commas(body),
        "comma_splices": comma_splices(sents),
        "commas_over_budget": sum(1 for c in commas_per if c >= 3),
        "max_commas_in_sentence": max(commas_per) if commas_per else 0,
        "semicolons": body.count(";"),
        "typographic_artifacts": arts,
        "passive": len(PASSIVE.findall(body)),
        "contractions": len(CONTRACTION.findall(body)),
        "trailing_ing": len(TRAILING_ING.findall(body)),
        "negation_traps": len(NEGATION_TRAP.findall(body)),
        "hedges": hedge_hits,
        "stock_headers": header_hits,
        "exclamations": body.count("!"),
    }


# ---------------------------------------------------------------- report

BLOCKS = " ▁▂▃▄▅▆▇█"


def spark(values, buckets=24):
    if not values:
        return ""
    lo, hi = min(values), max(values)
    span = (hi - lo) or 1
    vals = values[:buckets]
    return "".join(BLOCKS[min(8, int((v - lo) / span * 8) + 1)] for v in vals)


def burstiness_verdict(stdev, mean):
    if mean == 0:
        return "no text"
    ratio = stdev / mean
    if ratio < 0.35:
        return "FLAT - sentences are too uniform, this is the loudest tell"
    if ratio < 0.5:
        return "low - break one long sentence, stretch another"
    if ratio > 1.1:
        return "very high - check it still reads smoothly"
    return "good"


def delta(after, before, key, lower_is_better=True):
    if before is None:
        return ""
    a, b = after[key], before[key]
    if isinstance(a, dict):
        a, b = sum(a.values()), sum(b.values())
    if a == b:
        return "  (no change)"
    arrow = "down" if a < b else "up"
    good = (a < b) == lower_is_better
    return "  (%s from %s, %s)" % (arrow, b, "better" if good else "worse")


def report(after, before=None):
    out = []
    w = out.append
    w("=" * 64)
    w("HUMANIZER AUDIT")
    w("=" * 64)

    w("")
    w("SHAPE")
    if before:
        pct = ((after["words"] - before["words"]) / before["words"] * 100) if before["words"] else 0
        w("  words            %-6d (was %d, %+.0f%%)" % (after["words"], before["words"], pct))
    else:
        w("  words            %d" % after["words"])
    w("  sentences        %d in %d paragraphs" % (after["sentences"], after["paragraphs"]))
    w("  sentence length  mean %s, range %d-%d" % (
        after["mean_sentence"], after["shortest"], after["longest"]))
    w("  variation        stdev %s  %s" % (
        after["sentence_stdev"], burstiness_verdict(after["sentence_stdev"], after["mean_sentence"])))
    if after["lengths"]:
        w("  rhythm           %s" % spark(after["lengths"]))
    if after["para_lengths"]:
        w("  paragraphs       %s sentences each" % "/".join(map(str, after["para_lengths"][:14])))

    w("")
    w("HARD RULES")
    rows = [
        ("banned words", sum(after["banned_words"].values()), delta(after, before, "banned_words")),
        ("em dashes", after["em_dashes"], delta(after, before, "em_dashes")),
        ("oxford commas", after["oxford_commas"], delta(after, before, "oxford_commas")),
        ("comma splices", after["comma_splices"], delta(after, before, "comma_splices")),
        ("typographic artifacts", sum(after["typographic_artifacts"].values()),
         delta(after, before, "typographic_artifacts")),
    ]
    for label, n, d in rows:
        w("  %-22s %-4d %s%s" % (label, n, "ok" if n == 0 else "FIX", d))
    if after["banned_words"]:
        w("    still present: %s" % ", ".join(
            "%s x%d" % (k, v) for k, v in sorted(after["banned_words"].items())))
    if after["typographic_artifacts"]:
        w("    artifacts: %s" % ", ".join(
            "%s x%d" % (k, v) for k, v in after["typographic_artifacts"].items()))

    w("")
    w("SOFT FINDINGS")
    soft = [
        ("sentences with 3+ commas", after["commas_over_budget"], "chaining statements"),
        ("trailing -ing clauses", after["trailing_ing"], "', ensuring...' constructions"),
        ("negation traps", after["negation_traps"], "'not just X, but Y'"),
        ("passive constructions", after["passive"], "prefer active"),
        ("semicolons", after["semicolons"], "one per page is plenty"),
        ("softer-tier words", sum(after["softer_tier"].values()), "sometimes the right word"),
        ("hedging phrases", sum(after["hedges"].values()), "filler"),
        ("stock headers", len(after["stock_headers"]), "rename them"),
        ("exclamation marks", after["exclamations"], "default off"),
    ]
    for label, n, note in soft:
        flag = "   " if n == 0 else " ->"
        w("%s %-26s %-4d %s" % (flag, label, n, note if n else ""))
    if after["softer_tier"]:
        w("    softer tier: %s" % ", ".join(
            "%s x%d" % (k, v) for k, v in sorted(after["softer_tier"].items())))
    if after["hedges"]:
        w("    hedges: %s" % ", ".join(sorted(after["hedges"])))
    if after["stock_headers"]:
        w("    headers: %s" % ", ".join(after["stock_headers"]))

    w("")
    w("HUMAN SIGNALS")
    w("  contractions     %d%s" % (after["contractions"], delta(after, before, "contractions", False)))
    per_100 = after["contractions"] / after["words"] * 100 if after["words"] else 0
    w("  density          %.1f per 100 words %s" % (
        per_100, "(low, sounds formal)" if per_100 < 0.8 else "(fine)"))

    hard_fails = sum(1 for k in HARD
                     if (sum(after[k].values()) if isinstance(after[k], dict) else after[k]))
    w("")
    w("=" * 64)
    w("VERDICT: %s" % ("clean on every hard rule" if hard_fails == 0
                       else "%d hard rule%s still broken" % (hard_fails, "" if hard_fails == 1 else "s")))
    w("=" * 64)
    return "\n".join(out), hard_fails


# ---------------------------------------------------------------- cli

def read(path):
    if path == "-":
        return sys.stdin.read()
    try:
        return Path(path).read_text(encoding="utf-8")
    except FileNotFoundError:
        sys.exit("audit: no such file: %s" % path)
    except OSError as exc:
        sys.exit("audit: cannot read %s: %s" % (path, exc))


def main(argv=None):
    ap = argparse.ArgumentParser(description="Audit prose against the humanizer's rules.")
    ap.add_argument("after", help="the rewritten text, or - for stdin")
    ap.add_argument("--before", help="the original draft, to show the delta")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--strict", action="store_true", help="exit 1 if a hard rule is broken")
    args = ap.parse_args(argv)

    bans = banned_words()
    after = analyse(read(args.after), bans)
    before = analyse(read(args.before), bans) if args.before else None

    if args.json:
        print(json.dumps({"after": after, "before": before}, indent=2))
        hard = sum(1 for k in HARD
                   if (sum(after[k].values()) if isinstance(after[k], dict) else after[k]))
    else:
        text, hard = report(after, before)
        print(text)

    return 1 if (args.strict and hard) else 0


if __name__ == "__main__":
    sys.exit(main())
