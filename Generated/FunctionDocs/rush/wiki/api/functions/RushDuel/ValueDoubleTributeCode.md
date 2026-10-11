# RushDuel.ValueDoubleTributeCode

Alias: `RD.ValueDoubleTributeCode`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.ValueDoubleTributeCode(any code, any ignore) -> any
```

## Description

Rush Duel helper declared in `RDValue.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
效果值: 双重解放 卡名
```

## Parameters

- `code` `any`: Type and behavior are not yet reviewed; see the source.
- `ignore` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDValue.lua:61`

```lua
function RushDuel.ValueDoubleTributeCode(code, ignore)
    return RushDuel.ValueDoubleTributeMix(ignore, code, nil, nil, nil, nil, nil, nil)
end
```
