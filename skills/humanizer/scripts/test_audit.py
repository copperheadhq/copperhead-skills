#!/usr/bin/env python3
"""Tests for audit.py. Run with: python3 scripts/test_audit.py

Every case here came from a real false positive or false negative. The point of
a checker is that people trust its output, so a rule that fires on correct prose
costs more than a rule that misses one.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from audit import analyse, banned_words  # noqa: E402

BANS = banned_words()
FAILS = []


def check(name, text, key, want):
    got = analyse(text, BANS)[key]
    if isinstance(got, dict):
        got = sum(got.values())
    status = "ok  " if got == want else "FAIL"
    if got != want:
        FAILS.append("%s: %s == %s, wanted %s" % (name, key, got, want))
    print("  %s %-44s %s=%s" % (status, name, key, got))


print("comma splices (must catch lexical verbs, not just auxiliaries)")
check("canonical splice from SKILL.md", "The build failed, we rolled back.", "comma_splices", 1)
check("splice with lexical verb", "The deploy hung, we killed it.", "comma_splices", 1)
check("splice with auxiliary", "The test is slow, it is also flaky.", "comma_splices", 1)
check("leading dependent clause is fine",
      "If you reach for an em dash, you have found a sentence that wanted to be two.",
      "comma_splices", 0)
check("interjection is fine", "Yes, you could just use cron.", "comma_splices", 0)
check("parenthetical is fine", "The migration, they say, went badly.", "comma_splices", 0)
check("relative clause is fine", "We shipped the thing, which nobody reviewed.", "comma_splices", 0)

print("\noxford commas (must not fire on appositives)")
check("real oxford comma", "It was fast, cheap, and wrong.", "oxford_commas", 1)
check("no oxford comma", "It was fast, cheap and wrong.", "oxford_commas", 0)
check("appositive is not a list",
      "Priya, the release manager, and I rolled it back.", "oxford_commas", 0)
check("possessive appositive",
      "Dana, our on-call engineer, and Sam took the page.", "oxford_commas", 0)

print("\nban list: gating tier (never-ship vocabulary and pure filler)")
check("never-ship word is caught", "Let's delve into the tapestry.", "banned_words", 2)
check("six-word hedge is enforced",
      "At the end of the day it shipped.", "banned_words", 1)
check("clean prose is clean", "The queue drains in under a second.", "banned_words", 0)

print("\nban list: reporting tier (sometimes the right word, must not gate)")
check("softer tier reports", "A robust and seamless platform.", "softer_tier", 2)
check("softer tier does not gate", "A robust and seamless platform.", "banned_words", 0)

print("\ntechnical collocations (a checker that rejects correct prose gets switched off)")
check("dynamic programming is exempt",
      "The system uses dynamic programming to drain the queue.", "banned_words", 0)
check("test harness is exempt",
      "The test harness runs on every push.", "banned_words", 0)
check("bare dynamic is still caught",
      "It is a dynamic and evolving product.", "banned_words", 1)
check("bare harness is still caught",
      "We harness the power of the platform.", "banned_words", 1)

print("\nhard rules on clean text")
check("em dashes", "Short sentence. Longer one that carries a clause.", "em_dashes", 0)
check("artifacts", "It's fine, and it stays fine.", "typographic_artifacts", 0)

print()
if FAILS:
    print("%d FAILING:" % len(FAILS))
    for f in FAILS:
        print("  -", f)
    sys.exit(1)
print("all passing")
