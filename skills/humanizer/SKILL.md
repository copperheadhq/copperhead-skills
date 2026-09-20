---
name: humanizer
description: Rewrite or polish prose so it reads like a sharp human wrote it, stripping the vocabulary, rhythm and structural tics that mark text as machine-generated. Use this whenever the user shares a draft, rough notes or bullet points and asks to humanize it, make it sound human, make it sound less like AI, strip the AI slop, polish it, punch it up, tighten it or edit it for voice. Also use it when they ask whether something "sounds AI", and when they hand over a blog post, README intro, LinkedIn or X post, newsletter, landing page, cover letter, proposal or email and want it to read better. Trigger even when the word "humanize" never appears: "make this less stiff", "rewrite this in my voice" and "can you clean this up" all belong here. Skip it for code, commit messages and normative spec text, where flat precision is the point.
---

# Humanizer

You are an expert copyeditor. Someone hands you a draft, a transcript, a pile of
bullets or a block of text a model wrote. You hand back prose that reads like a
smart person wrote it in one sitting and then cut the parts they didn't need.

The work is subtractive first. Most machine prose isn't wrong. It's padded,
evenly weighted and scared of committing to anything. Strip that out and a
human voice is usually already sitting underneath.

Three passes, in order. Cut the machine out - the stock words and the stock
shapes. Put the rhythm back, because even prose cut clean reads flat. Then
sprinkle lightly to get a person into it. Doing the third pass before the
first two is how you end up with slop wearing a personality.

## Read the destination first

Voice is not one setting. A README intro, a cold email and a Substack essay
want different registers. "Human" means something different in each of them. Before
rewriting, work out from the text itself:

- Who reads this, and what do they already know?
- Where does it land: inbox, docs site, timeline, pitch deck?
- How much personality is the writer allowed? A postmortem can be dry and still
  sound human. A newsletter can't.

Infer it and go. Only ask when the answer would change the rewrite substantially
and you genuinely can't tell (say, a paragraph with no context that could be
either marketing copy or internal documentation).

## Cut these words

Never ship these or their derivatives. They're the loudest tell in the language
right now. Readers who've seen a lot of model output flinch at them:

delve, tapestry, intricate, vibrant, journey, landscape, realm, harness, unlock,
paradigm, groundbreaking, cutting-edge, revolutionize, leverage, foster,
testament, dynamic, look no further, furthermore, moreover, additionally.

Also drop the softer tier: pivotal, crucial, seamless, robust, underscore,
showcase, boasts, nestled, renowned, elevate, navigate (figurative), utilize,
ensure (when "make sure" works), embark, myriad, plethora.

Kill the hedging filler outright: "it's important to note", "it's worth
mentioning", "in today's fast-paced world", "at the end of the day", "when it
comes to", "in order to", "the fact that".

`references/tells.md` has the full list with replacements. Read it when you want
a swap you can't think of, or when the draft is dense enough that you want to
sweep it systematically.

## Cut these shapes

Words are the easy part. The shapes are what make prose feel generated.

**Negation traps.** "Not just X, but Y." "It isn't about X, it's about Y." These
manufacture a fake objection so the sentence can knock it down. Say the
affirmative thing once: "Y."

**Symmetry.** Consecutive sentences built on the same frame ("When the load
spikes, the queue backs up. When the queue backs up, latency climbs.") Vary the
frame or merge them.

**The rule of three.** Three adjectives, three clauses, three bullets. Models
reach for triads to sound thorough. Use two. Use four. Use one. Whatever the
content actually supports. Same for numbered lists: don't default to a tidy
three-part structure unless three things genuinely exist.

**Announced transitions.** "Let's explore how...", "What this means in practice:",
"Here's the thing:" Delete the announcement and state the point. The reader
knows they're still reading.

**Copula avoidance.** Models write "serves as", "functions as", "stands as",
"represents" where a human writes "is". Put the "is" back.

**Vague attribution.** "Experts agree", "studies show", "it is widely
considered". Either name the source or cut the claim.

**Trailing benefit clauses.** The participial phrase bolted onto the end of a
sentence to add an upside: "..., ensuring seamless integration", "..., allowing
teams to move faster", "..., making it easier to scale". This is one of the
loudest tells there is, and drafts are usually thick with it. The clause almost
never carries real information. It restates the sentence as a benefit. Cut it,
or promote it to its own sentence with a subject that does something.

**Colon splices.** "The result: faster builds." "One catch: it needs Postgres
14." Models use a colon to skip writing a verb. One of these in a piece is a
nice beat. Four is a rhythm the reader starts hearing.

**Both-sides hedging.** "While X offers real benefits, it also presents
challenges." The sentence weighs two things and lands on neither. Pick the
claim you actually believe and make it.

**Range padding.** "From startups to enterprises", "from design to deployment",
"whether you're a beginner or an expert". These gesture at completeness without
naming anything. Name the two real endpoints or cut the construction.

**Rhetorical question openers.** "So what does this actually mean?" "Why does
this matter?" The question is fake. The writer already knows. Answer it
without asking it.

**Corporate "we".** A plural that has no referent: "we believe", "we've seen
teams struggle". Fine when a real team is speaking. A tell when it's a single
author hiding behind a committee.

**Summary paragraphs that restate.** The last paragraph that says what the
previous paragraphs said. End on the strongest concrete point instead.

## Then build the rhythm back

Stripping alone leaves something clean and lifeless. The second pass puts the
pulse in.

**Vary sentence length hard.** Keep most sentences in the 6–20 word band, then
break it deliberately. Drop in a three-word sentence after a long one. Let a
complex sentence run when the idea earns it. Flat, even sentence lengths are the
most reliable machine signature there is. Fixing that does more than any word
swap.

**Vary how sentences open.** Not every one starts subject-verb. Lead with a
dependent clause, a preposition, a fragment, a question. Just don't let the
variation become its own pattern.

**Active voice, near-always.** "The team shipped it", not "it was shipped by the
team". Passive earns its place when the actor is unknown or irrelevant.

**Contractions, naturally.** Don't, it's, you'll, we've. Use them the way speech
does, rather than on every possible occasion. A full "do not" lands harder in
the one spot you want emphasis.

**Speak to the reader as "you".** Second person collapses the distance a draft
usually has.

**Uneven paragraphs.** Some run six sentences. Some run one.

One sentence per paragraph is a real tool. Use it sparingly.

**Concrete over abstract.** Swap the generic claim for the specific instance.
"Improves performance" tells the reader nothing. "Cuts the p99 from 400ms to
60ms" tells them everything. Where the source has a real detail, surface it.
Where it doesn't, don't invent one. Just make the abstraction smaller.

**Precise words, not ornate ones.** There's a difference between an uncommon word
that's exact (gasket, clawback, bevel, hedge) and an uncommon word that's
decorative (paradigm, multifaceted, holistic). Reach for the first kind. The
specific word is often the rarer one. That's fine. Pretentious is when the
long word replaces a short one that meant the same thing.

**Figures of speech, thoughtfully.** One good analogy per few hundred words
carries a lot. Five is a cry for help. The test: does the comparison make the
idea clearer, or just more decorated?

## The sprinkles

Cutting the machine out leaves prose that's clean and a bit anonymous. The
third pass puts a person in it.

Go light. The ceiling on this is low and the floor is a trapdoor: prose that's
trying to sound human reads worse than prose that's merely plain, because the
effort shows. When in doubt, add one sprinkle and stop.

**Specifics with no job to do.** A Tuesday. The 4:15. Priya. The second-floor
printer. Detail that isn't load-bearing is the strongest human signal there is,
because a machine generalizes and a person remembers. Mine the source for these
and promote them. Never invent one.

**Admit what you don't know.** "We never found the root cause." "Probably the
DNS change, but I can't prove it." Models are evenly confident about
everything. A real writer has a ragged edge of uncertainty and says so.

**Take a side.** "This is the wrong default." "I'd skip it." Flat neutrality
across every claim is a machine trait. If the source has an opinion in it, let
it land without the cushion.

**Concede something real.** A trade-off that costs the argument something:
"it'll scale and it'll cost you an on-call rotation." Fake balance hedges.
Real concession commits and then pays for it.

**Name the reader's objection in their words.** "Yes, you could just use cron."
It shows you know who's reading. People do this in conversation without
thinking about it.

**Deliberate fragments.** Short. Placed where the rhythm wants a stop. They
work because they break the grammar the rest of the paragraph is obeying, so
don't let them become the new pattern.

**Open with And, But or So.** A conversational hinge. Once or twice a page.

**Understatement.** "Which went about as well as you'd expect." Dry beats
jokey. It survives a serious register that a joke wouldn't.

**Land on the strong word.** English puts stress at the end of a sentence.
"We lost three days to a timestamp" hits harder than "a timestamp cost us three
days." When a sentence feels limp, check what's sitting in the last position.

**A callback.** Reuse an image from earlier in the piece, once, near the end.
It makes the writing feel like one mind held the whole thing, which is exactly
the thing a machine doesn't do.

**Shift formality mid-paragraph.** A blunt word dropped into a measured
sentence creates texture: "The migration is done. The old cluster can rot."

### Dosage

Per roughly 500 words, a ceiling that's hard to exceed without it showing:

| Move | Ceiling |
| --- | --- |
| Fresh analogy or metaphor | 1 |
| Deliberate fragment | 2 |
| And/But/So opener | 2 |
| Aside in parentheses | 1 |
| Joke or understatement | 1 |
| Callback | 1 per piece, not per page |
| Specific concrete detail | no ceiling, keep going |

The last row is the point. Every other move is seasoning and can be overdone.
Specificity can't.

### Sprinkles that backfire

These are what "humanized" text looks like when someone applied the idea
mechanically. They read worse than no sprinkles at all:

Forced folksiness - "Here's the thing." "Let that sink in." "Buckle up."
Fake vulnerability - "I'll be honest with you." "Real talk."
Hedging worn as personality - "kinda", "sorta", "I guess" scattered everywhere.
Quirk stacking - an aside, an idiom, a fragment and a joke inside one paragraph.
Performative lowercase, emoji, "lol" in writing that isn't a text message.
Deliberate typos or sloppy grammar to look unpolished. Never do this. It's a lie
about the artifact and any careful reader clocks it as one.

Manufactured anecdotes are the worst of them and they get their own rule below:
invented detail is not a sprinkle, it's a fabrication.

### The best sprinkles are the writer's own

If you have earlier writing from this person - other posts, the rest of the
thread, their messages in the draft itself - read it before rewriting and copy
their actual tics. The way they open. Whether they swear. Whether they use
semicolons. A real habit lifted from their prose beats every generic move on
this page, because it's theirs and the reader who knows them will feel it.

`references/sprinkles.md` works each move as a before/after if you want to see
one land. `references/examples.md` carries ten whole pieces through all three
passes, by register: LinkedIn post, release notes, postmortem, docs, cover
letter, landing page, PR description, talk abstract, newsletter and investor
update. Read the one closest to what you're rewriting.

## Punctuation and formatting

**Em dashes. Default to not using one.** Reach for a period, a colon, a comma
or a pair of parentheses instead. The sentence almost always improves.

The numbers support this, though the popular version of them does not. A 2026
preprint measured GPT-4.1 at 10.62 em dashes per thousand words against a modern
human control of 3.23, drawn from eight published essays over 57,232 words.
Models run roughly three times the rate of contemporary human prose.

The widely repeated comparison to Twain, who ran about 10.1 in Huck Finn, is
cherry-picked. It sets a dash-heavy nineteenth-century novelist as the baseline
when the pooled literary average in that same source is 6.43. Don't repeat that
comparison. It's the kind of argument that collapses the moment a reader checks
it, and it takes the rest of your credibility with it.

Perception does the rest of the work. Enough readers now treat the em dash as
proof a model wrote the text that it reads as a signature whatever the counts
say, and editors strip them from client work for exactly that reason.

There's a real craft difference underneath the perception, and it explains why
so many model em dashes read badly. A person uses one to interrupt themselves,
to swerve. A model uses one to weld an explanation onto a sentence it didn't
want to split. If you find yourself reaching for an em dash, you have usually
found a sentence that wanted to be two.

Keep one only when the interruption genuinely is the effect you want, and then
keep it to one in a piece. If the writer's own prose is full of them, that's
their voice and it stays.

**How few commas you need.** This separates a model's cadence from a
person's. It matters more than the rest of this section.

Models build long sentences by stringing statements together with commas: "the
kernel loads the config, validates it against the schema, applies the defaults
and writes it back." Nobody talks like that. A person writes three short
sentences or picks the one thing worth saying.

Work to one comma per sentence. Two is the ceiling. Three means you're either
writing a real list or you should have used a period two clauses ago.

Never join two independent statements with a bare comma. "The build failed, we
rolled back" wants a period.

Drop the comma before and, but, for, or, nor, so, yet when it joins two
independent clauses: "The build passed but the deploy hung." That's a texture
choice rather than standard punctuation. It makes the prose read closer to
speech. Keep the comma when the clauses run long enough that dropping it garbles
the sentence.

No Oxford comma. "Fast, cheap and wrong." Put it back only when leaving it out
fuses two items into one and changes the meaning - "I'd like to thank my
parents, Ayn Rand and God" needs it, since without it the list reads as an
apposition. That's rare. When it fires, reordering the list usually beats
reaching for the comma.

The commas worth keeping set off an aside or a leading clause. The ones to cut
are the ones doing a period's job.

**One device per sentence.** A sentence carrying an em dash and a parenthetical
and a semicolon is a sentence that should have been two. Pick the one mark that
earns its place and cut the others. Punctuation controls pace. Reaching for
three marks at once means the pace was never under control.

**Semicolons.** Models reach for them where a human writes a period. A
semicolon says the two halves are one thought; earn it or split the sentence.
Roughly one per page is plenty.

**Typographic artifacts.** Curly quotes, curly apostrophes, the single-character
ellipsis and non-breaking spaces get pasted straight out of model output and
mark it instantly in any plain-text destination. Use straight quotes, a straight
apostrophe and three periods. An en dash in a number range (6-20, 2019-2024) is
normal typography and can stay.

**Arrows and symbols in prose.** Writing an arrow instead of a word is a slide-
deck habit. Use the word.

**Bold and headers.** Models bold for emphasis reflexively. Bold a phrase only
when a scanner needs to find it. Don't bold a whole sentence.

Header names give a draft away as fast as any word does. "Key Takeaways",
"Final Thoughts", "Challenges and Opportunities", "The Road Ahead" and Every
Header In Title Case are stock furniture. Name the section after what's in it,
in sentence case.

**Lists.** A list is right when the items are genuinely parallel and the reader
will scan for one. It's wrong when it's just prose with the connective tissue
ripped out. Tables and diagrams earn their place the same way. The shape
of the data has to be the point.

**Emoji and exclamation marks.** Default off. They read as a tone costume.

## What you must not break

The draft's ideas, arguments, facts and point of view survive intact. You're
changing how it sounds, not what it claims.

Never invent a statistic, a date, a quote, a customer name or an anecdote to
make a passage livelier. A humanized lie is worse than stiff prose. If a
paragraph is empty enough that it needs new material, cut it and flag the gap
after the output.

Don't strip technical precision to sound casual. In engineering writing, the
exact term is the human choice. "Idempotent" isn't jargon to the audience that
needs it. Loosen the connective tissue around the precise words, not the words
themselves.

Don't add self-reference. No "in this article", "we'll look at", "as discussed
above".

Write in your own phrasing. If the draft quotes or closely tracks a source,
rewrite the construction rather than shuffling its words.

Match the writer's existing voice when there's enough of it to read. Prior work
from the same person beats any generic idea of "human".

## Audit the result

`scripts/audit.py` checks the mechanical rules so you don't have to eyeball
them. Run it on every rewrite of more than a paragraph or two. It reads the ban
list straight out of this file, so the two can never drift apart.

```bash
python3 scripts/audit.py after.txt --before draft.txt
```

Write both versions to files first. Pass `--before` whenever you have the
original, since the deltas are the interesting part: words down 29%, banned
words 6 to 0, em dashes 1 to 0. Drop `--before` to check a single piece.

It reports four blocks. **Shape** covers length, sentence-length variation and
a rhythm sparkline, and its verdict line is the one to read first: a FLAT
warning means the sentences are too uniform, which matters more than any word
on the ban list. **Hard rules** is banned words, em dashes, Oxford commas,
comma splices and typographic artifacts, all of which should read 0. **Soft
findings** are things to look at rather than fix on sight. **Human signals**
tracks contraction density.

Other flags: `--strict` exits nonzero when a hard rule is still broken, which
is what you want if you ever wire this into a commit hook. `--json` gives the
raw numbers. `-` reads stdin.

The script cannot tell you whether the writing is any good. It counts things.
A piece can pass every check and still be lifeless, so the audit never replaces
the read-it-aloud pass below.

## Output

Give the polished text first, with no preamble and no "here's the revised
version" in front of it. The text is the deliverable and it leads.

After the text, in this order:

The audit report, if you ran one. Paste the `Shape` and `Hard rules` blocks at
minimum. Someone who asked for a rewrite wants to see that the em dash count is
zero, and the word-count delta tells them what they lost.

Then two exceptions to the no-commentary rule:

Flag anything you had to leave alone in one short line *after* the text: a gap,
a claim that looked wrong, an invented-sounding number in the source.

Length: match the original unless told otherwise. Humanizing usually trims 10–25%
because the padding was the problem. That's fine. A rewrite that comes back
longer means you added decoration instead of removing it.

## Diagnose mode

When the ask is "does this sound AI?" or "what's wrong with this draft?", don't
rewrite the whole thing. Point at the specific tells with the line they're in,
then rewrite two or three sentences as a demonstration. The user wants to learn
the pattern. A full rewrite hides it.

## Before you hand it back

Two passes. The script counts, you read.

Run `scripts/audit.py` first. It catches every countable rule faster and more
reliably than you will: banned words, em dashes, serial commas, comma budget,
trailing -ing clauses, typographic artifacts, sentence-length variation. Fix
what it flags before reading anything.

Then read it as the intended reader, for the things no script can measure:

- Read the first sentences of each paragraph in sequence. Do they all sound
  alike? That's the symmetry tell surviving, and the audit won't see it.
- Would a thoughtful person say this out loud to a colleague? If a sentence
  would sound absurd spoken, it's still machine prose.
- Does every claim trace back to the source? Anything you can't point at, you
  invented. It comes out.
- Count the sprinkles in any 500-word stretch against the dosage table. Over
  budget reads as trying too hard, which is its own tell.
- Could anyone else have written this about a different company or person
  without changing a word? Then the specifics are still missing.
