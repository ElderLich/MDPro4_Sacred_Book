# Duel.EnableGlobalFlag

## Signature

```lua
Duel.EnableGlobalFlag(int global_flag) -> void
```

## Description

Enables the supplied core global_flag bit for the Duel and returns no Lua value.

## Parameters

- `global_flag` `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4845`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **47** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.EnableGlobalFlag`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Goyo Emperor](/examples/cards/59255742) | `59255742` | [Scripts/c59255742.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59255742.lua) | 1 |
| [Bujinki Ahashima](/examples/cards/71095768) | `71095768` | [Scripts/c71095768.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71095768.lua) | 1 |
| Grandpa Demetto | `44190146` | [Scripts/c44190146.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44190146.lua) | 1 |
| Numeron Calling | `77402960` | [Scripts/c77402960.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77402960.lua) | 1 |
| The Winged Dragon of Ra - Sphere Mode | `10000080` | [Scripts/c10000080.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10000080.lua) | 1 |
| Cucumber Horse | `89552119` | [Scripts/c89552119.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c89552119.lua) | 1 |
| Sky Striker Ace - Camellia | `63013339` | [Scripts/c63013339.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63013339.lua) | 1 |
| Tellarknight Constellar Caduceus | `58858807` | [Scripts/c58858807.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58858807.lua) | 1 |
| Advanced Crystal Beast Cobalt Eagle | `45236142` | [Scripts/c45236142.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45236142.lua) | 1 |
| Trick Box | `93983867` | [Scripts/c93983867.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93983867.lua) | 1 |
| Harmonizing Magician | `73941492` | [Scripts/c73941492.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c73941492.lua) | 1 |
| Performage Shadow Maker | `69655484` | [Scripts/c69655484.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c69655484.lua) | 1 |
| Number C102: Archfiend Seraph | `67173574` | [Scripts/c67173574.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67173574.lua) | 1 |
| Gigantic "Champion" Sargas | `11132674` | [Scripts/c11132674.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11132674.lua) | 1 |
| Goblin Biker Big Gabonga | `34001672` | [Scripts/c34001672.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34001672.lua) | 1 |
| Advanced Crystal Beast Ruby Carbuncle | `83575471` | [Scripts/c83575471.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c83575471.lua) | 1 |
| Re-qliate | `20426907` | [Scripts/c20426907.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20426907.lua) | 1 |
| Bazoo the Soul-Devourer | `79480466` | [Scripts/c79480466.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c79480466.lua) | 1 |
| Owner's Seal | `9720537` | [Scripts/c9720537.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9720537.lua) | 1 |
| Advanced Crystal Beast Amber Mammoth | `18847598` | [Scripts/c18847598.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18847598.lua) | 1 |
| Solitary Sword of Poison | `93377803` | [Scripts/c93377803.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93377803.lua) | 1 |
| Totem Pole | `47873397` | [Scripts/c47873397.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c47873397.lua) | 1 |
| Battlin' Boxer Lead Yoke | `23232295` | [Scripts/c23232295.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23232295.lua) | 1 |
| Void Purification | `61965407` | [Scripts/c61965407.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61965407.lua) | 1 |
| ...and 23 more |  |  |  |

## Script Examples

### Goyo Emperor (`59255742`)

Source: [Scripts/c59255742.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59255742.lua)

```lua
--ゴヨウ・エンペラー
function c59255742.initial_effect(c)
	Duel.EnableGlobalFlag(GLOBALFLAG_BRAINWASHING_CHECK)
	--fusion material
	c:EnableReviveLimit()
```

### Bujinki Ahashima (`71095768`)

Source: [Scripts/c71095768.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71095768.lua)

```lua
--武神姫－アハシマ
function c71095768.initial_effect(c)
	Duel.EnableGlobalFlag(GLOBALFLAG_DETACH_EVENT)
	--link summon
	aux.AddLinkProcedure(c,c71095768.mfilter,2,2,c71095768.lcheck)
```

### Grandpa Demetto (`44190146`)

Source: [Scripts/c44190146.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44190146.lua)

```lua
--デメット爺さん
function c44190146.initial_effect(c)
	Duel.EnableGlobalFlag(GLOBALFLAG_DETACH_EVENT)
	--special summon
	local e1=Effect.CreateEffect(c)
```
