# RushDuel.CopyCode

Alias: `RD.CopyCode`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CopyCode(any e, any card, any target, any reset, any forced) -> any
```

## Description

Rush Duel helper declared in `RDAttach.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
赋予: 复制卡名
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `target` `any`: Type and behavior are not yet reviewed; see the source.
- `reset` `any`: Type and behavior are not yet reviewed; see the source.
- `forced` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAttach.lua:238`

```lua
function RushDuel.CopyCode(e, card, target, reset, forced)
    local code = target:GetCode()
    return RushDuel.CreateSingleEffect(e, nil, card, EFFECT_CHANGE_CODE, code, reset, forced)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **6** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CopyCode) with `RushDuel.CopyCode`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Fairy of the Stars](/examples/rush-cards/120305016) | `120305016` | [Rush/Scripts/c120305016.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120305016.lua) | 1 |
| Etraynze the Shadow Flower Restricter | `120254041` | [Rush/Scripts/c120254041.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120254041.lua) | 1 |
| CAN - Eb:D | `120283034` | [Rush/Scripts/c120283034.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120283034.lua) | 1 |
| Magical Warrior of Heritage | `120285030` | [Rush/Scripts/c120285030.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120285030.lua) | 1 |
| Splame | `120244027` | [Rush/Scripts/c120244027.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120244027.lua) | 1 |
| Mirroring Wyvern | `120235013` | [Rush/Scripts/c120235013.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120235013.lua) | 1 |

## Script Examples

### Fairy of the Stars (`120305016`)

Source: [Rush/Scripts/c120305016.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120305016.lua)

```lua
		local filter=RD.Filter(cm.filter,c:GetCode())
		RD.SelectAndDoAction(aux.Stringid(m,1),aux.NecroValleyFilter(filter),tp,LOCATION_GRAVE,0,1,1,nil,function(g)
			RD.CopyCode(e,c,g:GetFirst(),RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
			RD.CanSelectAndDoAction(aux.Stringid(m,2),HINTMSG_ATOHAND,aux.NecroValleyFilter(cm.thfilter),tp,LOCATION_GRAVE,0,1,1,nil,function(g)
				Duel.BreakEffect()
```

### Etraynze the Shadow Flower Restricter (`120254041`)

Source: [Rush/Scripts/c120254041.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120254041.lua)

```lua
		local filter=RD.Filter(cm.filter,c:GetCode())
		RD.SelectAndDoAction(aux.Stringid(m,1),aux.NecroValleyFilter(filter),tp,LOCATION_GRAVE,0,1,1,nil,function(g)
			RD.CopyCode(e,c,g:GetFirst(),RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
			RD.CanSelectAndSet(aux.Stringid(m,2),aux.NecroValleyFilter(cm.setfilter),tp,LOCATION_GRAVE,0,1,1,nil,e,true)
		end)
```

### CAN - Eb:D (`120283034`)

Source: [Rush/Scripts/c120283034.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120283034.lua)

```lua
		local filter=RD.Filter(cm.filter,c:GetCode())
		RD.SelectAndDoAction(aux.Stringid(m,1),aux.NecroValleyFilter(filter),tp,LOCATION_GRAVE,0,1,1,nil,function(g)
			RD.CopyCode(e,c,g:GetFirst(),RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
			if not Duel.IsExistingMatchingCard(cm.exfilter,tp,LOCATION_MZONE,0,1,nil) then
				RD.CanSelectAndDoAction(aux.Stringid(m,1),HINTMSG_ATOHAND,aux.NecroValleyFilter(cm.thfilter),tp,LOCATION_GRAVE,0,1,1,nil,function(sg)
```
