# Card.IsDiscardable

## Signature

```lua
Card.IsDiscardable(Card c, [int reason]) -> bool
```

## Description

Checks whether c can be discarded for reason.
This is only a check: sending a card from the hand to the Graveyard with REASON_DISCARD does not by itself make that card unable to be discarded.

## Parameters

- `c` `Card`
- `reason` `int` optional - default: REASON_COST

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3600`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **656** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.IsDiscardable`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Artmage Non-Finito](/examples/cards/74631897) | `74631897` | [Scripts/c74631897.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74631897.lua) | 78 |
| [Eternal Favorite](/examples/cards/87532344) | `87532344` | [Scripts/c87532344.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87532344.lua) | 73 |
| [Lubellion the Searing Dragon](/examples/cards/70534340) | `70534340` | [Scripts/c70534340.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70534340.lua) | 65 |
| [Resurgam Xyz](/examples/cards/49082032) | `49082032` | [Scripts/c49082032.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49082032.lua) | 64 |
| [D/D Count Surveyor](/examples/cards/5997110) | `5997110` | [Scripts/c5997110.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5997110.lua) | 63 |
| [Junoldo the Shadespirit Power Patron](/examples/cards/10266279) | `10266279` | [Scripts/c10266279.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10266279.lua) | 62 |
| [A Bao A Qu, the Lightless Shadow](/examples/cards/4731783) | `4731783` | [Scripts/c4731783.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4731783.lua) | 61 |
| [Aroma Blend](/examples/cards/25861589) | `25861589` | [Scripts/c25861589.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25861589.lua) | 61 |
| D/D Extra Surveyor | `74387963` | [Scripts/c74387963.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74387963.lua) | 60 |
| A-to-Z-Dragon Buster Cannon | `65172015` | [Scripts/c65172015.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65172015.lua) | 58 |
| Deep Sea Minstrel | `71978434` | [Scripts/c71978434.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71978434.lua) | 58 |
| Super Quantal Mech Ship Magnacarrier | `10424147` | [Scripts/c10424147.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10424147.lua) | 57 |
| XYZ-Hyper Dragon Cannon | `75748977` | [Scripts/c75748977.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75748977.lua) | 57 |
| Lunalight Masquerade | `2344618` | [Scripts/c2344618.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2344618.lua) | 57 |
| Erebus the Underworld Monarch | `23064604` | [Scripts/c23064604.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23064604.lua) | 56 |
| Nebulus, Dragon Ruler of Mishaps | `94655777` | [Scripts/c94655777.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c94655777.lua) | 56 |
| Inzektor Picofalena | `97273514` | [Scripts/c97273514.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97273514.lua) | 56 |
| Witchcrafter Pittore | `95245544` | [Scripts/c95245544.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95245544.lua) | 56 |
| Witchcrafter Genni | `64756282` | [Scripts/c64756282.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c64756282.lua) | 56 |
| Darktellarknight Batlamyus | `64414267` | [Scripts/c64414267.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c64414267.lua) | 55 |
| Dual Avatar Invitation | `87669904` | [Scripts/c87669904.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87669904.lua) | 55 |
| Darkuriboh | `1035143` | [Scripts/c1035143.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1035143.lua) | 55 |
| ABC-Dragon Buster | `1561110` | [Scripts/c1561110.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1561110.lua) | 55 |
| Dark World Accession | `65956182` | [Scripts/c65956182.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65956182.lua) | 55 |
| ...and 632 more |  |  |  |

## Script Examples

### Artmage Non-Finito (`74631897`)

Source: [Scripts/c74631897.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74631897.lua)

```lua
end
function s.cfilter(c)
	return c:IsType(TYPE_SPELL+TYPE_TRAP) and c:IsDiscardable(REASON_SPSUMMON)
end
function s.spcon(e,c)
```

### Eternal Favorite (`87532344`)

Source: [Scripts/c87532344.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87532344.lua)

```lua
function s.fucost(e,tp,eg,ep,ev,re,r,rp,chk)
	local c=e:GetHandler()
	if chk==0 then return Duel.IsExistingMatchingCard(Card.IsDiscardable,tp,LOCATION_HAND,0,1,e:GetHandler())
		and c:IsAbleToGraveAsCost() and c:IsStatus(STATUS_EFFECT_ENABLED) end
	Duel.DiscardHand(tp,Card.IsDiscardable,1,1,REASON_COST+REASON_DISCARD)
```

### Lubellion the Searing Dragon (`70534340`)

Source: [Scripts/c70534340.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70534340.lua)

```lua
end
function c70534340.spcost(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsExistingMatchingCard(Card.IsDiscardable,tp,LOCATION_HAND,0,1,nil) end
	Duel.DiscardHand(tp,Card.IsDiscardable,1,1,REASON_COST+REASON_DISCARD)
end
```
