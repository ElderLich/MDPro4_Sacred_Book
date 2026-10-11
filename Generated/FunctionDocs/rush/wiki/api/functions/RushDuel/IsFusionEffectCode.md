# RushDuel.IsFusionEffectCode

Alias: `RD.IsFusionEffectCode`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsFusionEffectCode(any code) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 当前的融合效果的卡片编号
```

## Parameters

- `code` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:144`

```lua
function RushDuel.IsFusionEffectCode(code)
    if RD.CurrentFusionEffect then
        return RD.CurrentFusionEffect:GetHandler():IsCode(code)
    end
    return false
end
```
