# RushDuel.ValueDoubleTributeAtkDef

Alias: `RD.ValueDoubleTributeAtkDef`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.ValueDoubleTributeAtkDef(any attack, any defense, any ignore) -> any
```

## Description

Rush Duel helper declared in `RDValue.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
效果值: 双重解放 攻击力/守备力
```

## Parameters

- `attack` `any`: Type and behavior are not yet reviewed; see the source.
- `defense` `any`: Type and behavior are not yet reviewed; see the source.
- `ignore` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDValue.lua:77`

```lua
function RushDuel.ValueDoubleTributeAtkDef(attack, defense, ignore)
    return RushDuel.ValueDoubleTributeMix(ignore, nil, nil, nil, nil, nil, attack, defense)
end
```
