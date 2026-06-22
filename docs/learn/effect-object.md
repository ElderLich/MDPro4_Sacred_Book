# Creation, Building, and Registration of an Effect Object

Most card effects are built in three steps:

1. Create an `Effect`.
2. Set properties on it.
3. Register it to a card or to the Duel.

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
| `SetCode` | Which event, phase, or continuous rule does this use? |
| `SetProperty` | Does it target, work in the Damage Step, ignore immunity, and so on? |
| `SetRange` | Where must the handler be for this effect to exist or activate? |
| `SetTargetRange` | Which cards or players are affected by a field/equip/procedure effect? |
| `SetValue` | Which number or function supplies the continuous value? |
| `SetCountLimit` | How often may this effect be used? |
| `SetCondition` | Is the effect allowed to be considered? |
| `SetCost` | Can the cost be paid, and how is it paid? |
| `SetTarget` | Can it activate, and what will it affect? |
| `SetOperation` | What happens when it resolves or when a continuous event fires? |
| `SetReset` | When does a temporary effect disappear? |

## Registering to a Card

Use `c:RegisterEffect(e)` when the effect belongs to the card whose script is
loading.

```lua
local e1=Effect.CreateEffect(c)
e1:SetType(EFFECT_TYPE_SINGLE)
e1:SetCode(EFFECT_UPDATE_ATTACK)
e1:SetValue(500)
c:RegisterEffect(e1)
```

After registration, the engine knows that the card has this effect. For most
normal card text, this is the registration you want.

## Registering to the Duel

Use `Duel.RegisterEffect(e,tp)` for a temporary rule that is created while an
effect resolves and is not simply attached as one of the handler's regular
effects.

```lua
local e1=Effect.CreateEffect(e:GetHandler())
e1:SetType(EFFECT_TYPE_FIELD)
e1:SetCode(EFFECT_CANNOT_SPECIAL_SUMMON)
e1:SetTargetRange(1,0)
e1:SetTarget(s.splimit)
e1:SetReset(RESET_PHASE+PHASE_END)
Duel.RegisterEffect(e1,tp)
```

Temporary Duel effects almost always need `SetReset`. Without a reset, the
effect can last longer than intended.

## Cloning Effects

When two effects share most settings, scripts often clone the first one and
change only the difference.

```lua
local e1=Effect.CreateEffect(c)
e1:SetType(EFFECT_TYPE_FIELD)
e1:SetRange(LOCATION_MZONE)
e1:SetCode(EFFECT_UPDATE_ATTACK)
e1:SetTargetRange(LOCATION_MZONE,0)
e1:SetValue(200)
c:RegisterEffect(e1)
local e2=e1:Clone()
e2:SetCode(EFFECT_UPDATE_DEFENSE)
c:RegisterEffect(e2)
```

This pattern appears in scripts such as `c10002346.lua`: one field effect
updates ATK, the clone updates DEF.

## Building Order

The engine does not require every setter to appear in a single exact order, but
readable scripts usually group them like this:

1. User-facing fields: `SetDescription`, `SetCategory`.
2. Shape and timing: `SetType`, `SetCode`, `SetProperty`.
3. Location and limits: `SetRange`, `SetTargetRange`, `SetCountLimit`.
4. Logic: `SetCondition`, `SetCost`, `SetTarget`, `SetOperation`, `SetValue`.
5. Registration: `RegisterEffect` or `Duel.RegisterEffect`.

Keeping that order makes later review much easier.

Relevant API pages:

- [`Effect.CreateEffect`](/api/functions/Effect/CreateEffect)
- [`Card.RegisterEffect`](/api/functions/Card/RegisterEffect)
- [`Duel.RegisterEffect`](/api/functions/Duel/RegisterEffect)
- [`Effect.Clone`](/api/functions/Effect/Clone)
