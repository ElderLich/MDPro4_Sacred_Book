# Card.CheckFusionSubstitute

## Signature

```lua
Card.CheckFusionSubstitute(Card c, Card fcard) -> bool
```

## Description

Checks whether c can substitute for a specifically named Fusion Material listed by Fusion Monster fcard.

## Parameters

- `c` `Card`
- `fcard` `Card`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3700`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **5** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.CheckFusionSubstitute) with `Card.CheckFusionSubstitute`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Dragon Master Magia | `12381100` | [Scripts/c12381100.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c12381100.lua) | 1 |
| Windwitch - Crystal Bell | `25793414` | [Scripts/c25793414.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c25793414.lua) | 1 |
| Mirrorjade the Iceblade Dragon | `44146295` | [Scripts/c44146295.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c44146295.lua) | 1 |
| Rune-Eyes Pendulum Dragon | `1516510` | [Scripts/c1516510.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c1516510.lua) | 1 |
| Elemental HERO Neos Knight | `72926163` | [Scripts/c72926163.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c72926163.lua) | 1 |

## Script Examples

### Dragon Master Magia (`12381100`)

Source: [Scripts/c12381100.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c12381100.lua)

```lua
end
function s.ffilter1(c,fc)
	return c:IsFusionCode(23995346) or c:CheckFusionSubstitute(fc)
end
function s.ffilter2(c)
```

### Windwitch - Crystal Bell (`25793414`)

Source: [Scripts/c25793414.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c25793414.lua)

```lua
c25793414.material_type=TYPE_SYNCHRO
function c25793414.sfcfilter(c,fc)
	return (c:IsFusionCode(14577226) or c:CheckFusionSubstitute(fc)) and c:IsFusionType(TYPE_SYNCHRO)
end
function c25793414.synchro_fusion_check(tp,sg,fc)
```

### Mirrorjade the Iceblade Dragon (`44146295`)

Source: [Scripts/c44146295.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c44146295.lua)

```lua
c44146295.material_type=TYPE_FUSION+TYPE_SYNCHRO+TYPE_XYZ+TYPE_LINK
function c44146295.sfcfilter(c,fc)
	return c:IsFusionCode(68468459) or c:CheckFusionSubstitute(fc)
end
function c44146295.synchro_fusion_check(tp,sg,fc)
```
