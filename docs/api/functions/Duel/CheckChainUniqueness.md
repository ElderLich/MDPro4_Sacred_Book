# Duel.CheckChainUniqueness

## Signature

```lua
Duel.CheckChainUniqueness() -> bool
```

## Description

Checks whether all current Chain Links have different handler card codes.

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5065`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **8** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.CheckChainUniqueness`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Lightning Punisher | `45023678` | [Scripts/c45023678.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45023678.lua) | 28 |
| Iris, the Earth Mother | `9628664` | [Scripts/c9628664.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9628664.lua) | 23 |
| Surprise Chain | `70491413` | [Scripts/c70491413.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70491413.lua) | 22 |
| Mystical Wind Typhoon | `63516460` | [Scripts/c63516460.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63516460.lua) | 22 |
| Miraculous Rebirth | `37011715` | [Scripts/c37011715.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37011715.lua) | 21 |
| Chain Summoning | `9952083` | [Scripts/c9952083.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9952083.lua) | 18 |
| Accumulated Fortune | `98444741` | [Scripts/c98444741.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c98444741.lua) | 17 |
| Chain Strike | `91623717` | [Scripts/c91623717.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c91623717.lua) | 15 |

## Script Examples

### Lightning Punisher (`45023678`)

Source: [Scripts/c45023678.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45023678.lua)

```lua
	if ct==1 then
		e:SetLabel(0)
	elseif not Duel.CheckChainUniqueness() then
		e:SetLabel(2)
	elseif ct>=3 and e:GetLabel()~=2 then
```

### Iris, the Earth Mother (`9628664`)

Source: [Scripts/c9628664.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9628664.lua)

```lua
	if ct==1 then
		e:SetLabel(0)
	elseif not Duel.CheckChainUniqueness() then
		e:SetLabel(2)
	elseif ct>=3 and e:GetLabel()~=2 then
```

### Surprise Chain (`70491413`)

Source: [Scripts/c70491413.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70491413.lua)

```lua
end
function c70491413.condition(e,tp,eg,ep,ev,re,r,rp)
	return Duel.GetCurrentChain()>0 and Duel.CheckChainUniqueness()
end
function c70491413.target(e,tp,eg,ep,ev,re,r,rp,chk)
```
