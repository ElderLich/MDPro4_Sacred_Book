# Duel.IsEnvironment

## Signature

```lua
Duel.IsEnvironment(int code, [int player], [int loc]) -> bool
```

## Description

Checks whether code is currently treated as the environment card or as a matching face-up card in the requested locations.
player defaults to PLAYER_ALL and loc defaults to LOCATION_ONFIELD. The core checks Field Zones first; if no face-up Field Zone card exists, it can also match the latest EFFECT_CHANGE_ENVIRONMENT effect.

## Parameters

- `code` `int`
- `player` `int` optional - default: PLAYER_ALL
- `loc` `int` optional - default: LOCATION_ONFIELD

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4898`

## Guided Examples

Learn how to use this function in context:

- [Field Spells](/learn/field-spells)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **121** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.IsEnvironment) with `Duel.IsEnvironment`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Hojo the Vaylantz Warrior | `88919365` | [Scripts/c88919365.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c88919365.lua) | 1 |
| Sea Stealth Attack | `19089195` | [Scripts/c19089195.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c19089195.lua) | 2 |
| Numeron Calling | `77402960` | [Scripts/c77402960.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c77402960.lua) | 1 |
| Malefic Paradigm Dragon | `16958382` | [Scripts/c16958382.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c16958382.lua) | 1 |
| Protector of The Agents - Moon | `90290572` | [Scripts/c90290572.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c90290572.lua) | 2 |
| Arcana Force EX - The Chaos Ruler | `12686296` | [Scripts/c12686296.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c12686296.lua) | 1 |
| Mega Fortress Whale | `96546575` | [Scripts/c96546575.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c96546575.lua) | 1 |
| The Sacred Waters in the Sky | `26684111` | [Scripts/c26684111.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c26684111.lua) | 1 |
| Celestial Knightlord Parshath | `48589580` | [Scripts/c48589580.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c48589580.lua) | 2 |
| Dream Mirror of Chaos | `98570539` | [Scripts/c98570539.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c98570539.lua) | 4 |
| Yorishiro of the Aqua | `57511992` | [Scripts/c57511992.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c57511992.lua) | 2 |
| The Executor of the Underworld - Pluto | `37706769` | [Scripts/c37706769.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c37706769.lua) | 1 |
| Light Force | `30913809` | [Scripts/c30913809.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c30913809.lua) | 1 |
| Atlantis Call | `65785782` | [Scripts/c65785782.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c65785782.lua) | 1 |
| Coralianektes the Shimmering Shining Dragon | `82692552` | [Scripts/c82692552.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c82692552.lua) | 1 |
| Vaylantz Mad Marquess | `87897777` | [Scripts/c87897777.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c87897777.lua) | 1 |
| Necrovalley Temple | `56773577` | [Scripts/c56773577.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c56773577.lua) | 1 |
| Phantasm Spiral Power | `61397885` | [Scripts/c61397885.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c61397885.lua) | 1 |
| Advanced Crystal Beast Cobalt Eagle | `45236142` | [Scripts/c45236142.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c45236142.lua) | 1 |
| Phantasm Spiral Assault | `97795930` | [Scripts/c97795930.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c97795930.lua) | 1 |
| Ocean Dragon Lord - Kairyu-Shin | `23931679` | [Scripts/c23931679.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c23931679.lua) | 1 |
| Symphonic Warrior Rockks | `24070330` | [Scripts/c24070330.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c24070330.lua) | 1 |
| Ojama Emperor | `34031284` | [Scripts/c34031284.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c34031284.lua) | 1 |
| Prinzessin | `78527720` | [Scripts/c78527720.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c78527720.lua) | 1 |
| ...and 97 more |  |  |  |

## Script Examples

### Hojo the Vaylantz Warrior (`88919365`)

Source: [Scripts/c88919365.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c88919365.lua)

```lua
end
function c88919365.spcon(e,tp,eg,ep,ev,re,r,rp)
	return Duel.IsEnvironment(49568943) or Duel.IsExistingMatchingCard(c88919365.cfilter,tp,LOCATION_MZONE,0,1,nil)
end
function c88919365.sptg(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Sea Stealth Attack (`19089195`)

Source: [Scripts/c19089195.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c19089195.lua)

```lua
end
function c19089195.econ(e,tp,eg,ep,ev,re,r,rp)
	return Duel.IsEnvironment(22702055) and not Duel.IsPlayerAffectedByEffect(tp,19089195)
end
function c19089195.costfilter(c)
```

### Numeron Calling (`77402960`)

Source: [Scripts/c77402960.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c77402960.lua)

```lua
end
function c77402960.condition(e,tp,eg,ep,ev,re,r,rp)
	return Duel.IsEnvironment(41418852,tp,LOCATION_FZONE) and Duel.GetFieldGroupCount(tp,LOCATION_MZONE,0)==0
end
function c77402960.spfilter(c,e,tp)
```
