# Structure of a Card Script

New to Lua? Read [Lua Essentials](lua-essentials) first for functions, masks,
`nil`, and the difference between passing a callback and calling it.

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

Both styles are valid in local scripts. When writing new tutorial examples,
Sacred Book uses `local s,id=GetID()` because it keeps callback names short and
keeps the card ID available for descriptions and count limits.

If an old-style script has the wrong table name, the engine may fail while
trying to call the card's `initial_effect`. Check that the file name, card ID,
and `c12345678.initial_effect` prefix all match the loaded card.

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

## What Belongs In `initial_effect`

`initial_effect(c)` should register the card's effect objects. It should not
pay costs, select targets, or resolve effects immediately.

```lua
function s.initial_effect(c)
    local e1=Effect.CreateEffect(c)
    e1:SetType(EFFECT_TYPE_SINGLE)
    e1:SetCode(EFFECT_UPDATE_ATTACK)
    e1:SetValue(500)
    c:RegisterEffect(e1)
end
```

Read `c:RegisterEffect(e1)` as method-call syntax for registering the effect on
the card. Local scripts use this colon style throughout. The object before the
colon becomes the first argument to the underlying function.

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

## Callback Parameters

Activated-effect callbacks often keep the same parameter list even when only a
few values are used.

```lua
function s.target(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
    -- e: the Effect object
    -- tp: the activating player
    -- chk: legality check branch
    -- chkc: manual target recheck branch
end
```

Filters are smaller and start with the candidate card.

```lua
function s.filter(c,e,tp)
    return c:IsLevelBelow(4)
        and c:IsCanBeSpecialSummoned(e,0,tp,false,false)
end
```

Extra filter arguments are supplied by the Duel or Group function that calls the
filter.

## Comments And Local Style

Local scripts often use short comments above effect blocks:

```lua
--draw
local e1=Effect.CreateEffect(c)
```

Use comments to separate effects or explain a non-obvious rule. The effect
setters themselves should usually be readable without a comment on every line.

## Reading Real Scripts

Open a generated example such as [Salamandra with Chain](/examples/cards/62091148)
and read only its `initial_effect` first. You will see several effect blocks.
Each block is a small machine: type, timing, range, callbacks, then registration.

After that, jump to the callback names referenced by the block. Read helper
filters last. They usually answer only "which cards count?"
