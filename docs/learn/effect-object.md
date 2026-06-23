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
| `SetHintTiming` | Which timing hints should the client show for optional fast effects? |
| `SetCondition` | Is the effect allowed to be considered? |
| `SetCost` | Can the cost be paid, and how is it paid? |
| `SetTarget` | Can it activate, and what will it affect? |
| `SetOperation` | What happens when it resolves or when a continuous event fires? |
| `SetLabel` | Which small integer should this effect remember? |
| `SetLabelObject` | Which object, usually another Effect or Group, should this effect remember? |
| `SetReset` | When does a temporary effect disappear? |

## User-Facing Text And Categories

`SetDescription` usually receives `aux.Stringid(id,n)`, where `n` selects the
card text string shown to the player for that effect.

```lua
e1:SetDescription(aux.Stringid(id,0))
```

Some scripts use built-in description constants or raw description IDs. Prefer
`aux.Stringid(id,n)` when the prompt belongs to this card's own text.

`SetCategory` stores category flags. Combine multiple categories with the same
bit-flag style used by local scripts.

```lua
e1:SetCategory(CATEGORY_TOHAND+CATEGORY_SEARCH)
```

The category should describe what the effect announces, not every helper check
inside the script.

## Properties

`SetProperty` controls special handling such as targeting, Damage Step
permission, delayed triggers, or continuous targeting.

```lua
e1:SetProperty(EFFECT_FLAG_CARD_TARGET+EFFECT_FLAG_DAMAGE_STEP)
```

The local core accepts a second property slot too. Local scripts mostly use the
first slot, but the signature is:

```lua
e1:SetProperty(prop1,prop2)
```

Use the second slot only for constants that are documented as second-property
flags. Do not mix ordinary `EFFECT_FLAG_*` values into the wrong slot.

## Hint Timing

`SetHintTiming` controls when the client should offer an optional activation
prompt. The local define file documents the second argument as the handler
controller's timing and the optional third argument as the opponent-turn timing.
If the third argument is omitted, the second value is reused.

```lua
e1:SetHintTiming(TIMING_END_PHASE)
e1:SetHintTiming(0,TIMINGS_CHECK_MONSTER+TIMING_MAIN_END)
e1:SetHintTiming(TIMING_DAMAGE_STEP,TIMING_DAMAGE_STEP+TIMING_END_PHASE)
```

This does not make an effect legal by itself. It only helps the client ask at
the right windows after the effect's type, code, condition, cost, and target
checks allow activation.

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

Cloning copies the current settings. Change the fields that differ before
registration. If two effects need different reset, category, code, target, or
operation behavior, set those differences explicitly on the clone.

## Labels And Label Objects

`SetLabel` is useful for small numbers that the operation needs later.

```lua
e:SetLabel(op)
```

The local core supports multiple integer labels.

```lua
e:SetLabel(race,attribute)
local race,attribute=e:GetLabel()
```

`SetLabelObject` stores a Lua-exposed object. Grant effects commonly store the
effect object that will be granted to other cards.

```lua
local ge=Effect.CreateEffect(c)
ge:SetType(EFFECT_TYPE_SINGLE)
ge:SetCode(EFFECT_UPDATE_ATTACK)
ge:SetValue(500)

local e1=Effect.CreateEffect(c)
e1:SetType(EFFECT_TYPE_FIELD+EFFECT_TYPE_GRANT)
e1:SetLabelObject(ge)
c:RegisterEffect(e1)
```

Use labels for simple Chain choices. Use label objects only when the local
script pattern expects an object to be attached to the effect.

When storing a `Group` in a label object beyond the current callback, local
scripts commonly call `g:KeepAlive()` and later clean up the kept group when the
effect no longer needs it. Do not use a label object as a casual global
variable; it creates lifetime concerns that a plain label avoids.

## Reset For Temporary Effects

Effects created in `initial_effect` are usually part of the card's normal text.
Effects created during an operation are usually temporary and should say when
they disappear.

```lua
e1:SetReset(RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
```

The exact reset depends on the card text. A stat boost until the End Phase, a
lingering summon restriction, and a copied effect do not necessarily share the
same reset flags.

## Building Order

The engine does not require every setter to appear in a single exact order, but
readable scripts usually group them like this:

1. User-facing fields: `SetDescription`, `SetCategory`.
2. Shape and timing: `SetType`, `SetCode`, `SetProperty`.
3. Location and limits: `SetRange`, `SetTargetRange`, `SetCountLimit`.
4. Logic and stored data: `SetCondition`, `SetCost`, `SetTarget`,
   `SetOperation`, `SetValue`, `SetLabel`, `SetLabelObject`.
5. Registration: `RegisterEffect` or `Duel.RegisterEffect`.

Keeping that order makes later review much easier.

Relevant API pages:

- [`Effect.CreateEffect`](/api/functions/Effect/CreateEffect)
- [`Card.RegisterEffect`](/api/functions/Card/RegisterEffect)
- [`Duel.RegisterEffect`](/api/functions/Duel/RegisterEffect)
- [`Effect.Clone`](/api/functions/Effect/Clone)
