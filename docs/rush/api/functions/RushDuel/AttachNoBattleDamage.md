# RushDuel.AttachNoBattleDamage

Alias: `RD.AttachNoBattleDamage`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AttachNoBattleDamage(any e, any card, any desc, any reset, any forced) -> any
```

## Description

Rush Duel helper declared in `RDAttach.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
赋予: 战斗不会让双方受到伤害
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `desc` `any`: Type and behavior are not yet reviewed; see the source.
- `reset` `any`: Type and behavior are not yet reviewed; see the source.
- `forced` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAttach.lua:104`

```lua
function RushDuel.AttachNoBattleDamage(e, card, desc, reset, forced)
    local e1 =  RushDuel.CreateSingleEffect(e, desc, card, EFFECT_AVOID_BATTLE_DAMAGE, 1, reset, forced)
    local e2 =  RushDuel.CreateSingleEffect(e, desc, card, EFFECT_NO_BATTLE_DAMAGE, 1, reset, forced)
    return e1, e2
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **2** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.AttachNoBattleDamage) with `RushDuel.AttachNoBattleDamage`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Brassdes of the Diabolic Duds | `120301073` | [Rush/Scripts/c120301073.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120301073.lua) | 1 |
| The Disciple of Sacred Silence | `120306066` | [Rush/Scripts/c120306066.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120306066.lua) | 1 |

## Script Examples

### Brassdes of the Diabolic Duds (`120301073`)

Source: [Rush/Scripts/c120301073.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120301073.lua)

```lua
			local tc=g:GetFirst()
			RD.AttachAtkDef(e,c,tc:GetAttack(),0,RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
			RD.AttachNoBattleDamage(e,c,aux.Stringid(m,2),RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END+RESET_OPPO_TURN)
		end)
	end
```

### The Disciple of Sacred Silence (`120306066`)

Source: [Rush/Scripts/c120306066.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120306066.lua)

```lua
	local c=e:GetHandler()
	if c:IsFaceup() and c:IsRelateToEffect(e) then
		RD.AttachNoBattleDamage(e,c,aux.Stringid(m,1),RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END+RESET_OPPO_TURN)
		RD.CanSelectAndDoAction(aux.Stringid(m,1),HINTMSG_ATOHAND,aux.NecroValleyFilter(cm.thfilter),tp,LOCATION_GRAVE,0,1,1,nil,function(sg)
			RD.SendToHandAndExists(sg,e,tp,REASON_EFFECT)
```
