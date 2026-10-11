# Learning Path

Sacred Book has two useful modes: a guided curve for learning the engine and a
task library for finding one exact pattern. New scripters should follow the
first curve in order. Experienced scripters can jump to a branch, confirm the
call in the API, then search real local use in the Script Explorer.

## Pick Your Starting Point

| Your experience or task | Start here |
| --- | --- |
| New to programming or Lua. | Start with [Lua Essentials](lua-essentials), then follow the seven-step curve below. |
| Familiar with Lua; new to card scripts. | Follow the seven-step curve below. |
| Comfortable with Lua, but new to YGOPro effects. | Read [Effect Objects](effect-object), [Effect Types](effect-types), and [Callbacks](effect-callbacks). |
| You know the engine and need one implementation pattern. | Jump to the [Lesson Library](#lesson-library), then use the [Script Explorer](/tools/script-explorer). |
| A script almost works, but fails in one game state. | Trace [Activation Legality](activation-legality), [Effect Lifecycle](cost-target-operation-lifecycle), and [Common Script Errors](common-script-errors-and-debugging). |
| Building a Rush Duel card. | Follow the [Rush Duel track](rush-duel). |
| Returning after an engine update. | Read [Applying Engine and Script Changes](engine-updates) for the new card-type API and corrected patterns. |

## First Complete Card Curve

<div class="learn-priority-grid">
  <a class="learn-priority" href="script-structure">
    <small>Step 1</small>
    <strong>Read a card file</strong>
    <span>Learn <code>GetID</code>, <code>initial_effect</code>, effect blocks, filters, and callbacks.</span>
  </a>
  <a class="learn-priority" href="first-scripts">
    <small>Step 2</small>
    <strong>Trace real effects</strong>
    <span>Follow small local scripts that draw, target, prompt, modify, and choose by stats.</span>
  </a>
  <a class="learn-priority" href="beginner-script-ladder">
    <small>Step 3</small>
    <strong>Build small effects</strong>
    <span>Follow complete draw, target, Group, trigger, Quick-Play, and Trap scripts in order.</span>
  </a>
  <a class="learn-priority" href="first-custom-card">
    <small>Step 4</small>
    <strong>Write one card</strong>
    <span>Combine two proven patterns into a small, complete, testable custom Spell.</span>
  </a>
  <a class="learn-priority" href="card-data-and-script-wiring">
    <small>Step 5</small>
    <strong>Wire card data</strong>
    <span>Match the card ID, type bits, prompt strings, set codes, and Lua file.</span>
  </a>
  <a class="learn-priority" href="effect-callbacks">
    <small>Step 6</small>
    <strong>Trace activation flow</strong>
    <span>Separate condition, cost, target, operation, and <code>chk==0</code> legality.</span>
  </a>
  <a class="learn-priority" href="common-script-errors-and-debugging">
    <small>Step 7</small>
    <strong>Debug the script</strong>
    <span>Fix nil values, invisible prompts, stale targets, count limits, reset flags, and stored Groups.</span>
  </a>
</div>

## Checkpoints For Your First Card

You do not need to memorize every function before moving on. Use these
observable checkpoints to choose your next lesson:

| After | You should be able to |
| --- | --- |
| Reading a file | Point to the effect registration, the callbacks, and the filters. |
| Building small effects | Explain what `chk==0` checks without selecting or moving cards. |
| Writing and wiring a card | Load your card with the correct name, type, script, and prompt text. |
| Tracing activation | Explain which values are chosen now and which must be checked again at resolution. |
| Debugging | Reproduce one legal activation, one illegal activation, and one changed-state resolution. |

If a checkpoint fails, return to that stage with one small card. For a Rush
card, complete the shared Lua/callback foundations, then follow the
[Rush track](rush-duel) before copying a standard-format effect.

## Learn, Verify, Search

Use the site layers together instead of expecting one page to answer every
question:

| Layer | Best use |
| --- | --- |
| Learning pages | Understand why a pattern is shaped a certain way and see a complete example. |
| [Function reference](/api/functions/) | Confirm the exact signature, parameters, return value, and local source. |
| [Script Explorer](/tools/script-explorer) | Find every local card that uses a function or a similar text pattern. |
| [Featured examples](/examples/) | Read larger real cards with their detected calls and source. |

For a new effect, read one relevant lesson, find two local scripts with the same
shape, and verify unfamiliar calls in the API. That workflow scales from a
first card to veteran-level edge cases.

## Common Effect Pattern Route

Once you can follow target and operation callbacks, these three pages answer a
lot of real custom-card questions:

1. [Functions that move cards across locations](moving-cards)
2. [Equip Spells and Equip Cards](equip-spells)
3. [LP Recovery and Effect Damage](lp-recovery-and-damage)

Read them when the card text says "send", "banish", "equip", "recover LP", or
"inflict damage" and you need to choose the right local API shape.

## Lesson Library

Use this library after the first route, or jump to the branch that matches the
card you are scripting.

<div class="learn-stage-grid">
  <section class="learn-stage">
    <h3>Foundations</h3>
    <a href="lua-essentials">Lua essentials</a>
    <a href="script-structure">Script structure</a>
    <a href="effect-object">Effect objects</a>
    <a href="effect-types">Effect types</a>
    <a href="categories-properties-and-hints">Categories and properties</a>
    <a href="first-scripts">First scripts</a>
    <a href="beginner-script-ladder">Beginner script ladder</a>
    <a href="first-custom-card">First custom card</a>
    <a href="card-data-and-script-wiring">Card data and script wiring</a>
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
    <a href="min-max-stat-selection">Min/Max stat selection</a>
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
    <h3>Rush Duel</h3>
    <a href="rush-duel">Choose your Rush starting point</a>
    <a href="rush-duel-scripting">Requirements and resolution</a>
    <a href="rush-selection-and-actions">Selection, actions, and temporary stats</a>
    <a href="rush-summon-procedures">Maximum, Fusion, and Ritual</a>
    <a href="../examples/rush">Real Rush scripts</a>
    <a href="../rush/api/functions/">Rush helper reference</a>
  </section>
  <section class="learn-stage">
    <h3>Maintenance And Debugging</h3>
    <a href="engine-updates">Apply engine and script changes</a>
    <a href="common-script-errors-and-debugging">Common script errors</a>
    <a href="card-data-and-script-wiring">Verify card data and scripts</a>
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
