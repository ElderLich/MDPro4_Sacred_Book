# RushDuel.FusionToGrave

Alias: `RD.FusionToGrave`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.FusionToGrave(any tp, any mat) -> any
```

## Description

Rush Duel helper declared in `RDFusion.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
素材去向: 墓地
```

## Parameters

- `tp` `any`: Type and behavior are not yet reviewed; see the source.
- `mat` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDFusion.lua:620`

```lua
function RushDuel.FusionToGrave(tp, mat)
    Duel.SendtoGrave(mat, REASON_EFFECT + REASON_MATERIAL + REASON_FUSION)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **34** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.FusionToGrave) with `RushDuel.FusionToGrave`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Handy Girl](/examples/rush-cards/120290012) | `120290012` | [Rush/Scripts/c120290012.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290012.lua) | 1 |
| Jointech Joint | `120257058` | [Rush/Scripts/c120257058.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120257058.lua) | 1 |
| Plandolin-a-la-Mode | `120264042` | [Rush/Scripts/c120264042.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120264042.lua) | 1 |
| Prime Dwarf | `120257001` | [Rush/Scripts/c120257001.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120257001.lua) | 1 |
| Power Meter | `120294054` | [Rush/Scripts/c120294054.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120294054.lua) | 1 |
| Ancient Gear Hunting Hound | `120283048` | [Rush/Scripts/c120283048.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120283048.lua) | 1 |
| OuTerverSe Rainpale | `120290004` | [Rush/Scripts/c120290004.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290004.lua) | 1 |
| Fist the Star Protector's Roaring Gauntlet | `120306011` | [Rush/Scripts/c120306011.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120306011.lua) | 1 |
| Pupating Larvae Moth | `120298033` | [Rush/Scripts/c120298033.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120298033.lua) | 1 |
| Tama Bond | `120285053` | [Rush/Scripts/c120285053.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120285053.lua) | 1 |
| Magnet Speeder | `120285024` | [Rush/Scripts/c120285024.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120285024.lua) | 1 |
| Galaxy Chaos Fusion | `120277051` | [Rush/Scripts/c120277051.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120277051.lua) | 1 |
| Towline Cattle Healer | `120290026` | [Rush/Scripts/c120290026.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290026.lua) | 1 |
| Infinite Heavy Cavalry Buildragoon | `120264015` | [Rush/Scripts/c120264015.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120264015.lua) | 1 |
| Protorion the Magna Warrior | `120260028` | [Rush/Scripts/c120260028.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120260028.lua) | 1 |
| Galactica Fusion Space | `120304047` | [Rush/Scripts/c120304047.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304047.lua) | 1 |
| Dice Key Mix | `120272007` | [Rush/Scripts/c120272007.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120272007.lua) | 1 |
| Power Bond | `120231070` | [Rush/Scripts/c120231070.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120231070.lua) | 1 |
| Delirium Embrace | `120274065` | [Rush/Scripts/c120274065.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120274065.lua) | 1 |
| Alpha The Eternal Magnet Warrior | `120260032` | [Rush/Scripts/c120260032.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120260032.lua) | 1 |
| Gamma The Eternal Magnet Warrior | `120260034` | [Rush/Scripts/c120260034.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120260034.lua) | 1 |
| Beta The Eternal Magnet Warrior | `120260033` | [Rush/Scripts/c120260033.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120260033.lua) | 1 |
| Deep Warning Fusion | `120260020` | [Rush/Scripts/c120260020.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120260020.lua) | 1 |
| Super Polymerization | `120307014` | [Rush/Scripts/c120307014.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120307014.lua) | 1 |
| ...and 10 more |  |  |  |

## Script Examples

### Handy Girl (`120290012`)

Source: [Rush/Scripts/c120290012.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290012.lua)

```lua
		if not Duel.IsExistingMatchingCard(cm.exfilter,tp,LOCATION_MZONE,0,1,nil) then
			RD.SetFusionSummonMaterialCount(e,2,2)
			RD.CanFusionSummon(aux.Stringid(m,1),cm.matfilter,nil,nil,0,0,nil,RD.FusionToGrave,e,tp,POS_FACEUP)
			RD.ResetFusionSummonMaterialCount(e)
		end
```

### Jointech Joint (`120257058`)

Source: [Rush/Scripts/c120257058.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120257058.lua)

```lua
		pos=Duel.SelectPosition(tp,tc,pos)
		if RD.ChangePosition(tc,e,tp,REASON_EFFECT,pos)~=0 then
			RD.CanFusionSummon(aux.Stringid(m,1),nil,cm.spfilter,nil,0,0,nil,RD.FusionToGrave,e,tp,POS_FACEUP,true)
		end
	end)
```

### Plandolin-a-la-Mode (`120264042`)

Source: [Rush/Scripts/c120264042.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120264042.lua)

```lua
		RD.FusionToDeck(tp,mat)
	else
		RD.FusionToGrave(tp,mat)
	end
end
```
