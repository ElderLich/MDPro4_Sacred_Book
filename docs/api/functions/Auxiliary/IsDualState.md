# Auxiliary.IsDualState

## Signature

```lua
Auxiliary.IsDualState(Effect e) -> bool
```

## Description

Condition helper that is true when e's handler is not disabled and is in Dual State.

## Parameters

- `e` `Effect`

## Returns

- `bool`

## Source

- `Utilities/procedure.lua:10`

## Guided Examples

Learn how to use this function in context:

- [Gemini Monsters](/learn/gemini-monsters)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **43** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.IsDualState) with `Auxiliary.IsDualState`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Poly-Chemicritter Hydragon | `80476891` | [Scripts/c80476891.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80476891.lua) | 2 |
| Phoenix Gearfried | `69488544` | [Scripts/c69488544.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c69488544.lua) | 2 |
| Alien Hypno | `38468214` | [Scripts/c38468214.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38468214.lua) | 1 |
| Gem-Knight Iolite | `45662855` | [Scripts/c45662855.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45662855.lua) | 1 |
| Gem-Knight Amber | `72056560` | [Scripts/c72056560.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c72056560.lua) | 1 |
| Chemicritter Oxy Ox | `18993198` | [Scripts/c18993198.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18993198.lua) | 1 |
| Doom Shaman | `94944637` | [Scripts/c94944637.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c94944637.lua) | 1 |
| Poly-Chemicritter Dioxogre | `44088292` | [Scripts/c44088292.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44088292.lua) | 2 |
| Il Blud | `70595331` | [Scripts/c70595331.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70595331.lua) | 1 |
| Evocator Eveque | `16146511` | [Scripts/c16146511.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16146511.lua) | 1 |
| Blazewing Butterfly | `16984449` | [Scripts/c16984449.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16984449.lua) | 1 |
| Skelesaurus | `89362180` | [Scripts/c89362180.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c89362180.lua) | 2 |
| Chemicritter Hydron Hawk | `55100740` | [Scripts/c55100740.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55100740.lua) | 1 |
| Evocator Chevalier | `96872283` | [Scripts/c96872283.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96872283.lua) | 1 |
| Dark Valkyria | `83269557` | [Scripts/c83269557.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c83269557.lua) | 4 |
| Future Samurai | `90642597` | [Scripts/c90642597.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90642597.lua) | 1 |
| Geminize Lord Golknight | `72305034` | [Scripts/c72305034.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c72305034.lua) | 2 |
| Gemini Soldier | `68366996` | [Scripts/c68366996.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c68366996.lua) | 2 |
| Chemicritter Carbo Crab | `81599449` | [Scripts/c81599449.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81599449.lua) | 1 |
| Shadow Delver | `57827484` | [Scripts/c57827484.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57827484.lua) | 1 |
| Crusader of Endymion | `73853830` | [Scripts/c73853830.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c73853830.lua) | 1 |
| Gem-Knight Sardonyx | `43114901` | [Scripts/c43114901.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43114901.lua) | 1 |
| Hieratic Seal of the Dragon King | `64514622` | [Scripts/c64514622.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c64514622.lua) | 1 |
| Darkstorm Dragon | `57662975` | [Scripts/c57662975.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57662975.lua) | 1 |
| ...and 19 more |  |  |  |

## Script Examples

### Poly-Chemicritter Hydragon (`80476891`)

Source: [Scripts/c80476891.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80476891.lua)

```lua
	e1:SetRange(LOCATION_MZONE)
	e1:SetCode(EVENT_SUMMON_SUCCESS)
	e1:SetCondition(aux.IsDualState)
	e1:SetTarget(c80476891.target)
	e1:SetOperation(c80476891.operation)
```

### Phoenix Gearfried (`69488544`)

Source: [Scripts/c69488544.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c69488544.lua)

```lua
function c69488544.spcon(e,tp,eg,ep,ev,re,r,rp)
	return not e:GetHandler():IsStatus(STATUS_BATTLE_DESTROYED)
		and aux.IsDualState(e) and rp==1-tp and re:IsActiveType(TYPE_SPELL) and re:IsHasType(EFFECT_TYPE_ACTIVATE)
end
function c69488544.filter(c,e,tp)
```

### Alien Hypno (`38468214`)

Source: [Scripts/c38468214.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38468214.lua)

```lua
	e1:SetType(EFFECT_TYPE_IGNITION)
	e1:SetRange(LOCATION_MZONE)
	e1:SetCondition(aux.IsDualState)
	e1:SetTarget(c38468214.target)
	e1:SetOperation(c38468214.operation)
```
