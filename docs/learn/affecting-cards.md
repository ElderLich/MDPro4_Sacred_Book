# Methods for Affecting Cards

Card scripts affect the game in two broad ways:

1. They call `Duel.*` functions to perform actions, such as destroy, send, draw,
   banish, Special Summon, equip, or change position.
2. They register effects that continuously change what cards can do or how they
   are treated.

Use engine functions and registered effects. Do not try to manually edit a card
as if it were a plain Lua table.

## Choose The Right Kind Of Effect

| Card text shape | Usually read next |
| --- | --- |
| "Activate this card/effect..." | [Activated effects](activated-effects) |
| "Target 1 card..." | [Targeting flow](targeting-flow) |
| "Destroy/send/banish/add..." | [Functions that move cards across locations](moving-cards) |
| "Gain/lose ATK/DEF..." | [Continuous stat modifiers](continuous-stat-modifiers) |
| "Negate/unaffected/cannot be targeted..." | [Negation and immunity](negation-and-immunity) |
| "Take control/swap control..." | [Control change](control-change) |
| "Change battle position/Set..." | [Battle position effects](battle-position-effects) |
| "Equip this card..." | [Equip Spells and Equip Cards](equip-spells) |
| "Inflict damage/recover LP..." | [LP Recovery and Effect Damage](lp-recovery-and-damage) |
| "Cards in this Set/archetype..." | [Archetypes and set codes](archetypes-and-setcodes) |

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
| Inflict damage | `Duel.Damage` |
| Recover LP | `Duel.Recover` |

Example:

```lua
local tc=Duel.GetFirstTarget()
if tc and tc:IsRelateToEffect(e) then
    Duel.Destroy(tc,REASON_EFFECT)
end
```

The operation uses a `Duel` function because the action changes the game state.

## Affecting Every Card In A Group

Some effects do not ask the player to choose individual cards. They affect all
cards that match a filter at the relevant moment.

Black Hole (`c53129443.lua`) is the clean local template:

```lua
function c53129443.target(e,tp,eg,ep,ev,re,r,rp,chk)
    if chk==0 then
        return Duel.IsExistingMatchingCard(aux.TRUE,tp,LOCATION_MZONE,LOCATION_MZONE,1,nil)
    end
    local sg=Duel.GetMatchingGroup(aux.TRUE,tp,LOCATION_MZONE,LOCATION_MZONE,nil)
    Duel.SetOperationInfo(0,CATEGORY_DESTROY,sg,sg:GetCount(),0,0)
end

function c53129443.activate(e,tp,eg,ep,ev,re,r,rp)
    local sg=Duel.GetMatchingGroup(aux.TRUE,tp,LOCATION_MZONE,LOCATION_MZONE,nil)
    Duel.Destroy(sg,REASON_EFFECT)
end
```

The check branch proves there is at least one monster. The real target branch
builds the current Group only to announce the expected destroy operation. The
operation builds the Group again because the field may have changed while the
Chain was resolving.

Mirror Force (`c44095762.lua`) uses the same shape with a real filter:

```lua
function c44095762.filter(c)
    return c:IsAttackPos()
end

function c44095762.target(e,tp,eg,ep,ev,re,r,rp,chk)
    if chk==0 then
        return Duel.IsExistingMatchingCard(c44095762.filter,tp,0,LOCATION_MZONE,1,nil)
    end
    local g=Duel.GetMatchingGroup(c44095762.filter,tp,0,LOCATION_MZONE,nil)
    Duel.SetOperationInfo(0,CATEGORY_DESTROY,g,g:GetCount(),0,0)
end

function c44095762.activate(e,tp,eg,ep,ev,re,r,rp)
    local g=Duel.GetMatchingGroup(c44095762.filter,tp,0,LOCATION_MZONE,nil)
    if g:GetCount()>0 then
        Duel.Destroy(g,REASON_EFFECT)
    end
end
```

Use this pattern when the text means "all matching cards," not "target those
cards." Do not store the target-branch Group and assume it is still current at
resolution. Rebuild it, or filter the stored target Group when the effect
actually targets.

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

See [Negation and immunity](negation-and-immunity) for the full split between
activation negation, effect negation, lingering monster disable, immunity,
targeting protection, and effect-destruction protection.

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

Permanent or always-on stat changes are usually registered in
`initial_effect`. Temporary stat changes are usually created during an
operation and registered to the affected card with a reset. See
[Continuous stat modifiers](continuous-stat-modifiers) for the complete
workflow.

## Change Control and Equip

Changing control and equipping are not the same as moving a card to a zone by
hand. Use the appropriate Duel function so the engine can update relations,
equipment state, triggers, and legality.

```lua
Duel.GetControl(tc,tp)
Duel.Equip(tp,c,tc)
```

After equipping, register equip effects and equip limits on the Equip Card.

See [Control change](control-change) for `Duel.GetControl`,
`Duel.SwapControl`, Monster Zone checks, owner/controller differences, and
equip-based control rules.

See [Equip Spells and Equip Cards](equip-spells) for the target, operation,
equip limit, and `EFFECT_TYPE_EQUIP` pieces together.

## Change Battle Position

One-time battle position changes use `Duel.ChangePosition`:

```lua
local tc=Duel.GetFirstTarget()
if tc:IsRelateToEffect(e) and tc:IsFaceup() then
    Duel.ChangePosition(tc,POS_FACEDOWN_DEFENSE)
end
```

Lasting position rules use registered effects such as `EFFECT_SET_POSITION`,
`EFFECT_CANNOT_CHANGE_POSITION`, or `EFFECT_CANNOT_TURN_SET`.

See [Battle position effects](battle-position-effects) for Set effects,
face-up Attack/Defense changes, forced positions, and common legality checks.

## A Review Checklist

Before finishing an operation that affects cards, check:

1. Did the target or selected group exist at activation?
2. If it targets, are the cards still related to the effect?
3. Does the movement/action use the correct `REASON_*` flags?
4. Does any temporary registered effect have the correct reset?
5. Does the category and operation info match the actual action?

Useful API pages:

- [`Duel.Destroy`](/api/functions/Duel/Destroy)
- [`Duel.GetMatchingGroup`](/api/functions/Duel/GetMatchingGroup)
- [`Duel.IsExistingMatchingCard`](/api/functions/Duel/IsExistingMatchingCard)
- [`Duel.SetOperationInfo`](/api/functions/Duel/SetOperationInfo)
- [`Duel.SendtoGrave`](/api/functions/Duel/SendtoGrave)
- [`Duel.Remove`](/api/functions/Duel/Remove)
- [`Duel.SpecialSummon`](/api/functions/Duel/SpecialSummon)
- [`Duel.Equip`](/api/functions/Duel/Equip)
- [`Duel.NegateActivation`](/api/functions/Duel/NegateActivation)
- [`Duel.GetControl`](/api/functions/Duel/GetControl)
- [`Duel.ChangePosition`](/api/functions/Duel/ChangePosition)
- [`Card.RegisterEffect`](/api/functions/Card/RegisterEffect)
