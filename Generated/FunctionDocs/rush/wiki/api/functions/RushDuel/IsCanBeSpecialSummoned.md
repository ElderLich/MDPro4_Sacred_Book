# RushDuel.IsCanBeSpecialSummoned

Alias: `RD.IsCanBeSpecialSummoned`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsCanBeSpecialSummoned(any card, any effect, any player, any position) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 可否特殊召唤
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `effect` `any`: Type and behavior are not yet reviewed; see the source.
- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `position` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:126`

```lua
function RushDuel.IsCanBeSpecialSummoned(card, effect, player, position)
    return card:IsCanBeSpecialSummoned(effect, 0, player, false, false, position)
end
```
