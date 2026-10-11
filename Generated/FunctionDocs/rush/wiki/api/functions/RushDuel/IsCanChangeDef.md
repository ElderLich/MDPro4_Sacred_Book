# RushDuel.IsCanChangeDef

Alias: `RD.IsCanChangeDef`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsCanChangeDef(any card) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 可否改变守备力
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:107`

```lua
function RushDuel.IsCanChangeDef(card)
    return card:IsDefenseAbove(0) and not RushDuel.IsMaximumMode(card)
end
```
