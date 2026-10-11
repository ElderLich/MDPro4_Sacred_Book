# RushDuel.IsPreviousRace

Alias: `RD.IsPreviousRace`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsPreviousRace(any card, any race) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 位置变化前的种族
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `race` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:206`

```lua
function RushDuel.IsPreviousRace(card, race)
    return (card:GetPreviousRaceOnField() & race) ~= 0
end
```
