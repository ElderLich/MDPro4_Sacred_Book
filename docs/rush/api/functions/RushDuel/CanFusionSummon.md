# RushDuel.CanFusionSummon

Alias: `RD.CanFusionSummon`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CanFusionSummon(any desc, any matfilter, any spfilter, any exfilter, any s_range, any o_range, any mat_check, any mat_move, any e, any tp, any pos, any break_effect, any including_self, any self_leave) -> any
```

## Description

Rush Duel helper declared in `RDFusion.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
可以进行融合召唤
```

## Parameters

- `desc` `any`: Type and behavior are not yet reviewed; see the source.
- `matfilter` `any`: Type and behavior are not yet reviewed; see the source.
- `spfilter` `any`: Type and behavior are not yet reviewed; see the source.
- `exfilter` `any`: Type and behavior are not yet reviewed; see the source.
- `s_range` `any`: Type and behavior are not yet reviewed; see the source.
- `o_range` `any`: Type and behavior are not yet reviewed; see the source.
- `mat_check` `any`: Type and behavior are not yet reviewed; see the source.
- `mat_move` `any`: Type and behavior are not yet reviewed; see the source.
- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `tp` `any`: Type and behavior are not yet reviewed; see the source.
- `pos` `any`: Type and behavior are not yet reviewed; see the source.
- `break_effect` `any`: Type and behavior are not yet reviewed; see the source.
- `including_self` `any`: Type and behavior are not yet reviewed; see the source.
- `self_leave` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDFusion.lua:587`

```lua
function RushDuel.CanFusionSummon(desc, matfilter, spfilter, exfilter, s_range, o_range, mat_check, mat_move, e, tp, pos, break_effect, including_self, self_leave)
    local include = including_self or false
    local leave = self_leave or false
    RushDuel.FusionExtraChecker = RushDuel.FusionCheckLocation(e, self_leave, mat_check)
    local fusionable, list, chkf, gc = RushDuel.GetFusionSummonData(e, tp, pos, matfilter, spfilter, exfilter, s_range, o_range, include, leave, nil, e)
    local fc = nil
    ::cancel::
    if fusionable and Duel.SelectYesNo(tp, desc) then
        if break_effect then
            Duel.BreakEffect()
        end
        fc = RushDuel.ExecuteFusionSummon(e, tp, pos, list, chkf, gc, mat_move, true)
        if not fc then
            goto cancel
        end
    end
    RushDuel.FusionExtraChecker = nil
    return fc
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **32** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CanFusionSummon) with `RushDuel.CanFusionSummon`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Hybridrive Back Fusion](/examples/rush-cards/120261052) | `120261052` | [Rush/Scripts/c120261052.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120261052.lua) | 1 |
| [Handy Girl](/examples/rush-cards/120290012) | `120290012` | [Rush/Scripts/c120290012.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290012.lua) | 1 |
| Rising HERO Argent O | `120304042` | [Rush/Scripts/c120304042.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304042.lua) | 1 |
| Jointech Joint | `120257058` | [Rush/Scripts/c120257058.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120257058.lua) | 1 |
| Battletested Curse of Dragon | `120249031` | [Rush/Scripts/c120249031.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120249031.lua) | 1 |
| Ultra Evolution Miracle | `120274051` | [Rush/Scripts/c120274051.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120274051.lua) | 1 |
| OuTerverSe Detonation Fusion | `120290058` | [Rush/Scripts/c120290058.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290058.lua) | 1 |
| Battletested Gaia The Fierce Knight | `120249032` | [Rush/Scripts/c120249032.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120249032.lua) | 1 |
| Princess Cosmos the Trickster | `120293046` | [Rush/Scripts/c120293046.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120293046.lua) | 1 |
| Prime Dwarf | `120257001` | [Rush/Scripts/c120257001.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120257001.lua) | 1 |
| The Draco | `120294002` | [Rush/Scripts/c120294002.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120294002.lua) | 1 |
| Power Meter | `120294054` | [Rush/Scripts/c120294054.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120294054.lua) | 1 |
| Slay the Star Protector's Gunslinger | `120306010` | [Rush/Scripts/c120306010.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120306010.lua) | 1 |
| Ancient Gear Hunting Hound | `120283048` | [Rush/Scripts/c120283048.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120283048.lua) | 1 |
| OuTerverSe Rainpale | `120290004` | [Rush/Scripts/c120290004.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290004.lua) | 1 |
| Fist the Star Protector's Roaring Gauntlet | `120306011` | [Rush/Scripts/c120306011.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120306011.lua) | 1 |
| Pupating Larvae Moth | `120298033` | [Rush/Scripts/c120298033.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120298033.lua) | 1 |
| Y-Trial Dragon | `120305009` | [Rush/Scripts/c120305009.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120305009.lua) | 1 |
| Z-Trial Tank | `120305010` | [Rush/Scripts/c120305010.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120305010.lua) | 1 |
| Pulsating Cocoon of Evolution | `120298036` | [Rush/Scripts/c120298036.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120298036.lua) | 1 |
| Magnet Speeder | `120285024` | [Rush/Scripts/c120285024.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120285024.lua) | 1 |
| Transam Nebula Fusion | `120272048` | [Rush/Scripts/c120272048.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120272048.lua) | 1 |
| Skullcrag Incursion | `120298015` | [Rush/Scripts/c120298015.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120298015.lua) | 1 |
| Towline Cattle Healer | `120290026` | [Rush/Scripts/c120290026.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290026.lua) | 1 |
| ...and 8 more |  |  |  |

## Script Examples

### Hybridrive Back Fusion (`120261052`)

Source: [Rush/Scripts/c120261052.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120261052.lua)

```lua
	if RD.SelectAndSpecialSummon(cm.filter,1-tp,LOCATION_GRAVE,0,1,1,nil,e,POS_FACEDOWN_DEFENSE)~=0 then
		RD.SetFusionSummonMaterialCount(e,2,2)
		RD.CanFusionSummon(aux.Stringid(m,1),aux.FALSE,nil,cm.exfilter,LOCATION_GRAVE,0,cm.matcheck,RD.FusionToDeck,e,tp,POS_FACEUP,true)
		RD.ResetFusionSummonMaterialCount(e)
	end
```

### Handy Girl (`120290012`)

Source: [Rush/Scripts/c120290012.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290012.lua)

```lua
		if not Duel.IsExistingMatchingCard(cm.exfilter,tp,LOCATION_MZONE,0,1,nil) then
			RD.SetFusionSummonMaterialCount(e,2,2)
			RD.CanFusionSummon(aux.Stringid(m,1),cm.matfilter,nil,nil,0,0,nil,RD.FusionToGrave,e,tp,POS_FACEUP)
			RD.ResetFusionSummonMaterialCount(e)
		end
```

### Rising HERO Argent O (`120304042`)

Source: [Rush/Scripts/c120304042.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304042.lua)

```lua
	RD.SelectAndDoAction(HINTMSG_DESTROY,nil,tp,0,LOCATION_ONFIELD,1,1,nil,function(g)
		if Duel.Destroy(g,REASON_EFFECT)~=0 then
			RD.CanFusionSummon(aux.Stringid(m,1),aux.FALSE,cm.spfilter,cm.exfilter,LOCATION_GRAVE,0,nil,RD.FusionToDeck,e,tp,POS_FACEUP_ATTACK,true)
		end
	end)
```
