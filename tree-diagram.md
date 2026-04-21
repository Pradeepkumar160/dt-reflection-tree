# Daily Reflection Tree — Visual Diagram

```mermaid
flowchart TD
    START([🌙 START\nGood evening...]) --> A1_OPEN

    A1_OPEN[A1_OPEN\n❓ Weather report for today?]
    A1_OPEN --> A1_D1{A1_D1\nRouting}
    A1_D1 -->|Sunny / Unpredictable| A1_Q_AGENCY_HIGH
    A1_D1 -->|Overcast / Stormy| A1_Q_AGENCY_LOW

    A1_Q_AGENCY_HIGH[A1_Q_AGENCY_HIGH\n❓ When things went well, what made it happen?]
    A1_Q_AGENCY_LOW[A1_Q_AGENCY_LOW\n❓ When things got difficult, what was your first instinct?]

    A1_Q_AGENCY_HIGH --> A1_D2_HIGH{A1_D2_HIGH}
    A1_D2_HIGH -->|Prepared / Adapted| A1_Q2_INTERNAL
    A1_D2_HIGH -->|Team / Lucky| A1_Q2_CREDIT

    A1_Q_AGENCY_LOW --> A1_D2_LOW{A1_D2_LOW}
    A1_D2_LOW -->|Controlled / Pushed through| A1_Q2_INTERNAL
    A1_D2_LOW -->|Waited / Felt stuck| A1_Q2_EXTERNAL

    A1_Q2_INTERNAL[A1_Q2_INTERNAL\n❓ Did you make a choice in a hard moment?]
    A1_Q2_CREDIT[A1_Q2_CREDIT\n❓ Did you feel you could claim any credit?]
    A1_Q2_EXTERNAL[A1_Q2_EXTERNAL\n❓ When things were hard, who came to mind first?]

    A1_Q2_INTERNAL --> A1_D3{A1_D3}
    A1_D3 -->|Yes / Sort of| A1_R_INTERNAL
    A1_D3 -->|Not sure / Nothing| A1_R_EXTERNAL

    A1_Q2_CREDIT --> A1_D3B{A1_D3B}
    A1_D3B -->|Contributed / Team| A1_R_INTERNAL
    A1_D3B -->|Lucky / Unsure| A1_R_EXTERNAL

    A1_Q2_EXTERNAL --> A1_D3C{A1_D3C}
    A1_D3C -->|Should have handled earlier| A1_R_INTERNAL
    A1_D3C -->|Others / Situation / Heavy| A1_R_EXTERNAL

    A1_R_INTERNAL[/A1_R_INTERNAL\n💬 You see your own hand in today.\]/]
    A1_R_EXTERNAL[/A1_R_EXTERNAL\n💬 A hard day pulls attention outward...\]/]

    A1_R_INTERNAL --> BRIDGE_1_2_A[⟶ BRIDGE: Now let's look at what you gave.]
    A1_R_EXTERNAL --> BRIDGE_1_2_B[⟶ BRIDGE: Let's turn the lens outward...]

    BRIDGE_1_2_A --> A2_OPEN
    BRIDGE_1_2_B --> A2_OPEN

    %% ============ AXIS 2 ============
    A2_OPEN[A2_OPEN\n❓ One interaction today — giving or expecting?]
    A2_OPEN --> A2_D1{A2_D1}
    A2_D1 -->|Gave / Was present| A2_Q_CONTRIBUTION
    A2_D1 -->|Keeping score / Felt under-received| A2_Q_ENTITLEMENT

    A2_Q_CONTRIBUTION[A2_Q_CONTRIBUTION\n❓ Did you do something unasked, untracked, unrewarded?]
    A2_Q_ENTITLEMENT[A2_Q_ENTITLEMENT\n❓ When you thought about recognition, what came up?]

    A2_Q_CONTRIBUTION --> A2_D2_CONT{A2_D2_CONT}
    A2_D2_CONT -->|Yes / Maybe| A2_Q2_GIVING
    A2_D2_CONT -->|No / Thought about it| A2_Q2_WITHHOLD

    A2_Q_ENTITLEMENT --> A2_D2_ENT{A2_D2_ENT}
    A2_D2_ENT -->|Felt seen / Didn't think about it| A2_Q2_GIVING
    A2_D2_ENT -->|Unacknowledged / Credit taken| A2_Q2_WITHHOLD

    A2_Q2_GIVING[A2_Q2_GIVING\n❓ How much space did team progress take in your mind?]
    A2_Q2_WITHHOLD[A2_Q2_WITHHOLD\n❓ Did you hold back something someone else needed?]

    A2_Q2_GIVING --> A2_D3{A2_D3}
    A2_D3 -->| | A2_R_CONTRIBUTION

    A2_Q2_WITHHOLD --> A2_D3B{A2_D3B}
    A2_D3B -->|Could have / Wasn't sure| A2_R_ENTITLEMENT
    A2_D3B -->|Stretched / Didn't notice| A2_R_CONTRIBUTION

    A2_R_CONTRIBUTION[/A2_R_CONTRIBUTION\n💬 Contribution means orienting outward.\]/]
    A2_R_ENTITLEMENT[/A2_R_ENTITLEMENT\n💬 Keeping score is human...\]/]

    A2_R_CONTRIBUTION --> BRIDGE_2_3_A[⟶ BRIDGE: How wide did your concern reach today?]
    A2_R_ENTITLEMENT --> BRIDGE_2_3_B[⟶ BRIDGE: Who else were you thinking about?]

    BRIDGE_2_3_A --> A3_OPEN
    BRIDGE_2_3_B --> A3_OPEN

    %% ============ AXIS 3 ============
    A3_OPEN[A3_OPEN\n❓ Whose face comes to mind beyond your own?]
    A3_OPEN --> A3_D1{A3_D1}
    A3_D1 -->|No one| A3_Q_SELF
    A3_D1 -->|Teammate / Colleague / End user| A3_Q_OTHER

    A3_Q_SELF[A3_Q_SELF\n❓ Did you ever wonder how someone else experienced today?]
    A3_Q_OTHER[A3_Q_OTHER\n❓ What did you do with that awareness?]

    A3_Q_SELF --> A3_D2_SELF{A3_D2_SELF}
    A3_D2_SELF -->|Yes / A little| A3_Q2_EXPAND
    A3_D2_SELF -->|Too absorbed / No| A3_Q2_NARROW

    A3_Q_OTHER --> A3_D2_OTHER{A3_D2_OTHER}
    A3_D2_OTHER -->|Acted / Held in mind| A3_Q2_EXPAND
    A3_D2_OTHER -->|Moved on / Didn't know what to do| A3_Q2_NARROW

    A3_Q2_EXPAND[A3_Q2_EXPAND\n❓ Was someone on your team having a harder day than you?]
    A3_Q2_NARROW[A3_Q2_NARROW\n❓ When today felt heavy, what frame were you using?]

    A3_Q2_EXPAND --> A3_D3{A3_D3}
    A3_D3 -->|Checked in / Noticed| A3_R_ALTROCENTRIC
    A3_D3 -->|Not sure / Everyone seemed fine| A3_R_SELF

    A3_Q2_NARROW --> A3_D3B{A3_D3B}
    A3_D3B -->|Team / People we serve| A3_R_ALTROCENTRIC
    A3_D3B -->|My workload / Surviving| A3_R_SELF

    A3_R_ALTROCENTRIC[/A3_R_ALTROCENTRIC\n💬 Your concern reaches beyond yourself.\]/]
    A3_R_SELF[/A3_R_SELF\n💬 Today your radius was narrow — that's OK.\]/]

    A3_R_ALTROCENTRIC --> SUMMARY
    A3_R_SELF --> SUMMARY

    SUMMARY[📋 SUMMARY\nToday you leaned...\nOn agency...\nOn contribution...\nOn radius...]
    SUMMARY --> END([👋 END\nSee you tomorrow.])

    %% Styling
    classDef questionNode fill:#1a1a2e,stroke:#e94560,color:#fff,rx:8
    classDef decisionNode fill:#16213e,stroke:#f5a623,color:#fff
    classDef reflectionNode fill:#0f3460,stroke:#53c0f0,color:#fff
    classDef bridgeNode fill:#1a1a2e,stroke:#7bed9f,color:#fff
    classDef startEnd fill:#e94560,stroke:#e94560,color:#fff

    class A1_OPEN,A1_Q_AGENCY_HIGH,A1_Q_AGENCY_LOW,A1_Q2_INTERNAL,A1_Q2_CREDIT,A1_Q2_EXTERNAL,A2_OPEN,A2_Q_CONTRIBUTION,A2_Q_ENTITLEMENT,A2_Q2_GIVING,A2_Q2_WITHHOLD,A3_OPEN,A3_Q_SELF,A3_Q_OTHER,A3_Q2_EXPAND,A3_Q2_NARROW questionNode
    class A1_D1,A1_D2_HIGH,A1_D2_LOW,A1_D3,A1_D3B,A1_D3C,A2_D1,A2_D2_CONT,A2_D2_ENT,A2_D3,A2_D3B,A3_D1,A3_D2_SELF,A3_D2_OTHER,A3_D3,A3_D3B decisionNode
    class A1_R_INTERNAL,A1_R_EXTERNAL,A2_R_CONTRIBUTION,A2_R_ENTITLEMENT,A3_R_ALTROCENTRIC,A3_R_SELF reflectionNode
    class BRIDGE_1_2_A,BRIDGE_1_2_B,BRIDGE_2_3_A,BRIDGE_2_3_B bridgeNode
    class START,END,SUMMARY startEnd
```

## Node Count Summary

| Type | Count |
|------|-------|
| start | 1 |
| question | 12 |
| decision | 14 |
| reflection | 6 |
| bridge | 4 |
| summary | 1 |
| end | 1 |
| **Total** | **39** |

## Path Examples

### Path A: Victor / Contribution / Altrocentric
START → A1_OPEN("Sunny") → A1_D1 → A1_Q_AGENCY_HIGH("I prepared") → A1_D2_HIGH → A1_Q2_INTERNAL("Yes, I can name it") → A1_D3 → **A1_R_INTERNAL** → BRIDGE → A2_OPEN("Gave without tracking return") → A2_D1 → A2_Q_CONTRIBUTION("Yes, I can picture it") → A2_D2_CONT → A2_Q2_GIVING("A lot — we were a unit") → A2_D3 → **A2_R_CONTRIBUTION** → BRIDGE → A3_OPEN("End user I serve") → A3_D1 → A3_Q_OTHER("I acted on it") → A3_D2_OTHER → A3_Q2_EXPAND("Yes, I checked in") → A3_D3 → **A3_R_ALTROCENTRIC** → SUMMARY → END

### Path B: Victim / Entitlement / Self-Centric
START → A1_OPEN("Stormy") → A1_D1 → A1_Q_AGENCY_LOW("Wait for someone to step in") → A1_D2_LOW → A1_Q2_EXTERNAL("A person who created the problem") → A1_D3C → **A1_R_EXTERNAL** → BRIDGE → A2_OPEN("I kept score a bit") → A2_D1 → A2_Q_ENTITLEMENT("Nobody acknowledged it") → A2_D2_ENT → A2_Q2_WITHHOLD("Stretched thin") → A2_D3B → **A2_R_ENTITLEMENT** → BRIDGE → A3_OPEN("No one — my problem") → A3_D1 → A3_Q_SELF("Too absorbed") → A3_D2_SELF → A3_Q2_NARROW("My workload, my stress") → A3_D3B → **A3_R_SELF** → SUMMARY → END
