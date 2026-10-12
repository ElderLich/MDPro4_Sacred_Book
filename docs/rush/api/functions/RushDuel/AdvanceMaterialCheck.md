# RushDuel.AdvanceMaterialCheck

Alias: `RD.AdvanceMaterialCheck`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AdvanceMaterialCheck(any card, any effect, any getter) -> any
```

## Description

Rush Duel helper declared in `RDSummon.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
计算上级召唤时解放怪兽的合计值
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `effect` `any`: Type and behavior are not yet reviewed; see the source.
- `getter` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDSummon.lua:247`

```lua
function RushDuel.AdvanceMaterialCheck(card, effect, getter)
    local e = Effect.CreateEffect(card)
    e:SetType(EFFECT_TYPE_SINGLE)
    e:SetCode(EFFECT_MATERIAL_CHECK)
    e:SetLabelObject(effect)
    e:SetValue(RushDuel.AdvanceMaterialCheckValue(getter))
    card:RegisterEffect(e)
    return e
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **5** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.AdvanceMaterialCheck) with `RushDuel.AdvanceMaterialCheck`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Transam Prime Armor Nova | `120257008` | [Rush/Scripts/c120257008.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120257008.lua) | 1 |
| God Maju Garzett | `120261043` | [Rush/Scripts/c120261043.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120261043.lua) | 1 |
| Volcalize Ifrit | `120272004` | [Rush/Scripts/c120272004.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120272004.lua) | 1 |
| Maju Garzett | `120238004` | [Rush/Scripts/c120238004.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120238004.lua) | 1 |
| Great Maju Garzett | `120238019` | [Rush/Scripts/c120238019.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120238019.lua) | 1 |

## Script Examples

### Transam Prime Armor Nova (`120257008`)

Source: [Rush/Scripts/c120257008.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120257008.lua)

```lua
	c:RegisterEffect(e2)
	--Material Check
	RD.AdvanceMaterialCheck(c,e2,cm.getter)
	--Continuous Effect
	RD.AddContinuousEffect(c,e1)
```

### God Maju Garzett (`120261043`)

Source: [Rush/Scripts/c120261043.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120261043.lua)

```lua
	c:RegisterEffect(e2)
	--Material Check
	RD.AdvanceMaterialCheck(c,e2,cm.getter)
	--Continuous Effect
	RD.AddContinuousEffect(c,e1)
```

### Volcalize Ifrit (`120272004`)

Source: [Rush/Scripts/c120272004.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120272004.lua)

```lua
	c:RegisterEffect(e1)
	--Material Check
	RD.AdvanceMaterialCheck(c,e1,cm.getter)
	--Continuous Effect
	RD.AddContinuousEffect(c,e1)
```
