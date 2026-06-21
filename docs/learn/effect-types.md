# EFFECT_TYPE Constants and Templates

`SetType` decides the broad shape of an effect. Some scripts combine values with
`+` because a field trigger, for example, is both `EFFECT_TYPE_FIELD` and
`EFFECT_TYPE_TRIGGER_O`.

## Common Types

| Type | Typical use | Common companion setters |
| --- | --- | --- |
| `EFFECT_TYPE_ACTIVATE` | Activating a Spell/Trap Card. | `SetCode(EVENT_FREE_CHAIN)`, `SetTarget`, `SetOperation` |
| `EFFECT_TYPE_IGNITION` | An effect the turn player chooses to activate in an open game state. | `SetRange`, `SetCountLimit`, `SetTarget`, `SetOperation` |
| `EFFECT_TYPE_TRIGGER_O` | Optional trigger effect. | `SetCode`, `SetProperty(EFFECT_FLAG_DELAY)` when needed |
| `EFFECT_TYPE_TRIGGER_F` | Mandatory trigger effect. | `SetCode`, `SetCondition`, `SetOperation` |
| `EFFECT_TYPE_QUICK_O` | Optional fast effect. | `SetCode(EVENT_FREE_CHAIN)`, timing hints, count limits |
| `EFFECT_TYPE_SINGLE` | Continuous property of the handler itself. | `SetCode`, `SetValue`, sometimes `SetCondition` |
| `EFFECT_TYPE_FIELD` | Applies to cards or players in a range. | `SetRange`, `SetTargetRange`, `SetTarget` |
| `EFFECT_TYPE_CONTINUOUS` | Watches an event and runs without activation. | `SetCode`, `SetOperation` |
| `EFFECT_TYPE_EQUIP` | Equip Card effect applied to the equipped monster. | `SetCode`, `SetValue` |

## Template: Ignition Effect

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

## Template: Optional Trigger

```lua
local e1=Effect.CreateEffect(c)
e1:SetDescription(aux.Stringid(id,0))
e1:SetCategory(CATEGORY_TOHAND)
e1:SetType(EFFECT_TYPE_FIELD+EFFECT_TYPE_TRIGGER_O)
e1:SetCode(EVENT_TO_GRAVE)
e1:SetRange(LOCATION_MZONE)
e1:SetProperty(EFFECT_FLAG_DELAY)
e1:SetCondition(s.thcon)
e1:SetTarget(s.thtg)
e1:SetOperation(s.thop)
c:RegisterEffect(e1)
```

See all values in [constants](/api/constants).
