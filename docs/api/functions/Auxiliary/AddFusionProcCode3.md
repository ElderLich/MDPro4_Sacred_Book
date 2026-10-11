# Auxiliary.AddFusionProcCode3

## Signature

```lua
Auxiliary.AddFusionProcCode3(Card c, int code1, int code2, int code3, bool sub, bool insf) -> void
```

## Description

Registers a Fusion Material procedure requiring monsters with code1, code2, and code3 as fixed materials.

## Parameters

- `c` `Card`
- `code1` `int`
- `code2` `int`
- `code3` `int`
- `sub` `bool`
- `insf` `bool`

## Source

- `Utilities/procedure.lua:1219`

## Guided Examples

Learn how to use this function in context:

- [Fusion Procedure Guide](/learn/fusion-procedure)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **19** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.AddFusionProcCode3) with `Auxiliary.AddFusionProcCode3`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| XYZ-Hyper Dragon Cannon | `75748977` | [Scripts/c75748977.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75748977.lua) | 1 |
| ABC-Dragon Buster | `1561110` | [Scripts/c1561110.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1561110.lua) | 1 |
| Gate Guardians Combined | `8505920` | [Scripts/c8505920.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8505920.lua) | 1 |
| Prank-Kids Battle Butler | `81997228` | [Scripts/c81997228.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81997228.lua) | 1 |
| Timaeus the Knight of Destiny | `53315891` | [Scripts/c53315891.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53315891.lua) | 1 |
| Elemental HERO Nebula Neos | `40080312` | [Scripts/c40080312.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40080312.lua) | 1 |
| Elemental HERO Chaos Neos | `17032740` | [Scripts/c17032740.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17032740.lua) | 1 |
| Armityle the Chaos Phantasm - Phantom of Fury | `60110982` | [Scripts/c60110982.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60110982.lua) | 1 |
| Elemental HERO Tempest | `83121692` | [Scripts/c83121692.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c83121692.lua) | 1 |
| Cyberdark Dragon | `40418351` | [Scripts/c40418351.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40418351.lua) | 1 |
| Elemental HERO Storm Neos | `49352945` | [Scripts/c49352945.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49352945.lua) | 1 |
| XYZ-Dragon Cannon | `91998119` | [Scripts/c91998119.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c91998119.lua) | 1 |
| Elemental HERO Magma Neos | `78512663` | [Scripts/c78512663.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78512663.lua) | 1 |
| Arcana Knight Joker | `6150044` | [Scripts/c6150044.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6150044.lua) | 1 |
| Armityle the Chaos Phantasm | `43378048` | [Scripts/c43378048.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43378048.lua) | 1 |
| Ojama King | `90140980` | [Scripts/c90140980.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90140980.lua) | 1 |
| Super Vehicroid Jumbo Drill | `36256625` | [Scripts/c36256625.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36256625.lua) | 1 |
| Aqua Dragon | `86164529` | [Scripts/c86164529.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c86164529.lua) | 1 |
| Man-eating Black Shark | `80727036` | [Scripts/c80727036.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80727036.lua) | 1 |

## Script Examples

### XYZ-Hyper Dragon Cannon (`75748977`)

Source: [Scripts/c75748977.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75748977.lua)

```lua
function s.initial_effect(c)
	c:EnableReviveLimit()
	aux.AddFusionProcCode3(c,70860415,6355563,33744268,true,true)
	aux.AddContactFusionProcedure(c,Card.IsAbleToRemoveAsCost,LOCATION_ONFIELD+LOCATION_GRAVE,0,Duel.Remove,POS_FACEUP,REASON_COST)
	--
```

### ABC-Dragon Buster (`1561110`)

Source: [Scripts/c1561110.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1561110.lua)

```lua
	--fusion material
	c:EnableReviveLimit()
	aux.AddFusionProcCode3(c,30012506,77411244,3405259,true,true)
	aux.AddContactFusionProcedure(c,Card.IsAbleToRemoveAsCost,LOCATION_ONFIELD+LOCATION_GRAVE,0,Duel.Remove,POS_FACEUP,REASON_COST)
	--spsummon condition
```

### Gate Guardians Combined (`8505920`)

Source: [Scripts/c8505920.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8505920.lua)

```lua
	--fusion material
	c:EnableReviveLimit()
	aux.AddFusionProcCode3(c,25955164,62340868,98434877,true,true)
	aux.AddContactFusionProcedure(c,Card.IsAbleToRemoveAsCost,LOCATION_ONFIELD+LOCATION_HAND+LOCATION_GRAVE,0,Duel.Remove,POS_FACEUP,REASON_COST)
	--spsummon condition
```
