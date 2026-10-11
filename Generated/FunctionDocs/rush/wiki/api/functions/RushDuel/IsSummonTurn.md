# RushDuel.IsSummonTurn

Alias: `RD.IsSummonTurn`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsSummonTurn(Card card) -> bool
```

## Description

Checks REASON_SUMMON, STATUS_SUMMON_TURN and the Rush FLAG_SUMMON_TURN marker. The Rush bootstrap installs the tracking effects required by this predicate.

## Parameters

- `card` `Card`: Card to inspect.

## Returns

- `bool`: Whether the card satisfies the current-turn Normal Summon checks.

## Source

`Rush/Utilities/RDCondition.lua:30`

```lua
function RushDuel.IsSummonTurn(card)
    return card:IsReason(REASON_SUMMON) and card:IsStatus(STATUS_SUMMON_TURN) and card:GetFlagEffect(FLAG_SUMMON_TURN) ~= 0
end
```
