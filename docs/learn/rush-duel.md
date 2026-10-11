# Learn Rush Duel Scripting

Build a Rush card using the same effect fundamentals as the main learning path,
then add the Rush library's requirements, rules, and summon procedures.

<div class="learn-priority-grid">
  <a class="learn-priority" href="rush-duel-scripting">
    <small>1 · First effect</small>
    <strong>Requirement to resolution</strong>
    <span>Walk through Mystic Dealer, callback factories, drawing, and the Rush rules layer.</span>
  </a>
  <a class="learn-priority" href="rush-summon-procedures">
    <small>2 · Advanced mechanics</small>
    <strong>Maximum, Fusion, Ritual</strong>
    <span>Connect the database, monster procedure, and effect that performs the summon.</span>
  </a>
  <a class="learn-priority" href="../examples/rush">
    <small>3 · Read real cards</small>
    <strong>Rush examples</strong>
    <span>Compare full imported scripts with their card text and helper calls.</span>
  </a>
</div>

## Start At Your Level

| Your starting point | Next step |
| --- | --- |
| New to Lua | [Lua Essentials](lua-essentials), then [Script Structure](script-structure). |
| Know normal YGOPro scripts | [Rush Duel Scripting](rush-duel-scripting); focus on helper shapes and shared rules. |
| Need a particular helper | [Rush function reference](/rush/api/functions/) and the Rush format in [Script Explorer](/tools/script-explorer). |
| Card loads but Rush behavior is missing | Check [database and runtime wiring](../guides/card-database#rush-card-data-and-runtime-rules). |
| Implementing a Maximum or Ritual card | Follow [Rush summon procedures](rush-summon-procedures) and its source examples. |

## Keep Three Questions Separate

1. **Is this Rush card data?** Check the database, ID, and type flags.
2. **Has the duel loaded Rush rules?** The game must initialize the Rush runtime.
3. **Does this particular effect work?** Trace its condition, cost, target, and operation.

A Rush pool flag does not load `RD`, and a working draw effect does not prove
that the duel loaded the Maximum, Legend, or timing behavior. The lessons mark
which layer is responsible and give observable checks for each example.

## Ready To Move On?

After the first lesson, explain why `RD.CostSendHandToGrave(...)` is called while
building the script but `RD.Draw()` is called during resolution. After the
summon lesson, explain why a Maximum side piece uses `EFFECT_TYPE_XMATERIAL`
and why that does not make it an Xyz Monster.

Return to the [lesson library](./#lesson-library) for shared topics such as
Groups, reset flags, card movement, and debugging.
