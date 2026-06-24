# Learning Path

Sacred Book teaches MDPro3/YGOPro Lua scripting as a curve, not a catalogue.
Start with a few concrete scripts, learn the activation lifecycle, then branch
into the card pattern you are actually trying to build.

<div class="learn-priority-grid">
  <a class="learn-priority" href="script-structure">
    <small>Step 1</small>
    <strong>Read a card file</strong>
    <span>Learn <code>GetID</code>, <code>initial_effect</code>, effect blocks, filters, and callbacks.</span>
  </a>
  <a class="learn-priority" href="first-scripts">
    <small>Step 2</small>
    <strong>Study first scripts</strong>
    <span>Walk through five local scripts that draw, target, prompt, modify, and choose by stats.</span>
  </a>
  <a class="learn-priority" href="effect-callbacks">
    <small>Step 3</small>
    <strong>Trace activation flow</strong>
    <span>Separate condition, cost, target, operation, and <code>chk==0</code> legality.</span>
  </a>
  <a class="learn-priority" href="targeting-flow">
    <small>Step 4</small>
    <strong>Choose cards safely</strong>
    <span>Use targeting, matching, Groups, relation checks, and resolution selections correctly.</span>
  </a>
  <a class="learn-priority" href="common-script-errors-and-debugging">
    <small>Step 5</small>
    <strong>Debug the script</strong>
    <span>Fix nil values, invisible prompts, stale targets, count limits, reset flags, and stored Groups.</span>
  </a>
</div>

## What To Learn First

1. [Structure of a card script](script-structure)
2. [First Scripts To Study](first-scripts)
3. [Creation, building, and registration of an effect object](effect-object)
4. [EFFECT_TYPE constants and templates](effect-types)
5. [Conditions, costs, activation procedures, and resolution](effect-callbacks)
6. [Activated effects](activated-effects)
7. [Activation legality](activation-legality)
8. [Targeting flow](targeting-flow)
9. [Selection and Group handling](selection-and-group-handling)
10. [Client UI and prompt behavior](client-ui-and-prompt-behavior)
11. [Common script errors and debugging](common-script-errors-and-debugging)

That first route is deliberately short. It gives you enough structure to read a
local script without drowning in every summon type, card family, and helper.

## Lesson Library

Use this library after the first route, or jump to the branch that matches the
card you are scripting.

<div class="learn-stage-grid">
  <section class="learn-stage">
    <h3>Foundations</h3>
    <a href="script-structure">Script structure</a>
    <a href="effect-object">Effect objects</a>
    <a href="effect-types">Effect types</a>
    <a href="categories-properties-and-hints">Categories and properties</a>
    <a href="first-scripts">First scripts</a>
  </section>
  <section class="learn-stage">
    <h3>Activation Flow</h3>
    <a href="effect-callbacks">Callbacks</a>
    <a href="activated-effects">Activated effects</a>
    <a href="activation-legality">Activation legality</a>
    <a href="cost-target-operation-lifecycle">Effect lifecycle</a>
    <a href="chain-timing-and-activation-windows">Chain timing</a>
    <a href="client-ui-and-prompt-behavior">Client UI and prompts</a>
  </section>
  <section class="learn-stage">
    <h3>Cards And Groups</h3>
    <a href="filters-and-groups">Filters and Groups</a>
    <a href="targeting-flow">Targeting flow</a>
    <a href="selection-and-group-handling">Selection and Group handling</a>
    <a href="moving-cards">Moving cards</a>
    <a href="reset-flags-and-duration">Reset flags and duration</a>
  </section>
  <section class="learn-stage">
    <h3>Spell And Trap Patterns</h3>
    <a href="spell-card-patterns">Spell Cards</a>
    <a href="quick-play-spells">Quick-Play Spells</a>
    <a href="equip-spells">Equip Spells</a>
    <a href="field-spells">Field Spells</a>
    <a href="trap-card-patterns">Trap Cards</a>
    <a href="normal-and-continuous-traps">Normal and Continuous Traps</a>
    <a href="counter-traps">Counter Traps</a>
  </section>
  <section class="learn-stage">
    <h3>Summon Procedures</h3>
    <a href="ritual-procedure">Ritual procedure</a>
    <a href="fusion-procedure">Fusion procedure</a>
    <a href="synchro-procedure">Synchro procedure</a>
    <a href="xyz-procedure">Xyz procedure</a>
    <a href="link-procedure">Link procedure</a>
    <a href="pendulum-procedure">Pendulum procedure</a>
    <a href="special-summon-only-monsters">Special Summon-only monsters</a>
    <a href="tribute-summon-materials">Tribute Summon materials</a>
  </section>
  <section class="learn-stage">
    <h3>Monster Families</h3>
    <a href="gemini-monsters">Gemini Monsters</a>
    <a href="toon-monsters">Toon Monsters</a>
    <a href="union-monsters">Union Monsters</a>
    <a href="spirit-monsters">Spirit Monsters</a>
    <a href="archetypes-and-setcodes">Archetypes and set codes</a>
  </section>
  <section class="learn-stage">
    <h3>Card Outcomes</h3>
    <a href="affecting-cards">Methods for affecting cards</a>
    <a href="continuous-effects">Continuous effects</a>
    <a href="continuous-stat-modifiers">Continuous stat modifiers</a>
    <a href="counters">Counters</a>
    <a href="negation-and-immunity">Negation and immunity</a>
    <a href="control-change">Control change</a>
    <a href="battle-position-effects">Battle position effects</a>
    <a href="field-zones-and-sequences">Field zones and sequences</a>
  </section>
  <section class="learn-stage">
    <h3>Player Data And Memory</h3>
    <a href="lp-recovery-and-damage">LP recovery and effect damage</a>
    <a href="player-targeted-effects">Player-targeted effects</a>
    <a href="player-restrictions">Player restrictions</a>
    <a href="draw-hand-and-deck-effects">Draw, hand, and Deck effects</a>
    <a href="flag-effects">Flag effects</a>
    <a href="count-limits">Count limits</a>
  </section>
</div>

## How To Use The Wiki Archive Pass

The downloaded wiki pages are a teaching checklist, not factual authority for
this project. Sacred Book rewrites that material in its own words and verifies
behavior against local MDPro3/YGOPro core, local scripts, local define files,
and generated API data.

When an external page uses another simulator's helper name, Sacred Book should
replace it with a local equivalent or document that it is not local. See
[Downloaded Tutorial Coverage](/tools/page-analysis) for the audit trail.

## How To Read A Real Script

When a local card script looks confusing, read it in this order:

1. Find `initial_effect(c)`.
2. Read each `Effect.CreateEffect(c)` block.
3. Note `SetType`, `SetCode`, `SetRange`, `SetProperty`, and callbacks.
4. Read `SetCondition`, `SetCost`, `SetTarget`, and `SetOperation` callbacks.
5. Read helper filters last, because they usually only answer "which cards count?"

Useful reference while learning:

- [Function index](/api/functions/)
- [Constants](/api/constants)
- [Featured script examples](/examples/)
- [Script Explorer](/tools/script-explorer)
