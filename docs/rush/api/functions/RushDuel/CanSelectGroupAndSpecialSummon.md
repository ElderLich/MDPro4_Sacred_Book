# RushDuel.CanSelectGroupAndSpecialSummon

Alias: `RD.CanSelectGroupAndSpecialSummon`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CanSelectGroupAndSpecialSummon(any desc, any filter, any check, any tp, any s_range, any o_range, any min, any max, any expect, any e, any pos, any break_effect, any target_player) -> any
```

## Description

Rush Duel helper declared in `RDAction.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
可选操作: 选择怪兽特殊召唤 (子卡片组)
```

## Parameters

- `desc` `any`: Type and behavior are not yet reviewed; see the source.
- `filter` `any`: Type and behavior are not yet reviewed; see the source.
- `check` `any`: Type and behavior are not yet reviewed; see the source.
- `tp` `any`: Type and behavior are not yet reviewed; see the source.
- `s_range` `any`: Type and behavior are not yet reviewed; see the source.
- `o_range` `any`: Type and behavior are not yet reviewed; see the source.
- `min` `any`: Type and behavior are not yet reviewed; see the source.
- `max` `any`: Type and behavior are not yet reviewed; see the source.
- `expect` `any`: Type and behavior are not yet reviewed; see the source.
- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `pos` `any`: Type and behavior are not yet reviewed; see the source.
- `break_effect` `any`: Type and behavior are not yet reviewed; see the source.
- `target_player` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAction.lua:149`

```lua
function RushDuel.CanSelectGroupAndSpecialSummon(desc, filter, check, tp, s_range, o_range, min, max, expect, e, pos, break_effect, target_player)
    local ct = RushDuel.GetMZoneCount(target_player or tp, max)
    if ct >= min then
        return RushDuel._private_action_can_select_group(desc, HINTMSG_SPSUMMON, filter, check, tp, s_range, o_range, min, ct, expect, false, false, RushDuel._special_summon, e, tp, pos, break_effect,
            target_player)
    end
    return 0
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **3** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CanSelectGroupAndSpecialSummon) with `RushDuel.CanSelectGroupAndSpecialSummon`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Tama Tama Gachance | `120109053` | [Rush/Scripts/c120109053.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120109053.lua) | 1 |
| Fusion Cancel | `120253066` | [Rush/Scripts/c120253066.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120253066.lua) | 1 |
| Ancient Arrive Dragon | `120203009` | [Rush/Scripts/c120203009.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120203009.lua) | 1 |

## Script Examples

### Tama Tama Gachance (`120109053`)

Source: [Rush/Scripts/c120109053.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120109053.lua)

```lua
function cm.activate(e,tp,eg,ep,ev,re,r,rp)
	if RD.DiscardDeck()~=0 and Duel.GetOperatedGroup():IsExists(cm.exfilter,1,nil) then
		RD.CanSelectGroupAndSpecialSummon(aux.Stringid(m,1),aux.NecroValleyFilter(cm.spfilter),cm.spcheck,tp,LOCATION_GRAVE,0,1,3,nil,e,POS_FACEUP,true)
	end
end
```

### Fusion Cancel (`120253066`)

Source: [Rush/Scripts/c120253066.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120253066.lua)

```lua
			local filter=RD.Filter(cm.spfilter,e,sump,tc)
			local check=RD.Check(cm.check,tc)
			RD.CanSelectGroupAndSpecialSummon(aux.Stringid(m,1),filter,check,sump,LOCATION_GRAVE,0,min,min,nil,e,POS_FACEUP)
		end
	end)
```

### Ancient Arrive Dragon (`120203009`)

Source: [Rush/Scripts/c120203009.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120203009.lua)

```lua
			RD.AttachAtkDef(e,tc,-400,0,RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
		end)
		RD.CanSelectGroupAndSpecialSummon(aux.Stringid(m,2),aux.NecroValleyFilter(cm.spfilter),aux.dncheck,tp,LOCATION_GRAVE,0,1,2,nil,e,POS_FACEUP,true)
	end)
end
```
