# Write Your First Custom Card

This page walks through one small original script: a Normal Spell that targets
1 face-up monster, changes it to face-down Defense Position, then draws 1 card
if the position change succeeds.

It is intentionally modest. A first custom card should teach script structure,
legality, targeting, operation info, and resolution rechecks before it tries to
be clever.

## Pick The Script Shape

This effect combines two local patterns:

| Pattern | Local source |
| --- | --- |
| Target a face-up monster and change its position. | Book of Moon, `c14087893.lua` |
| Store and resolve player draw data. | Pot of Greed, `c55144522.lua` |

The custom effect will be a Spell/Trap Card activation:

```lua
e1:SetType(EFFECT_TYPE_ACTIVATE)
e1:SetCode(EVENT_FREE_CHAIN)
```

Because it targets a card, it also needs:

```lua
e1:SetProperty(EFFECT_FLAG_CARD_TARGET)
```

## Complete Script

Use this as the first full version:

```lua
local s,id=GetID()

function s.initial_effect(c)
    local e1=Effect.CreateEffect(c)
    e1:SetCategory(CATEGORY_POSITION+CATEGORY_DRAW)
    e1:SetType(EFFECT_TYPE_ACTIVATE)
    e1:SetProperty(EFFECT_FLAG_CARD_TARGET)
    e1:SetCode(EVENT_FREE_CHAIN)
    e1:SetTarget(s.target)
    e1:SetOperation(s.activate)
    c:RegisterEffect(e1)
end

function s.filter(c)
    return c:IsFaceup() and c:IsCanTurnSet()
end

function s.target(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
    if chkc then return chkc:IsLocation(LOCATION_MZONE) and s.filter(chkc) end
    if chk==0 then
        return Duel.IsExistingTarget(s.filter,tp,LOCATION_MZONE,LOCATION_MZONE,1,nil)
            and Duel.IsPlayerCanDraw(tp,1)
    end
    Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_FACEUP)
    local g=Duel.SelectTarget(tp,s.filter,tp,LOCATION_MZONE,LOCATION_MZONE,1,1,nil)
    Duel.SetTargetPlayer(tp)
    Duel.SetTargetParam(1)
    Duel.SetOperationInfo(0,CATEGORY_POSITION,g,1,0,0)
    Duel.SetOperationInfo(0,CATEGORY_DRAW,nil,0,tp,1)
end

function s.activate(e,tp,eg,ep,ev,re,r,rp)
    local tc=Duel.GetFirstTarget()
    local p,d=Duel.GetChainInfo(0,CHAININFO_TARGET_PLAYER,CHAININFO_TARGET_PARAM)
    if tc:IsRelateToEffect(e) and tc:IsLocation(LOCATION_MZONE) and tc:IsFaceup()
        and Duel.ChangePosition(tc,POS_FACEDOWN_DEFENSE)>0 then
        Duel.Draw(p,d,REASON_EFFECT)
    end
end
```

## Read The Script In Order

Start with `initial_effect`:

| Line | Why it is there |
| --- | --- |
| `SetCategory(CATEGORY_POSITION+CATEGORY_DRAW)` | The effect announces both possible actions. |
| `SetType(EFFECT_TYPE_ACTIVATE)` | This is the card activation. |
| `SetProperty(EFFECT_FLAG_CARD_TARGET)` | The chosen monster is an official Chain target. |
| `SetCode(EVENT_FREE_CHAIN)` | The Spell can be activated in a free-chain window. |
| `SetTarget` and `SetOperation` | The script has one legality/prompt callback and one resolution callback. |

Then read the filter:

```lua
function s.filter(c)
    return c:IsFaceup() and c:IsCanTurnSet()
end
```

The filter checks the action, not only the card type. A face-up monster that
cannot be changed to face-down Defense Position is not a legal target.

## Why The Target Callback Does So Much

The `target` callback has two jobs.

First, `chk==0` proves the activation is legal:

```lua
if chk==0 then
    return Duel.IsExistingTarget(s.filter,tp,LOCATION_MZONE,LOCATION_MZONE,1,nil)
        and Duel.IsPlayerCanDraw(tp,1)
end
```

This card needs a legal target and needs the player to be able to draw. If
either part is impossible, the card should not be activatable.

Second, the real activation prompts the player and records what the Chain Link
is expected to do:

```lua
local g=Duel.SelectTarget(tp,s.filter,tp,LOCATION_MZONE,LOCATION_MZONE,1,1,nil)
Duel.SetTargetPlayer(tp)
Duel.SetTargetParam(1)
Duel.SetOperationInfo(0,CATEGORY_POSITION,g,1,0,0)
Duel.SetOperationInfo(0,CATEGORY_DRAW,nil,0,tp,1)
```

`Duel.SelectTarget` records the official target. `SetTargetPlayer` and
`SetTargetParam` store the draw player and amount. `SetOperationInfo` announces
the position change and draw categories.

## Why Resolution Rechecks Everything

By the time the Chain resolves, the target may have moved, become face-down, or
stopped being related to the effect. Recheck before acting:

```lua
if tc:IsRelateToEffect(e) and tc:IsLocation(LOCATION_MZONE) and tc:IsFaceup()
    and Duel.ChangePosition(tc,POS_FACEDOWN_DEFENSE)>0 then
    Duel.Draw(p,d,REASON_EFFECT)
end
```

The draw happens only if the position change succeeds. If the target is no
longer valid, the operation does nothing.

## Safe Variations

Change one thing at a time:

| Variation | What to change |
| --- | --- |
| Draw 2 cards. | Change every draw amount from `1` to `2`. |
| Target only opponent's monsters. | Change target locations to `0,LOCATION_MZONE` from the activating player's view. |
| Destroy the target instead. | Replace `CATEGORY_POSITION`, `IsCanTurnSet`, and `Duel.ChangePosition` with the destroy pattern from [Targeting Flow](targeting-flow). |
| Make it a Quick-Play Spell. | Keep the script shape, then use the Quick-Play card type in card data and study [Quick-Play Spells](quick-play-spells). |
| Add a once-per-turn effect. | Add `SetCountLimit` and read [Count Limits](count-limits). |

## Checklist

Before testing a custom script, check:

1. File name and card ID match.
2. `local s,id=GetID()` is present.
3. `s.initial_effect(c)` registers every effect.
4. Every callback name passed to a setter exists.
5. `chk==0` checks the required action.
6. Targeting effects use `EFFECT_FLAG_CARD_TARGET`.
7. Resolution rechecks relation and current state.
8. Categories and operation info match the action.

Useful API pages:

- [`Effect.CreateEffect`](/api/functions/Effect/CreateEffect)
- [`Effect.SetCategory`](/api/functions/Effect/SetCategory)
- [`Effect.SetType`](/api/functions/Effect/SetType)
- [`Effect.SetProperty`](/api/functions/Effect/SetProperty)
- [`Effect.SetTarget`](/api/functions/Effect/SetTarget)
- [`Effect.SetOperation`](/api/functions/Effect/SetOperation)
- [`Duel.IsExistingTarget`](/api/functions/Duel/IsExistingTarget)
- [`Duel.SelectTarget`](/api/functions/Duel/SelectTarget)
- [`Duel.SetTargetPlayer`](/api/functions/Duel/SetTargetPlayer)
- [`Duel.SetTargetParam`](/api/functions/Duel/SetTargetParam)
- [`Duel.SetOperationInfo`](/api/functions/Duel/SetOperationInfo)
- [`Duel.GetChainInfo`](/api/functions/Duel/GetChainInfo)
- [`Duel.ChangePosition`](/api/functions/Duel/ChangePosition)
- [`Duel.Draw`](/api/functions/Duel/Draw)
- [`Card.IsRelateToEffect`](/api/functions/Card/IsRelateToEffect)
