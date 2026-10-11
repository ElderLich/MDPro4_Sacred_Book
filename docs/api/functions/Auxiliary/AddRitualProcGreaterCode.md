# Auxiliary.AddRitualProcGreaterCode

## Signature

```lua
Auxiliary.AddRitualProcGreaterCode(Card c, int code1, [int summon_location], [function grave_filter], [function mat_filter], [bool pause], [function extra_operation], [function extra_target]) -> Effect
```

## Description

Registers a Ritual Summon procedure for Ritual Monster code1, allowing material Ritual Levels to meet or exceed the Ritual Monster's original Level.
The helper also adds code1 to c's code/material list and returns the created procedure effect.

## Parameters

- `c` `Card`
- `code1` `int`
- `summon_location` `int` optional - default: LOCATION_HAND
- `grave_filter` `function` optional
- `mat_filter` `function` optional
- `pause` `bool` optional
- `extra_operation` `function` optional
- `extra_target` `function` optional

## Returns

- `Effect`

## Source

- `Utilities/procedure.lua:1909`

## Guided Examples

Learn how to use this function in context:

- [Ritual Procedure Guide](/learn/ritual-procedure)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **36** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.AddRitualProcGreaterCode) with `Auxiliary.AddRitualProcGreaterCode`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Armor Dragon Ritual | `58827995` | [Scripts/c58827995.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58827995.lua) | 1 |
| Primal Cry | `47435107` | [Scripts/c47435107.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c47435107.lua) | 1 |
| Litmus Doom Ritual | `8955148` | [Scripts/c8955148.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8955148.lua) | 1 |
| Good &amp; Evil in the Burning Abyss | `62835876` | [Scripts/c62835876.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62835876.lua) | 1 |
| Ritual of Grace | `60234913` | [Scripts/c60234913.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60234913.lua) | 1 |
| Ritual of the Matador | `70105073` | [Scripts/c70105073.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70105073.lua) | 1 |
| Prediction Ritual | `30392583` | [Scripts/c30392583.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30392583.lua) | 1 |
| Dark Dragon Ritual | `18803791` | [Scripts/c18803791.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18803791.lua) | 1 |
| Ritual of Destruction | `52913738` | [Scripts/c52913738.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52913738.lua) | 1 |
| Hymn of Light | `80566312` | [Scripts/c80566312.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80566312.lua) | 1 |
| Oracle of the Herald | `79306385` | [Scripts/c79306385.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c79306385.lua) | 1 |
| Red-Eyes Transmigration | `45410988` | [Scripts/c45410988.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45410988.lua) | 1 |
| Shinato's Ark | `60365591` | [Scripts/c60365591.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60365591.lua) | 1 |
| Turtle Oath | `76806714` | [Scripts/c76806714.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76806714.lua) | 1 |
| Doriado's Blessing | `23965037` | [Scripts/c23965037.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23965037.lua) | 1 |
| Emblem of the Awakening | `9845733` | [Scripts/c9845733.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9845733.lua) | 1 |
| Final Ritual of the Ancients | `60369732` | [Scripts/c60369732.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60369732.lua) | 1 |
| Incandescent Ordeal | `33031674` | [Scripts/c33031674.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33031674.lua) | 1 |
| Black Magic Ritual | `76792184` | [Scripts/c76792184.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76792184.lua) | 1 |
| White Dragon Ritual | `9786492` | [Scripts/c9786492.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9786492.lua) | 1 |
| Black Luster Ritual | `55761792` | [Scripts/c55761792.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55761792.lua) | 1 |
| Commencement Dance | `43417563` | [Scripts/c43417563.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43417563.lua) | 1 |
| Beastly Mirror Ritual | `81933259` | [Scripts/c81933259.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81933259.lua) | 1 |
| Contract with the Dark Master | `96420087` | [Scripts/c96420087.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96420087.lua) | 1 |
| ...and 12 more |  |  |  |

## Script Examples

### Armor Dragon Ritual (`58827995`)

Source: [Scripts/c58827995.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58827995.lua)

```lua
--鎧竜降臨
function c58827995.initial_effect(c)
	aux.AddRitualProcGreaterCode(c,75901113)
	local e1=Effect.CreateEffect(c)
	e1:SetCategory(CATEGORY_SPECIAL_SUMMON+CATEGORY_REMOVE)
```

### Primal Cry (`47435107`)

Source: [Scripts/c47435107.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c47435107.lua)

```lua
--原初の叫喚
function c47435107.initial_effect(c)
	aux.AddRitualProcGreaterCode(c,10441498)
	--special summon
	local e1=Effect.CreateEffect(c)
```

### Litmus Doom Ritual (`8955148`)

Source: [Scripts/c8955148.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8955148.lua)

```lua
--リトマスの死儀式
function c8955148.initial_effect(c)
	aux.AddRitualProcGreaterCode(c,72566043)
	--to deck
	local e1=Effect.CreateEffect(c)
```
