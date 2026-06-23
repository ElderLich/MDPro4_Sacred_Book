# Learning Path

This section teaches MDPro3/YGOPro Lua card scripting from the shape of a card
script up to real effect resolution. It is written for this project and links
back into the generated API reference and live card examples.

<div class="sacred-grid">
  <a class="sacred-card" href="script-structure">
    <strong>Script structure</strong>
    <span>How one card file is loaded and where effects are registered.</span>
  </a>
  <a class="sacred-card" href="effect-object">
    <strong>Effect objects</strong>
    <span>The practical order for CreateEffect, setters, and RegisterEffect.</span>
  </a>
  <a class="sacred-card" href="effect-callbacks">
    <strong>Callbacks</strong>
    <span>How condition, cost, target, and operation functions divide work.</span>
  </a>
  <a class="sacred-card" href="activated-effects">
    <strong>Activated effects</strong>
    <span>How Chain Links move from legal activation to later resolution.</span>
  </a>
  <a class="sacred-card" href="spell-card-patterns">
    <strong>Spell Cards</strong>
    <span>Normal, Continuous, Quick-Play, and Ritual Spell activation shapes.</span>
  </a>
  <a class="sacred-card" href="trap-card-patterns">
    <strong>Trap Cards</strong>
    <span>Normal, Continuous, and Counter Trap timing patterns.</span>
  </a>
  <a class="sacred-card" href="ritual-procedure">
    <strong>Ritual procedures</strong>
    <span>Choose helpers or manual flow for Ritual Monsters, materials, and proper Summons.</span>
  </a>
  <a class="sacred-card" href="fusion-procedure">
    <strong>Fusion procedures</strong>
    <span>Define Fusion Materials, select legal groups, and resolve Fusion Summons.</span>
  </a>
  <a class="sacred-card" href="synchro-procedure">
    <strong>Synchro procedures</strong>
    <span>Register Synchro Material rules, Level checks, and effect-driven Synchro Summons.</span>
  </a>
  <a class="sacred-card" href="xyz-procedure">
    <strong>Xyz procedures</strong>
    <span>Register Xyz Material rules, overlay materials, and detach costs safely.</span>
  </a>
  <a class="sacred-card" href="filters-and-groups">
    <strong>Filters and Groups</strong>
    <span>How scripts find, select, count, and iterate cards.</span>
  </a>
  <a class="sacred-card" href="moving-cards">
    <strong>Moving cards</strong>
    <span>Which Duel functions send, destroy, banish, summon, equip, or set cards.</span>
  </a>
  <a class="sacred-card" href="field-zones-and-sequences">
    <strong>Field zones</strong>
    <span>How location counts, sequence numbers, zone masks, and columns fit together.</span>
  </a>
  <a class="sacred-card" href="field-spells">
    <strong>Field Spells</strong>
    <span>Activate Field Spells, read the Field Zone, and place field cards from the Deck.</span>
  </a>
  <a class="sacred-card" href="targeting-flow">
    <strong>Targeting flow</strong>
    <span>How scripts check, select, record, and resolve official effect targets.</span>
  </a>
  <a class="sacred-card" href="cost-target-operation-lifecycle">
    <strong>Effect lifecycle</strong>
    <span>How costs, target branches, labels, Chain data, and operations work together.</span>
  </a>
  <a class="sacred-card" href="continuous-effects">
    <strong>Continuous effects</strong>
    <span>How always-on, field, equip, and event-watching effects are built.</span>
  </a>
  <a class="sacred-card" href="continuous-stat-modifiers">
    <strong>Stat modifiers</strong>
    <span>Build ATK/DEF modifiers for the handler, a field range, or an Equip Card.</span>
  </a>
  <a class="sacred-card" href="equip-spells">
    <strong>Equip Spells</strong>
    <span>Target, equip, limit, and apply effects from Equip Cards.</span>
  </a>
  <a class="sacred-card" href="lp-recovery-and-damage">
    <strong>LP and damage</strong>
    <span>Script effect damage, recovery, target player data, and stepped LP changes.</span>
  </a>
  <a class="sacred-card" href="flag-effects">
    <strong>Flag effects</strong>
    <span>How scripts remember player or card state with RegisterFlagEffect and GetFlagEffect.</span>
  </a>
  <a class="sacred-card" href="count-limits">
    <strong>Count limits</strong>
    <span>How once-per-turn limits, shared count codes, and activity counters work.</span>
  </a>
</div>

## Suggested Order

1. Start with [Structure of a card script](script-structure).
2. Build an effect in [Creation, building, and registration of an effect object](effect-object).
3. Choose timing and shape in [EFFECT_TYPE constants and templates](effect-types).
4. Write callbacks with [Conditions, costs, activation procedures, and resolution](effect-callbacks).
5. Understand Chain Links with [Activated effects](activated-effects).
6. Check legality with [Activation legality](activation-legality).
7. Split Spell activations with [Spell Card Patterns](spell-card-patterns).
8. Split Trap timing with [Trap Card Patterns](trap-card-patterns).
9. Learn Ritual Summon flow with [Ritual Procedure Guide](ritual-procedure).
10. Learn Fusion Material and Summon flow with [Fusion Procedure Guide](fusion-procedure).
11. Learn Synchro procedures and effect-driven Synchro Summons with [Synchro Procedure Guide](synchro-procedure).
12. Learn overlaying and detaching with [Xyz Procedure Guide](xyz-procedure).
13. Work with cards and groups through [Filters, Card objects, and Group objects](filters-and-groups).
14. Move cards correctly with [Functions that move cards across locations](moving-cards).
15. Place cards and read zones with [Field zones and sequences](field-zones-and-sequences).
16. Script Field Spell patterns with [Field Spells](field-spells).
17. Target cards correctly with [Targeting flow](targeting-flow).
18. Resolve activated effects with [Cost, target, and operation lifecycle](cost-target-operation-lifecycle).
19. Read always-on behavior through [Continuous effects](continuous-effects).
20. Build visible modifiers with [Continuous stat modifiers](continuous-stat-modifiers).
21. Script Equip Cards with [Equip Spells and Equip Cards](equip-spells).
22. Script LP changes with [LP Recovery and Effect Damage](lp-recovery-and-damage).
23. Track temporary script memory with [Flag effects](flag-effects).
24. Limit effect usage with [Count limits and once per turn](count-limits).
25. Apply outcomes through [Methods for affecting cards](affecting-cards).
26. Use card families through [Archetypes and set codes](archetypes-and-setcodes).

## Tutorial Equivalents

The downloaded tutorial archive was used as a topic checklist, excluding the
editor-tool page. Sacred Book now has original MDPro3/YGOPro equivalents for
each scripting topic in that archive. See [Page Analysis](/tools/page-analysis)
for the coverage map.

## How To Read This Book

Each lesson starts with the idea, then shows a small script pattern, then links
to the API page for exact signatures. The examples are intentionally small:
real scripts often combine several ideas, while the learning pages isolate one
reason at a time.

When a card script looks confusing, read it in this order:

1. Find `initial_effect(c)`.
2. Read each `Effect.CreateEffect(c)` block and note `SetType`, `SetCode`, `SetRange`, and callbacks.
3. Read the callback functions named by `SetCondition`, `SetCost`, `SetTarget`, and `SetOperation`.
4. Read helper filters last, because they usually only answer "which cards count?"

## Useful Reference While Learning

- [Function index](/api/functions/)
- [Constants](/api/constants)
- [Featured script examples](/examples/)
- [Script Explorer](/tools/script-explorer)
