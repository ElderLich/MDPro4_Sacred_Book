# RushDuel.IsUnionMonsterCard

Alias: `RD.IsUnionMonsterCard`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsUnionMonsterCard(any card) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 卡片是同盟怪兽卡
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:9`

```lua
function RushDuel.IsUnionMonsterCard(card)
    return card:GetOriginalType()&TYPE_UNION==TYPE_UNION
end
```
