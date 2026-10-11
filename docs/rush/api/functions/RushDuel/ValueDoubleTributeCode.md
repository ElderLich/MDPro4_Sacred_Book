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

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **4** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.ValueDoubleTributeCode) with `RushDuel.ValueDoubleTributeCode`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Cosmo Predictor | `120236001` | [Rush/Scripts/c120236001.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120236001.lua) | 1 |
| OuTerverSe Sylphy Seyfert | `120290007` | [Rush/Scripts/c120290007.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290007.lua) | 1 |
| Chaos Coolstars | `120277004` | [Rush/Scripts/c120277004.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120277004.lua) | 2 |
| OuTerverSe Needle Maker | `120290005` | [Rush/Scripts/c120290005.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290005.lua) | 1 |

## Script Examples

### Cosmo Predictor (`120236001`)

Source: [Rush/Scripts/c120236001.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120236001.lua)

```lua
end
--To Hand
cm.trival=RD.ValueDoubleTributeCode(list[1])
function cm.thfilter(c)
	return c:IsLevel(8) and c:IsRace(RACE_GALAXY) and c:IsAbleToHand()
```

### OuTerverSe Sylphy Seyfert (`120290007`)

Source: [Rush/Scripts/c120290007.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290007.lua)

```lua
end
--Change Race
cm.trival=RD.ValueDoubleTributeCode(list[2])
function cm.condition(e,tp,eg,ep,ev,re,r,rp)
	return RD.IsCanChangeRace(e:GetHandler(),RACE_GALAXY)
```

### Chaos Coolstars (`120277004`)

Source: [Rush/Scripts/c120277004.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120277004.lua)

```lua
end
--Draw
cm.trival1=RD.ValueDoubleTributeCode(list[1])
cm.trival2=RD.ValueDoubleTributeCode(list[2])
function cm.costfilter(c)
```
