# RushDuel.AttachAvoidBattleDamage

Alias: `RD.AttachAvoidBattleDamage`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AttachAvoidBattleDamage(any e, any card, any desc, any reset, any forced) -> any
```

## Description

Rush Duel helper declared in `RDAttach.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
赋予: 战斗不会让自己受到伤害
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

`Rush/Utilities/RDAttach.lua:99`

```lua
function RushDuel.AttachAvoidBattleDamage(e, card, desc, reset, forced)
    local e1 =  RushDuel.CreateSingleEffect(e, desc, card, EFFECT_AVOID_BATTLE_DAMAGE, 1, reset, forced)
    return e1
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.AttachAvoidBattleDamage) with `RushDuel.AttachAvoidBattleDamage`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Rocket Warrior | `120307023` | [Rush/Scripts/c120307023.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120307023.lua) | 1 |

## Script Examples

### Rocket Warrior (`120307023`)

Source: [Rush/Scripts/c120307023.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120307023.lua)

```lua
		if c:IsFaceup() and c:IsRelateToEffect(e) then
			RD.AttachBattleIndes(e,c,1,aux.Stringid(m,2),RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
			RD.AttachAvoidBattleDamage(e,c,aux.Stringid(m,3),RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
		end
	end)
```
