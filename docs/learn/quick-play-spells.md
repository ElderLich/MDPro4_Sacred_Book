# Quick-Play Spells

Quick-Play Spells are still card activations. In script, their first effect is
usually `EFFECT_TYPE_ACTIVATE` with `EVENT_FREE_CHAIN`; the card's
`TYPE_QUICKPLAY` is what makes that activation Spell Speed 2.

That one distinction prevents most beginner mistakes. Do not rewrite a
Quick-Play Spell as a monster-style `EFFECT_TYPE_QUICK_O`. Write a normal Spell
activation, then let the local core read the card type.

## The Basic Shape

Mystical Space Typhoon (`c5318639.lua`) is the smallest local pattern:

```lua
local e1=Effect.CreateEffect(c)
e1:SetCategory(CATEGORY_DESTROY)
e1:SetType(EFFECT_TYPE_ACTIVATE)
e1:SetCode(EVENT_FREE_CHAIN)
e1:SetHintTiming(0,TIMING_END_PHASE+TIMING_EQUIP)
e1:SetProperty(EFFECT_FLAG_CARD_TARGET)
e1:SetTarget(c5318639.target)
e1:SetOperation(c5318639.activate)
c:RegisterEffect(e1)
```

The activation is free-chain because it is not waiting for a specific event.
Its speed comes from the handler being a Quick-Play Spell, not from the effect
type.

## Timing Is Three Separate Things

Read a Quick-Play Spell's timing in three layers:

| Layer | Script piece | What it does |
| --- | --- | --- |
| Activation family | `EFFECT_TYPE_ACTIVATE`, `EVENT_FREE_CHAIN` or another event | Describes which window the card can use. |
| Card speed | `TYPE_QUICKPLAY` on the card data | Makes the card activation Spell Speed 2 in the local core. |
| Prompt hint | `SetHintTiming` | Helps the client decide when to offer the activation. |
| Legality | condition, cost, target, and `chk==0` | Decides whether the activation is currently legal. |

`SetHintTiming` never creates permission by itself. Mystical Space Typhoon can
be offered around End Phase or equip-related windows, but its target callback
still checks for a legal Spell/Trap target:

```lua
function c5318639.target(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
    if chkc then return chkc:IsOnField() and c5318639.filter(chkc) and chkc~=e:GetHandler() end
    if chk==0 then return Duel.IsExistingTarget(c5318639.filter,tp,LOCATION_ONFIELD,LOCATION_ONFIELD,1,e:GetHandler()) end
    Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_DESTROY)
    local g=Duel.SelectTarget(tp,c5318639.filter,tp,LOCATION_ONFIELD,LOCATION_ONFIELD,1,1,e:GetHandler())
    Duel.SetOperationInfo(0,CATEGORY_DESTROY,g,1,0,0)
end
```

If no legal target exists, the `chk==0` branch returns false. The timing hint
does not override that.

## Target At Activation, Recheck At Resolution

Quick-Play Spells are often activated in response to changing field states, so
the selected card may be gone or no longer valid by resolution. Book of Moon
(`c14087893.lua`) shows the normal defensive pattern:

```lua
function c14087893.activate(e,tp,eg,ep,ev,re,r,rp)
    local tc=Duel.GetFirstTarget()
    if tc:IsRelateToEffect(e) and tc:IsLocation(LOCATION_MZONE) and tc:IsFaceup() then
        Duel.ChangePosition(tc,POS_FACEDOWN_DEFENSE)
    end
end
```

The target was recorded with `Duel.SelectTarget` during activation. Resolution
then checks `IsRelateToEffect`, confirms the card is still in the Monster Zone,
and confirms it is still face-up before changing position.

Use `Duel.SelectMatchingCard` only when the card text chooses during
resolution and does not target. For a targeted Quick-Play Spell, use
`Duel.SelectTarget` in the target callback.

## Activation Windows And Chaining

Most simple Quick-Play Spells use `EVENT_FREE_CHAIN`. They are not responding
to the exact Chain Link in `ev`; they are just legal in open response windows
when the card type, phase rules, and target checks allow them.

Use `EVENT_CHAINING` only when the card text answers another activation, such
as "when a card or effect is activated." In that case the condition should read
the Chain Link through `ev`, `re`, `rp`, and related Chain APIs. A Quick-Play
Spell can use a response event, but it is still an activation effect, not a
monster Quick Effect.

## Set-Turn And Hand Exceptions

The local core enforces the normal Quick-Play Spell restrictions:

| Situation | Normal result | Script exception |
| --- | --- | --- |
| Quick-Play Spell Set this turn | Cannot be activated that turn | Grant `EFFECT_QP_ACT_IN_SET_TURN` when card text allows it. |
| Quick-Play Spell from the hand on the opponent's turn | Cannot be activated by default | Grant `EFFECT_QP_ACT_IN_NTPHAND` when card text allows it. |

Do not try to express those exceptions with `SetHintTiming`, target filters, or
`SetRange(LOCATION_HAND)`. Local scripts grant them as separate effects when a
card text really creates that permission.

## Common Spell Speed Mistakes

| Mistake | Better pattern |
| --- | --- |
| Writing the activation as `EFFECT_TYPE_QUICK_O`. | Use `EFFECT_TYPE_ACTIVATE`; the card type supplies Spell Speed 2. |
| Treating `SetHintTiming` as a legality check. | Keep the legality in condition, cost, and `chk==0`. |
| Targeting with `SelectMatchingCard`. | Use `SelectTarget` and `EFFECT_FLAG_CARD_TARGET` for targeted text. |
| Destroying or changing the target without a relation check. | Re-read the target and call `tc:IsRelateToEffect(e)`. |
| Adding hand or set-turn rules to the target callback. | Use the proper Quick-Play exception effect when the card text grants it. |
| Assuming Spell Speed 2 means "can always chain." | The card still needs a legal activation window, a legal target, and any cost. |

## Useful API Pages

- [`Effect.SetType`](/api/functions/Effect/SetType)
- [`Effect.SetCode`](/api/functions/Effect/SetCode)
- [`Effect.SetHintTiming`](/api/functions/Effect/SetHintTiming)
- [`Effect.SetProperty`](/api/functions/Effect/SetProperty)
- [`Effect.SetTarget`](/api/functions/Effect/SetTarget)
- [`Effect.SetOperation`](/api/functions/Effect/SetOperation)
- [`Duel.IsExistingTarget`](/api/functions/Duel/IsExistingTarget)
- [`Duel.SelectTarget`](/api/functions/Duel/SelectTarget)
- [`Duel.GetFirstTarget`](/api/functions/Duel/GetFirstTarget)
- [`Duel.SetOperationInfo`](/api/functions/Duel/SetOperationInfo)
- [`Card.IsRelateToEffect`](/api/functions/Card/IsRelateToEffect)
- [`Duel.Destroy`](/api/functions/Duel/Destroy)
- [`Duel.ChangePosition`](/api/functions/Duel/ChangePosition)

Related lessons:

- [Spell Card Patterns](spell-card-patterns)
- [Chain Timing And Activation Windows](chain-timing-and-activation-windows)
- [Targeting flow](targeting-flow)
- [Common Script Errors And Debugging](common-script-errors-and-debugging)
