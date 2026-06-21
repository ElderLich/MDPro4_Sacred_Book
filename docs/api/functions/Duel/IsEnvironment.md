# Duel.IsEnvironment

## Signature

```lua
Duel.IsEnvironment(int code, [int player], [int loc]) -> bool
```

## Description

Check whether the player player is the source code of the venue code
The site code refers to the code of the venue card in effect, or the value of the effect of the venue change
Source Player is the controller of the card in effect, or the controller of the Poseidon Witch, etc.

## Parameters

- `code` `int`
- `player` `int` optional - default: PLAYER_ALL
- `loc` `int` optional - default: LOCATION_ONFIELD

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4898`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **114** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.IsEnvironment`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Hojo the Vaylantz Warrior | `88919365` | [Scripts/c88919365.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88919365.lua) | 59 |
| Sea Stealth Attack | `19089195` | [Scripts/c19089195.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c19089195.lua) | 57 |
| Numeron Calling | `77402960` | [Scripts/c77402960.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77402960.lua) | 56 |
| Malefic Paradigm Dragon | `16958382` | [Scripts/c16958382.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16958382.lua) | 55 |
| Protector of The Agents - Moon | `90290572` | [Scripts/c90290572.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90290572.lua) | 50 |
| Arcana Force EX - The Chaos Ruler | `12686296` | [Scripts/c12686296.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12686296.lua) | 49 |
| Mega Fortress Whale | `96546575` | [Scripts/c96546575.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96546575.lua) | 49 |
| The Sacred Waters in the Sky | `26684111` | [Scripts/c26684111.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c26684111.lua) | 48 |
| Celestial Knightlord Parshath | `48589580` | [Scripts/c48589580.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48589580.lua) | 47 |
| Dream Mirror of Chaos | `98570539` | [Scripts/c98570539.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c98570539.lua) | 47 |
| Yorishiro of the Aqua | `57511992` | [Scripts/c57511992.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57511992.lua) | 46 |
| The Executor of the Underworld - Pluto | `37706769` | [Scripts/c37706769.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37706769.lua) | 45 |
| Light Force | `30913809` | [Scripts/c30913809.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30913809.lua) | 45 |
| Vaylantz Mad Marquess | `87897777` | [Scripts/c87897777.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87897777.lua) | 44 |
| Necrovalley Temple | `56773577` | [Scripts/c56773577.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56773577.lua) | 44 |
| Phantasm Spiral Power | `61397885` | [Scripts/c61397885.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61397885.lua) | 44 |
| Advanced Crystal Beast Cobalt Eagle | `45236142` | [Scripts/c45236142.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45236142.lua) | 43 |
| Phantasm Spiral Assault | `97795930` | [Scripts/c97795930.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97795930.lua) | 43 |
| Ocean Dragon Lord - Kairyu-Shin | `23931679` | [Scripts/c23931679.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23931679.lua) | 43 |
| Symphonic Warrior Rockks | `24070330` | [Scripts/c24070330.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24070330.lua) | 42 |
| Ojama Emperor | `34031284` | [Scripts/c34031284.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34031284.lua) | 42 |
| Prinzessin | `78527720` | [Scripts/c78527720.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78527720.lua) | 42 |
| Number C1: Numeron Chaos Gate Sunya | `79747096` | [Scripts/c79747096.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c79747096.lua) | 42 |
| Symphonic Warrior DJJ | `70204022` | [Scripts/c70204022.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70204022.lua) | 41 |
| ...and 90 more |  |  |  |

## Script Examples

### Hojo the Vaylantz Warrior (`88919365`)

Source: [Scripts/c88919365.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88919365.lua)

```lua
end
function c88919365.spcon(e,tp,eg,ep,ev,re,r,rp)
	return Duel.IsEnvironment(49568943) or Duel.IsExistingMatchingCard(c88919365.cfilter,tp,LOCATION_MZONE,0,1,nil)
end
function c88919365.sptg(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Sea Stealth Attack (`19089195`)

Source: [Scripts/c19089195.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c19089195.lua)

```lua
end
function c19089195.econ(e,tp,eg,ep,ev,re,r,rp)
	return Duel.IsEnvironment(22702055) and not Duel.IsPlayerAffectedByEffect(tp,19089195)
end
function c19089195.costfilter(c)
```

### Numeron Calling (`77402960`)

Source: [Scripts/c77402960.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77402960.lua)

```lua
end
function c77402960.condition(e,tp,eg,ep,ev,re,r,rp)
	return Duel.IsEnvironment(41418852,tp,LOCATION_FZONE) and Duel.GetFieldGroupCount(tp,LOCATION_MZONE,0)==0
end
function c77402960.spfilter(c,e,tp)
```
