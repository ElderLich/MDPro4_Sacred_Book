# RushDuel.IsCanAttachBattleIndes

Alias: `RD.IsCanAttachBattleIndes`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsCanAttachBattleIndes(any card, any value) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 可否赋予效果 - 战斗破坏抗性
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `value` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:306`

```lua
function RushDuel.IsCanAttachBattleIndes(card, value)
    local values = RushDuel.GetEffectValues(card, EFFECT_INDESTRUCTABLE_BATTLE)
    for _, val in ipairs(values) do
        if val == 1 then
            return false
        end
    end
    return true
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **8** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.IsCanAttachBattleIndes) with `RushDuel.IsCanAttachBattleIndes`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Fusionic Defense | `120257064` | [Rush/Scripts/c120257064.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120257064.lua) | 1 |
| Skysavior Defense | `120301054` | [Rush/Scripts/c120301054.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120301054.lua) | 1 |
| Supreme Dog Ropero | `120239022` | [Rush/Scripts/c120239022.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120239022.lua) | 1 |
| Destined Doom of the Defiant Souls | `120298016` | [Rush/Scripts/c120298016.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120298016.lua) | 1 |
| Magic Fire Guard | `120217023` | [Rush/Scripts/c120217023.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120217023.lua) | 1 |
| Rolled Sticky Save | `120151046` | [Rush/Scripts/c120151046.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120151046.lua) | 1 |
| Transam Lightning | `120235056` | [Rush/Scripts/c120235056.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120235056.lua) | 1 |
| Spectral Swords of the Everloyal Guard | `120196047` | [Rush/Scripts/c120196047.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120196047.lua) | 1 |

## Script Examples

### Fusionic Defense (`120257064`)

Source: [Rush/Scripts/c120257064.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120257064.lua)

```lua
end
function cm.filter(c,tp)
	return c:IsFaceup() and (RD.IsCanAttachBattleIndes(c,1) or RD.IsCanAttachEffectIndes(c,tp,cm.indval))
end
function cm.condition(e,tp,eg,ep,ev,re,r,rp)
```

### Skysavior Defense (`120301054`)

Source: [Rush/Scripts/c120301054.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120301054.lua)

```lua
function cm.filter(c)
	return c:IsPosition(POS_FACEUP_ATTACK) and (c:IsRace(RACE_CELESTIALWARRIOR)
		or c:IsRace(RACE_WARRIOR)) and RD.IsCanAttachBattleIndes(c,1)
end
function cm.setfilter(c)
```

### Supreme Dog Ropero (`120239022`)

Source: [Rush/Scripts/c120239022.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120239022.lua)

```lua
end
function cm.condition(e,tp,eg,ep,ev,re,r,rp)
	return RD.IsCanAttachBattleIndes(e:GetHandler(),1)
end
cm.cost1=RD.CostPayLP(500)
```
