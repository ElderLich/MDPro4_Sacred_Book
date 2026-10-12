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

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **2** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.ValueDoubleTributeAttrType) with `RushDuel.ValueDoubleTributeAttrType`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Light Effigy | `120252014` | [Rush/Scripts/c120252014.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120252014.lua) | 1 |
| Dark Effigy | `120253032` | [Rush/Scripts/c120253032.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120253032.lua) | 1 |

## Script Examples

### Light Effigy (`120252014`)

Source: [Rush/Scripts/c120252014.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120252014.lua)

```lua
end
--Double Tribute
cm.trival=RD.ValueDoubleTributeAttrType(ATTRIBUTE_LIGHT,TYPE_NORMAL,true)
```

### Dark Effigy (`120253032`)

Source: [Rush/Scripts/c120253032.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120253032.lua)

```lua
end
--Double Tribute
cm.trival=RD.ValueDoubleTributeAttrType(ATTRIBUTE_DARK,TYPE_NORMAL,true)
```
