# Structure of a Card Script

A card script is a Lua file named after the card ID. A card with ID `12345678`
is usually loaded from:

```text
Scripts/c12345678.lua
```

The engine calls `initial_effect(c)` once to let the script register the card's
effects. The `c` parameter is the card object whose script is running.

## Modern Skeleton

```lua
local s,id=GetID()

function s.initial_effect(c)
  -- Effects are created and registered here.
end
```

`GetID()` gives the script table and card ID. Older scripts may use
`function c12345678.initial_effect(c)` directly. Both shapes bind code to the
same card.

## Usual File Shape

<div class="script-flow">
  <span>local s,id=GetID()</span>
  <span>initial_effect(c)</span>
  <span>conditions / costs / targets / operations</span>
  <span>helper filters</span>
</div>

Callbacks are normal Lua functions. The engine calls them later when an effect
is checked, activated, or resolved.

## Example

```lua
local s,id=GetID()
function s.initial_effect(c)
  local e1=Effect.CreateEffect(c)
  e1:SetDescription(aux.Stringid(id,0))
  e1:SetType(EFFECT_TYPE_IGNITION)
  e1:SetRange(LOCATION_MZONE)
  e1:SetTarget(s.target)
  e1:SetOperation(s.operation)
  c:RegisterEffect(e1)
end
```

Open a generated example such as
[Salamandra with Chain](/examples/cards/62091148) and read only its
`initial_effect` first. That gives you the map before you read the callback
details.
