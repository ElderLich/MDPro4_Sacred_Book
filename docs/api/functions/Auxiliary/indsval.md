# Auxiliary.indsval

## Signature

```lua
Auxiliary.indsval(Effect e, Effect re, int rp) -> bool
```

## Description

Value helper for self-protection from effect destruction; it returns true when the reason player is the handler's player.

## Parameters

- `e` `Effect`
- `re` `Effect`
- `rp` `int`

## Returns

- `bool`

## Source

- `Utilities/utility.lua:824`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **3** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.indsval`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Pendulum Encore | `6992184` | [Scripts/c6992184.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6992184.lua) | 39 |
| Magical Mid-Breaker Field | `71650854` | [Scripts/c71650854.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71650854.lua) | 23 |
| Defense Zone | `59687381` | [Scripts/c59687381.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59687381.lua) | 20 |

## Script Examples

### Pendulum Encore (`6992184`)

Source: [Scripts/c6992184.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6992184.lua)

```lua
		local e2=e1:Clone()
		e2:SetCode(EFFECT_INDESTRUCTABLE_EFFECT)
		e2:SetValue(aux.indsval)
		Duel.RegisterEffect(e2,tp)
		local e3=Effect.CreateEffect(c)
```

### Magical Mid-Breaker Field (`71650854`)

Source: [Scripts/c71650854.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71650854.lua)

```lua
	e5:SetCode(EFFECT_INDESTRUCTABLE_EFFECT)
	e5:SetProperty(EFFECT_FLAG_SET_AVAILABLE)
	e5:SetValue(aux.indsval)
	c:RegisterEffect(e5)
	--cannot set/activate
```

### Defense Zone (`59687381`)

Source: [Scripts/c59687381.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59687381.lua)

```lua
	local e4=e3:Clone()
	e4:SetCode(EFFECT_INDESTRUCTABLE_EFFECT)
	e4:SetValue(aux.indsval)
	c:RegisterEffect(e4)
end
```
