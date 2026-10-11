# RushDuel.IsCanAttachExtraAttackMonster

Alias: `RD.IsCanAttachExtraAttackMonster`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsCanAttachExtraAttackMonster(any card, any value) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 可否赋予效果 - 多次攻击 (怪兽限定)
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `value` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:260`

```lua
function RushDuel.IsCanAttachExtraAttackMonster(card, value)
    if not RushDuel.IsCanAttack(card) then
        return false
    end
    local values = RushDuel.GetEffectValues(card, EFFECT_EXTRA_ATTACK_MONSTER)
    for _, val in ipairs(values) do
        if val >= value then
            return false
        end
    end
    return true
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **6** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.IsCanAttachExtraAttackMonster) with `RushDuel.IsCanAttachExtraAttackMonster`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Meet and Greed | `120208044` | [Rush/Scripts/c120208044.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120208044.lua) | 1 |
| Mega Multistrike Dragon Dragias Burst \[L\] | `120210001` | [Rush/Scripts/c120210001.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120210001.lua) | 1 |
| Elemental HERO Sky Neos | `120272066` | [Rush/Scripts/c120272066.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120272066.lua) | 1 |
| Gilford the Rising | `120235028` | [Rush/Scripts/c120235028.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120235028.lua) | 1 |
| Neutron Blast | `120283038` | [Rush/Scripts/c120283038.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120283038.lua) | 1 |
| Degrace, the Flash Skysavior | `120235040` | [Rush/Scripts/c120235040.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120235040.lua) | 1 |

## Script Examples

### Meet and Greed (`120208044`)

Source: [Rush/Scripts/c120208044.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120208044.lua)

```lua
--Activate
function cm.filter(c)
	return c:IsFaceup() and c:IsType(TYPE_NORMAL) and c:IsRace(RACE_BEAST) and RD.IsCanAttachExtraAttackMonster(c,2)
end
function cm.exfilter(c)
```

### Mega Multistrike Dragon Dragias Burst [L] (`120210001`)

Source: [Rush/Scripts/c120210001.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120210001.lua)

```lua
--Multiple Attack
function cm.condition(e,tp,eg,ep,ev,re,r,rp)
	return RD.MaximumMode(e) and Duel.IsAbleToEnterBP() and RD.IsCanAttachExtraAttackMonster(e:GetHandler(),2)
end
cm.cost=RD.CostSendDeckTopToGrave(1)
```

### Elemental HERO Sky Neos (`120272066`)

Source: [Rush/Scripts/c120272066.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120272066.lua)

```lua
	local c=e:GetHandler()
	return Duel.GetLP(tp)~=Duel.GetLP(1-tp) and Duel.IsAbleToEnterBP()
		and RD.IsCanAttachExtraAttackMonster(c,1)
end
cm.cost=RD.CostSendDeckTopToGrave(1)
```
