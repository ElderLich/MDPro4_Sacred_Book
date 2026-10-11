# RushDuel.IsPlayerNoDrawInThisMain

Alias: `RD.IsPlayerNoDrawInThisMain`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsPlayerNoDrawInThisMain(any player) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 玩家在这次主要阶段没有抽卡
```

## Parameters

- `player` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:73`

```lua
function RushDuel.IsPlayerNoDrawInThisMain(player)
    return Duel.GetFlagEffect(player, FLAG_HAS_DRAW_IN_MAIN_PHASE) == 0
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **9** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.IsPlayerNoDrawInThisMain) with `RushDuel.IsPlayerNoDrawInThisMain`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Moonforce Rifet | `120300012` | [Rush/Scripts/c120300012.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300012.lua) | 1 |
| Executie Mates | `120283050` | [Rush/Scripts/c120283050.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120283050.lua) | 1 |
| Cosmic Sucker | `120294021` | [Rush/Scripts/c120294021.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120294021.lua) | 2 |
| Speed Roll | `120301063` | [Rush/Scripts/c120301063.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120301063.lua) | 1 |
| Pliage the Sacred Shooting Star | `120274069` | [Rush/Scripts/c120274069.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120274069.lua) | 1 |
| Winged Dragon of Chaos | `120280006` | [Rush/Scripts/c120280006.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120280006.lua) | 1 |
| Plasmatic Model Lenoir | `120285021` | [Rush/Scripts/c120285021.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120285021.lua) | 1 |
| Rolling x Rolling | `120294048` | [Rush/Scripts/c120294048.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120294048.lua) | 1 |
| Innocent Fadrawl | `120261037` | [Rush/Scripts/c120261037.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120261037.lua) | 1 |

## Script Examples

### Moonforce Rifet (`120300012`)

Source: [Rush/Scripts/c120300012.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300012.lua)

```lua
	if RD.SendDeckTopToGraveAndExists(1-tp,2)
		and Duel.IsExistingMatchingCard(cm.confilter,tp,0,LOCATION_GRAVE,5,nil)
		and RD.IsPlayerNoDrawInThisMain(tp) then
		RD.CanDraw(aux.Stringid(m,1),tp,2,true)
	end
```

### Executie Mates (`120283050`)

Source: [Rush/Scripts/c120283050.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120283050.lua)

```lua
	if c:IsFaceup() and c:IsRelateToEffect(e) then
		RD.AttachLevel(e,c,2,RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
		if RD.IsPlayerNoDrawInThisMain(tp) then
			RD.CanDraw(aux.Stringid(m,1),tp,1)
		end
```

### Cosmic Sucker (`120294021`)

Source: [Rush/Scripts/c120294021.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120294021.lua)

```lua
end
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return not RD.IsPlayerNoDrawInThisMain(tp) or Duel.IsPlayerCanDraw(tp,1) end
	RD.TargetRecover(tp,300)
end
```
