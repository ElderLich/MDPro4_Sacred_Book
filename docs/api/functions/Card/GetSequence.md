# Card.GetSequence

## Signature

```lua
Card.GetSequence(Card c) -> int
```

## Description

Returns c's sequence within its current location.
For field zones, Main Monster Zones and Spell & Trap Zones use 0-4 from left to right, the Field Zone uses 5, and Pendulum Zones use 6-7.
For other locations, sequence is the card's position in that location, starting from 0.

## Parameters

- `c` `Card` - Card whose current sequence is returned.

## Returns

- `int` - Sequence in c's current location.

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3520`

## Guided Examples

Learn how to use this function in context:

- [Field Zones And Sequences](/learn/field-zones-and-sequences)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **339** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.GetSequence) with `Card.GetSequence`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [GMX 55th Experiment Report](/examples/cards/38984832) | `38984832` | [Scripts/c38984832.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c38984832.lua) | 2 |
| [Nekroz Kaleidoscope](/examples/cards/51124303) | `51124303` | [Scripts/c51124303.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c51124303.lua) | 1 |
| Vaylantz Genesis Grand Duke | `76075139` | [Scripts/c76075139.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c76075139.lua) | 5 |
| Trickstar Light Stage | `35371948` | [Scripts/c35371948.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c35371948.lua) | 1 |
| Hojo the Vaylantz Warrior | `88919365` | [Scripts/c88919365.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c88919365.lua) | 4 |
| Chaos Magical Hats | `2372506` | [Scripts/c2372506.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c2372506.lua) | 1 |
| Trickstar Light Arena | `63492244` | [Scripts/c63492244.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c63492244.lua) | 1 |
| Mixeroid | `71340250` | [Scripts/c71340250.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c71340250.lua) | 1 |
| Magical Hats | `81210420` | [Scripts/c81210420.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c81210420.lua) | 1 |
| Chaos Emperor, the Dragon of Armageddon | `4538826` | [Scripts/c4538826.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c4538826.lua) | 1 |
| Arktos XII - Chronochasm Vaylantz | `50687050` | [Scripts/c50687050.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c50687050.lua) | 6 |
| Beyond the Pendulum | `22125101` | [Scripts/c22125101.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c22125101.lua) | 1 |
| Arms of Genex Return Zero | `61775475` | [Scripts/c61775475.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c61775475.lua) | 1 |
| GMX - VELOX | `82706696` | [Scripts/c82706696.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c82706696.lua) | 1 |
| Seven Cities of the Golden Land | `95034141` | [Scripts/c95034141.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c95034141.lua) | 1 |
| Elfnotes: Rhapsodia of Madness | `24092792` | [Scripts/c24092792.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c24092792.lua) | 2 |
| Mamonaka the Vaylantz United | `40680521` | [Scripts/c40680521.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c40680521.lua) | 8 |
| Elfnote Tinia | `59581480` | [Scripts/c59581480.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c59581480.lua) | 4 |
| Cynet Circuit | `82886276` | [Scripts/c82886276.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c82886276.lua) | 2 |
| Odd-Eyes Lancer Dragon | `83347294` | [Scripts/c83347294.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c83347294.lua) | 1 |
| Geira Guile the Cubic King | `40392714` | [Scripts/c40392714.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c40392714.lua) | 1 |
| Shadowreaver Knight 21 | `95506252` | [Scripts/c95506252.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c95506252.lua) | 3 |
| Paleozoic Cambroraster | `36346532` | [Scripts/c36346532.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c36346532.lua) | 1 |
| Vision Fusion | `57425061` | [Scripts/c57425061.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c57425061.lua) | 1 |
| ...and 315 more |  |  |  |

## Script Examples

### GMX 55th Experiment Report (`38984832`)

Source: [Scripts/c38984832.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c38984832.lua)

```lua
	local qc=nil
	for sc in aux.Next(mg) do
		if sc:GetSequence()>seq then
			seq=sc:GetSequence()
			qc=sc
```

### Nekroz Kaleidoscope (`51124303`)

Source: [Scripts/c51124303.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c51124303.lua)

```lua
end
function c51124303.mzfilter(c,tp)
	return c:IsLocation(LOCATION_MZONE) and c:IsControler(tp) and c:GetSequence()<5
end
function c51124303.target(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Vaylantz Genesis Grand Duke (`76075139`)

Source: [Scripts/c76075139.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c76075139.lua)

```lua
end
function c76075139.hspfilter(c,tp,sc)
	local seq=c:GetSequence()
	return (seq==1 or seq==3 or seq>4) and not c:IsFusionType(TYPE_FUSION) and c:IsLevelAbove(5) and c:IsFusionSetCard(0x17d)
		and c:IsControler(tp) and Duel.GetLocationCountFromEx(tp,tp,c,sc)>0 and c:IsCanBeFusionMaterial(sc,SUMMON_TYPE_SPECIAL)
```
