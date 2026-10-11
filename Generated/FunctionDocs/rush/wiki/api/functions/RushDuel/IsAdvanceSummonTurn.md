# RushDuel.IsAdvanceSummonTurn

Alias: `RD.IsAdvanceSummonTurn`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsAdvanceSummonTurn(any card) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 这张卡攻击表示上级召唤的回合
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:34`

```lua
function RushDuel.IsAdvanceSummonTurn(card)
    return RushDuel.IsSummonTurn(card) and card:IsSummonType(SUMMON_TYPE_ADVANCE)
end
```
