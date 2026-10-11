# RushDuel.CanSelectGroupAndDoAction

Alias: `RD.CanSelectGroupAndDoAction`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CanSelectGroupAndDoAction(any desc, any hint, any filter, any check, any tp, any s_range, any o_range, any min, any max, any expect, any action) -> any
```

## Description

Rush Duel helper declared in `RDAction.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
可选操作: 选择子卡片组
```

## Parameters

- `desc` `any`: Type and behavior are not yet reviewed; see the source.
- `hint` `any`: Type and behavior are not yet reviewed; see the source.
- `filter` `any`: Type and behavior are not yet reviewed; see the source.
- `check` `any`: Type and behavior are not yet reviewed; see the source.
- `tp` `any`: Type and behavior are not yet reviewed; see the source.
- `s_range` `any`: Type and behavior are not yet reviewed; see the source.
- `o_range` `any`: Type and behavior are not yet reviewed; see the source.
- `min` `any`: Type and behavior are not yet reviewed; see the source.
- `max` `any`: Type and behavior are not yet reviewed; see the source.
- `expect` `any`: Type and behavior are not yet reviewed; see the source.
- `action` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAction.lua:117`

```lua
function RushDuel.CanSelectGroupAndDoAction(desc, hint, filter, check, tp, s_range, o_range, min, max, expect, action)
    local hint_selection = RushDuel._private_is_include_public(s_range, o_range)
    return RushDuel._private_action_can_select_group(desc, hint, filter, check, tp, s_range, o_range, min, max, expect, hint_selection, false, action)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **9** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CanSelectGroupAndDoAction) with `RushDuel.CanSelectGroupAndDoAction`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Valkyrian Guard](/examples/rush-cards/120231066) | `120231066` | [Rush/Scripts/c120231066.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120231066.lua) | 1 |
| Imaginary Leading Actor | `120271029` | [Rush/Scripts/c120271029.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120271029.lua) | 1 |
| Destructor Soldier Bokka | `120285015` | [Rush/Scripts/c120285015.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120285015.lua) | 1 |
| Prime Dwarf | `120257001` | [Rush/Scripts/c120257001.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120257001.lua) | 1 |
| Extra Plorer | `120244031` | [Rush/Scripts/c120244031.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120244031.lua) | 1 |
| Ancient Arise Dragon | `120145024` | [Rush/Scripts/c120145024.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120145024.lua) | 1 |
| Session Together! | `120253059` | [Rush/Scripts/c120253059.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120253059.lua) | 1 |
| Legacyrex Legarex | `120239032` | [Rush/Scripts/c120239032.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120239032.lua) | 1 |
| Bladesaurus | `120183037` | [Rush/Scripts/c120183037.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120183037.lua) | 1 |

## Script Examples

### Valkyrian Guard (`120231066`)

Source: [Rush/Scripts/c120231066.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120231066.lua)

```lua
	if RD.SelectAndSpecialSummon(aux.NecroValleyFilter(cm.spfilter),tp,LOCATION_GRAVE,0,1,1,nil,e,POS_FACEUP_ATTACK)~=0 then
		local filter=RD.Filter(cm.posfilter,e,tp)
		RD.CanSelectGroupAndDoAction(aux.Stringid(m,1),HINTMSG_POSCHANGE,filter,cm.poscheck,tp,LOCATION_MZONE,0,1,3,nil,function(g)
			if RD.ChangePosition(g,e,tp,REASON_EFFECT,POS_FACEUP_DEFENSE)~=0 then
				local og=Duel.GetOperatedGroup()
```

### Imaginary Leading Actor (`120271029`)

Source: [Rush/Scripts/c120271029.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120271029.lua)

```lua
	if c:IsFaceup() and c:IsRelateToEffect(e) then
		RD.ChangeCode(e,c,list[1],RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
		RD.CanSelectGroupAndDoAction(aux.Stringid(m,1),HINTMSG_ATOHAND,aux.NecroValleyFilter(cm.filter),cm.check,tp,LOCATION_GRAVE,0,1,2,nil,function(g)
			Duel.BreakEffect()
			RD.SendToHandAndExists(g,e,tp,REASON_EFFECT)
```

### Destructor Soldier Bokka (`120285015`)

Source: [Rush/Scripts/c120285015.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120285015.lua)

```lua
function cm.operation(e,tp,eg,ep,ev,re,r,rp)
	if RD.SendDeckTopToGraveAndExists(tp,3,cm.exfilter,1,nil) then
		RD.CanSelectGroupAndDoAction(aux.Stringid(m,1),HINTMSG_ATOHAND,aux.NecroValleyFilter(cm.thfilter),cm.check,tp,LOCATION_GRAVE,0,1,2,nil,function(g)
			Duel.BreakEffect()
			RD.SendToHandAndExists(g,e,tp,REASON_EFFECT)
```
