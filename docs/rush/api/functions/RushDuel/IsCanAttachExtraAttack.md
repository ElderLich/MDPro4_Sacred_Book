# RushDuel.IsCanAttachExtraAttack

Alias: `RD.IsCanAttachExtraAttack`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsCanAttachExtraAttack(any card, any value) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 可否赋予效果 - 多次攻击
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `value` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:247`

```lua
function RushDuel.IsCanAttachExtraAttack(card, value)
    if not RushDuel.IsCanAttack(card) then
        return false
    end
    local values = RushDuel.GetEffectValues(card, EFFECT_EXTRA_ATTACK)
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

- Detected in **17** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.IsCanAttachExtraAttack) with `RushDuel.IsCanAttachExtraAttack`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| The Trinity Dragiastar | `120109031` | [Rush/Scripts/c120109031.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120109031.lua) | 1 |
| The Dragiastar | `120235035` | [Rush/Scripts/c120235035.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120235035.lua) | 1 |
| Gias x Gias | `120246032` | [Rush/Scripts/c120246032.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120246032.lua) | 1 |
| Lightning Volteagle | `120246001` | [Rush/Scripts/c120246001.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120246001.lua) | 1 |
| Purple-Eyes Star Cat | `120235014` | [Rush/Scripts/c120235014.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120235014.lua) | 1 |
| Cross Lostream Melutine | `120309036` | [Rush/Scripts/c120309036.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120309036.lua) | 1 |
| Madrhea Aquila | `120244030` | [Rush/Scripts/c120244030.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120244030.lua) | 1 |
| Double Chill Dragons | `120235034` | [Rush/Scripts/c120235034.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120235034.lua) | 1 |
| Steel Steed Martin Vainari | `120238016` | [Rush/Scripts/c120238016.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120238016.lua) | 1 |
| Ghost Vicious | `120228033` | [Rush/Scripts/c120228033.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120228033.lua) | 1 |
| Hyperstrike Dragon Dragiastar F | `120196022` | [Rush/Scripts/c120196022.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120196022.lua) | 1 |
| Multistrike Dragon Dragias | `120110001` | [Rush/Scripts/c120110001.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120110001.lua) | 1 |
| Vice Jacker | `120170025` | [Rush/Scripts/c120170025.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120170025.lua) | 1 |
| Digracheon the Skysavior Radiaknight | `120301036` | [Rush/Scripts/c120301036.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120301036.lua) | 1 |
| Abad the Negahell Emperor | `120290100` | [Rush/Scripts/c120290100.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120290100.lua) | 1 |
| Hydra Viper | `120109047` | [Rush/Scripts/c120109047.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120109047.lua) | 1 |
| Twin Edge Dragon | `120110006` | [Rush/Scripts/c120110006.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120110006.lua) | 1 |

## Script Examples

### The Trinity Dragiastar (`120109031`)

Source: [Rush/Scripts/c120109031.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120109031.lua)

```lua
--Attack Thrice
function cm.target1(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsAbleToEnterBP() and RD.IsCanAttachExtraAttack(e:GetHandler(),2) end
	Duel.Hint(HINT_OPSELECTED,1-tp,e:GetDescription())
end
```

### The Dragiastar (`120235035`)

Source: [Rush/Scripts/c120235035.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120235035.lua)

```lua
--Attack Twice
function cm.filter1(c)
	return c:IsPosition(POS_FACEUP_ATTACK) and RD.IsCanAttachExtraAttack(c,1)
end
function cm.target1(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Gias x Gias (`120246032`)

Source: [Rush/Scripts/c120246032.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120246032.lua)

```lua
end
function cm.exfilter(c,tc)
	return c:IsFaceup() and c:IsLevel(tc:GetLevel()) and c:IsRace(tc:GetRace()) and RD.IsCanAttachExtraAttack(c,1)
end
cm.cost=RD.CostSendHandToGrave(cm.costfilter,1,1)
```
