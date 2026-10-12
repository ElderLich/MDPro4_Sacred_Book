# Card.GetReasonCard

## Signature

```lua
Card.GetReasonCard(Card c) -> Card|nil
```

## Description

Returns c's current reason card, or nil when no reason card is recorded.

## Parameters

- `c` `Card`

## Returns

- `Card|nil`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3512`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **158** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.GetReasonCard) with `Card.GetReasonCard`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Ultra Polymerization](/examples/cards/76647978) | `76647978` | [Scripts/c76647978.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c76647978.lua) | 1 |
| [Goyo Emperor](/examples/cards/59255742) | `59255742` | [Scripts/c59255742.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c59255742.lua) | 2 |
| Ostinato | `9113513` | [Scripts/c9113513.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c9113513.lua) | 1 |
| Hi-Speedroid Cork Shooter | `23361526` | [Scripts/c23361526.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c23361526.lua) | 1 |
| X-Saber Pellina | `9978697` | [Scripts/c9978697.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c9978697.lua) | 2 |
| Link into the VRAINS! | `28827503` | [Scripts/c28827503.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c28827503.lua) | 2 |
| Chevreuil, Hunting Scout of the Deep Forest | `13023431` | [Scripts/c13023431.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c13023431.lua) | 1 |
| D/D/D Vice King Requiem | `25857977` | [Scripts/c25857977.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c25857977.lua) | 2 |
| Salamangreat Zebroid X | `44161893` | [Scripts/c44161893.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c44161893.lua) | 1 |
| Evil HERO Inferno Wing - Backfire | `59893882` | [Scripts/c59893882.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c59893882.lua) | 1 |
| Grenosaurus Giga-Cannon | `34481518` | [Scripts/c34481518.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c34481518.lua) | 1 |
| Shining Star Dragon | `75874514` | [Scripts/c75874514.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c75874514.lua) | 2 |
| Number 104: Masquerade Vain | `16908882` | [Scripts/c16908882.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c16908882.lua) | 1 |
| Deep Sea Prima Donna | `50793215` | [Scripts/c50793215.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c50793215.lua) | 1 |
| Centaur Mina | `33129626` | [Scripts/c33129626.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c33129626.lua) | 2 |
| Vampire Scarlet Scourge | `79523365` | [Scripts/c79523365.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c79523365.lua) | 1 |
| Vampire Red Baron | `6917479` | [Scripts/c6917479.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c6917479.lua) | 1 |
| Horn of the Phantom Beast | `21350571` | [Scripts/c21350571.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c21350571.lua) | 1 |
| D - Chain | `43405287` | [Scripts/c43405287.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c43405287.lua) | 1 |
| Vampire Fraulein | `6039967` | [Scripts/c6039967.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c6039967.lua) | 1 |
| THE Star Ham | `15123983` | [Scripts/c15123983.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c15123983.lua) | 1 |
| SPYRAL MISSION - Assault | `27642961` | [Scripts/c27642961.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c27642961.lua) | 1 |
| Salamangreat Fennec | `49094491` | [Scripts/c49094491.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c49094491.lua) | 1 |
| Gagaga Head | `67120578` | [Scripts/c67120578.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c67120578.lua) | 1 |
| ...and 134 more |  |  |  |

## Script Examples

### Ultra Polymerization (`76647978`)

Source: [Scripts/c76647978.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c76647978.lua)

```lua
function c76647978.mgfilter(c,e,tp,fusc,mg)
	return c:IsControler(tp) and c:IsLocation(LOCATION_GRAVE)
		and c:GetReason()&(REASON_FUSION+REASON_MATERIAL)==(REASON_FUSION+REASON_MATERIAL) and c:GetReasonCard()==fusc
		and c:IsCanBeSpecialSummoned(e,0,tp,false,false)
		and fusc:CheckFusionMaterial(mg,c,PLAYER_NONE,true)
```

### Goyo Emperor (`59255742`)

Source: [Scripts/c59255742.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c59255742.lua)

```lua
function c59255742.spcon2(e,tp,eg,ep,ev,re,r,rp)
	local tc=eg:GetFirst()
	local rc=tc:GetReasonCard()
	return eg:GetCount()==1 and rc:IsControler(tp) and rc:GetOwner()~=tp
		and tc:IsType(TYPE_MONSTER) and tc:IsReason(REASON_BATTLE) and tc:IsLocation(LOCATION_GRAVE)
```

### Ostinato (`9113513`)

Source: [Scripts/c9113513.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c9113513.lua)

```lua
function c9113513.mgfilter(c,e,tp,fusc,mg)
	return c:IsControler(tp) and c:IsLocation(LOCATION_GRAVE)
		and c:GetReason()&(REASON_FUSION+REASON_MATERIAL)==(REASON_FUSION+REASON_MATERIAL) and c:GetReasonCard()==fusc
		and c:IsCanBeSpecialSummoned(e,0,tp,false,false)
		and fusc:CheckFusionMaterial(mg,c,PLAYER_NONE,true)
```
