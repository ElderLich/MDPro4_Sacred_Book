# Effect Anatomy

Most effects are built by creating an `Effect`, setting fields on it, and then
registering it on a card.

```lua
local e1=Effect.CreateEffect(c)
e1:SetDescription(aux.Stringid(id,0))
e1:SetCategory(CATEGORY_DRAW)
e1:SetType(EFFECT_TYPE_IGNITION)
e1:SetRange(LOCATION_MZONE)
e1:SetCountLimit(1,id)
e1:SetTarget(s.drtg)
e1:SetOperation(s.drop)
c:RegisterEffect(e1)
```

The engine does not read this as prose. It reads flags and callbacks:

- `SetDescription` points at text from the card database.
- `SetCategory` announces the kind of operation.
- `SetType`, `SetCode`, and `SetRange` decide when the effect exists.
- `SetTarget` checks whether the effect can be activated and declares info.
- `SetOperation` resolves the effect.
