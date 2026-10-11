# RushDuel.IsSpecialSummonTurn

Alias: `RD.IsSpecialSummonTurn`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsSpecialSummonTurn(Card card) -> bool
```

## Description

Checks REASON_SPSUMMON, STATUS_SPSUMMON_TURN and the Rush FLAG_SUMMON_TURN marker. The Rush bootstrap installs the tracking effects required by this predicate.

## Parameters

- `card` `Card`: Card to inspect.

## Returns

- `bool`: Whether the card satisfies the current-turn Special Summon checks.

## Source

`Rush/Utilities/RDCondition.lua:38`

```lua
function RushDuel.IsSpecialSummonTurn(card)
    return card:IsReason(REASON_SPSUMMON) and card:IsStatus(STATUS_SPSUMMON_TURN) and card:GetFlagEffect(FLAG_SUMMON_TURN) ~= 0
end
```
