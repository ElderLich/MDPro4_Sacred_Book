# RushDuel.CopyCode

Alias: `RD.CopyCode`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CopyCode(any e, any card, any target, any reset, any forced) -> any
```

## Description

Rush Duel helper declared in `RDAttach.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
赋予: 复制卡名
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `target` `any`: Type and behavior are not yet reviewed; see the source.
- `reset` `any`: Type and behavior are not yet reviewed; see the source.
- `forced` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAttach.lua:238`

```lua
function RushDuel.CopyCode(e, card, target, reset, forced)
    local code = target:GetCode()
    return RushDuel.CreateSingleEffect(e, nil, card, EFFECT_CHANGE_CODE, code, reset, forced)
end
```
