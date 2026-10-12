# RushDuel.AttachAttackAll

Alias: `RD.AttachAttackAll`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AttachAttackAll(any e, any card, any value, any desc, any reset, any forced) -> any
```

## Description

Rush Duel helper declared in `RDAttach.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
赋予: 全体攻击
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

`Rush/Utilities/RDAttach.lua:34`

```lua
function RushDuel.AttachAttackAll(e, card, value, desc, reset, forced)
    return RushDuel.CreateSingleEffect(e, desc, card, EFFECT_ATTACK_ALL, value, reset, forced)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **4** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.AttachAttackAll) with `RushDuel.AttachAttackAll`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Beast Gear King Convoy Liogon | `120145031` | [Rush/Scripts/c120145031.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120145031.lua) | 1 |
| Supreme Skystream Magnum Overlord \[R\] | `120151003` | [Rush/Scripts/c120151003.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120151003.lua) | 1 |
| OuTerverSe Endless Doom Oblivion | `120290029` | [Rush/Scripts/c120290029.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120290029.lua) | 1 |
| The Perfect Dragiastar | `120283026` | [Rush/Scripts/c120283026.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120283026.lua) | 1 |

## Script Examples

### Beast Gear King Convoy Liogon (`120145031`)

Source: [Rush/Scripts/c120145031.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120145031.lua)

```lua
		RD.AttachCannotSelectBattleTarget(e,c,cm.atlimit,aux.Stringid(m,2),reset2)
		RD.AttachCannotDirectAttack(e,c,aux.Stringid(m,3),reset2)
		RD.AttachAttackAll(e,c,1,aux.Stringid(m,4),reset1)
	end
	RD.CreateHintEffect(e,aux.Stringid(m,1),tp,1,0,RESET_PHASE+PHASE_END)
```

### Supreme Skystream Magnum Overlord [R] (`120151003`)

Source: [Rush/Scripts/c120151003.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120151003.lua)

```lua
		RD.AttachAtkDef(e,c,-1000,0,reset)
		RD.AttachCannotDirectAttack(e,c,aux.Stringid(m,1),reset)
		RD.AttachAttackAll(e,c,1,aux.Stringid(m,2),reset)
		RD.AttachPierce(e,c,aux.Stringid(m,3),reset)
	end
```

### OuTerverSe Endless Doom Oblivion (`120290029`)

Source: [Rush/Scripts/c120290029.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120290029.lua)

```lua
	if c:IsFaceup() and c:IsRelateToEffect(e) then
		RD.ChangeRace(e,c,RACE_GALAXY,RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
		RD.AttachAttackAll(e,c,1,aux.Stringid(m,1),RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
	end
end
```
