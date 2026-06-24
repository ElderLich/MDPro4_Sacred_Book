# Mind Scan

Mind Scan (`34298391`) is a Continuous Trap case study for information effects.
It is not in the local `cards.cdb` at the time of this note, so this page is
hand-written from the imported local script and the card details supplied from
the Yugipedia card entry.

The script source is `Scripts/c34298391.lua`, imported from the local
`ygopro-scripts` update ending at commit `06ccc5a99`.

## What The Card Needs

Mind Scan has two separate jobs:

| Job | Script shape |
| --- | --- |
| Keep the opponent's hand revealed while you have a "Toon" card in your field or GY. | A field effect in the Spell & Trap Zone using `EFFECT_PUBLIC` and `SetTargetRange(0,LOCATION_HAND)`. |
| Let you inspect the opponent's Set cards while that same condition is true. | A cloned field effect using `EFFECT_REVEAL_ONFIELD`, filtered to face-down cards on the opponent's field. |
| Once per turn, declare a card name that has not appeared earlier in the current Chain, then negate activated effects from cards with that original name until the End Phase while Mind Scan stays face-up. | A `LOCATION_SZONE` Quick Effect that stores the declared code, then registers an `EVENT_CHAIN_SOLVING` watcher. |

The card's public-information effect is continuous-like. The declared-name
negation is an activated Quick-like effect. Keeping those in separate effect
objects makes the script easier to reason about.

## Activation Shell

Like many Continuous Traps, the first effect simply activates the card:

```lua
local e1=Effect.CreateEffect(c)
e1:SetType(EFFECT_TYPE_ACTIVATE)
e1:SetCode(EVENT_FREE_CHAIN)
c:RegisterEffect(e1)
```

The card's later effects are separate `LOCATION_SZONE` effects. Do not put the
hand reveal, Set-card reveal, or declared-name negation inside the activation
operation.

## Revealing The Hand

The opponent's hand is handled by `EFFECT_PUBLIC`:

```lua
local e2=Effect.CreateEffect(c)
e2:SetType(EFFECT_TYPE_FIELD)
e2:SetCode(EFFECT_PUBLIC)
e2:SetRange(LOCATION_SZONE)
e2:SetCondition(s.picon)
e2:SetTargetRange(0,LOCATION_HAND)
c:RegisterEffect(e2)
```

The condition checks the controller's field and GY for a face-up or otherwise
public "Toon" card:

```lua
function s.cfilter(c)
    return c:IsFaceupEx() and c:IsSetCard(0x62)
end
function s.picon(e)
    return Duel.IsExistingMatchingCard(s.cfilter,e:GetHandlerPlayer(),LOCATION_ONFIELD+LOCATION_GRAVE,0,1,nil)
end
```

`Card.IsFaceupEx` matters here because the GY is a public location. A plain
`IsFaceup` check is usually for cards currently on the field.

## Revealing Set Cards

Older scripts often had to force information updates manually with
`Duel.ConfirmCards`. Mind Scan uses the local core-supported effect code
`EFFECT_REVEAL_ONFIELD` instead:

```lua
local e3=e2:Clone()
e3:SetCode(EFFECT_REVEAL_ONFIELD)
e3:SetTarget(aux.TargetBoolFunction(Card.IsFacedown))
e3:SetTargetRange(0,LOCATION_ONFIELD)
c:RegisterEffect(e3)
```

This is a clean pattern for "you can look at Set cards" effects:

| Piece | Why it is there |
| --- | --- |
| `e2:Clone()` | Reuses the same type, range, and condition as the hand-reveal effect. |
| `EFFECT_REVEAL_ONFIELD` | Marks affected on-field face-down cards as inspectable to the effect controller. |
| `aux.TargetBoolFunction(Card.IsFacedown)` | Limits the continuous effect to Set cards. |
| `SetTargetRange(0,LOCATION_ONFIELD)` | Applies only to the opponent's on-field cards. |

This behavior is locally verified in `ygopro-core`: `effect.h` defines
`EFFECT_REVEAL_ONFIELD`, `card.cpp` checks it for on-field cards, and
`effect.cpp` treats it as a special code that can apply to face-down cards
without the usual `EFFECT_FLAG_SET_AVAILABLE` requirement.

## Declared-Name Quick Effect

The once-per-turn part is a separate Quick Effect:

```lua
local e4=Effect.CreateEffect(c)
e4:SetDescription(aux.Stringid(id,1))
e4:SetCategory(CATEGORY_DISABLE)
e4:SetType(EFFECT_TYPE_QUICK_O)
e4:SetCode(EVENT_FREE_CHAIN)
e4:SetRange(LOCATION_SZONE)
e4:SetHintTiming(0,TIMING_DRAW+TIMINGS_CHECK_MONSTER)
e4:SetCountLimit(1,id)
e4:SetCondition(s.accon)
e4:SetTarget(s.actg)
e4:SetOperation(s.acop)
c:RegisterEffect(e4)
```

The activation condition requires a Toon monster and a "Toon" Spell in the
controller's field and/or GY:

```lua
function s.cfilter2(c)
    return c:IsFaceupEx() and c:IsType(TYPE_TOON)
end
function s.cfilter3(c)
    return c:IsFaceupEx() and c:IsSetCard(0x62) and c:IsType(TYPE_SPELL)
end
function s.accon(e)
    return Duel.IsExistingMatchingCard(s.cfilter2,e:GetHandlerPlayer(),LOCATION_MZONE+LOCATION_GRAVE,0,1,nil)
        and Duel.IsExistingMatchingCard(s.cfilter3,e:GetHandlerPlayer(),LOCATION_ONFIELD+LOCATION_GRAVE,0,1,nil)
end
```

Notice that the Toon monster check uses `TYPE_TOON`, while the "Toon" Spell
check uses set code `0x62` plus `TYPE_SPELL`. Toon subtype and Toon archetype
support are different questions.

## Excluding Names Already Used In This Chain

The target function stores the announced card code as Chain target data. If this
is Chain Link 1, any card can be announced:

```lua
local ac=Duel.AnnounceCard(tp)
Duel.SetTargetParam(ac)
Duel.SetOperationInfo(0,CATEGORY_ANNOUNCE,nil,0,tp,0)
```

If earlier Chain Links exist, the script collects their triggering cards,
deduplicates their current codes, and passes an opcode filter to
`Duel.AnnounceCard`:

```lua
local ch=Duel.GetCurrentChain()
local g=Group.CreateGroup()
for i=1,ch-1 do
    local te=Duel.GetChainInfo(i,CHAININFO_TRIGGERING_EFFECT)
    g:AddCard(te:GetHandler())
end

local codes={}
local ag=Group.CreateGroup()
for c in aux.Next(g) do
    local code=c:GetCode()
    if not ag:IsExists(Card.IsCode,1,nil,code) then
        ag:AddCard(c)
        table.insert(codes,code)
    end
end
table.sort(codes)

local afilter={codes[1],OPCODE_ISCODE}
for i=2,#codes do
    table.insert(afilter,codes[i])
    table.insert(afilter,OPCODE_ISCODE)
    table.insert(afilter,OPCODE_OR)
end
table.insert(afilter,OPCODE_NOT)
local ac=Duel.AnnounceCard(tp,table.unpack(afilter))
Duel.SetTargetParam(ac)
```

The important learner idea is not the opcode syntax itself. The important idea
is that the forbidden names are gathered from the Chain that already exists,
then `Duel.AnnounceCard` receives a filter that excludes those names.

## Negating Matching Activated Effects

At resolution, Mind Scan checks that it is still face-up and related to the
Chain, stores its current field ID, and registers a temporary watcher:

```lua
function s.acop(e,tp,eg,ep,ev,re,r,rp)
    local c=e:GetHandler()
    if c:IsRelateToChain() and c:IsFaceup() then
        local ac=Duel.GetChainInfo(0,CHAININFO_TARGET_PARAM)
        local fid=c:GetFieldID()
        c:RegisterFlagEffect(id,RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END,0,1,fid)
        local e1=Effect.CreateEffect(c)
        e1:SetType(EFFECT_TYPE_FIELD+EFFECT_TYPE_CONTINUOUS)
        e1:SetCode(EVENT_CHAIN_SOLVING)
        e1:SetCondition(s.discon)
        e1:SetOperation(s.disop)
        e1:SetLabel(ac,fid)
        e1:SetLabelObject(c)
        e1:SetReset(RESET_PHASE+PHASE_END)
        Duel.RegisterEffect(e1,tp)
    end
end
```

The watcher negates matching activated effects as they resolve:

```lua
function s.discon(e,tp,eg,ep,ev,re,r,rp)
    local ac,fid=e:GetLabel()
    local ec=e:GetLabelObject()
    return ec:IsFaceupEx()
        and ec:GetFlagEffectLabel(id)==fid
        and re:GetHandler():IsOriginalCodeRule(ac)
end
function s.disop(e,tp,eg,ep,ev,re,r,rp)
    Duel.NegateEffect(ev)
end
```

`IsOriginalCodeRule` is the key name check here. The card text cares about the
original card name, so a temporary name or code change should not dodge the
declared-name restriction.

The field ID flag is the safety latch. If the original Mind Scan leaves the
field and another copy appears, the old watcher should not keep working for the
new card.

## Common Mistakes

| Mistake | Better pattern |
| --- | --- |
| Manually confirming Set cards over and over. | Use `EFFECT_REVEAL_ONFIELD` for continuous inspectability when the core supports it. |
| Using `EFFECT_PUBLIC` for Set cards on the field. | Use `EFFECT_PUBLIC` for the hand and `EFFECT_REVEAL_ONFIELD` for face-down on-field cards. |
| Checking only `Card.IsFaceup` in the GY. | Use `Card.IsFaceupEx` when the check spans field and public non-field locations. |
| Registering a lingering negate watcher without tying it to the source card. | Store the field ID and require the same face-up card to still be present. |
| Matching the declared name with `IsCode`. | Use `IsOriginalCodeRule` when the effect says original name. |

## API Links

- [`Effect.CreateEffect`](/api/functions/Effect/CreateEffect)
- [`Effect.Clone`](/api/functions/Effect/Clone)
- [`Effect.SetType`](/api/functions/Effect/SetType)
- [`Effect.SetCode`](/api/functions/Effect/SetCode)
- [`Effect.SetRange`](/api/functions/Effect/SetRange)
- [`Effect.SetTargetRange`](/api/functions/Effect/SetTargetRange)
- [`Effect.SetTarget`](/api/functions/Effect/SetTarget)
- [`Effect.SetHintTiming`](/api/functions/Effect/SetHintTiming)
- [`Effect.SetCountLimit`](/api/functions/Effect/SetCountLimit)
- [`Effect.SetLabel`](/api/functions/Effect/SetLabel)
- [`Effect.SetLabelObject`](/api/functions/Effect/SetLabelObject)
- [`Duel.IsExistingMatchingCard`](/api/functions/Duel/IsExistingMatchingCard)
- [`Duel.GetCurrentChain`](/api/functions/Duel/GetCurrentChain)
- [`Duel.GetChainInfo`](/api/functions/Duel/GetChainInfo)
- [`Duel.AnnounceCard`](/api/functions/Duel/AnnounceCard)
- [`Duel.SetTargetParam`](/api/functions/Duel/SetTargetParam)
- [`Duel.SetOperationInfo`](/api/functions/Duel/SetOperationInfo)
- [`Duel.RegisterEffect`](/api/functions/Duel/RegisterEffect)
- [`Duel.NegateEffect`](/api/functions/Duel/NegateEffect)
- [`Card.IsFaceupEx`](/api/functions/Card/IsFaceupEx)
- [`Card.IsFacedown`](/api/functions/Card/IsFacedown)
- [`Card.IsSetCard`](/api/functions/Card/IsSetCard)
- [`Card.IsType`](/api/functions/Card/IsType)
- [`Card.IsRelateToChain`](/api/functions/Card/IsRelateToChain)
- [`Card.GetFieldID`](/api/functions/Card/GetFieldID)
- [`Card.RegisterFlagEffect`](/api/functions/Card/RegisterFlagEffect)
- [`Card.GetFlagEffectLabel`](/api/functions/Card/GetFlagEffectLabel)
- [`Card.IsOriginalCodeRule`](/api/functions/Card/IsOriginalCodeRule)
- [`Auxiliary.TargetBoolFunction`](/api/functions/Auxiliary/TargetBoolFunction)
- [`Auxiliary.Next`](/api/functions/Auxiliary/Next)
- [Constant reference](/api/constants)

Related learning pages: [Trap Card Patterns](/learn/trap-card-patterns),
[Toon Monsters](/learn/toon-monsters),
[Chain Timing And Activation Windows](/learn/chain-timing-and-activation-windows),
[Negation And Immunity](/learn/negation-and-immunity), and
[Reset Flags And Effect Duration](/learn/reset-flags-and-duration).
