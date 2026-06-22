# Duel.DiscardHand

## Signature

```lua
Duel.DiscardHand(int player, [function|nil f], int min, int max, int reason, [Card|Group|nil ex], ... any) -> int
```

## Description

Lets player choose and discard min to max matching cards from their hand for reason, then returns the number discarded.
Cards in ex are excluded. Extra arguments after ex are passed to filter f.

## Parameters

- `player` `int`
- `f` `function|nil` optional
- `min` `int`
- `max` `int`
- `reason` `int`
- `ex` `Card|Group|nil` optional
- `...` `any`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4911`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **625** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.DiscardHand`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Eternal Favorite](/examples/cards/87532344) | `87532344` | [Scripts/c87532344.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87532344.lua) | 73 |
| [El Shaddoll Apkallone](/examples/cards/50907446) | `50907446` | [Scripts/c50907446.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50907446.lua) | 68 |
| [Lubellion the Searing Dragon](/examples/cards/70534340) | `70534340` | [Scripts/c70534340.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70534340.lua) | 65 |
| [D/D Count Surveyor](/examples/cards/5997110) | `5997110` | [Scripts/c5997110.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5997110.lua) | 63 |
| [A Bao A Qu, the Lightless Shadow](/examples/cards/4731783) | `4731783` | [Scripts/c4731783.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4731783.lua) | 61 |
| [Aroma Blend](/examples/cards/25861589) | `25861589` | [Scripts/c25861589.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25861589.lua) | 61 |
| A-to-Z-Dragon Buster Cannon | `65172015` | [Scripts/c65172015.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65172015.lua) | 58 |
| Super Quantal Mech Ship Magnacarrier | `10424147` | [Scripts/c10424147.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10424147.lua) | 57 |
| XYZ-Hyper Dragon Cannon | `75748977` | [Scripts/c75748977.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75748977.lua) | 57 |
| Erebus the Underworld Monarch | `23064604` | [Scripts/c23064604.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23064604.lua) | 56 |
| Inzektor Picofalena | `97273514` | [Scripts/c97273514.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97273514.lua) | 56 |
| Darktellarknight Batlamyus | `64414267` | [Scripts/c64414267.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c64414267.lua) | 55 |
| Dual Avatar Invitation | `87669904` | [Scripts/c87669904.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87669904.lua) | 55 |
| Ojama Pajama | `75884822` | [Scripts/c75884822.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75884822.lua) | 55 |
| ABC-Dragon Buster | `1561110` | [Scripts/c1561110.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1561110.lua) | 55 |
| Dark World Accession | `65956182` | [Scripts/c65956182.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65956182.lua) | 55 |
| Genex Ally Triarm | `17760003` | [Scripts/c17760003.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17760003.lua) | 55 |
| Angello Vaalmonica | `3048768` | [Scripts/c3048768.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3048768.lua) | 54 |
| Megalith Anastasis | `29876299` | [Scripts/c29876299.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29876299.lua) | 54 |
| Crealtar, the Impcantation Originator | `96915510` | [Scripts/c96915510.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96915510.lua) | 54 |
| Fabled Realm's Revival | `57775790` | [Scripts/c57775790.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57775790.lua) | 54 |
| Dimonno Vaalmonica | `30432463` | [Scripts/c30432463.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30432463.lua) | 53 |
| Abyssrhine, the Atlantean Spirit | `17080584` | [Scripts/c17080584.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17080584.lua) | 53 |
| Heraldic Beast Stad Whale | `97662494` | [Scripts/c97662494.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97662494.lua) | 53 |
| ...and 601 more |  |  |  |

## Script Examples

### Eternal Favorite (`87532344`)

Source: [Scripts/c87532344.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87532344.lua)

```lua
	if chk==0 then return Duel.IsExistingMatchingCard(Card.IsDiscardable,tp,LOCATION_HAND,0,1,e:GetHandler())
		and c:IsAbleToGraveAsCost() and c:IsStatus(STATUS_EFFECT_ENABLED) end
	Duel.DiscardHand(tp,Card.IsDiscardable,1,1,REASON_COST+REASON_DISCARD)
	Duel.SendtoGrave(c,REASON_COST)
end
```

### El Shaddoll Apkallone (`50907446`)

Source: [Scripts/c50907446.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50907446.lua)

```lua
			Duel.BreakEffect()
			Duel.ShuffleHand(tp)
			Duel.DiscardHand(tp,aux.TRUE,1,1,REASON_EFFECT+REASON_DISCARD,nil)
		end
	end
```

### Lubellion the Searing Dragon (`70534340`)

Source: [Scripts/c70534340.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70534340.lua)

```lua
function c70534340.spcost(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsExistingMatchingCard(Card.IsDiscardable,tp,LOCATION_HAND,0,1,nil) end
	Duel.DiscardHand(tp,Card.IsDiscardable,1,1,REASON_COST+REASON_DISCARD)
end
function c70534340.filter0(c)
```
