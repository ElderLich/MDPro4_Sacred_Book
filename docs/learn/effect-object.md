# Creation, Building, and Registration of an Effect Object

Most card effects are built in three steps:

1. Create an `Effect`.
2. Set properties on it.
3. Register it to a card or to the duel.

```lua
local e1=Effect.CreateEffect(c)
e1:SetDescription(aux.Stringid(id,0))
e1:SetCategory(CATEGORY_TOHAND)
e1:SetType(EFFECT_TYPE_IGNITION)
e1:SetRange(LOCATION_MZONE)
e1:SetCountLimit(1,id)
e1:SetTarget(s.thtg)
e1:SetOperation(s.thop)
c:RegisterEffect(e1)
```

## What Each Setter Answers

| Setter | Question |
| --- | --- |
| `SetDescription` | Which card text line or prompt should be shown? |
| `SetCategory` | What kind of action should the engine announce? |
| `SetType` | What kind of effect is this? |
| `SetCode` | Which event or rule does this react to? |
| `SetProperty` | Does it target, damage step, cannot be disabled, and so on? |
| `SetRange` | Where must the handler be for this effect to exist or activate? |
| `SetCountLimit` | How often may this effect be used? |
| `SetTarget` | Can it activate, and what will it affect? |
| `SetOperation` | What happens when it resolves? |

## Registering

Use `c:RegisterEffect(e)` when the effect belongs to the card. Use
`Duel.RegisterEffect(e,tp)` for temporary field-wide effects that are created
while resolving another effect.

Relevant API pages:

- [`Effect.CreateEffect`](/api/functions/Effect/CreateEffect)
- [`Card.RegisterEffect`](/api/functions/Card/RegisterEffect)
- [`Duel.RegisterEffect`](/api/functions/Duel/RegisterEffect)
