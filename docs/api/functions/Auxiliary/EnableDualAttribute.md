# Auxiliary.EnableDualAttribute

## Signature

```lua
Auxiliary.EnableDualAttribute(Card c) -> void
```

## Description

Registers standard Gemini Monster handling on c.
The card can be Normal Summoned again, and while face-up in the Monster Zone or GY and not in Dual State, it is treated as a Normal Monster instead of an Effect Monster.

## Parameters

- `c` `Card`

## Source

- `Utilities/procedure.lua:22`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **45** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.EnableDualAttribute) with `Auxiliary.EnableDualAttribute`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Poly-Chemicritter Hydragon | `80476891` | [Scripts/c80476891.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80476891.lua) | 1 |
| Phoenix Gearfried | `69488544` | [Scripts/c69488544.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c69488544.lua) | 1 |
| Alien Hypno | `38468214` | [Scripts/c38468214.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38468214.lua) | 1 |
| Gem-Knight Iolite | `45662855` | [Scripts/c45662855.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45662855.lua) | 1 |
| Gem-Knight Amber | `72056560` | [Scripts/c72056560.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c72056560.lua) | 1 |
| Chemicritter Oxy Ox | `18993198` | [Scripts/c18993198.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18993198.lua) | 1 |
| Doom Shaman | `94944637` | [Scripts/c94944637.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c94944637.lua) | 1 |
| Poly-Chemicritter Dioxogre | `44088292` | [Scripts/c44088292.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44088292.lua) | 1 |
| Il Blud | `70595331` | [Scripts/c70595331.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70595331.lua) | 1 |
| Evocator Eveque | `16146511` | [Scripts/c16146511.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16146511.lua) | 1 |
| Blazewing Butterfly | `16984449` | [Scripts/c16984449.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16984449.lua) | 1 |
| Skelesaurus | `89362180` | [Scripts/c89362180.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c89362180.lua) | 1 |
| Chemicritter Hydron Hawk | `55100740` | [Scripts/c55100740.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55100740.lua) | 1 |
| Evocator Chevalier | `96872283` | [Scripts/c96872283.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96872283.lua) | 1 |
| Dark Valkyria | `83269557` | [Scripts/c83269557.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c83269557.lua) | 1 |
| Future Samurai | `90642597` | [Scripts/c90642597.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90642597.lua) | 1 |
| Geminize Lord Golknight | `72305034` | [Scripts/c72305034.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c72305034.lua) | 1 |
| Gemini Soldier | `68366996` | [Scripts/c68366996.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c68366996.lua) | 1 |
| Chemicritter Carbo Crab | `81599449` | [Scripts/c81599449.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81599449.lua) | 1 |
| Knight Day Grepher | `15767889` | [Scripts/c15767889.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15767889.lua) | 1 |
| Shadow Delver | `57827484` | [Scripts/c57827484.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57827484.lua) | 1 |
| Crusader of Endymion | `73853830` | [Scripts/c73853830.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c73853830.lua) | 1 |
| Gem-Knight Sardonyx | `43114901` | [Scripts/c43114901.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43114901.lua) | 1 |
| Hieratic Seal of the Dragon King | `64514622` | [Scripts/c64514622.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c64514622.lua) | 1 |
| ...and 21 more |  |  |  |

## Script Examples

### Poly-Chemicritter Hydragon (`80476891`)

Source: [Scripts/c80476891.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80476891.lua)

```lua
--進化合獣ヒュードラゴン
function c80476891.initial_effect(c)
	aux.EnableDualAttribute(c)
	--atkup
	local e1=Effect.CreateEffect(c)
```

### Phoenix Gearfried (`69488544`)

Source: [Scripts/c69488544.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c69488544.lua)

```lua
--フェニックス・ギア・フリード
function c69488544.initial_effect(c)
	aux.EnableDualAttribute(c)
	--special summon
	local e1=Effect.CreateEffect(c)
```

### Alien Hypno (`38468214`)

Source: [Scripts/c38468214.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38468214.lua)

```lua
--エーリアン・ヒュプノ
function c38468214.initial_effect(c)
	aux.EnableDualAttribute(c)
	--add counter
	local e1=Effect.CreateEffect(c)
```
