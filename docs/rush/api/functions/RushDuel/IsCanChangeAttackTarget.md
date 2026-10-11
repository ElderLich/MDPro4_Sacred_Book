# RushDuel.IsCanChangeAttackTarget

Alias: `RD.IsCanChangeAttackTarget`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsCanChangeAttackTarget(any card) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 可以改变攻击对象
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:394`

```lua
function RushDuel.IsCanChangeAttackTarget(card)
    local g = card:GetAttackableTarget()
    return #g > 1
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **3** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.IsCanChangeAttackTarget) with `RushDuel.IsCanChangeAttackTarget`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Dragon Double-Doom | `120235060` | [Rush/Scripts/c120235060.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120235060.lua) | 1 |
| Burning Wind | `120264061` | [Rush/Scripts/c120264061.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120264061.lua) | 1 |
| Call of the Earthbound | `120120047` | [Rush/Scripts/c120120047.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120120047.lua) | 1 |

## Script Examples

### Dragon Double-Doom (`120235060`)

Source: [Rush/Scripts/c120235060.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120235060.lua)

```lua
end
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return RD.IsCanChangeAttackTarget(Duel.GetAttacker()) end
end
function cm.activate(e,tp,eg,ep,ev,re,r,rp)
```

### Burning Wind (`120264061`)

Source: [Rush/Scripts/c120264061.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120264061.lua)

```lua
	RD.SelectAndDoAction(aux.Stringid(m,1),cm.filter,tp,LOCATION_MZONE,0,1,1,nil,function(g)
		RD.AttachAtkDef(e,g:GetFirst(),1000,0,RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
		if RD.IsCanChangeAttackTarget(tc) and Duel.SelectYesNo(tp,aux.Stringid(m,2)) then
			RD.ChangeAttackTarget(tc,tp,Duel.GetAttackTarget())
		end
```

### Call of the Earthbound (`120120047`)

Source: [Rush/Scripts/c120120047.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120120047.lua)

```lua
end
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return RD.IsCanChangeAttackTarget(Duel.GetAttacker()) end
end
function cm.activate(e,tp,eg,ep,ev,re,r,rp)
```
