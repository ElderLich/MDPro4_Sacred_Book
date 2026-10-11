# RushDuel.IsFlipMainPhase

Alias: `RD.IsFlipMainPhase`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsFlipMainPhase(any card) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 这张卡反转的自己主要阶段
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:52`

```lua
function RushDuel.IsFlipMainPhase(card)
    return card:GetFlagEffect(FLAG_FLIP_MAIN_PHASE) ~= 0
end
```
