# Card.SetSPSummonOnce

## Signature

```lua
Card.SetSPSummonOnce(Card c, int spsummon_code) -> void
```

## Description

Marks c as sharing a once-per-turn Special Summon limit under spsummon_code.
Cards with the same nonzero spsummon_code share the limit for each player. The binding does nothing while c is copying another card's effect.

## Parameters

- `c` `Card`
- `spsummon_code` `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3661`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **76** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.SetSPSummonOnce`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Odd-Eyes Rebellion Dragon Overlord | `98452268` | [Scripts/c98452268.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c98452268.lua) | 55 |
| Veda Kalarcanum | `40785230` | [Scripts/c40785230.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40785230.lua) | 55 |
| Dreaming Nemleria | `70155677` | [Scripts/c70155677.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70155677.lua) | 55 |
| Sosei Ryu-Ge Mistva | `92487128` | [Scripts/c92487128.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92487128.lua) | 54 |
| Reflection of Endymion | `39000945` | [Scripts/c39000945.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39000945.lua) | 53 |
| Magister of Endymion | `66104644` | [Scripts/c66104644.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66104644.lua) | 52 |
| Daigusto Laplampilica | `76937326` | [Scripts/c76937326.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76937326.lua) | 52 |
| Zebufera, Vaalmonican Hallow Heathen | `2815176` | [Scripts/c2815176.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2815176.lua) | 52 |
| Servant of Endymion | `92559258` | [Scripts/c92559258.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92559258.lua) | 50 |
| Sky Striker Ace = Zero | `76072561` | [Scripts/c76072561.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76072561.lua) | 50 |
| Fiendsmith's Requiem | `2463794` | [Scripts/c2463794.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2463794.lua) | 50 |
| Artemis, the Magistus Moon Maiden | `34755994` | [Scripts/c34755994.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34755994.lua) | 48 |
| Nerva the Power Patron of Creation | `53589300` | [Scripts/c53589300.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53589300.lua) | 48 |
| Sky Striker Ace - Camellia | `63013339` | [Scripts/c63013339.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63013339.lua) | 48 |
| Repair Genex Controller | `8173184` | [Scripts/c8173184.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8173184.lua) | 47 |
| Volcanic Emperor | `46412900` | [Scripts/c46412900.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46412900.lua) | 46 |
| Sky Striker Ace - Zeke | `75147529` | [Scripts/c75147529.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75147529.lua) | 46 |
| Geistgrinder Golem | `26913989` | [Scripts/c26913989.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c26913989.lua) | 45 |
| Dinovatus Docus | `84631951` | [Scripts/c84631951.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84631951.lua) | 45 |
| Denglong, First of the Yang Zing | `65536818` | [Scripts/c65536818.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65536818.lua) | 45 |
| Darklord Tezcatlipoca | `88234365` | [Scripts/c88234365.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88234365.lua) | 45 |
| Darklord Amdusc | `51728779` | [Scripts/c51728779.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c51728779.lua) | 45 |
| Borreload Liberator Dragon | `27096833` | [Scripts/c27096833.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27096833.lua) | 44 |
| Darklord Ixchel | `52840267` | [Scripts/c52840267.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52840267.lua) | 44 |
| ...and 52 more |  |  |  |

## Script Examples

### Odd-Eyes Rebellion Dragon Overlord (`98452268`)

Source: [Scripts/c98452268.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c98452268.lua)

```lua
--覇王黒竜オッドアイズ・リベリオン・ドラゴン－オーバーロード
function c98452268.initial_effect(c)
	c:SetSPSummonOnce(98452268)
	--xyz summon
	aux.AddXyzProcedure(c,nil,7,2,c98452268.ovfilter,aux.Stringid(98452268,0))
```

### Veda Kalarcanum (`40785230`)

Source: [Scripts/c40785230.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40785230.lua)

```lua
--ヴェーダ＝ウパニシャッド
function c40785230.initial_effect(c)
	c:SetSPSummonOnce(40785230)
	c:EnableCounterPermit(0x69,LOCATION_PZONE)
	--pendulum summon
```

### Dreaming Nemleria (`70155677`)

Source: [Scripts/c70155677.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70155677.lua)

```lua
function c70155677.initial_effect(c)
	c:EnableReviveLimit()
	c:SetSPSummonOnce(70155677)
	--pendulum summon
	aux.EnablePendulumAttribute(c)
```
