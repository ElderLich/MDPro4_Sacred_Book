# RushDuel.IsPreviousMaximumMode

Alias: `RD.IsPreviousMaximumMode`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsPreviousMaximumMode(Card card) -> bool
```

## Description

Checks the Maximum type bit, Maximum Summon type and previous on-field overlay count. Use when an effect needs to know that components were attached before the card left the field.

## Parameters

- `card` `Card`: Card to inspect.

## Returns

- `bool`: Whether the previous-Maximum check passes.

## Source

`Rush/Utilities/RDCondition.lua:17`

```lua
function RushDuel.IsPreviousMaximumMode(card)
    return card:IsType(TYPE_MAXIMUM) and card:IsSummonType(SUMMON_TYPE_MAXIMUM) and card:GetPreviousOverlayCountOnField()>0
end
```
