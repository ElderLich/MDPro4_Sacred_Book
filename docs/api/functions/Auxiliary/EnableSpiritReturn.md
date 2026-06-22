# Auxiliary.EnableSpiritReturn

## Signature

```lua
Auxiliary.EnableSpiritReturn(Card c, int event1, [... int]) -> void
```

## Description

Registers Spirit return setup for c.
When any listed event happens, it creates End Phase return-to-hand effects in the Monster Zone, respecting EFFECT_SPIRIT_DONOT_RETURN and EFFECT_SPIRIT_MAYNOT_RETURN.

## Parameters

- `c` `Card`
- `event1` `int`
- `...` `int` optional

## Source

- `Utilities/utility.lua:167`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **39** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.EnableSpiritReturn`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Tsumuha-Kutsunagi the Lord of Swords | `78098950` | [Scripts/c78098950.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78098950.lua) | 39 |
| Rasetsu | `43378076` | [Scripts/c43378076.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43378076.lua) | 39 |
| Shinobird Crow | `39817919` | [Scripts/c39817919.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39817919.lua) | 38 |
| Han-Shi Kyudo Spirit | `53270092` | [Scripts/c53270092.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53270092.lua) | 36 |
| Shinobaron Shade Peacock | `60823690` | [Scripts/c60823690.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60823690.lua) | 36 |
| Hebo, Lord of the River | `90365482` | [Scripts/c90365482.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90365482.lua) | 36 |
| Yamato-no-Kami | `82841979` | [Scripts/c82841979.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82841979.lua) | 35 |
| Ichiki Sayori-Hime | `9627299` | [Scripts/c9627299.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9627299.lua) | 34 |
| Kinka-byo | `45452224` | [Scripts/c45452224.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45452224.lua) | 34 |
| Shinobaroness Shade Peacock | `33325951` | [Scripts/c33325951.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33325951.lua) | 32 |
| Izanami | `43543777` | [Scripts/c43543777.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43543777.lua) | 32 |
| Konohanasakuya | `57722593` | [Scripts/c57722593.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57722593.lua) | 30 |
| Sakitama | `67972302` | [Scripts/c67972302.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67972302.lua) | 30 |
| Nikitama | `24701235` | [Scripts/c24701235.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24701235.lua) | 29 |
| Amaterasu | `20073910` | [Scripts/c20073910.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20073910.lua) | 29 |
| Shinobird Crane | `66815913` | [Scripts/c66815913.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66815913.lua) | 29 |
| Kuro-Obi Karate Spirit | `77511331` | [Scripts/c77511331.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77511331.lua) | 27 |
| Gishki Emilia | `73551138` | [Scripts/c73551138.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c73551138.lua) | 27 |
| Gundari | `38975369` | [Scripts/c38975369.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38975369.lua) | 27 |
| Gishki Natalia | `17241370` | [Scripts/c17241370.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17241370.lua) | 27 |
| Yoko-Zuna Sumo Spirit | `40516623` | [Scripts/c40516623.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40516623.lua) | 26 |
| Maharaghi | `40695128` | [Scripts/c40695128.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40695128.lua) | 26 |
| Otohime | `39751093` | [Scripts/c39751093.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39751093.lua) | 26 |
| Yaksha | `94215860` | [Scripts/c94215860.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c94215860.lua) | 26 |
| ...and 15 more |  |  |  |

## Script Examples

### Tsumuha-Kutsunagi the Lord of Swords (`78098950`)

Source: [Scripts/c78098950.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78098950.lua)

```lua
	c:RegisterEffect(e0)
	--spirit return
	aux.EnableSpiritReturn(c,EVENT_SUMMON_SUCCESS,EVENT_FLIP)
	--summon with 1 tribute
	local e1=Effect.CreateEffect(c)
```

### Rasetsu (`43378076`)

Source: [Scripts/c43378076.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43378076.lua)

```lua
function c43378076.initial_effect(c)
	--spirit return
	aux.EnableSpiritReturn(c,EVENT_SUMMON_SUCCESS,EVENT_FLIP)
	--cannot special summon
	local e1=Effect.CreateEffect(c)
```

### Shinobird Crow (`39817919`)

Source: [Scripts/c39817919.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39817919.lua)

```lua
function c39817919.initial_effect(c)
	--spirit return
	aux.EnableSpiritReturn(c,EVENT_SUMMON_SUCCESS,EVENT_FLIP)
	--cannot special summon
	local e1=Effect.CreateEffect(c)
```
