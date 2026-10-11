# RushDuel.IsAnnounceType

Alias: `RD.IsAnnounceType`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsAnnounceType(any card) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 是宣言的种类
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:86`

```lua
function RushDuel.IsAnnounceType(card)
    local announce = Duel.GetChainInfo(0, CHAININFO_TARGET_PARAM)
    return (announce == 0 and card:IsType(TYPE_MONSTER)) or (announce == 1 and card:IsType(TYPE_SPELL)) or (announce == 2 and card:IsType(TYPE_TRAP))
end
```
