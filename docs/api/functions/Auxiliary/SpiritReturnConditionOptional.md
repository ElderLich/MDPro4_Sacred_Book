# Auxiliary.SpiritReturnConditionOptional

## Signature

```lua
Auxiliary.SpiritReturnConditionOptional(Effect e, int tp, Group eg, int ep, any ev, Effect re, any r, int rp) -> bool
```

## Description

Condition for the optional Spirit Monster End Phase return effect. It returns true while the handler is not prevented from returning and does have the optional-return permission effect.

## Parameters

- `e` `Effect`
- `tp` `int`
- `eg` `Group`
- `ep` `int`
- `ev` `any`
- `re` `Effect`
- `r` `any`
- `rp` `int`

## Returns

- `bool` - true if the optional Spirit return effect should apply.

## Source

- `Utilities/utility.lua:208`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **3** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.SpiritReturnConditionOptional) with `Auxiliary.SpiritReturnConditionOptional`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Shinobaroness Peacock | `25415052` | [Scripts/c25415052.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c25415052.lua) | 1 |
| Shinobaron Peacock | `52900000` | [Scripts/c52900000.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c52900000.lua) | 1 |
| Sacred Spirit of the Ice Barrier | `44877690` | [Scripts/c44877690.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c44877690.lua) | 1 |

## Script Examples

### Shinobaroness Peacock (`25415052`)

Source: [Scripts/c25415052.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c25415052.lua)

```lua
	local e2=e1:Clone()
	e2:SetType(EFFECT_TYPE_FIELD+EFFECT_TYPE_TRIGGER_O)
	e2:SetCondition(aux.SpiritReturnConditionOptional)
	c:RegisterEffect(e2)
end
```

### Shinobaron Peacock (`52900000`)

Source: [Scripts/c52900000.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c52900000.lua)

```lua
	local e2=e1:Clone()
	e2:SetType(EFFECT_TYPE_FIELD+EFFECT_TYPE_TRIGGER_O)
	e2:SetCondition(aux.SpiritReturnConditionOptional)
	c:RegisterEffect(e2)
end
```

### Sacred Spirit of the Ice Barrier (`44877690`)

Source: [Scripts/c44877690.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c44877690.lua)

```lua
		return aux.SpiritReturnConditionForced(e,tp,eg,ep,ev,re,r,rp)
	else
		return aux.SpiritReturnConditionOptional(e,tp,eg,ep,ev,re,r,rp)
	end
end
```
