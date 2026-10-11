# RushDuel.SelectAndSpecialSummon

Alias: `RD.SelectAndSpecialSummon`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.SelectAndSpecialSummon(function filter, int tp, int s_range, int o_range, int min, int max, Card|Group|nil expect, Effect e, int pos, [bool break_effect], [int target_player]) -> int
```

## Description

Checks destination Monster Zone capacity, selects a nonempty Group and performs an ordinary Special Summon with summon type 0, nocheck=false and nolimit=false. The filter must supply per-card summon legality; zone capacity alone does not make every monster summonable.
Unlike the general SelectAndDoAction wrapper, this helper passes e,tp,pos,break_effect,target_player as extra filter arguments. The return value is the actual Duel.SpecialSummon count, or 0 when no selection/summon occurs. Face-down summon confirmation is handled by the Rush private wrapper.

## Parameters

- `filter` `function`: Candidate predicate; receives card,e,tp,pos,break_effect,target_player. Include per-card summon legality.
- `tp` `int`: Selecting and summoning player.
- `s_range` `int`: Source locations on tp side.
- `o_range` `int`: Source locations on the opponent side.
- `min` `int`: Minimum selected count.
- `max` `int`: Maximum count, capped by the destination zone count.
- `expect` `Card|Group|nil`: Excluded Card(s), or nil.
- `e` `Effect`: Source effect passed to the filter.
- `pos` `int`: Required summon position mask.
- `break_effect` `bool` (optional): Call Duel.BreakEffect immediately before summoning; default false.
- `target_player` `int` (optional): Destination player; defaults to tp. Does not change which player makes the choice.

## Returns

- `int`: Actual summon count, or 0 if capacity/candidates/selection do not permit the operation.

## Source

`Rush/Utilities/RDAction.lua:123`

```lua
function RushDuel.SelectAndSpecialSummon(filter, tp, s_range, o_range, min, max, expect, e, pos, break_effect, target_player)
    local ct = RushDuel.GetMZoneCount(target_player or tp, max)
    if ct >= min then
        return RushDuel._private_action_select_match(HINTMSG_SPSUMMON, filter, tp, s_range, o_range, min, ct, expect, false, false, RushDuel._special_summon, e, tp, pos, break_effect, target_player)
    end
    return 0
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **270** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.SelectAndSpecialSummon) with `RushDuel.SelectAndSpecialSummon`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Nativity of the Monarchs](/examples/rush-cards/120244063) | `120244063` | [Rush/Scripts/c120244063.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120244063.lua) | 1 |
| [Instant Gift](/examples/rush-cards/120306059) | `120306059` | [Rush/Scripts/c120306059.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120306059.lua) | 1 |
| [Valkyrian Guard](/examples/rush-cards/120231066) | `120231066` | [Rush/Scripts/c120231066.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120231066.lua) | 1 |
| [Hybridrive Back Fusion](/examples/rush-cards/120261052) | `120261052` | [Rush/Scripts/c120261052.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120261052.lua) | 1 |
| [Jinzo the Machine Menace](/examples/rush-cards/120257028) | `120257028` | [Rush/Scripts/c120257028.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120257028.lua) | 1 |
| [YXZ-Cannon Dragon](/examples/rush-cards/120305004) | `120305004` | [Rush/Scripts/c120305004.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120305004.lua) | 1 |
| [Evolution Result Flash](/examples/rush-cards/120290063) | `120290063` | [Rush/Scripts/c120290063.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290063.lua) | 1 |
| [Devil Foolish](/examples/rush-cards/120244026) | `120244026` | [Rush/Scripts/c120244026.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120244026.lua) | 1 |
| [Sunset Rebirth](/examples/rush-cards/120257066) | `120257066` | [Rush/Scripts/c120257066.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120257066.lua) | 1 |
| [Necromaid Timer](/examples/rush-cards/120294014) | `120294014` | [Rush/Scripts/c120294014.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120294014.lua) | 1 |
| [Road Servant Flare](/examples/rush-cards/120109050) | `120109050` | [Rush/Scripts/c120109050.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120109050.lua) | 1 |
| Blaze Fiend Overlord Zebulth | `120287033` | [Rush/Scripts/c120287033.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120287033.lua) | 1 |
| Shadow Flower Clone | `120228049` | [Rush/Scripts/c120228049.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120228049.lua) | 1 |
| Cosmostar the White Hole Polairy | `120293045` | [Rush/Scripts/c120293045.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120293045.lua) | 1 |
| Plasmatic Model Tool Ceto | `120301069` | [Rush/Scripts/c120301069.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120301069.lua) | 1 |
| Speed Carrier | `120301059` | [Rush/Scripts/c120301059.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120301059.lua) | 1 |
| Etraynze the Shadow Flower Ninja | `120170029` | [Rush/Scripts/c120170029.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120170029.lua) | 1 |
| Excutie Riding! | `120249064` | [Rush/Scripts/c120249064.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120249064.lua) | 1 |
| Soul Drake | `120252007` | [Rush/Scripts/c120252007.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120252007.lua) | 1 |
| Pholus the Star Knight | `120203020` | [Rush/Scripts/c120203020.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120203020.lua) | 1 |
| Reborn Pattern | `120294064` | [Rush/Scripts/c120294064.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120294064.lua) | 1 |
| Despair and Desire | `120301034` | [Rush/Scripts/c120301034.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120301034.lua) | 1 |
| Ice Age Pounder | `120304027` | [Rush/Scripts/c120304027.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304027.lua) | 1 |
| Transam Road Linac | `120235030` | [Rush/Scripts/c120235030.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120235030.lua) | 1 |
| ...and 246 more |  |  |  |

## Script Examples

### Nativity of the Monarchs (`120244063`)

Source: [Rush/Scripts/c120244063.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120244063.lua)

```lua
end
function cm.activate(e,tp,eg,ep,ev,re,r,rp)
	if RD.SelectAndSpecialSummon(cm.spfilter,tp,LOCATION_HAND,0,1,1,nil,e,POS_FACEUP_ATTACK)~=0 then
		local g=eg:Filter(Card.IsRelateToEffect,nil,e)
		if g:GetCount()>0 and Duel.SelectYesNo(tp,aux.Stringid(m,1)) then
```

### Instant Gift (`120306059`)

Source: [Rush/Scripts/c120306059.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120306059.lua)

```lua
	local code=Duel.GetChainInfo(0,CHAININFO_TARGET_PARAM)
	local filter=RD.Filter(cm.spfilter,e,tp,code)
	if RD.SelectAndSpecialSummon(aux.NecroValleyFilter(filter),tp,LOCATION_GRAVE,0,1,1,nil,e,POS_FACEUP)~=0 then
		RD.CanDraw(aux.Stringid(m,1),tp,1,true)
	end
```

### Valkyrian Guard (`120231066`)

Source: [Rush/Scripts/c120231066.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120231066.lua)

```lua
end
function cm.activate(e,tp,eg,ep,ev,re,r,rp)
	if RD.SelectAndSpecialSummon(aux.NecroValleyFilter(cm.spfilter),tp,LOCATION_GRAVE,0,1,1,nil,e,POS_FACEUP_ATTACK)~=0 then
		local filter=RD.Filter(cm.posfilter,e,tp)
		RD.CanSelectGroupAndDoAction(aux.Stringid(m,1),HINTMSG_POSCHANGE,filter,cm.poscheck,tp,LOCATION_MZONE,0,1,3,nil,function(g)
```
