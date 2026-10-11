# RushDuel.ChangeRace

Alias: `RD.ChangeRace`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.ChangeRace(any e, any card, any race, any reset, any forced) -> any
```

## Description

Rush Duel helper declared in `RDAttach.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
赋予: 改变种族
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `race` `any`: Type and behavior are not yet reviewed; see the source.
- `reset` `any`: Type and behavior are not yet reviewed; see the source.
- `forced` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAttach.lua:230`

```lua
function RushDuel.ChangeRace(e, card, race, reset, forced)
    return RushDuel.CreateSingleEffect(e, nil, card, EFFECT_CHANGE_RACE, race, reset, forced)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **26** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.ChangeRace) with `RushDuel.ChangeRace`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| OuTerverSe Direct Driver | `120109056` | [Rush/Scripts/c120109056.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120109056.lua) | 1 |
| OuTerverSe Burst Oblivion | `120290008` | [Rush/Scripts/c120290008.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290008.lua) | 1 |
| OuTerverSe Wish of Angeleva | `120293061` | [Rush/Scripts/c120293061.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120293061.lua) | 1 |
| OuTerverSe Wish of Devilgear | `120293062` | [Rush/Scripts/c120293062.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120293062.lua) | 1 |
| OuTerverSe Byugyuwazzo | `120290006` | [Rush/Scripts/c120290006.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290006.lua) | 1 |
| OuTerverSe Toxic Blob | `120290028` | [Rush/Scripts/c120290028.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290028.lua) | 1 |
| Delirium Shewel | `120274058` | [Rush/Scripts/c120274058.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120274058.lua) | 1 |
| OuTerverSe Bug Fungus | `120290002` | [Rush/Scripts/c120290002.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290002.lua) | 1 |
| Wish of OuTerverSe the World-Shattering Emperor \[L\] | `120293058` | [Rush/Scripts/c120293058.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120293058.lua) | 1 |
| OuTerverSe Mother Fungus | `120293063` | [Rush/Scripts/c120293063.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120293063.lua) | 1 |
| OuTerverSe Sylphy Seyfert | `120290007` | [Rush/Scripts/c120290007.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290007.lua) | 1 |
| Delirium Drone | `120274059` | [Rush/Scripts/c120274059.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120274059.lua) | 1 |
| OuTerverSe Rainpale | `120290004` | [Rush/Scripts/c120290004.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290004.lua) | 1 |
| Delirium Polynea | `120277033` | [Rush/Scripts/c120277033.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120277033.lua) | 1 |
| Delirium Mariquita | `120274057` | [Rush/Scripts/c120274057.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120274057.lua) | 1 |
| OuTerverSe Anubistar | `120290003` | [Rush/Scripts/c120290003.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290003.lua) | 1 |
| OuTerverSe Acid Blob | `120290001` | [Rush/Scripts/c120290001.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290001.lua) | 1 |
| Evil Bowler | `120271027` | [Rush/Scripts/c120271027.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120271027.lua) | 2 |
| OuTerverSe Needle Maker | `120290005` | [Rush/Scripts/c120290005.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290005.lua) | 1 |
| OuTerverSe Endless Doom Oblivion | `120290029` | [Rush/Scripts/c120290029.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290029.lua) | 1 |
| Accel Wonder Flare | `120186010` | [Rush/Scripts/c120186010.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120186010.lua) | 1 |
| Bio Mechmantis | `120208030` | [Rush/Scripts/c120208030.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120208030.lua) | 1 |
| Delirium Teega | `120300025` | [Rush/Scripts/c120300025.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300025.lua) | 1 |
| Delirium Papillon | `120222035` | [Rush/Scripts/c120222035.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120222035.lua) | 1 |
| ...and 2 more |  |  |  |

## Script Examples

### OuTerverSe Direct Driver (`120109056`)

Source: [Rush/Scripts/c120109056.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120109056.lua)

```lua
	local c=e:GetHandler()
	if c:IsFaceup() and c:IsRelateToEffect(e) then
		RD.ChangeRace(e,c,RACE_GALAXY,RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
		if Duel.IsAbleToEnterBP() then
			RD.CanSelectAndDoAction(aux.Stringid(m,1),aux.Stringid(m,2),cm.filter,tp,LOCATION_MZONE,0,2,2,nil,function(g)
```

### OuTerverSe Burst Oblivion (`120290008`)

Source: [Rush/Scripts/c120290008.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290008.lua)

```lua
	local c=e:GetHandler()
	if c:IsFaceup() and c:IsRelateToEffect(e) then
		RD.ChangeRace(e,c,RACE_GALAXY,RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
		if RD.CanSelectAndSpecialSummon(aux.Stringid(m,1),aux.NecroValleyFilter(cm.spfilter),tp,LOCATION_GRAVE,0,1,1,nil,e,POS_FACEUP,true)~=0 then
			local tc=Duel.GetOperatedGroup():GetFirst()
```

### OuTerverSe Wish of Angeleva (`120293061`)

Source: [Rush/Scripts/c120293061.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120293061.lua)

```lua
			and Duel.SelectEffectYesNo(tp,c,aux.Stringid(m,1)) then
			Duel.BreakEffect()
			RD.ChangeRace(e,c,RACE_GALAXY,RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
		end
	end)
```
