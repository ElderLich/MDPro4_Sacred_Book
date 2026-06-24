# Categories, Properties, And Hint Timing

An effect object has more than timing and callbacks. It also carries metadata
that helps the engine, response checks, and client understand what the effect
is trying to do.

This page covers four pieces that often appear together:

| Setter or function | Main job |
| --- | --- |
| [`Effect.SetCategory`](/api/functions/Effect/SetCategory) | Describes the kinds of actions the effect may perform. |
| [`Effect.SetProperty`](/api/functions/Effect/SetProperty) | Adds behavior flags such as targeting, Damage Step access, player targeting, or delayed triggers. |
| [`Effect.SetHintTiming`](/api/functions/Effect/SetHintTiming) | Tells the client when it should offer or highlight the effect. |
| [`Duel.SetOperationInfo`](/api/functions/Duel/SetOperationInfo) | Records the known operation details for the current Chain Link. |

None of these performs the effect by itself. The operation callback still does
the action.

## A Complete Small Shape

Book of Moon (`c14087893.lua`) shows the normal shape:

```lua
local e1=Effect.CreateEffect(c)
e1:SetCategory(CATEGORY_POSITION+CATEGORY_MSET)
e1:SetType(EFFECT_TYPE_ACTIVATE)
e1:SetProperty(EFFECT_FLAG_CARD_TARGET)
e1:SetCode(EVENT_FREE_CHAIN)
e1:SetHintTiming(TIMING_BATTLE_PHASE,TIMINGS_CHECK_MONSTER+TIMING_BATTLE_PHASE)
e1:SetTarget(s.target)
e1:SetOperation(s.activate)
c:RegisterEffect(e1)
```

The target callback then selects the actual card and records operation info:

```lua
Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_FACEUP)
local g=Duel.SelectTarget(tp,s.filter,tp,LOCATION_MZONE,LOCATION_MZONE,1,1,nil)
Duel.SetOperationInfo(0,CATEGORY_POSITION,g,1,0,0)
```

Read it as four layers:

| Layer | Meaning |
| --- | --- |
| `CATEGORY_POSITION+CATEGORY_MSET` | This effect belongs to the position/Set family. |
| `EFFECT_FLAG_CARD_TARGET` | It officially targets a card. |
| `SetHintTiming(...)` | The client should ask at useful Battle Phase and monster-check windows. |
| `SetOperationInfo(...)` | This Chain Link currently expects to change the selected card's position. |

## Categories

Categories are broad action labels. They answer "what kind of effect is this?"

```lua
e1:SetCategory(CATEGORY_DESTROY)
e1:SetCategory(CATEGORY_NEGATE+CATEGORY_DESTROY)
e1:SetCategory(CATEGORY_SPECIAL_SUMMON+CATEGORY_FUSION_SUMMON+CATEGORY_GRAVE_ACTION)
```

They are used by scripts and response checks that care about what an effect may
do. For example, some effects look for a Chain Link with
`CATEGORY_DESTROY`, `CATEGORY_NEGATE`, `CATEGORY_TOHAND`,
`CATEGORY_GRAVE_ACTION`, or `CATEGORY_SPECIAL_SUMMON`.

Use every category that honestly describes the effect's possible action, but
do not confuse category with resolution. This does not destroy, draw, or
Special Summon anything:

```lua
e1:SetCategory(CATEGORY_DESTROY)
```

The operation still needs a `Duel.*` call, such as
[`Duel.Destroy`](/api/functions/Duel/Destroy).

## Operation Info

Operation info is more specific than category. It records what the current
Chain Link is expected to affect, when that information is known.

For a known target, pass the selected card or group:

```lua
local g=Duel.SelectTarget(tp,s.filter,tp,0,LOCATION_MZONE,1,1,nil)
Duel.SetOperationInfo(0,CATEGORY_DESTROY,g,1,0,0)
```

For a non-targeting movement effect whose card is chosen later, pass `nil` and
record the expected count, player, and location:

```lua
Duel.SetOperationInfo(0,CATEGORY_TOHAND,nil,1,tp,LOCATION_DECK)
Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,nil,1,tp,LOCATION_EXTRA)
```

The local define comments for `Duel.SetOperationInfo` note that this data is
used by many activation checks, including effects that respond to destruction
or GY movement. In practice, bad operation info can make other cards respond
when they should not, or fail to respond when they should.

## Possible Action Versus Guaranteed Action

Sometimes a category is possible, but the exact operation is not known at
activation.

Snipe Hunter (`c84290642.lua`) may destroy its target, but only after a die
roll. The effect category includes both destroy and dice:

```lua
e1:SetCategory(CATEGORY_DESTROY+CATEGORY_DICE)
```

The target callback records only the dice operation info:

```lua
Duel.SelectTarget(tp,aux.TRUE,tp,LOCATION_ONFIELD,LOCATION_ONFIELD,1,1,nil)
Duel.SetOperationInfo(0,CATEGORY_DICE,nil,0,tp,1)
```

The operation rolls the die and destroys only on the successful result:

```lua
local d=Duel.TossDice(tp,1)
if d~=1 and d~=6 then
    Duel.Destroy(tc,REASON_EFFECT)
end
```

That pattern avoids announcing a guaranteed destroy before the random result
exists.

## Target Properties

Use `EFFECT_FLAG_CARD_TARGET` only when the effect creates official card
targets through targeting APIs.

Infinite Impermanence (`c10045474.lua`) targets a monster, so it sets the card
target property:

```lua
e1:SetCategory(CATEGORY_DISABLE)
e1:SetType(EFFECT_TYPE_ACTIVATE)
e1:SetProperty(EFFECT_FLAG_CARD_TARGET)
e1:SetCode(EVENT_FREE_CHAIN)
e1:SetHintTiming(0,TIMINGS_CHECK_MONSTER)
```

Pot of Greed (`c55144522.lua`) targets a player instead:

```lua
e1:SetCategory(CATEGORY_DRAW)
e1:SetType(EFFECT_TYPE_ACTIVATE)
e1:SetProperty(EFFECT_FLAG_PLAYER_TARGET)
e1:SetCode(EVENT_FREE_CHAIN)
```

Player-targeted effects usually store Chain data with
[`Duel.SetTargetPlayer`](/api/functions/Duel/SetTargetPlayer) and
[`Duel.SetTargetParam`](/api/functions/Duel/SetTargetParam), then read it back
with [`Duel.GetChainInfo`](/api/functions/Duel/GetChainInfo).

Do not add `EFFECT_FLAG_CARD_TARGET` to a non-targeting effect just because it
selects a card during resolution. Targeting is a rules meaning, not "a script
eventually chooses a card."

## Timing Properties

Some properties widen or refine when an effect may activate.

Cyber Dragon Infinity (`c10443957.lua`) can negate during the Damage Step and
Damage Calculation, so the Quick Effect uses both flags:

```lua
e3:SetCategory(CATEGORY_NEGATE+CATEGORY_DESTROY)
e3:SetType(EFFECT_TYPE_QUICK_O)
e3:SetCode(EVENT_CHAINING)
e3:SetProperty(EFFECT_FLAG_DAMAGE_STEP+EFFECT_FLAG_DAMAGE_CAL)
```

Those flags do not replace the condition:

```lua
function s.discon(e,tp,eg,ep,ev,re,r,rp)
    return not e:GetHandler():IsStatus(STATUS_BATTLE_DESTROYED)
        and Duel.IsChainNegatable(ev)
end
```

The property opens the broad timing. The condition still checks this exact
Chain Link.

`EFFECT_FLAG_DELAY` is common on optional triggers that should not miss their
activation window when the trigger event happens during another action. When a
local script uses it, read the surrounding event and card text carefully; do
not add it to every trigger by habit.

## Single Range And Continuous Target Flags

`EFFECT_FLAG_SINGLE_RANGE` is used when a single-card continuous effect should
only apply while the handler is in a specific range:

```lua
e1:SetType(EFFECT_TYPE_SINGLE)
e1:SetCode(EFFECT_UPDATE_ATTACK)
e1:SetProperty(EFFECT_FLAG_SINGLE_RANGE)
e1:SetRange(LOCATION_MZONE)
```

`EFFECT_FLAG_CONTINUOUS_TARGET` appears on effects that keep a continuous
relationship with their target, such as Equip Spell patterns. See
[Equip Spells and Equip Cards](equip-spells) for the full workflow.

## Oath And Cannot-Disable Flags

`EFFECT_FLAG_CANNOT_DISABLE` is common on rules that should not be switched off
by normal effect negation, such as revive limits, equip limits, Summon
conditions, and many procedure effects.

`EFFECT_FLAG_OATH` is used for once-per-turn activity promises and restrictions
that should be tied to the player. Lava Golem (`c102380.lua`) uses it when
registering the "you cannot Normal Summon/Set this turn" restriction after its
Special Summon procedure:

```lua
local e1=Effect.CreateEffect(c)
e1:SetType(EFFECT_TYPE_FIELD)
e1:SetCode(EFFECT_CANNOT_SUMMON)
e1:SetProperty(EFFECT_FLAG_PLAYER_TARGET+EFFECT_FLAG_OATH)
e1:SetReset(RESET_PHASE+PHASE_END)
e1:SetTargetRange(1,0)
Duel.RegisterEffect(e1,tp)
```

See [Count limits and once per turn](count-limits) for shared count codes and
activity counters.

## Hint Timing

`SetHintTiming` is a client prompt hint. It does not make the effect legal.

```lua
e1:SetHintTiming(TIMING_DAMAGE_STEP)
e1:SetHintTiming(0,TIMINGS_CHECK_MONSTER)
e1:SetHintTiming(TIMING_BATTLE_PHASE,TIMINGS_CHECK_MONSTER+TIMING_BATTLE_PHASE)
```

The first argument is for the handler controller. The second argument, when
present, is for the opponent. If the second argument is omitted, the local core
copies the first timing mask to both sides.

Common timing masks include:

| Timing | Typical use |
| --- | --- |
| `TIMING_MAIN_END` | Prompt near the end of a Main Phase. |
| `TIMING_BATTLE_PHASE` | Prompt during the Battle Phase. |
| `TIMING_DAMAGE_STEP` | Prompt during the Damage Step. |
| `TIMINGS_CHECK_MONSTER` | Prompt around monsters entering or changing visible state. |
| `TIMING_END_PHASE` | Prompt near the End Phase. |

Use hint timing to make legal effects visible at sensible times. Keep the real
legality in `SetCode`, `SetRange`, `SetCondition`, `SetCost`, and the
`chk==0` branch of the target callback.

For Chain response windows, Spell Speed, and Damage Step prompt details, see
[Chain Timing And Activation Windows](chain-timing-and-activation-windows).
For a practical guide to UI-facing prompts, opponent notices, target prompts,
resolution choices, and awkward/invisible effects, see
[Client UI And Prompt Behavior](client-ui-and-prompt-behavior).

## Selection Hints

`Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_*)` controls the prompt shown before a
selection.

```lua
Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_DESTROY)
Duel.SelectTarget(tp,s.filter,tp,0,LOCATION_ONFIELD,1,1,nil)
```

Pick the hint that matches the action:

| Hint | Use when selecting |
| --- | --- |
| `HINTMSG_DESTROY` | Cards to destroy. |
| `HINTMSG_REMOVE` | Cards to banish. |
| `HINTMSG_TOGRAVE` | Cards to send to the GY. |
| `HINTMSG_ATOHAND` | Cards to add to the hand. |
| `HINTMSG_SPSUMMON` | Cards to Special Summon. |
| `HINTMSG_EQUIP` | Cards to equip. |
| `HINTMSG_DISABLE` | Cards whose effects will be negated. |
| `HINTMSG_POSCHANGE` | Monsters whose battle position will change. |
| `HINTMSG_FACEUP` | Face-up cards when the action needs that visible state. |

The hint does not filter anything. The filter passed to `SelectTarget`,
`SelectMatchingCard`, or a Group selection function decides which cards are
legal.

## Common Mistakes

| Mistake | Better pattern |
| --- | --- |
| Thinking `SetCategory` performs the action. | Use a `Duel.*` function in the operation. |
| Setting operation info for an action that is not known or guaranteed yet. | Record only the known operation info; update the actual action at resolution. |
| Adding `EFFECT_FLAG_CARD_TARGET` to a non-targeting effect. | Use it only with official targeting APIs and card text that targets. |
| Using `SetHintTiming` as a legality check. | Keep legality in conditions, costs, target checks, and range/code/type. |
| Forgetting `EFFECT_FLAG_PLAYER_TARGET` for player-targeted draw, damage, recovery, or lock effects. | Add the player target property and store player data with `SetTargetPlayer`/`SetTargetParam` when needed. |
| Using a generic selection prompt. | Match `HINTMSG_*` to the action so the player understands what they are choosing. |
| Adding Damage Step flags without a real Damage Step-safe condition and operation. | Pair timing properties with local legality checks and resolution safeguards. |

Useful API pages:

- [`Effect.SetCategory`](/api/functions/Effect/SetCategory)
- [`Effect.SetProperty`](/api/functions/Effect/SetProperty)
- [`Effect.SetHintTiming`](/api/functions/Effect/SetHintTiming)
- [`Duel.SetOperationInfo`](/api/functions/Duel/SetOperationInfo)
- [`Duel.GetOperationInfo`](/api/functions/Duel/GetOperationInfo)
- [`Duel.Hint`](/api/functions/Duel/Hint)
- [`Duel.SelectTarget`](/api/functions/Duel/SelectTarget)
- [`Duel.SetTargetPlayer`](/api/functions/Duel/SetTargetPlayer)
- [Constants](/api/constants)
