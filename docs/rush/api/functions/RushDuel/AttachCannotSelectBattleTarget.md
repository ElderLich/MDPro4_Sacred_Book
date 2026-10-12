# RushDuel.AttachCannotSelectBattleTarget

Alias: `RD.AttachCannotSelectBattleTarget`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AttachCannotSelectBattleTarget(any e, any card, any value, any desc, any reset, any forced) -> any
```

## Description

Rush Duel helper declared in `RDAttach.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
赋予: 不能选择攻击目标
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `value` `any`: Type and behavior are not yet reviewed; see the source.
- `desc` `any`: Type and behavior are not yet reviewed; see the source.
- `reset` `any`: Type and behavior are not yet reviewed; see the source.
- `forced` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAttach.lua:178`

```lua
function RushDuel.AttachCannotSelectBattleTarget(e, card, value, desc, reset, forced)
    return RushDuel.CreateSingleEffect(e, desc, card, EFFECT_CANNOT_SELECT_BATTLE_TARGET, value, reset, forced)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **2** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.AttachCannotSelectBattleTarget) with `RushDuel.AttachCannotSelectBattleTarget`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Beast Gear King Convoy Liogon | `120145031` | [Rush/Scripts/c120145031.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120145031.lua) | 1 |
| Shock Dragon | `120130021` | [Rush/Scripts/c120130021.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120130021.lua) | 1 |

## Script Examples

### Beast Gear King Convoy Liogon (`120145031`)

Source: [Rush/Scripts/c120145031.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120145031.lua)

```lua
		local reset2=RESET_EVENT+RESETS_STANDARD-RESET_TURN_SET+RESET_PHASE+PHASE_END
		RD.AttachAtkDef(e,c,atk,0,reset1)
		RD.AttachCannotSelectBattleTarget(e,c,cm.atlimit,aux.Stringid(m,2),reset2)
		RD.AttachCannotDirectAttack(e,c,aux.Stringid(m,3),reset2)
		RD.AttachAttackAll(e,c,1,aux.Stringid(m,4),reset1)
```

### Shock Dragon (`120130021`)

Source: [Rush/Scripts/c120130021.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120130021.lua)

```lua
	if c:IsFaceup() and c:IsRelateToEffect(e) then
		--Attack Limit
		RD.AttachCannotSelectBattleTarget(e,c,cm.atlimit,aux.Stringid(m,1),RESET_EVENT+RESETS_STANDARD-RESET_TURN_SET+RESET_PHASE+PHASE_END)
		RD.AttachCannotDirectAttack(e,c,aux.Stringid(m,2),RESET_EVENT+RESETS_STANDARD-RESET_TURN_SET+RESET_PHASE+PHASE_END)
	end
```
