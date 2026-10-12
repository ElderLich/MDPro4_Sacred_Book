# RushDuel.IsPlayerCanActivateTrapBattle

Alias: `RD.IsPlayerCanActivateTrapBattle`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsPlayerCanActivateTrapBattle(any player) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 玩家是否能够在战斗阶段发动陷阱卡
```

## Parameters

- `player` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:417`

```lua
function RushDuel.IsPlayerCanActivateTrapBattle(player)
    return RushDuel.IsPlayerCanActivateTrap(player) and not Duel.IsPlayerAffectedByEffect(player, EFFECT_PLAYER_CANNOT_ACTIVATE_TRAP_BATTLE)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.IsPlayerCanActivateTrapBattle) with `RushDuel.IsPlayerCanActivateTrapBattle`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Dark Matter Jelly | `120261022` | [Rush/Scripts/c120261022.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120261022.lua) | 1 |

## Script Examples

### Dark Matter Jelly (`120261022`)

Source: [Rush/Scripts/c120261022.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120261022.lua)

```lua
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	local c=e:GetHandler()
	if chk==0 then return RD.IsPlayerCanActivateTrapBattle(1-tp) and RD.IsCanChangePosition(c,e,tp,REASON_EFFECT) and c:IsCanTurnSet() end
	Duel.SetOperationInfo(0,CATEGORY_POSITION,c,1,0,0)
end
```
