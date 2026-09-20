# The full tell list

Load this when you want a replacement you can't think of, or when a draft is
dense enough to sweep systematically. Contents:

1. Word swaps
2. Phrase deletions
3. Sentence-shape repairs
4. Worked examples across registers
5. Why the ban list keeps moving

---

## 1. Word swaps

Left column out, right column in. The right column is a starting point, not a
lookup table. The best replacement depends on the sentence. Sometimes the
answer is to delete the word and rebuild the clause.

| Instead of | Write |
|---|---|
| delve into | dig into, study, go through |
| tapestry, mosaic (figurative) | mix, range, or name the parts |
| intricate | complicated, detailed, fiddly |
| vibrant | busy, loud, crowded (or cut) |
| journey (figurative) | path, process, or cut |
| landscape, realm, sphere, space (figurative) | field, market, world, or name it |
| harness, unlock, tap into | use, get at, open up |
| paradigm, paradigm shift | model, approach, big change |
| groundbreaking, cutting-edge, game-changing | new, first, or state the specific advance |
| revolutionize, transform | change, rebuild, replace |
| leverage (verb) | use, apply, build on |
| foster, cultivate | build, grow, encourage |
| testament to | shows, proves |
| dynamic (adjective) | fast-moving, shifting, or cut |
| furthermore, moreover, additionally | also, and, plus (or start the sentence clean) |
| pivotal, crucial, vital, key | important, or cut the intensifier |
| seamless, frictionless | smooth, quick, invisible |
| robust | solid, reliable, holds up |
| underscore, highlight, showcase | show, point to, prove |
| boasts, features | has |
| nestled | sits, is |
| renowned, acclaimed, esteemed | well-known, or name why |
| elevate | raise, improve, lift |
| navigate (figurative) | handle, work through, get past |
| utilize | use |
| ensure | make sure, guarantee |
| embark on | start, begin |
| myriad, plethora, vast array | many, lots of, a pile of |
| meticulous | careful, exact |
| profound | deep, big, or cut |
| comprehensive | complete, full, thorough |
| innovative | new, unusual, or say what's new |
| streamline | simplify, speed up, cut steps |
| empower, enable | let, help, give |
| resonate with | land with, ring true for |
| align with | match, fit, agree with |
| holistic, multifaceted | whole, broad, or name the sides |
| serves as, functions as, stands as | is |
| in order to | to |
| due to the fact that | because |
| a wide range of | many, or name them |
| it is important to note that | (delete) |
| when it comes to | for, with, in (or restructure) |

## 2. Phrase deletions

Cut these whole. They add length and no information.

- "In today's fast-paced world" / "In an increasingly digital age"
- "At the end of the day"
- "It's worth mentioning that" / "It should be noted that"
- "Needless to say"
- "The fact of the matter is"
- "One of the most important things to consider"
- "Whether you're X or Y" (the universal-audience opener)
- "In conclusion" / "To sum up" / "In summary"
- "Let's dive in" / "Let's explore" / "Let's take a look at"
- "That being said" (use "still", "but", or nothing)
- "Ultimately" as a paragraph opener
- "This begs the question" (usually also misused)
- "Here's the thing:"
- "Trust me" / "Believe it or not"
- "In the world of X" openers
- "Think of it like..." as an analogy preamble
- "The short answer is" / "The long answer is"
- "Gone are the days when"
- "More than ever before"
- "Countless" (as a stand-in for a number you don't have)

### Stock section headers

Rename these. They're furniture, not headings:

"Key Takeaways", "Final Thoughts", "Wrapping Up", "The Bottom Line",
"Challenges and Opportunities", "Benefits and Drawbacks", "The Road Ahead",
"What's Next", "Getting Started" (when nothing starts), "Understanding X",
"Why X Matters", "A Deeper Look".

Also drop Title Case. Sentence case reads like a person wrote it.

## 3. Sentence-shape repairs

**Negation trap.**
Before: *It's not just a database, it's a coordination layer.*
After: *It's a coordination layer that happens to store things.*

**Parallel frames.**
Before: *When traffic rises, latency follows. When latency rises, retries follow.
When retries rise, the system collapses.*
After: *Traffic rises, latency follows and the retries pile on until the whole
thing falls over.*

**Rule of three.**
Before: *The tool is fast, flexible, and intuitive.*
After: *The tool is fast and you can bend it into shapes it wasn't designed for.*

**Announced transition.**
Before: *What this means in practice is that teams ship faster.*
After: *Teams ship faster.*

**Copula avoidance.**
Before: *The registry serves as the single source of truth for constraints.*
After: *The registry is the only place constraints live.*

**Vague attribution.**
Before: *Studies show that shorter sentences improve comprehension.*
After: *Cut the sentence in half and people read it faster.* (or cite the study)

**Trailing benefit clause.**
Before: *The kernel validates each transaction before commit, ensuring data
integrity and allowing teams to move quickly.*
After: *The kernel validates each transaction before commit. Nothing bad gets in,
so nobody has to review the graph by hand later.*

**Colon splice pile-up.**
Before: *The problem: latency. The cause: retries. The fix: a circuit breaker.*
After: *Latency was the problem and retries were causing it, so we put a circuit
breaker in front.*

**Both-sides hedge.**
Before: *While microservices offer scalability benefits, they also introduce
operational complexity.*
After: *Microservices will scale and they'll cost you an on-call rotation.*

**Range padding.**
Before: *Used by everyone from indie developers to Fortune 500 enterprises.*
After: *Used by a two-person shop in Lisbon and by Cisco.*

**Rhetorical question opener.**
Before: *So why does any of this matter? Because latency compounds.*
After: *Latency compounds.*

**Restating summary.**
Before: *As we've seen, the three factors above all contribute to the outcome.*
After: (delete, and let the last real point close the piece)

**Evenly weighted list-prose.**
Before: *The system handles authentication. The system handles routing. The
system handles logging.*
After: *It does auth, routing and logging. Three jobs that should probably live
in three services.*

## 4. Worked examples across registers

### Technical README intro

**Before**
> Fang is a comprehensive hardware kernel that empowers engineers to leverage a
> single canonical model for their designs. By harnessing a validated transaction
> system, it ensures that every change is thoroughly verified before being
> committed, fostering a robust and reliable workflow. Whether you're designing a
> simple sensor board or an intricate multi-rail system, Fang provides the tools
> you need.

**After**
> Fang holds your hardware design as one typed graph and refuses to change it
> until the change checks out. Every edit goes in as a transaction. The kernel
> applies it to a copy, runs the gate and either advances the head or hands you
> back the reason it didn't.
>
> That's the whole idea. One model, one place it lives and no way to move it
> sideways.

Notice what survived: the actual mechanism. Notice what went: "comprehensive",
"empowers", "leverage", "harnessing", "fostering", "robust", the whether-you're
opener and the closing sentence that promised tools without naming one.

### Cold email

**Before**
> I hope this email finds you well. I wanted to reach out regarding a potential
> opportunity for collaboration. Our platform leverages cutting-edge AI to
> streamline your workflow and unlock new efficiencies for teams like yours. I'd
> love to hop on a quick call to explore how we might be able to help.

**After**
> Quick one. You mentioned on the Rails podcast that your test suite takes 40
> minutes. We cut that to six for two teams your size, both on similar Postgres
> setups.
>
> Worth 15 minutes? I can show you the before-and-after from the closer of the two.

The rewrite invents specifics here only because the example needs them. In real
work you'd pull them from the source or ask. Never fabricate.

### Personal essay / newsletter

**Before**
> Learning to code was a transformative journey that taught me invaluable lessons
> about perseverance and problem-solving. Throughout this process, I discovered
> that the most crucial skill isn't technical proficiency but rather the ability
> to embrace failure as a stepping stone to growth.

**After**
> I spent four months on my first real program and most of it was wrong. The part
> nobody tells you: that's the job. You write something broken, you find out how
> it's broken, you fix that and it breaks somewhere else.
>
> The coding got easier. Being wrong all day never really did.

### Internal status update (where dry is correct)

**Before**
> The migration effort is currently progressing well. We have successfully
> completed the initial phase and are now transitioning into validation. Some
> challenges have been encountered with respect to data consistency, but the team
> is actively working to resolve these issues.

**After**
> Migration's about two-thirds done. Phase one shipped Tuesday, validation starts
> this week.
>
> We hit a data consistency problem on the orders table. Roughly 8,000 rows have
> timestamps that don't match the source. Priya's writing a reconciliation script.
> It'll cost us maybe three days, not more.

Human doesn't mean chatty. This version is shorter, flatter and more useful. The
difference is that it commits to numbers and names instead of "progressing well".

## 5. Why the ban list keeps moving

"Delve" was the signature tell in 2023 and had mostly faded by 2025. The
vocabulary rotates as models get tuned and as writers overcorrect. Treat the
lists above as the current state, not a law.

The durable signals are structural. They're the ones worth internalizing:

- Sentences of uniform length and identical construction
- Perfect symmetry across clauses, sentences and sections
- Every paragraph the same size
- Claims pitched at a level of abstraction where nothing can be checked
- A tone that's evenly enthusiastic about everything and commits to nothing
- Every sentence ending in a clause that explains why the sentence was good news

If you only fix one thing in a draft, fix the rhythm. A page with real variation
in sentence length reads human even when a few suspect words survive. A page of
identical 18-word sentences reads like a machine even with a perfect vocabulary.
