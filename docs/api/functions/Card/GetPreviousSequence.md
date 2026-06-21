# Card.GetPreviousSequence

## Signature

```lua
Card.GetPreviousSequence(Card c) -> int
```

## Description

Returns the sequence number before the c position changes

## Parameters

- `c` `Card`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3469`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **59** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.GetPreviousSequence`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Hojo the Vaylantz Warrior | `88919365` | [Scripts/c88919365.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88919365.lua) | 59 |
| Arktos XII - Chronochasm Vaylantz | `50687050` | [Scripts/c50687050.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50687050.lua) | 56 |
| Enlilgirsu, the Orcust Mekk-Knight | `74820316` | [Scripts/c74820316.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74820316.lua) | 56 |
| Cyberse Contract Witch | `37458564` | [Scripts/c37458564.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37458564.lua) | 55 |
| Neo Super Quantal Mech King Blaster Magna | `95493471` | [Scripts/c95493471.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95493471.lua) | 53 |
| Cyberse Witch | `11674673` | [Scripts/c11674673.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11674673.lua) | 53 |
| Salamangreat Sunlight Wolf | `87871125` | [Scripts/c87871125.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87871125.lua) | 52 |
| Zefra Metaltron | `85216896` | [Scripts/c85216896.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85216896.lua) | 52 |
| Firewall Dragon Singularity | `21637210` | [Scripts/c21637210.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21637210.lua) | 50 |
| Life Extreme | `36148308` | [Scripts/c36148308.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36148308.lua) | 49 |
| Qliphort Genius | `22423493` | [Scripts/c22423493.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22423493.lua) | 49 |
| Battle Shogun of the Six Samurai | `74752631` | [Scripts/c74752631.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74752631.lua) | 48 |
| Transcendosaurus Exaraptor | `56818742` | [Scripts/c56818742.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56818742.lua) | 48 |
| Ogdoadic Hollow | `96433300` | [Scripts/c96433300.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96433300.lua) | 48 |
| True Light | `62089826` | [Scripts/c62089826.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62089826.lua) | 47 |
| Topologic Blaster Dragon | `30064423` | [Scripts/c30064423.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30064423.lua) | 47 |
| Xtra HERO Wonder Driver | `1948619` | [Scripts/c1948619.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1948619.lua) | 47 |
| Flash Charge Dragon | `95372220` | [Scripts/c95372220.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95372220.lua) | 47 |
| Tindangle Base Gardna | `94365540` | [Scripts/c94365540.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c94365540.lua) | 46 |
| Subterror Behemoth Fiendess | `74937659` | [Scripts/c74937659.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74937659.lua) | 45 |
| Firewall Dragon | `5043010` | [Scripts/c5043010.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5043010.lua) | 45 |
| Vaylantz Mad Marquess | `87897777` | [Scripts/c87897777.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87897777.lua) | 44 |
| Vaylantz Wave - Master Phase | `84281045` | [Scripts/c84281045.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84281045.lua) | 44 |
| Saion the Vaylantz Archer | `15130912` | [Scripts/c15130912.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15130912.lua) | 43 |
| ...and 35 more |  |  |  |

## Script Examples

### Hojo the Vaylantz Warrior (`88919365`)

Source: [Scripts/c88919365.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88919365.lua)

```lua
	local ph=Duel.GetCurrentPhase()
	return c:IsPreviousLocation(LOCATION_MZONE) and c:IsLocation(LOCATION_MZONE)
		and (c:GetPreviousSequence()~=c:GetSequence() or c:GetPreviousControler()~=tp)
		and ph~=PHASE_DAMAGE and ph~=PHASE_DAMAGE_CAL
end
```

### Arktos XII - Chronochasm Vaylantz (`50687050`)

Source: [Scripts/c50687050.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50687050.lua)

```lua
function s.cfilter(c)
	return c:IsLocation(LOCATION_MZONE) and c:IsPreviousLocation(LOCATION_MZONE)
		and (c:GetPreviousSequence()~=c:GetSequence() or c:GetPreviousControler()~=c:GetControler())
end
function s.descon(e,tp,eg,ep,ev,re,r,rp)
```

### Enlilgirsu, the Orcust Mekk-Knight (`74820316`)

Source: [Scripts/c74820316.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74820316.lua)

```lua
function s.regcon(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	return c:GetPreviousSequence()>4 and c:IsPreviousLocation(LOCATION_MZONE)
end
function s.regop(e,tp,eg,ep,ev,re,r,rp)
```
