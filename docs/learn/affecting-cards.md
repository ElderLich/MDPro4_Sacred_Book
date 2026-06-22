# Methods for Affecting Cards

Card scripts affect the game in two broad ways:

1. They call `Duel.*` functions to perform actions, such as destroy, send, draw,
   banish, Special Summon, equip, or change position.
2. They register effects that continuously change what cards can do or how they
   are treated.

Use engine functions and registered effects. Do not try to manually edit a card
as if it were a plain Lua table.

## Immediate Actions

Immediate actions usually happen in an operation callback.

| Outcome | Common API |
| --- | --- |
| Destroy | `Duel.Destroy` |
| Send to GY | `Duel.SendtoGrave` |
| Add to hand | `Duel.SendtoHand` |
| Return to Deck | `Duel.SendtoDeck` |
| Banish | `Duel.Remove` |
| Special Summon | `Duel.SpecialSummon` |
| Set a Spell/Trap | `Duel.SSet` |
| Set a monster | `Duel.MSet` |
| Change position | `Duel.ChangePosition` |
| Equip | `Duel.Equip` |
| Attach as Xyz Material | `Duel.Overlay` |

Example:

```lua
local tc=Duel.GetFirstTarget()
if tc and tc:IsRelateToEffect(e) then
    Duel.Destroy(tc,REASON_EFFECT)
end
```

The operation uses a `Duel` function because the action changes the game state.

## Continuous Changes

Continuous changes are registered as effects.

```lua
local e1=Effect.CreateEffect(c)
e1:SetType(EFFECT_TYPE_SINGLE)
e1:SetCode(EFFECT_UPDATE_ATTACK)
e1:SetReset(RESET_EVENT+RESETS_STANDARD)
e1:SetValue(1000)
tc:RegisterEffect(e1)
```

This pattern is used for temporary ATK/DEF changes, type changes, effect
negation, cannot-attack restrictions, and similar outcomes.

## Choosing a Target Function

Many card-affecting mistakes come from mixing up these three stages:

| Stage | Question | Example |
| --- | --- | --- |
| Filter | Does this card qualify? | `c:IsFaceup() and c:IsAbleToHand()` |
| Legality | Is there at least one card/action available now? | `Duel.IsExistingTarget(...)` |
| Resolution | Is the affected card still valid? | `tc:IsRelateToEffect(e)` |

Keep each question in the right callback.

## Negating and Preventing

Some outcomes are immediate actions:

```lua
Duel.NegateActivation(ev)
Duel.NegateEffect(ev)
```

Other outcomes are continuous restrictions:

```lua
local e1=Effect.CreateEffect(c)
e1:SetType(EFFECT_TYPE_FIELD)
e1:SetCode(EFFECT_CANNOT_ACTIVATE)
e1:SetTargetRange(0,1)
e1:SetValue(s.aclimit)
e1:SetReset(RESET_PHASE+PHASE_END)
Duel.RegisterEffect(e1,tp)
```

Use `Duel.Negate*` when resolving a negation effect. Use registered effects when
the card creates a rule that lasts for a duration.

## Changing Stats and Properties

Temporary stat changes should include a reset.

```lua
local e1=Effect.CreateEffect(e:GetHandler())
e1:SetType(EFFECT_TYPE_SINGLE)
e1:SetCode(EFFECT_UPDATE_ATTACK)
e1:SetReset(RESET_EVENT+RESETS_STANDARD)
e1:SetValue(500)
tc:RegisterEffect(e1)
```

For property changes, use the matching effect code.

```lua
e1:SetCode(EFFECT_CHANGE_TYPE)
e1:SetValue(TYPE_SPELL+TYPE_CONTINUOUS)
```

## Change Control and Equip

Changing control and equipping are not the same as moving a card to a zone by
hand. Use the appropriate Duel function so the engine can update relations,
equipment state, triggers, and legality.

```lua
Duel.GetControl(tc,tp)
Duel.Equip(tp,c,tc)
```

After equipping, register equip effects and equip limits on the Equip Card.

## A Review Checklist

Before finishing an operation that affects cards, check:

1. Did the target or selected group exist at activation?
2. If it targets, are the cards still related to the effect?
3. Does the movement/action use the correct `REASON_*` flags?
4. Does any temporary registered effect have the correct reset?
5. Does the category and operation info match the actual action?

Useful API pages:

- [`Duel.Destroy`](/api/functions/Duel/Destroy)
- [`Duel.SendtoGrave`](/api/functions/Duel/SendtoGrave)
- [`Duel.Remove`](/api/functions/Duel/Remove)
- [`Duel.SpecialSummon`](/api/functions/Duel/SpecialSummon)
- [`Duel.Equip`](/api/functions/Duel/Equip)
- [`Card.RegisterEffect`](/api/functions/Card/RegisterEffect)
