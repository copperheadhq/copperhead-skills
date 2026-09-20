# The sprinkles, worked

Each additive move with a before and after. The "before" lines here are already
clean - the machine vocabulary is gone, the shapes are fixed. They're just
anonymous. That's the problem this file solves.

Read the dosage table in SKILL.md before using any of this. Most drafts need two
or three of these moves total, not twelve.

## Specifics with no job to do

Before: *The outage happened during a routine deployment and took several hours
to resolve.*
After: *It went down at 4:15 on a Friday, during a deploy nobody was watching,
and we had it back by nine.*

The Friday does no work. That's why it reads as a memory instead of a summary.
Every detail there has to come from the source. If the source only says "several
hours", you write "several hours" and move on.

## Admitting what you don't know

Before: *The issue was caused by a configuration change that introduced latency
into the request path.*
After: *A config change did it. We still don't know which one - the diff was
forty files and we rolled the whole thing back rather than find out.*

Confidence that varies is a human trait. Confidence that's uniformly high across
every sentence is the tell.

## Taking a side

Before: *There are various approaches to this problem, each with its own merits.*
After: *Use Postgres. The other options work, but you'll spend your weekends on
them.*

## Conceding something real

Before: *While the framework offers significant advantages, teams should consider
the learning curve.*
After: *It'll save you a month of plumbing and cost you two weeks of everyone
being confused. Worth it, barely.*

The fake version weighs and doesn't decide. The real version pays a price and
still commits.

## Naming the reader's objection

Before: *This approach provides several benefits over simpler alternatives.*
After: *Yes, you could do this with a cron job and a shell script. We did, for
two years. It broke every time someone rotated a credential.*

## Deliberate fragments

Before: *The migration completed successfully and the results exceeded our
expectations in every measurable dimension.*
After: *The migration finished Tuesday. Clean. No rollback, no pages, nobody
awake at 3am watching a progress bar.*

## Opening with And, But or So

Before: *However, the underlying problem remained unaddressed.*
After: *But the actual problem was still sitting there.*

## Understatement

Before: *The initial rollout encountered significant difficulties.*
After: *The first rollout went about as well as you'd guess from the fact that
we're on the third.*

## Landing on the strong word

Before: *A single mistyped timestamp cost the team three days.*
After: *The team lost three days to one mistyped timestamp.*

Same facts, same length. The second one ends on "timestamp" and the smallness of
it is the point, so the smallness gets the stress position.

## The callback

Early in a piece: *The scheduler was a shell script named `run.sh` that one
person understood.*

Near the end: *`run.sh` is still in the repo. Nobody's brave enough to delete
it.*

One callback per piece. Two starts to feel like a structure.

## Shifting formality mid-paragraph

Before: *The legacy system has been fully decommissioned and its resources
reallocated.*
After: *The old system is off. Decommissioned, resources reclaimed, the whole
ceremony. It can rot.*

## A full paragraph, all passes

**Raw draft, machine-written:**
> Our team recently embarked on a comprehensive migration journey, transitioning
> our legacy infrastructure to a modern cloud-native architecture. This pivotal
> initiative was not without its challenges, but through meticulous planning and
> robust collaboration, we successfully navigated the complexities and achieved
> significant improvements in both performance and reliability, ultimately
> positioning us for future growth.

**After the cuts only - clean, anonymous:**
> We moved our infrastructure to the cloud. It was difficult, but planning and
> teamwork got us through it, and performance and reliability both improved.

**After the sprinkles:**
> We moved off the old boxes in March. It took five weeks, which was three weeks
> longer than I told everyone it would take, and for eight days in the middle I
> genuinely thought we'd have to roll the whole thing back.
>
> We didn't. p99 went from 400ms to 60 and nobody's been paged at night since.

Count what's in the third version: one specific month, two real numbers, one
admission, one understatement, one fragment-adjacent short sentence to close.
Five moves across seventy words. That's already near the ceiling. A sixth
would start to show.

Every number in it would have to come from the source. If the draft doesn't say
how long it took, the rewrite doesn't either - it says "longer than I promised"
and leaves the slot empty for the writer to fill.
