# RushDuel.IsNormalSpell

Alias: `RD.IsNormalSpell`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsNormalSpell(any card) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 卡片是通常魔法卡
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:5`

```lua
function RushDuel.IsNormalSpell(card)
    return card:GetType()==TYPE_SPELL or card:GetType()==TYPE_SPELL+TYPE_LEGEND
end
```
