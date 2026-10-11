# RushDuel.ConditionFlipMainPhase

Alias: `RD.ConditionFlipMainPhase`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.ConditionFlipMainPhase(any e) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
通用条件: 这张卡反转的自己主要阶段
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:440`

```lua
function RushDuel.ConditionFlipMainPhase(e)
	return RushDuel.IsFlipMainPhase(e:GetHandler())
end
```
