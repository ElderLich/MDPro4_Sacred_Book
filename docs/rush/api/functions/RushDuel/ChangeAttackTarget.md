# RushDuel.ChangeAttackTarget

Alias: `RD.ChangeAttackTarget`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.ChangeAttackTarget(any card, any player, any target) -> any
```

## Description

Rush Duel helper declared in `RDAction.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
操作: 改变攻击对象
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `target` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAction.lua:552`

```lua
function RushDuel.ChangeAttackTarget(card, player, target)
    local g = card:GetAttackableTarget()
    Duel.Hint(HINT_SELECTMSG, player, HINTMSG_ATTACKTARGET)
    local sg = g:Select(player, 1, 1, nil)
    local tc = sg:GetFirst()
    return tc and (tc == target or Duel.ChangeAttackTarget(tc))
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **3** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.ChangeAttackTarget) with `RushDuel.ChangeAttackTarget`.

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
function cm.activate(e,tp,eg,ep,ev,re,r,rp)
	if RD.ChangeAttackTarget(Duel.GetAttacker(),tp,Duel.GetAttackTarget()) then
		local mg=Duel.GetMatchingGroup(Card.IsFaceup,tp,LOCATION_MZONE,0,nil)
		if mg:CheckSubGroup(cm.check,2,2) then
```

### Burning Wind (`120264061`)

Source: [Rush/Scripts/c120264061.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120264061.lua)

```lua
		RD.AttachAtkDef(e,g:GetFirst(),1000,0,RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
		if RD.IsCanChangeAttackTarget(tc) and Duel.SelectYesNo(tp,aux.Stringid(m,2)) then
			RD.ChangeAttackTarget(tc,tp,Duel.GetAttackTarget())
		end
	end)
```

### Call of the Earthbound (`120120047`)

Source: [Rush/Scripts/c120120047.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120120047.lua)

```lua
end
function cm.activate(e,tp,eg,ep,ev,re,r,rp)
	RD.ChangeAttackTarget(Duel.GetAttacker(),tp,Duel.GetAttackTarget())
end
```
