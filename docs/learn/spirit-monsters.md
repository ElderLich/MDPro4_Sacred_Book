# Spirit Monsters

Spirit Monsters usually return to the hand during the End Phase of the turn
they were Summoned or flipped face-up. Local scripts do not hand-write that
End Phase trigger every time. They usually call
[`aux.EnableSpiritReturn`](/api/functions/Auxiliary/EnableSpiritReturn).

The helper only handles the return setup. Other Spirit text, such as "cannot
be Special Summoned", extra Normal Summons, searches, or Ritual procedure
rules, must still be scripted separately.

## The Standard Return Setup

Most simple Spirit Monsters use:

```lua
function s.initial_effect(c)
    aux.EnableSpiritReturn(c,EVENT_SUMMON_SUCCESS,EVENT_FLIP)
end
```

The event list matters. The helper registers continuous single-card effects for
the events you pass. When one of those events happens, the helper creates the
End Phase return effects on that monster.

The common pair is:

| Event | Why it is included |
| --- | --- |
| `EVENT_SUMMON_SUCCESS` | The monster was Normal Summoned. |
| `EVENT_FLIP` | The monster was flipped face-up. |

If a Spirit Monster should return after a Special Summon, its script must
include an event that catches that Summon. Do not assume the helper covers
events you did not pass.

## What The Helper Creates

When the listed event happens, `aux.EnableSpiritReturn` calls
`aux.SpiritReturnReg`. That function creates temporary End Phase effects with:

| Piece | Value |
| --- | --- |
| Type | `EFFECT_TYPE_FIELD+EFFECT_TYPE_TRIGGER_F` for forced return. |
| Code | `EVENT_PHASE+PHASE_END`. |
| Range | `LOCATION_MZONE`. |
| Category | `CATEGORY_TOHAND`. |
| Reset | Standard event reset plus End Phase reset. |

The forced target always announces the handler:

```lua
Duel.SetOperationInfo(0,CATEGORY_TOHAND,e:GetHandler(),1,0,0)
```

The operation uses the normal resolution guard:

```lua
function aux.SpiritReturnOperation(e,tp,eg,ep,ev,re,r,rp)
    local c=e:GetHandler()
    if c:IsRelateToEffect(e) then
        Duel.SendtoHand(c,nil,REASON_EFFECT)
    end
end
```

Use [`Duel.SendtoHand`](/api/functions/Duel/SendtoHand) for the return, not a
manual location edit.

## Optional And Suppressed Returns

Two local effect codes modify the shared return:

| Effect code | Result |
| --- | --- |
| `EFFECT_SPIRIT_DONOT_RETURN` | The shared return does not happen. |
| `EFFECT_SPIRIT_MAYNOT_RETURN` | The forced return is replaced by an optional return. |

Yata Mirror (`c1200843.lua`) equips to a Spirit Monster and gives it
`EFFECT_SPIRIT_MAYNOT_RETURN`:

```lua
local e1=Effect.CreateEffect(c)
e1:SetType(EFFECT_TYPE_EQUIP)
e1:SetCode(EFFECT_SPIRIT_MAYNOT_RETURN)
e1:SetRange(LOCATION_SZONE)
c:RegisterEffect(e1)
```

The helper's optional target checks that the handler can currently return to
the hand:

```lua
function aux.SpiritReturnTargetOptional(e,tp,eg,ep,ev,re,r,rp,chk)
    if chk==0 then return e:GetHandler():IsAbleToHand() end
    Duel.SetOperationInfo(0,CATEGORY_TOHAND,e:GetHandler(),1,0,0)
end
```

That `IsAbleToHand` check is only on the optional target. The forced return
target always succeeds because mandatory effects still need to be placed on the
Chain when possible.

## Custom Spirit Return Effects

Some Spirit monsters need a custom End Phase operation. Spirit Ritual Monsters
are a good example: they return to the hand and then do something else.

Shinobaroness Peacock (`c25415052.lua`) uses a custom registration operation
instead of the one-line helper. It still reuses the shared return conditions:

```lua
function s.retreg(e,tp,eg,ep,ev,re,r,rp)
    local c=e:GetHandler()
    local e1=Effect.CreateEffect(c)
    e1:SetType(EFFECT_TYPE_FIELD+EFFECT_TYPE_TRIGGER_F)
    e1:SetDescription(1104)
    e1:SetCategory(CATEGORY_TOHAND+CATEGORY_SPECIAL_SUMMON+CATEGORY_TOKEN)
    e1:SetCode(EVENT_PHASE+PHASE_END)
    e1:SetRange(LOCATION_MZONE)
    e1:SetCountLimit(1)
    e1:SetReset(RESET_EVENT+0x1ee0000+RESET_PHASE+PHASE_END)
    e1:SetCondition(aux.SpiritReturnConditionForced)
    e1:SetTarget(s.rettg)
    e1:SetOperation(s.retop)
    c:RegisterEffect(e1)

    local e2=e1:Clone()
    e2:SetType(EFFECT_TYPE_FIELD+EFFECT_TYPE_TRIGGER_O)
    e2:SetCondition(aux.SpiritReturnConditionOptional)
    c:RegisterEffect(e2)
end
```

That pattern is useful when the return itself is only the first part of the End
Phase effect. Keep the shared forced/optional conditions so cards like Yata
Mirror still interact with the custom return.

## Spirit Support Filters

Use `TYPE_SPIRIT` for Spirit Monsters:

```lua
function s.filter(c)
    return c:IsFaceup() and c:IsType(TYPE_SPIRIT)
end
```

Spirit support cards often mark their own text type:

```lua
s.has_text_type=TYPE_SPIRIT
```

Then a card can search Spirit-related Spell/Trap Cards with
[`aux.IsTypeInText`](/api/functions/Auxiliary/IsTypeInText):

```lua
function s.thfilter(c)
    return c:IsType(TYPE_SPELL+TYPE_TRAP)
        and aux.IsTypeInText(c,TYPE_SPIRIT)
        and c:IsAbleToHand()
end
```

Shinobaroness Shade Peacock (`c33325951.lua`) uses that shape.

## Spirit Cards That Are Not Simple Monsters

Some Spirit support equips to Spirit Monsters instead of being a Spirit Monster
itself. Yata Mirror and Kusanagi Sword both use a face-up `TYPE_SPIRIT` target,
an equip limit, and ordinary equip resolution:

```lua
function s.eqlimit(e,c)
    return c:IsType(TYPE_SPIRIT)
end

function s.operation(e,tp,eg,ep,ev,re,r,rp)
    local c=e:GetHandler()
    local tc=Duel.GetFirstTarget()
    if c:IsRelateToEffect(e) and tc:IsRelateToEffect(e) and tc:IsFaceup() then
        Duel.Equip(tp,c,tc)
    end
end
```

This belongs in the Spirit guide because it changes Spirit return behavior, but
the equip mechanics themselves are covered in
[Equip Spells and Equip Cards](equip-spells).

## Common Mistakes

| Mistake | Better pattern |
| --- | --- |
| Hand-writing the basic End Phase return on every Spirit Monster. | Use `aux.EnableSpiritReturn(c,EVENT_SUMMON_SUCCESS,EVENT_FLIP)` when the shared behavior matches the card. |
| Assuming the helper prevents Special Summons. | Script `EFFECT_SPSUMMON_CONDITION` or another restriction separately when the card text needs it. |
| Passing the wrong event list. | Include only the Summon/flip events that should create the End Phase return. |
| Ignoring Yata Mirror-style interactions. | Reuse `aux.SpiritReturnConditionForced` and `aux.SpiritReturnConditionOptional` in custom return effects. |
| Forgetting the optional return target check. | Optional returns should check `IsAbleToHand()` before offering the choice. |

The Spirit workflow is: register the correct return event setup, then add the
card's own restrictions and effects around it.
