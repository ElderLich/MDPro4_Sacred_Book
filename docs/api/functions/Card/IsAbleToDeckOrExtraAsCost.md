# Card.IsAbleToDeckOrExtraAsCost

## Signature

```lua
Card.IsAbleToDeckOrExtraAsCost(Card c) -> bool
```

## Description

Checks whether c can be returned to the Deck or Extra Deck as a cost.

## Parameters

- `c` `Card`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3595`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **32** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.IsAbleToDeckOrExtraAsCost`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Gladiator Beast Gaiodiaz | `90957527` | [Scripts/c90957527.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90957527.lua) | 1 |
| Gladiator Beast Gyzarus | `48156348` | [Scripts/c48156348.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48156348.lua) | 1 |
| Blue-Eyes Toon Ultimate Dragon | `71808988` | [Scripts/c71808988.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71808988.lua) | 1 |
| Fiendsmith's Lacrima | `46640168` | [Scripts/c46640168.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46640168.lua) | 1 |
| Gladiator Beast Claudius | `48958757` | [Scripts/c48958757.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48958757.lua) | 1 |
| Fiendsmith's Desirae | `82135803` | [Scripts/c82135803.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82135803.lua) | 1 |
| Grand Knight of the Red Lotus | `51132012` | [Scripts/c51132012.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c51132012.lua) | 1 |
| Gladiator Beast Andabata | `3779662` | [Scripts/c3779662.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3779662.lua) | 1 |
| Gladiator Beast Domitianus | `33652635` | [Scripts/c33652635.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33652635.lua) | 1 |
| Gladiator Beast Tamer Editor | `30864377` | [Scripts/c30864377.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30864377.lua) | 2 |
| Mementoal Tecuhtlica - Combined Creation | `23288411` | [Scripts/c23288411.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23288411.lua) | 1 |
| Blackwing - Twin Shadow | `69973414` | [Scripts/c69973414.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c69973414.lua) | 1 |
| Gladiator Beast Nerokius | `29357956` | [Scripts/c29357956.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29357956.lua) | 1 |
| Test Bear | `62076252` | [Scripts/c62076252.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62076252.lua) | 1 |
| Exodius the Ultimate Forbidden Lord | `13893596` | [Scripts/c13893596.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13893596.lua) | 1 |
| Tierra, Source of Destruction | `91588074` | [Scripts/c91588074.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c91588074.lua) | 2 |
| Fiendsmith Engraver | `60764609` | [Scripts/c60764609.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60764609.lua) | 1 |
| Phantom of Yubel | `80453041` | [Scripts/c80453041.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80453041.lua) | 1 |
| Elemental HERO Nebula Neos | `40080312` | [Scripts/c40080312.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40080312.lua) | 1 |
| Elemental HERO Chaos Neos | `17032740` | [Scripts/c17032740.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17032740.lua) | 1 |
| Elemental HERO Glow Neos | `85507811` | [Scripts/c85507811.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85507811.lua) | 1 |
| Elemental HERO Cosmo Neos | `90050480` | [Scripts/c90050480.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90050480.lua) | 1 |
| Elemental HERO Dark Neos | `28677304` | [Scripts/c28677304.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28677304.lua) | 1 |
| Gladiator Beast Heraklinos | `27346636` | [Scripts/c27346636.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27346636.lua) | 1 |
| ...and 8 more |  |  |  |

## Script Examples

### Gladiator Beast Gaiodiaz (`90957527`)

Source: [Scripts/c90957527.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90957527.lua)

```lua
function c90957527.cfilter(c)
	return (c:IsFusionCode(79580323) or c:IsFusionSetCard(0x1019) and c:IsType(TYPE_MONSTER))
		and c:IsAbleToDeckOrExtraAsCost()
end
function c90957527.damcon(e,tp,eg,ep,ev,re,r,rp)
```

### Gladiator Beast Gyzarus (`48156348`)

Source: [Scripts/c48156348.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48156348.lua)

```lua
function c48156348.cfilter(c)
	return (c:IsFusionCode(41470137) or c:IsFusionSetCard(0x1019) and c:IsType(TYPE_MONSTER))
		and c:IsAbleToDeckOrExtraAsCost()
end
function c48156348.destg(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
```

### Blue-Eyes Toon Ultimate Dragon (`71808988`)

Source: [Scripts/c71808988.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71808988.lua)

```lua
function s.cfilter(c)
	return (c:IsFusionCode(53183600) or c:IsType(TYPE_MONSTER))
		and c:IsAbleToDeckOrExtraAsCost()
end
function s.ffilter(c)
```
