# RushDuel.SelectGroupAndSpecialSummon

Alias: `RD.SelectGroupAndSpecialSummon`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.SelectGroupAndSpecialSummon(any filter, any check, any tp, any s_range, any o_range, any min, any max, any expect, any e, any pos, any break_effect, any target_player) -> any
```

## Description

Rush Duel helper declared in `RDAction.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
操作: 选择怪兽特殊召唤 (子卡片组)
```

## Parameters

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

`Rush/Utilities/RDAction.lua:140`

```lua
function RushDuel.SelectGroupAndSpecialSummon(filter, check, tp, s_range, o_range, min, max, expect, e, pos, break_effect, target_player)
    local ct = RushDuel.GetMZoneCount(target_player or tp, max)
    if ct >= min then
        return RushDuel._private_action_select_group(HINTMSG_SPSUMMON, filter, check, tp, s_range, o_range, min, ct, expect, false, false, RushDuel._special_summon, e, tp, pos, break_effect,
            target_player)
    end
    return 0
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **9** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.SelectGroupAndSpecialSummon) with `RushDuel.SelectGroupAndSpecialSummon`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Rescue Rabbit](/examples/rush-cards/120109057) | `120109057` | [Rush/Scripts/c120109057.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120109057.lua) | 1 |
| [Star Cat Destronya](/examples/rush-cards/120235037) | `120235037` | [Rush/Scripts/c120235037.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120235037.lua) | 1 |
| Finalize Phoenix | `120231046` | [Rush/Scripts/c120231046.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120231046.lua) | 1 |
| The Dragiastar | `120235035` | [Rush/Scripts/c120235035.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120235035.lua) | 1 |
| Evil Star Beacon | `120155041` | [Rush/Scripts/c120155041.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120155041.lua) | 1 |
| Valkyrion the Unity Warrior | `120260025` | [Rush/Scripts/c120260025.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120260025.lua) | 1 |
| Hero Descent | `120264056` | [Rush/Scripts/c120264056.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120264056.lua) | 1 |
| Major Audition | `120246071` | [Rush/Scripts/c120246071.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120246071.lua) | 1 |
| Stone of the Dark Magicians | `120246083` | [Rush/Scripts/c120246083.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120246083.lua) | 1 |

## Script Examples

### Rescue Rabbit (`120109057`)

Source: [Rush/Scripts/c120109057.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120109057.lua)

```lua
end
function cm.operation(e,tp,eg,ep,ev,re,r,rp)
	if RD.SelectGroupAndSpecialSummon(aux.NecroValleyFilter(cm.spfilter),cm.check,tp,LOCATION_GRAVE,0,2,2,nil,e,POS_FACEUP)~=0 then
		local g=Duel.GetOperatedGroup()
		g:ForEach(function(tc)
```

### Star Cat Destronya (`120235037`)

Source: [Rush/Scripts/c120235037.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120235037.lua)

```lua
end
function cm.operation(e,tp,eg,ep,ev,re,r,rp)
	if RD.SelectGroupAndSpecialSummon(aux.NecroValleyFilter(cm.spfilter),cm.check,tp,LOCATION_GRAVE,0,2,2,nil,e,POS_FACEUP)~=0 then
		local og=Duel.GetOperatedGroup():Filter(cm.exfilter,nil)
		og:ForEach(function(tc)
```

### Finalize Phoenix (`120231046`)

Source: [Rush/Scripts/c120231046.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120231046.lua)

```lua
	local lv=g:GetSum(Card.GetLevel,nil)
	local check=RD.Check(cm.check,lv,tp)
	RD.SelectGroupAndSpecialSummon(aux.NecroValleyFilter(cm.spfilter),check,tp,LOCATION_GRAVE,0,1,2,nil,e,POS_FACEUP)
end
```
