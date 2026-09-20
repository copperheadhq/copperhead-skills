# Worked rewrites, by register

Ten full pieces, each one taken from machine draft to finished text. The atomic
repairs live in `tells.md` and the additive moves live in `sprinkles.md`. This
file is for seeing a whole piece move.

The numbers and names in the "after" columns are invented, because these samples
have no source behind them. In real work every specific has to come from the
draft or from the writer. Inventing one is the single rule this skill will not
bend on.

Every rewrite here obeys the house style: no em dash, no Oxford comma, roughly
one comma per sentence, active voice.

## 1. LinkedIn post

**Before**
> I'm thrilled to announce that after an incredible journey, I'm embarking on a
> new chapter as Senior Engineer at Acme! This opportunity represents a pivotal
> moment in my career, and I'm excited to leverage my skills to drive meaningful
> impact. Huge thanks to my amazing mentors who believed in me. Here's to new
> beginnings!

**After**
> New job. I start at Acme on Monday, working on their billing system.
>
> I applied in January and got rejected. Applied again in June for a different
> team and got it. If you're in the middle of a job search and something just
> fell through, that's the whole story: I sent the second application four days
> after the first rejection email.
>
> Thanks to Dana for the referral both times.

What moved: the announcement got shorter and the useful part got longer. The
original had one fact in it. The rewrite has four, and one of them is something
a reader can actually use.

## 2. Release notes

**Before**
> This release introduces a host of powerful enhancements designed to
> significantly improve your workflow. We've revolutionized our search
> capabilities, delivering lightning-fast results, and introduced a suite of new
> integrations that seamlessly connect with your favorite tools.

**After**
> Search is faster. Queries that took two seconds now take under 200ms, because
> we stopped rebuilding the index on every write.
>
> Three new integrations: Linear, Notion and PagerDuty.
>
> One thing to know before you upgrade. The `/v1/search` response now returns
> `matches` where it used to return `results`. The old key stays until March.

What moved: "lightning-fast" became a number. The breaking change, which the
original buried by not mentioning it, got its own paragraph at the end where
people actually look.

## 3. Incident postmortem, customer-facing

**Before**
> We want to acknowledge the service disruption that impacted some users
> yesterday. Our team worked diligently to restore functionality, and we deeply
> apologize for any inconvenience this may have caused. We remain committed to
> providing a reliable experience and have implemented measures to prevent
> similar occurrences.

**After**
> We were down for 52 minutes yesterday, from 2:14pm to 3:06pm UTC. If you tried
> to check out in that window, your cart went through but you didn't get a
> confirmation email. Those went out overnight.
>
> A config push set the database connection pool to 5 instead of 500. It passed
> review because the diff looked like a typo fix.
>
> We've added a bound on that value so the same change can't deploy again. That
> doesn't fix the review process, which is the real problem, and we don't have a
> good answer for it yet.

What moved: "some users" became a timestamp and a specific symptom. The apology
came out entirely, replaced by information, which is what an apology is for. The
last line admits an open problem rather than closing with a reassurance.

## 4. Technical documentation

**Before**
> To get started with the CLI, users should first ensure that they have properly
> configured their environment. Once the prerequisites have been satisfied, the
> initialization command can be executed, which will generate the necessary
> configuration files.

**After**
> Install it, then run `acme init` in your project root. It writes an
> `acme.toml` you'll want to commit.
>
> `init` needs a `$ACME_TOKEN` in your environment. If it's missing you'll get a
> 401 that says `unauthorized` and nothing else, which is unhelpful, and we know.

What moved: passive to imperative, which is what documentation wants. The
rewrite also names the confusing error the reader will actually hit, which the
original would never have done because it was describing an ideal path.

## 5. Cover letter

**Before**
> I am writing to express my strong interest in the Backend Engineer position at
> your esteemed organization. With over five years of experience in developing
> scalable solutions, I am confident that my skills align well with your
> requirements. I am passionate about leveraging technology to solve complex
> problems.

**After**
> I'd like the Backend Engineer job. I've spent five years on payment systems,
> the last two at Stripe scale, though at a much smaller company than Stripe.
>
> Your posting says the hard part is reconciliation across three providers. I
> did exactly that at Volt, badly the first time. The second design held for two
> years and I can walk you through what changed between them.

What moved: "passionate about leveraging technology" is a sentence that fits any
job at any company. The rewrite names one problem from their posting and one
failure from the writer's own history. Admitting the first attempt was bad is
the most credible line in it.

## 6. Landing page

**Before**
> Transform your workflow with our cutting-edge platform. Designed for modern
> teams, our solution seamlessly integrates with your existing tools to unlock
> unprecedented productivity gains. Join thousands of satisfied customers who
> have revolutionized the way they work.

**After**
> Your on-call engineer gets paged at 3am. She opens her laptop, and the graph
> she needs is four dashboards deep.
>
> We put it on the first one.
>
> Works with Datadog, Grafana and whatever you built yourself in 2019.

What moved: the original described the product. The rewrite describes the
reader's night. "Thousands of satisfied customers" went out because it's
unverifiable and everyone writes it.

## 7. Pull request description

**Before**
> This PR implements a comprehensive refactoring of the authentication module to
> improve maintainability and reduce technical debt. The changes encompass
> several key areas and should result in a more robust and scalable
> implementation going forward.

**After**
> Splits `auth.py` into `auth/tokens.py` and `auth/sessions.py`. No behavior
> changes, and the tests are untouched to prove it.
>
> The two things were tangled because session refresh reached into the token
> parser directly. There's now a function boundary between them.
>
> Review note: the diff looks bigger than it is. Most of it is the file move.

What moved: a reviewer can now tell what to look at and what to skip. The
original could describe almost any refactor ever written.

## 8. Conference talk abstract

**Before**
> In this talk, we will delve into the intricate challenges of distributed
> systems at scale. Attendees will gain valuable insights into best practices
> and learn how to harness modern tooling to build resilient architectures.

**After**
> We ran one Postgres instance until it held 4TB and served 60,000 writes a
> second. Everyone told us to shard two years before we did.
>
> This talk is about why we waited, what actually broke first (not what we
> expected), and the three months after that when the migration went sideways.
>
> You'll leave knowing when your own single instance is genuinely out of room,
> which is later than most people think.

What moved: "valuable insights" became a claim someone could disagree with. A
talk abstract has to make a programme committee choose it over forty others, and
nothing generic survives that.

## 9. Newsletter opener

**Before**
> Welcome back to another edition of our newsletter! This week, we're diving into
> some fascinating developments in the world of AI. As always, we've curated the
> most important stories so you don't have to. Let's get into it!

**After**
> Two things this week. A small model beat a large one on a benchmark that
> matters, and nobody can reproduce it.
>
> I spent Thursday trying. Notes below, including the part where I wasted four
> hours on a tokenizer version mismatch.

What moved: the welcome, the "let's get into it" and the "so you don't have to"
all went out. They're throat-clearing. The rewrite opens on the actual news.

## 10. Investor update

**Before**
> Q3 was a period of substantial growth and momentum for the company. We
> successfully onboarded several key accounts and continued to iterate on our
> product roadmap. While we faced some headwinds in the market, we remain
> confident in our trajectory heading into Q4.

**After**
> Revenue went from 180k to 240k MRR. Four new accounts, one of them 30k on its
> own, which makes the number look better than the quarter was.
>
> We lost Brightside in August. Their new CTO consolidated onto a competitor and
> we didn't see it coming, which is the part that concerns me.
>
> Q4 plan: two engineers on the enterprise SSO work that Brightside asked for and
> we deprioritized. Draw your own conclusion about the timing.

What moved: "headwinds" became a named churned customer. The rewrite volunteers
the bad news and flags that one account is flattering the growth figure, which
is the thing an investor would otherwise find on their own and trust you less
for hiding.

## The pattern across all ten

Every "before" is describable in one sentence: it could have been written about
a different company, a different product or a different person without changing
a word. Every "after" could only have been written about this one.

That's the test to carry into a rewrite. Not "does this sound human" but "could
anyone else have written this?" If the answer is yes, the specifics are missing,
and no amount of contractions or short sentences will fix it.
