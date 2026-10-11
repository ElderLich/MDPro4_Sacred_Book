# RushDuel.ValueDoubleTributeLvAttrRace

Alias: `RD.ValueDoubleTributeLvAttrRace`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.ValueDoubleTributeLvAttrRace(any level, any attribute, any race, any ignore) -> any
```

## Description

Rush Duel helper declared in `RDValue.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
效果值: 双重解放 等级/属性/种族
```

## Parameters

- `level` `any`: Type and behavior are not yet reviewed; see the source.
- `attribute` `any`: Type and behavior are not yet reviewed; see the source.
- `race` `any`: Type and behavior are not yet reviewed; see the source.
- `ignore` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDValue.lua:73`

```lua
function RushDuel.ValueDoubleTributeLvAttrRace(level, attribute, race, ignore)
    return RushDuel.ValueDoubleTributeMix(ignore, nil, attribute, nil, level, race, nil, nil)
end
```
