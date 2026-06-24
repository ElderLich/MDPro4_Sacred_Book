# Negation And Immunity

Many card effects say "negate", "unaffected", "cannot be targeted", or
"cannot be destroyed". Those phrases are related, but they are not the same
script shape.

Use this page when the effect changes whether another effect applies to a card
or Chain Link. If the effect moves the card instead, start with
[Functions that move cards across locations](moving-cards).

## Choose The Correct Mechanic

| Card text shape | Usual script tool |
| --- | --- |
| "Negate the activation..." | [`Duel.NegateActivation`](/api/functions/Duel/NegateActivation) during the negating effect's operation. |
| "Negate that effect..." | [`Duel.NegateEffect`](/api/functions/Duel/NegateEffect) during the negating effect's operation. |
| "That monster's effects are negated until..." | Register `EFFECT_DISABLE` and `EFFECT_DISABLE_EFFECT` on that monster. |
| "Unaffected by..." | Register `EFFECT_IMMUNE_EFFECT` and provide a value filter. |
| "Cannot be targeted by..." | Register `EFFECT_CANNOT_BE_EFFECT_TARGET`. |
| "Cannot be destroyed by card effects..." | Register `EFFECT_INDESTRUCTABLE_EFFECT` or a destroy replacement effect. |

Negation usually answers "does this Chain Link or card effect apply?"
Immunity and protection answer "can this outside effect touch this card at
all?"

## Negating An Activation

Cyber Dragon Infinity (`c10443957.lua`) is a clean local example. Its Quick
Effect responds to `EVENT_CHAINING`, checks whether the Chain Link can be
negated, detaches material as cost, then negates the activation and destroys
the activating card only if the negation succeeded:

```lua
function s.discon(e,tp,eg,ep,ev,re,r,rp)
    return not e:GetHandler():IsStatus(STATUS_BATTLE_DESTROYED)
        and Duel.IsChainNegatable(ev)
end

function s.disop(e,tp,eg,ep,ev,re,r,rp)
    if Duel.NegateActivation(ev) and re:GetHandler():IsRelateToEffect(re) then
        Duel.Destroy(eg,REASON_EFFECT)
    end
end
```

The target function should announce both categories:

```lua
Duel.SetOperationInfo(0,CATEGORY_NEGATE,eg,1,0,0)
if re:GetHandler():IsDestructable() and re:GetHandler():IsRelateToEffect(re) then
    Duel.SetOperationInfo(0,CATEGORY_DESTROY,eg,1,0,0)
end
```

The important part is the return value. `Duel.NegateActivation(ev)` returns a
boolean. Follow-up actions such as destroy, banish, send to the GY, or Set are
usually gated behind that return.

## Negating Only The Effect

Use [`Duel.NegateEffect`](/api/functions/Duel/NegateEffect) when the card text
negates the resolving effect but not the activation itself. Infinite
Impermanence (`c10045474.lua`) uses it for the same-column Spell/Trap lock
while a Chain Link is solving:

```lua
function s.disop(e,tp,eg,ep,ev,re,r,rp)
    local tseq=e:GetLabel()
    local controller,loc,seq=Duel.GetChainInfo(ev,
        CHAININFO_TRIGGERING_CONTROLER,
        CHAININFO_TRIGGERING_LOCATION,
        CHAININFO_TRIGGERING_SEQUENCE)
    if loc&LOCATION_SZONE~=0 and seq<=4 and re:IsActiveType(TYPE_SPELL+TYPE_TRAP)
        and ((controller==tp and seq==tseq) or (controller==1-tp and seq==4-tseq)) then
        Duel.NegateEffect(ev)
    end
end
```

That pattern is different from "negate the activation". The Chain Link still
exists, but its effect is negated.

## Negating A Card's Effects Until A Time

Effect Veiler (`c97268402.lua`) shows the common temporary monster-negation
shape:

```lua
function s.operation(e,tp,eg,ep,ev,re,r,rp)
    local c=e:GetHandler()
    local tc=Duel.GetFirstTarget()
    if tc:IsFaceup() and tc:IsRelateToEffect(e)
        and tc:IsControler(1-tp)
        and tc:IsCanBeDisabledByEffect(e) then
        Duel.NegateRelatedChain(tc,RESET_TURN_SET)
        local e1=Effect.CreateEffect(c)
        e1:SetType(EFFECT_TYPE_SINGLE)
        e1:SetCode(EFFECT_DISABLE)
        e1:SetReset(RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
        tc:RegisterEffect(e1)
        local e2=Effect.CreateEffect(c)
        e2:SetType(EFFECT_TYPE_SINGLE)
        e2:SetCode(EFFECT_DISABLE_EFFECT)
        e2:SetValue(RESET_TURN_SET)
        e2:SetReset(RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
        tc:RegisterEffect(e2)
    end
end
```

There are three lessons packed into that small operation:

| Piece | Why it is there |
| --- | --- |
| [`Card.IsCanBeDisabledByEffect`](/api/functions/Card/IsCanBeDisabledByEffect) | Checks whether this effect is allowed to disable the target now. |
| [`Duel.NegateRelatedChain`](/api/functions/Duel/NegateRelatedChain) | Handles already-created Chain Links related to the target. |
| `EFFECT_DISABLE` plus `EFFECT_DISABLE_EFFECT` | Applies the visible "effects are negated" state to the monster until reset. |

For temporary negation, always think about reset. A missing reset creates a
lingering rule that lasts much longer than the card text says.

## Immunity

Immunity is not the same as negation. An unaffected card is still allowed to
have active effects, but outside effects that match the immunity filter do not
apply to it.

The Winged Dragon of Ra - Immortal Phoenix (`c10000090.lua`) registers
`EFFECT_IMMUNE_EFFECT` while it is in the Monster Zone:

```lua
local e3=Effect.CreateEffect(c)
e3:SetType(EFFECT_TYPE_SINGLE)
e3:SetCode(EFFECT_IMMUNE_EFFECT)
e3:SetProperty(EFFECT_FLAG_SINGLE_RANGE)
e3:SetRange(LOCATION_MZONE)
e3:SetValue(s.efilter)
c:RegisterEffect(e3)

function s.efilter(e,te)
    return te:GetOwner()~=e:GetOwner()
end
```

For `EFFECT_IMMUNE_EFFECT`, the value is usually a function. It receives the
immunity effect and the incoming effect being tested. Return `true` when the
incoming effect should not affect the protected card.

Be careful with owner and controller wording. In this local example, the
filter compares effect owners, not current controllers.

## Cannot Be Targeted

"Cannot be targeted" does not make a card unaffected. It only prevents effects
from choosing that card as an effect target.

Toon Kingdom (`c43175858.lua`) protects Toon monsters from the opponent's
targeting effects:

```lua
local e3=Effect.CreateEffect(c)
e3:SetType(EFFECT_TYPE_FIELD)
e3:SetCode(EFFECT_CANNOT_BE_EFFECT_TARGET)
e3:SetProperty(EFFECT_FLAG_IGNORE_IMMUNE)
e3:SetRange(LOCATION_FZONE)
e3:SetTargetRange(LOCATION_MZONE,0)
e3:SetTarget(aux.TargetBoolFunction(Card.IsType,TYPE_TOON))
e3:SetValue(aux.tgoval)
c:RegisterEffect(e3)
```

The local helper [`aux.tgoval`](/api/functions/Auxiliary/tgoval) means
"targeting effects controlled by the opponent." Its sibling
[`aux.tgsval`](/api/functions/Auxiliary/tgsval) is for targeting effects
controlled by the same player.

## Cannot Be Destroyed

Destruction protection has two common shapes:

1. A simple indestructible rule with `EFFECT_INDESTRUCTABLE_EFFECT`.
2. A replacement effect such as `EFFECT_DESTROY_REPLACE`.

The utility helpers mirror the targeting helpers:

```lua
e1:SetCode(EFFECT_INDESTRUCTABLE_EFFECT)
e1:SetValue(aux.indoval)
```

Use `aux.indoval` for opponent-controlled effects and `aux.indsval` for
same-player effects. Use a replacement effect when the card text says to do
something instead of destruction, such as banishing cards from the Deck.

## What To Recheck At Resolution

Card-affecting negation effects commonly recheck:

| Recheck | Example question |
| --- | --- |
| `tc:IsRelateToEffect(e)` | Is the targeted card still the same card this effect targeted? |
| `tc:IsFaceup()` | Does the effect only work on face-up monsters? |
| `tc:IsCanBeDisabledByEffect(e)` | Can this effect still disable the monster? |
| `re:GetHandler():IsRelateToEffect(re)` | Is the activating card still related to its own Chain Link? |
| `Duel.NegateActivation(ev)` return | Did the activation actually get negated? |

Do not assume the target state from activation still exists at resolution.

## Common Mistakes

| Mistake | Better pattern |
| --- | --- |
| Using `Duel.NegateEffect` for text that says "negate the activation". | Use `Duel.NegateActivation` and gate follow-up actions behind its return value. |
| Registering only `EFFECT_DISABLE` for temporary monster negation. | Pair it with `EFFECT_DISABLE_EFFECT` and the correct reset. |
| Forgetting `Duel.NegateRelatedChain` on a target whose already-created Chain Links should be disabled. | Call it before registering the lingering disable effects. |
| Treating "cannot be targeted" as "unaffected". | Use `EFFECT_CANNOT_BE_EFFECT_TARGET` only for targeting protection; use `EFFECT_IMMUNE_EFFECT` for unaffected text. |
| Writing an immunity value function that blocks your own intended effects. | Decide whether the filter should compare owner, controller, player, type, or effect source. |
| Applying a temporary disable without `RESET_PHASE+PHASE_END` or another duration. | Match the reset to the card text. |

Useful API pages:

- [`Duel.NegateActivation`](/api/functions/Duel/NegateActivation)
- [`Duel.NegateEffect`](/api/functions/Duel/NegateEffect)
- [`Duel.NegateRelatedChain`](/api/functions/Duel/NegateRelatedChain)
- [`Duel.IsChainNegatable`](/api/functions/Duel/IsChainNegatable)
- [`Card.IsCanBeDisabledByEffect`](/api/functions/Card/IsCanBeDisabledByEffect)
- [`Card.IsImmuneToEffect`](/api/functions/Card/IsImmuneToEffect)
- [`Effect.SetValue`](/api/functions/Effect/SetValue)
- [`Card.RegisterEffect`](/api/functions/Card/RegisterEffect)
