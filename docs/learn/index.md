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
  <a class="sacred-card" href="effect-types">
    <strong>Effect types</strong>
    <span>Choose activate, ignition, trigger, quick, single, field, equip, and material shapes.</span>
  </a>
  <a class="sacred-card" href="categories-properties-and-hints">
    <strong>Categories and properties</strong>
    <span>Set categories, operation info, target flags, Damage Step flags, and prompt timing.</span>
  </a>
  <a class="sacred-card" href="client-ui-and-prompt-behavior">
    <strong>Client UI and prompts</strong>
    <span>Make legal effects visible and readable with hints, timing masks, and operation info.</span>
  </a>
  <a class="sacred-card" href="selection-and-group-handling">
    <strong>Selection and groups</strong>
    <span>Choose targets, resolution cards, subgroups, and stored Groups without losing state.</span>
  </a>
  <a class="sacred-card" href="reset-flags-and-duration">
    <strong>Reset flags and duration</strong>
    <span>Control how temporary effects, player locks, and flag markers expire.</span>
  </a>
  <a class="sacred-card" href="effect-callbacks">
    <strong>Callbacks</strong>
    <span>How condition, cost, target, and operation functions divide work.</span>
  </a>
  <a class="sacred-card" href="activated-effects">
    <strong>Activated effects</strong>
    <span>How Chain Links move from legal activation to later resolution.</span>
  </a>
  <a class="sacred-card" href="chain-timing-and-activation-windows">
    <strong>Chain timing</strong>
    <span>Separate client prompts, activation windows, Chain responses, and Damage Step access.</span>
  </a>
  <a class="sacred-card" href="spell-card-patterns">
    <strong>Spell Cards</strong>
    <span>Normal, Continuous, Quick-Play, and Ritual Spell activation shapes.</span>
  </a>
  <a class="sacred-card" href="quick-play-spells">
    <strong>Quick-Play Spells</strong>
    <span>Script Spell Speed 2 activations, prompt timing, targets, and relation checks.</span>
  </a>
  <a class="sacred-card" href="trap-card-patterns">
    <strong>Trap Cards</strong>
    <span>Normal, Continuous, and Counter Trap timing patterns.</span>
  </a>
  <a class="sacred-card" href="normal-and-continuous-traps">
    <strong>Normal and Continuous Traps</strong>
    <span>Separate one-shot Trap activation from face-up S/T Zone effects and cleanup.</span>
  </a>
  <a class="sacred-card" href="counter-traps">
    <strong>Counter Traps</strong>
    <span>Choose summon negation, activation negation, or effect negation patterns clearly.</span>
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
  <a class="sacred-card" href="link-procedure">
    <strong>Link procedures</strong>
    <span>Register Link Material rules, Link Rating counts, and linked-zone checks.</span>
  </a>
  <a class="sacred-card" href="pendulum-procedure">
    <strong>Pendulum procedures</strong>
    <span>Enable Pendulum Summons, script Pendulum Zone effects, read scales, and place cards.</span>
  </a>
  <a class="sacred-card" href="special-summon-only-monsters">
    <strong>Special Summon-only monsters</strong>
    <span>Build revive limits, hand procedures, reveal costs, summon restrictions, and proper-Summon completion.</span>
  </a>
  <a class="sacred-card" href="gemini-monsters">
    <strong>Gemini Monsters</strong>
    <span>Use local Dual constants, register Gemini handling, and script gained-effect state safely.</span>
  </a>
  <a class="sacred-card" href="toon-monsters">
    <strong>Toon Monsters</strong>
    <span>Script Toon World checks, Toon type filters, attack rules, and Toon-specific procedures.</span>
  </a>
  <a class="sacred-card" href="union-monsters">
    <strong>Union Monsters</strong>
    <span>Equip, unequip, check Union targets, and preserve Union state after manual equips.</span>
  </a>
  <a class="sacred-card" href="spirit-monsters">
    <strong>Spirit Monsters</strong>
    <span>Register End Phase return behavior, optional-return modifiers, and Spirit support filters.</span>
  </a>
  <a class="sacred-card" href="tribute-summon-materials">
    <strong>Tribute Summon materials</strong>
    <span>Script cards treated as multiple Tributes, custom Tribute procedures, and material memory.</span>
  </a>
  <a class="sacred-card" href="counters">
    <strong>Counters</strong>
    <span>Permit, add, read, limit, remove, and preserve card counters safely.</span>
  </a>
  <a class="sacred-card" href="filters-and-groups">
    <strong>Filters and Groups</strong>
    <span>How scripts find, select, count, and iterate cards.</span>
  </a>
  <a class="sacred-card" href="moving-cards">
    <strong>Moving cards</strong>
    <span>Which Duel functions send, destroy, banish, summon, equip, or set cards.</span>
  </a>
  <a class="sacred-card" href="negation-and-immunity">
    <strong>Negation and immunity</strong>
    <span>Separate Chain negation, lingering disable, unaffected text, and protection rules.</span>
  </a>
  <a class="sacred-card" href="control-change">
    <strong>Control change</strong>
    <span>Take, swap, and continuously set control while preserving controller and owner logic.</span>
  </a>
  <a class="sacred-card" href="battle-position-effects">
    <strong>Battle position effects</strong>
    <span>Change, Set, force, and prevent battle positions with the right local helpers.</span>
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
  <a class="sacred-card" href="player-targeted-effects">
    <strong>Player-targeted effects</strong>
    <span>Store target players and parameters, then read Chain data at resolution.</span>
  </a>
  <a class="sacred-card" href="player-restrictions">
    <strong>Player restrictions</strong>
    <span>Script player locks, oath restrictions, action limits, and phase skips.</span>
  </a>
  <a class="sacred-card" href="draw-hand-and-deck-effects">
    <strong>Draw, hand, and Deck effects</strong>
    <span>Draw, discard, reveal, sort, shuffle, and send cards from the top of the Deck safely.</span>
  </a>
  <a class="sacred-card" href="flag-effects">
    <strong>Flag effects</strong>
    <span>How scripts remember player or card state with RegisterFlagEffect and GetFlagEffect.</span>
  </a>
  <a class="sacred-card" href="count-limits">
    <strong>Count limits</strong>
    <span>How once-per-turn limits, shared count codes, and activity counters work.</span>
  </a>
  <a class="sacred-card" href="common-script-errors-and-debugging">
    <strong>Common script errors</strong>
    <span>Debug nil values, legality branches, target flow, relation checks, resets, count limits, and stored Groups.</span>
  </a>
</div>

## Suggested Order

1. Start with [Structure of a card script](script-structure).
2. Build an effect in [Creation, building, and registration of an effect object](effect-object).
3. Choose timing and shape in [EFFECT_TYPE constants and templates](effect-types).
4. Add metadata with [Categories, Properties, And Hint Timing](categories-properties-and-hints).
5. Make effects readable in the client with [Client UI And Prompt Behavior](client-ui-and-prompt-behavior).
6. Write callbacks with [Conditions, costs, activation procedures, and resolution](effect-callbacks).
7. Understand Chain Links with [Activated effects](activated-effects).
8. Check legality with [Activation legality](activation-legality).
9. Separate prompts and response windows with [Chain Timing And Activation Windows](chain-timing-and-activation-windows).
10. Split Spell activations with [Spell Card Patterns](spell-card-patterns).
11. Learn fast Spell activation flow with [Quick-Play Spells](quick-play-spells).
12. Split Trap timing with [Trap Card Patterns](trap-card-patterns).
13. Separate one-shot and face-up Trap behavior with [Normal And Continuous Traps](normal-and-continuous-traps).
14. Choose the right negation family with [Counter Traps](counter-traps).
15. Learn Ritual Summon flow with [Ritual Procedure Guide](ritual-procedure).
16. Learn Fusion Material and Summon flow with [Fusion Procedure Guide](fusion-procedure).
17. Learn Synchro procedures and effect-driven Synchro Summons with [Synchro Procedure Guide](synchro-procedure).
18. Learn overlaying and detaching with [Xyz Procedure Guide](xyz-procedure).
19. Learn Link Rating, materials, and linked zones with [Link Procedure Guide](link-procedure).
20. Learn Pendulum Zones, scales, and Pendulum Summon flow with [Pendulum Procedure Guide](pendulum-procedure).
21. Handle revive limits and self-Summon procedures with [Special Summon-only Monster Guide](special-summon-only-monsters).
22. Learn local Gemini/Dual state with [Gemini Monsters](gemini-monsters).
23. Script Toon type and Toon World patterns with [Toon Monsters](toon-monsters).
24. Equip and unequip monsters with [Union Monsters](union-monsters).
25. Register End Phase return behavior with [Spirit Monsters](spirit-monsters).
26. Handle Tribute Summon material value with [Tribute Summon Materials](tribute-summon-materials).
27. Add and spend visible card counters with [Counters](counters).
28. Work with cards and groups through [Filters, Card objects, and Group objects](filters-and-groups).
29. Choose cards safely with [Selection And Group Handling](selection-and-group-handling).
30. Control temporary effect lifetimes with [Reset Flags And Effect Duration](reset-flags-and-duration).
31. Move cards correctly with [Functions that move cards across locations](moving-cards).
32. Negate effects and protect cards with [Negation and Immunity](negation-and-immunity).
33. Take or swap control with [Control Change](control-change).
34. Change or lock battle positions with [Battle Position Effects](battle-position-effects).
35. Place cards and read zones with [Field zones and sequences](field-zones-and-sequences).
36. Script Field Spell patterns with [Field Spells](field-spells).
37. Target cards correctly with [Targeting flow](targeting-flow).
38. Resolve activated effects with [Cost, target, and operation lifecycle](cost-target-operation-lifecycle).
39. Read always-on behavior through [Continuous effects](continuous-effects).
40. Build visible modifiers with [Continuous stat modifiers](continuous-stat-modifiers).
41. Script Equip Cards with [Equip Spells and Equip Cards](equip-spells).
42. Script LP changes with [LP Recovery and Effect Damage](lp-recovery-and-damage).
43. Store player Chain data with [Player-Targeted Effects](player-targeted-effects).
44. Apply player locks with [Player Restrictions](player-restrictions).
45. Script draw, hand, and Deck movement with [Draw, Hand, And Deck Effects](draw-hand-and-deck-effects).
46. Track temporary script memory with [Flag effects](flag-effects).
47. Limit effect usage with [Count limits and once per turn](count-limits).
48. Debug common failure modes with [Common Script Errors And Debugging](common-script-errors-and-debugging).
49. Apply outcomes through [Methods for affecting cards](affecting-cards).
50. Use card families through [Archetypes and set codes](archetypes-and-setcodes).

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
