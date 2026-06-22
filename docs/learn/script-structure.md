# Structure of a Card Script

A card script is a Lua file named after the card ID. A card with ID `12345678`
is usually loaded from:

```text
Scripts/c12345678.lua
```

The engine calls `initial_effect(c)` once while loading the card. The `c`
parameter is the card object whose script is running. Inside that function, the
script creates effects and registers them to the card.

## Modern Skeleton

```lua
local s,id=GetID()

function s.initial_effect(c)
    -- Effects are created and registered here.
end
```

`GetID()` gives the script table and card ID. The table `s` is used as the
namespace for callbacks and helper filters. The variable `id` is the card ID,
which is usually passed to `aux.Stringid(id,n)` and `SetCountLimit`.

Older scripts may use `function c12345678.initial_effect(c)` directly. That
style is still common in old cards; the idea is the same, but the function names
use `c12345678` instead of `s`.

## Usual File Shape

<div class="script-flow">
  <span>local s,id=GetID()</span>
  <span>initial_effect(c)</span>
  <span>effect objects</span>
  <span>callbacks</span>
  <span>helper filters</span>
</div>

The file normally starts with the namespace, then registers effects, then
defines the callback and filter functions referenced by those effects.

## A Tiny Complete Effect

This is the smallest useful shape: an Ignition Effect that draws 1 card.

```lua
local s,id=GetID()

function s.initial_effect(c)
    local e1=Effect.CreateEffect(c)
    e1:SetDescription(aux.Stringid(id,0))
    e1:SetCategory(CATEGORY_DRAW)
    e1:SetType(EFFECT_TYPE_IGNITION)
    e1:SetRange(LOCATION_MZONE)
    e1:SetCountLimit(1,id)
    e1:SetTarget(s.drtg)
    e1:SetOperation(s.drop)
    c:RegisterEffect(e1)
end

function s.drtg(e,tp,eg,ep,ev,re,r,rp,chk)
    if chk==0 then return Duel.IsPlayerCanDraw(tp,1) end
    Duel.SetOperationInfo(0,CATEGORY_DRAW,nil,0,tp,1)
end

function s.drop(e,tp,eg,ep,ev,re,r,rp)
    Duel.Draw(tp,1,REASON_EFFECT)
end
```

Read it as a sentence:

| Line | Meaning |
| --- | --- |
| `Effect.CreateEffect(c)` | Make a new effect owned by this card. |
| `SetDescription` | Tell the client which card text line describes the effect. |
| `SetCategory` | Tell the engine what action this effect announces. |
| `SetType` | Make it an Ignition Effect. |
| `SetRange` | The card must be in the Monster Zone to activate it. |
| `SetTarget` | Use `s.drtg` to check legality and announce the draw. |
| `SetOperation` | Use `s.drop` when the Chain resolves. |
| `RegisterEffect` | Attach the effect to the card. |

## Callback Naming

Callbacks can be named however you want, but local scripts commonly use short
suffixes:

| Suffix | Common meaning |
| --- | --- |
| `con` | Condition |
| `cost` | Cost |
| `tg` | Target |
| `op` | Operation |
| `filter` | Card filter |

For example, `s.thtg` usually means "to hand target" and `s.thop` means "to
hand operation". Names do not affect the engine; only the function passed to the
setter matters.

## Reading Real Scripts

Open a generated example such as [Salamandra with Chain](/examples/cards/62091148)
and read only its `initial_effect` first. You will see several effect blocks.
Each block is a small machine: type, timing, range, callbacks, then registration.
