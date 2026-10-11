# RushDuel.ValueDoubleTributeAttrType

Alias: `RD.ValueDoubleTributeAttrType`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.ValueDoubleTributeAttrType(any attribute, any type, any ignore) -> any
```

## Description

Rush Duel helper declared in `RDValue.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
效果值: 双重解放 属性/类型
```

## Parameters

- `attribute` `any`: Type and behavior are not yet reviewed; see the source.
- `type` `any`: Type and behavior are not yet reviewed; see the source.
- `ignore` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDValue.lua:69`

```lua
function RushDuel.ValueDoubleTributeAttrType(attribute, type, ignore)
    return RushDuel.ValueDoubleTributeMix(ignore, nil, attribute, type, nil, nil, nil, nil)
end
```
