# Duel.Remove

## Signature

```lua
Duel.Remove(Card|Group targets, int pos, int reason, [int reason_player]) -> int
```

## Description

Banishes targets in position pos for reason and returns the number of cards actually banished.
If reason includes REASON_TEMPORARY, the banish is treated as temporary and the card can later be returned with Duel.ReturnToField.
Use POS_FACEDOWN only when the effect requires a face-down banish; ordinary banish effects usually use POS_FACEUP.

## How To Use It

Use this for banishing cards. The second argument is the banished position, usually `POS_FACEUP` or `POS_FACEDOWN`.

```lua
if c:IsRelateToEffect(e) then
    Duel.Remove(c,POS_FACEUP,REASON_EFFECT)
end
```

For temporary banish effects, scripts commonly include `REASON_TEMPORARY`; those cards can later be returned with `Duel.ReturnToField`.

## Related Functions

- [Card.IsAbleToRemove](/api/functions/Card/IsAbleToRemove)
- [Duel.ReturnToField](/api/functions/Duel/ReturnToField)
- [Duel.SetOperationInfo](/api/functions/Duel/SetOperationInfo)

## Parameters

- `targets` `Card|Group`
- `pos` `int`
- `reason` `int`
- `reason_player` `int` optional

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4859`

## Guided Examples

Learn how to use this function in context:

- [Methods for Affecting Cards](/learn/affecting-cards)
- [Fusion Procedure Guide](/learn/fusion-procedure)
- [Functions That Move Cards Across Locations](/learn/moving-cards)
- [Special Summon-Only Monster Guide](/learn/special-summon-only-monsters)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **1663** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.Remove) with `Duel.Remove`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Lady's Dragonmaid](/examples/cards/48658295) | `48658295` | [Scripts/c48658295.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c48658295.lua) | 1 |
| [Astrograph Sorcerer](/examples/cards/76794549) | `76794549` | [Scripts/c76794549.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c76794549.lua) | 1 |
| [Accel Synchro Stardust Dragon](/examples/cards/30983281) | `30983281` | [Scripts/c30983281.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c30983281.lua) | 1 |
| [Ashtraja Susanoo](/examples/cards/17020474) | `17020474` | [Scripts/c17020474.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c17020474.lua) | 2 |
| [Deftero Enneacraft - "alazoneIA"](/examples/cards/92171126) | `92171126` | [Scripts/c92171126.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c92171126.lua) | 1 |
| [Destiny HERO - Destro-Dogma](/examples/cards/25158975) | `25158975` | [Scripts/c25158975.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c25158975.lua) | 1 |
| [Mixousia the Confounder](/examples/cards/80843006) | `80843006` | [Scripts/c80843006.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c80843006.lua) | 1 |
| [Invoked Sorath](/examples/cards/43989315) | `43989315` | [Scripts/c43989315.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c43989315.lua) | 1 |
| [Ehther the Heavenly Monarch](/examples/cards/96570609) | `96570609` | [Scripts/c96570609.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c96570609.lua) | 1 |
| [Destratification Dino Stratiae](/examples/cards/3841104) | `3841104` | [Scripts/c3841104.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c3841104.lua) | 1 |
| [Am Duazenet](/examples/cards/45151304) | `45151304` | [Scripts/c45151304.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c45151304.lua) | 1 |
| [Hecahands Tartaros](/examples/cards/57809669) | `57809669` | [Scripts/c57809669.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c57809669.lua) | 1 |
| [Ursarctic Polari](/examples/cards/27693363) | `27693363` | [Scripts/c27693363.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c27693363.lua) | 1 |
| [Prank-Kids Weather Washer](/examples/cards/44509529) | `44509529` | [Scripts/c44509529.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c44509529.lua) | 1 |
| [Enneacraft - Asta.PIXEA](/examples/cards/28454232) | `28454232` | [Scripts/c28454232.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c28454232.lua) | 1 |
| [Converging Wishes](/examples/cards/20007374) | `20007374` | [Scripts/c20007374.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c20007374.lua) | 2 |
| [Tohushaddoll Grysta](/examples/cards/95072744) | `95072744` | [Scripts/c95072744.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c95072744.lua) | 1 |
| [Predaplant Bal Teah](/examples/cards/66787942) | `66787942` | [Scripts/c66787942.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c66787942.lua) | 1 |
| [PSY-Framelord Omega](/examples/cards/74586817) | `74586817` | [Scripts/c74586817.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c74586817.lua) | 1 |
| [Teleport Fusion](/examples/cards/36494597) | `36494597` | [Scripts/c36494597.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c36494597.lua) | 1 |
| [D/D/D/D Dimensional King Arc Crisis](/examples/cards/71398055) | `71398055` | [Scripts/c71398055.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c71398055.lua) | 1 |
| [Dark End Evaporation Dragon](/examples/cards/62002838) | `62002838` | [Scripts/c62002838.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c62002838.lua) | 1 |
| [Nekroz Kaleidoscope](/examples/cards/51124303) | `51124303` | [Scripts/c51124303.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c51124303.lua) | 1 |
| [Junoldo the Shadespirit Power Patron](/examples/cards/10266279) | `10266279` | [Scripts/c10266279.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c10266279.lua) | 2 |
| ...and 1639 more |  |  |  |

## Script Examples

### Lady's Dragonmaid (`48658295`)

Source: [Scripts/c48658295.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c48658295.lua)

```lua
	local sg=e:GetLabelObject()
	c:SetMaterial(sg)
	Duel.Remove(sg,POS_FACEUP,REASON_COST)
end
function s.spfilter(c,e,tp)
```

### Astrograph Sorcerer (`76794549`)

Source: [Scripts/c76794549.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c76794549.lua)

```lua
	local sg=mg:SelectSubGroupEach(tp,c76794549.hnchecks,false,c76794549.hngoal,e,tp,c)
	sg:AddCard(c)
	Duel.Remove(sg,POS_FACEUP,REASON_COST)
end
function c76794549.hntg(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Accel Synchro Stardust Dragon (`30983281`)

Source: [Scripts/c30983281.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c30983281.lua)

```lua
	local te=rc:IsHasEffect(84012625,tp)
	if te then
		Duel.Remove(rc,POS_FACEUP,REASON_COST+REASON_REPLACE)
	else
		Duel.Release(rc,REASON_COST)
```
