# Design Rationale: The Daily Reflection Tree

## Why These Questions

The central challenge in designing this tree wasn't technical — it was psychological. Most reflection tools ask employees to rate their day on a scale, write a journal entry, or pick a mood. None of that produces insight. Insight comes from noticing the gap between how you think you showed up and how you actually did.

Every question in this tree was designed to create a moment of honest recognition, not self-congratulation or shame. The options are written so that no choice is obviously "right." Someone who picks "I waited for someone to step in" isn't being judged — they're being seen. The follow-up question gives them a second, more specific look.

**Axis 1 — Locus of Control:** The opening question ("weather report") is deliberately indirect. Asking "was today good or bad?" invites performance. Asking for a weather metaphor slightly lowers the defenses — it's less evaluative, more observational. The follow-up then routes based on whether the day felt like something they navigated or something that happened to them. The second-level questions ("Did you make a choice in that hard moment?") are where the real work happens. Rotter's research showed that locus of control isn't a fixed trait — it's activated by noticing. The tree creates that noticing.

**Axis 2 — Contribution vs Entitlement:** The hardest axis to design, because entitlement is invisible to the person holding it. The trick was to approach it from the side. Instead of asking "Do you feel entitled?", the tree asks about a specific interaction and whether the person was "giving or expecting." This is a genuinely chooseable distinction — and the options don't label either choice as wrong. The Organizational Citizenship Behavior literature (Organ, 1988) is clear that OCB is *discretionary* and *non-transactional*. So the key diagnostic question is: was the person keeping a ledger? The second-level question — "Did you hold something back?" — surfaces a form of entitlement that's often invisible: the withholding of effort or knowledge that someone else could have used.

**Axis 3 — Radius of Concern:** Maslow's 1969 paper on self-transcendence makes the argument that the healthiest state of human motivation is not self-actualization but transcendence — orienting toward something beyond yourself. The tree surfaces this not by asking grand questions about meaning, but by asking a simple one: whose face came to mind? That's a behaviorally anchored, answer-able question. Batson's (2011) perspective-taking research shows that even brief, imagined engagement with another person's experience reliably shifts behavior. The tree's questions don't ask people to care more — they ask whether the caring was already there and was noticed.

## How I Designed the Branching

The branching structure operates on two levels:

**Surface routing** (decision nodes) uses the immediate answer to direct the follow-up question. This keeps the conversation feeling responsive — a "stormy" day gets a different second question than a "sunny" one, so the employee feels heard rather than processed.

**Signal accumulation** (axis tallies) determines which reflection node fires. Even if a person gave an "external" answer at the first question, strong "internal" signals later in the axis still push them toward the internal reflection. This prevents a single impulsive answer from defining the entire session — it takes a pattern.

**Trade-off I made:** The tree has 14 decision nodes, which feels heavy structurally. I could have simplified by routing only on the final answer per axis. I chose not to, because the psychological research suggests that the *process* of locating yourself on a spectrum matters — the reflection has more weight when it emerges from a sequence, not a single question.

**What I would do with more time:** Add a streak layer — the tree could show a user their axis signals over the past 7 days, which would reveal patterns invisible in a single session. Someone who is consistently "external" on Axis 1 every Monday might have a Monday problem, not a locus problem. Also: the summary node currently uses templated text. I'd replace it with a small library of ~20 variants per axis combination, so the language feels less formulaic over repeated use.

## Psychological Sources

- **Rotter, J. B. (1954).** *Social learning and clinical psychology.* Prentice-Hall. — Foundation for locus of control as a measurable, situationally activated construct.
- **Dweck, C. S. (2006).** *Mindset: The new psychology of success.* Random House. — Growth vs. fixed mindset; the belief that noticing your agency is itself a form of agency.
- **Campbell, W. K., Bonacci, A. M., Shelton, J., Exline, J. J., & Bushman, B. J. (2004).** *Psychological entitlement: Interpersonal consequences and validation of a self-report measure.* Journal of Personality Assessment. — Entitlement as a stable, identity-level belief rather than a moment-to-moment mood.
- **Organ, D. W. (1988).** *Organizational citizenship behavior: The good soldier syndrome.* Lexington Books. — OCB as discretionary, role-exceeding, non-transactionally motivated behavior.
- **Maslow, A. H. (1969).** *The farther reaches of human nature.* Journal of Transpersonal Psychology. — Self-transcendence as the peak of motivation, above self-actualization.
- **Batson, C. D. (2011).** *Altruism in humans.* Oxford University Press. — Perspective-taking as a cognitive, learnable act that generates prosocial motivation.

## On Tone

The hardest constraint was: no moralizing. Every reflection node went through multiple revisions to remove sentences that sounded like advice ("You should try to...") or judgment ("This is a pattern to watch"). The final voice is a wise colleague who has noticed something you might not have — not a coach, not a therapist, not a performance system. That voice is the product.
