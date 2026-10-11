# RushDuel.AddRitualProcedure

Alias: `RD.AddRitualProcedure`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AddRitualProcedure(Card card) -> void
```

## Description

Registers the Rush Ritual monster's type-adjustment effect, removing the TYPE_FUSION compatibility bit. This helper does not create a Ritual Spell activation or summon anything; the spell uses CreateRitualEffect.

## Parameters

- `card` `Card`: Rush Ritual monster.

## Returns

No return values.

## Source

`Rush/Utilities/RDRitual.lua:32`

```lua
function RushDuel.AddRitualProcedure(card)
    if card:IsStatus(STATUS_COPYING_EFFECT) then
        return
    end
    local e = Effect.CreateEffect(card)
    e:SetType(EFFECT_TYPE_SINGLE)
    e:SetCode(EFFECT_REMOVE_TYPE)
    e:SetProperty(EFFECT_FLAG_CANNOT_DISABLE + EFFECT_FLAG_UNCOPYABLE + EFFECT_FLAG_SET_AVAILABLE)
    e:SetRange(0xff)
    e:SetValue(TYPE_FUSION)
    card:RegisterEffect(e)
end
```
