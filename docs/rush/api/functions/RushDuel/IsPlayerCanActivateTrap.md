# RushDuel.IsPlayerCanActivateTrap

Alias: `RD.IsPlayerCanActivateTrap`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsPlayerCanActivateTrap(any player) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 玩家是否能够发动陷阱卡
```

## Parameters

- `player` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:413`

```lua
function RushDuel.IsPlayerCanActivateTrap(player)
    return not Duel.IsPlayerAffectedByEffect(player, EFFECT_PLAYER_CANNOT_ACTIVATE_TRAP)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.IsPlayerCanActivateTrap) with `RushDuel.IsPlayerCanActivateTrap`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Ensembullfighter the Music Fiend | `120155028` | [Rush/Scripts/c120155028.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120155028.lua) | 1 |

## Script Examples

### Ensembullfighter the Music Fiend (`120155028`)

Source: [Rush/Scripts/c120155028.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120155028.lua)

```lua
function cm.condition(e,tp,eg,ep,ev,re,r,rp)
	return Duel.IsAbleToEnterBP() and RD.IsPlayerCanUseRaceAttack(tp,RACE_WARRIOR)
		and RD.IsPlayerCanActivateTrap(1-tp)
end
cm.cost=RD.CostSendHandToGrave(Card.IsAbleToGraveAsCost,1,1)
```
