# Your First Card

A small effect usually has four parts:

```lua
function s.initial_effect(c)
  local e1=Effect.CreateEffect(c)
  e1:SetType(EFFECT_TYPE_IGNITION)
  e1:SetRange(LOCATION_MZONE)
  e1:SetTarget(s.target)
  e1:SetOperation(s.operation)
  c:RegisterEffect(e1)
end
```

The important idea is that `initial_effect` creates and registers effects. The
other functions are callbacks that the engine calls later.

## Common Callback Shape

```lua
function s.target(e,tp,eg,ep,ev,re,r,rp,chk)
  if chk==0 then return true end
end

function s.operation(e,tp,eg,ep,ev,re,r,rp)
  -- resolve the effect
end
```

When you are unsure what a callback receives, check nearby real card scripts and
then open the API reference for the functions it calls.
