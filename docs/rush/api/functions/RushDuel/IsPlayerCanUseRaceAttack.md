# RushDuel.IsPlayerCanUseRaceAttack

Alias: `RD.IsPlayerCanUseRaceAttack`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsPlayerCanUseRaceAttack(any player, any race) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 玩家是否能够使用特定种族进行攻击
```

## Parameters

- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `race` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:400`

```lua
function RushDuel.IsPlayerCanUseRaceAttack(player, race)
    if Duel.IsPlayerAffectedByEffect(player, EFFECT_PLAYER_CANNOT_ATTACK) then
        return false
    end
    local effects = {Duel.IsPlayerAffectedByEffect(player, EFFECT_PLAYER_RACE_CANNOT_ATTACK)}
    for i, effect in ipairs(effects) do
        if (race & effect:GetValue()) == race then
            return false
        end
    end
    return true
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **2** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.IsPlayerCanUseRaceAttack) with `RushDuel.IsPlayerCanUseRaceAttack`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Ensembullfighter the Music Fiend | `120155028` | [Rush/Scripts/c120155028.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120155028.lua) | 1 |
| Constructor Blockade | `120155054` | [Rush/Scripts/c120155054.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120155054.lua) | 1 |

## Script Examples

### Ensembullfighter the Music Fiend (`120155028`)

Source: [Rush/Scripts/c120155028.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120155028.lua)

```lua
--Cannot Activate
function cm.condition(e,tp,eg,ep,ev,re,r,rp)
	return Duel.IsAbleToEnterBP() and RD.IsPlayerCanUseRaceAttack(tp,RACE_WARRIOR)
		and RD.IsPlayerCanActivateTrap(1-tp)
end
```

### Constructor Blockade (`120155054`)

Source: [Rush/Scripts/c120155054.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120155054.lua)

```lua
end
function cm.filter(c,tp)
	return c:IsFaceup() and RD.IsPlayerCanUseRaceAttack(1-tp,c:GetRace())
end
function cm.condition(e,tp,eg,ep,ev,re,r,rp)
```
