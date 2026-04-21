# Daily Reflection Tree
### DT Fellowship Assignment — Part A + Part B

> *A deterministic end-of-day reflection agent. No LLM at runtime. Same answers → same path → same reflection. Every time.*

---

## Quick Start

**Web app (recommended):**
```bash
# Just open in any browser — no server needed
open agent/index.html
```

**CLI:**
```bash
python agent/agent.py
# or with explicit path:
python agent/agent.py tree/reflection-tree.json
```
*Requires Python 3.7+. Zero external dependencies.*

---

## Repository Structure

```
/tree/
  reflection-tree.json       ← The tree: 45 nodes, all 3 axes, fully traceable as data
  tree-diagram.md            ← Mermaid visual diagram + two complete path walkthroughs

/agent/
  index.html                 ← Production web app (single file, no server, no dependencies)
  agent.py                   ← Python CLI agent

/transcripts/
  persona-1-transcript.md    ← Victor / Contribution / Altrocentric path
  persona-2-transcript.md    ← Victim / Entitlement / Self-Centric path

write-up.md                  ← Design rationale (2 pages, with citations)
README.md                    ← This file
```

---

## The Tree (Part A)

### Node count

| Type | Count | Description |
|------|-------|-------------|
| start | 1 | Opens the session |
| question | 16 | Fixed-option questions (4 options each) |
| decision | 16 | Internal routing — invisible to employee |
| reflection | 6 | Insight/reframe nodes (2 per axis) |
| bridge | 4 | Axis transition statements |
| summary | 1 | End-of-session synthesis |
| end | 1 | Closes the session |
| **Total** | **45** | |

### Axes covered

| Axis | Psychology | Questions |
|------|-----------|-----------|
| I — Locus | Rotter (1954) Locus of Control + Dweck (2006) Growth Mindset | 4 |
| II — Orientation | Organ (1988) OCB + Campbell et al. (2004) Entitlement | 4 |
| III — Radius | Maslow (1969) Self-Transcendence + Batson (2011) Perspective-Taking | 4 |

### How to read the tree data

Each node in `reflection-tree.json`:

```json
{
  "id": "A1_Q_AGENCY_HIGH",
  "parentId": "A1_D1",
  "type": "question",
  "text": "You described today as '{A1_OPEN.answer}'. When something went well...",
  "options": ["I prepared and it paid off", "The team delivered", ...],
  "target": "",
  "signal": "axis1:internal"
}
```

| Field | Purpose |
|-------|---------|
| `id` | Unique node identifier |
| `parentId` | Parent in the tree hierarchy |
| `type` | `start / question / decision / reflection / bridge / summary / end` |
| `text` | Employee-facing text. `{node_id.answer}` is replaced with prior answers |
| `options` | For questions: fixed choices. For decisions: routing rules |
| `target` | Hard jump override (bypasses child-following) |
| `signal` | Axis tally — e.g. `axis1:internal` increments the internal locus counter |

**Decision node routing format:**
```
"answer=Option A|Option B:TARGET_NODE;answer=Option C:OTHER_TARGET"
```
No code required to trace — follow the data directly.

### State accumulation

As the employee answers, the engine tallies signals:
```
axis1: { internal: 2, external: 0 }  →  dominant = internal
axis2: { contribution: 1, entitlement: 1 } →  dominant = contribution (first wins on tie)
```
The dominant pole per axis determines which reflection node fires.

---

## The Web App (Part B)

`agent/index.html` — open directly in any browser.

**Features:**
- Loads the embedded tree data (no network call, no server)
- Renders each node type with distinct visual treatment
- Question nodes: click or press `1`–`4` on keyboard to select; auto-advances
- Reflection nodes: read, press `Enter` or click to continue
- Bridge nodes: auto-advance after 2.2 seconds
- Progress bar tracks completion across all 3 axes
- Axis tracker in header highlights the active axis
- Summary screen shows dominant pole per axis with animated bars
- Zero LLM calls at runtime

**Design direction:** Editorial / refined. Cormorant Garamond serif for warmth and gravity. DM Mono for structural labels. Warm paper palette — not a dashboard, not a chat interface. An evening ritual.

---

## Psychology Citations

- **Rotter, J. B. (1954).** *Social learning and clinical psychology.* — Locus of control as a measurable, situationally activated construct.
- **Dweck, C. S. (2006).** *Mindset.* — The belief that noticing agency is itself an act of agency.
- **Campbell, W. K. et al. (2004).** Psychological entitlement. *Journal of Personality Assessment.* — Entitlement as stable identity-level belief, not momentary mood.
- **Organ, D. W. (1988).** *Organizational citizenship behavior.* — Discretionary, role-exceeding, non-transactional contribution.
- **Maslow, A. H. (1969).** The farther reaches of human nature. *Journal of Transpersonal Psychology.* — Self-transcendence as the peak of motivation.
- **Batson, C. D. (2011).** *Altruism in humans.* — Perspective-taking as a learnable cognitive act that shifts behavior.

---

## Key Design Constraints Met

- ✅ **No LLM at runtime** — pure decision tree lookup
- ✅ **Deterministic paths** — same answers always produce same path
- ✅ **Fixed options only** — no free text input
- ✅ **No moralizing** — reflections observe, they do not prescribe
- ✅ **Three axes in sequence** — each builds on the previous
- ✅ **Signal accumulation** — one answer doesn't define the session; patterns do
- ✅ **Interpolation** — tree references prior answers by node ID
