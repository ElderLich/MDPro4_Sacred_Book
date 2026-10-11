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

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.ValueDoubleTributeAtkDef) with `RushDuel.ValueDoubleTributeAtkDef`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Green-Eyes Star Cat | `120235015` | [Rush/Scripts/c120235015.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120235015.lua) | 1 |

## Script Examples

### Green-Eyes Star Cat (`120235015`)

Source: [Rush/Scripts/c120235015.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120235015.lua)

```lua
end
--Draw
cm.trival=RD.ValueDoubleTributeAtkDef(nil,200)
function cm.costfilter(c)
	return c:IsRace(RACE_BEAST+RACE_WARRIOR) and RD.IsDefense(c,200) and c:IsAbleToGraveAsCost()
```
