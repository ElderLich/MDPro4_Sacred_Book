# Effect.SetType

## Signature

```lua
Effect.SetType(Effect e, int type) -> void
```

## Description

Sets e's effect type flags.
The core normalizes some type combinations: Spell/Trap activation effects become field activation effects, Flip Effects receive EVENT_FLIP handling, and ignition/Quick Effects gain field behavior.

## How To Use It

Use `SetType` near the start of an effect definition. It decides whether the effect is activated, continuous, single-card, field-wide, trigger, ignition, or Quick.

A common activated ignition effect skeleton looks like this:

```lua
local e1=Effect.CreateEffect(c)
e1:SetDescription(aux.Stringid(id,0))
e1:SetCategory(CATEGORY_DESTROY)
e1:SetType(EFFECT_TYPE_IGNITION)
e1:SetRange(LOCATION_MZONE)
e1:SetCountLimit(1,id)
e1:SetTarget(s.destg)
e1:SetOperation(s.desop)
c:RegisterEffect(e1)
```

MDPro4 normalizes some type combinations. Spell/Trap activation effects become field activation effects and receive the usual hand/Spell & Trap/Field Zone activation range. Flip Effects are converted to `EVENT_FLIP` handling. Ignition and Quick effects gain field behavior internally.

## Related Functions

- [Effect.SetCode](/api/functions/Effect/SetCode)
- [Effect.SetRange](/api/functions/Effect/SetRange)
- [Card.RegisterEffect](/api/functions/Card/RegisterEffect)

## Parameters

- `e` `Effect`
- `type` `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libeffect.cpp:619`
