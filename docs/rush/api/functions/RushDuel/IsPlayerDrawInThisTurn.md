# RushDuel.IsPlayerDrawInThisTurn

Alias: `RD.IsPlayerDrawInThisTurn`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsPlayerDrawInThisTurn(any player) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 玩家在这个回合有抽卡
```

## Parameters

- `player` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:77`

```lua
function RushDuel.IsPlayerDrawInThisTurn(player)
    return Duel.GetFlagEffect(player, FLAG_HAS_DRAW_IN_TURN) ~= 0
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.IsPlayerDrawInThisTurn) with `RushDuel.IsPlayerDrawInThisTurn`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Fadronir the Wicked | `120294034` | [Rush/Scripts/c120294034.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120294034.lua) | 1 |

## Script Examples

### Fadronir the Wicked (`120294034`)

Source: [Rush/Scripts/c120294034.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120294034.lua)

```lua
end
function cm.condition(e,tp,eg,ep,ev,re,r,rp)
	return RD.IsPlayerDrawInThisTurn(1-tp)
end
cm.cost=RD.CostSendMZoneToGrave(cm.costfilter,1,1,false)
```
