# Card.GetBattleTarget

## Signature

```lua
Card.GetBattleTarget(Card c) -> Card
```

## Description

Returns the card that fought with c

## Parameters

- `c` `Card`

## Returns

- `Card`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3653`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **353** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.GetBattleTarget`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Goyo Emperor](/examples/cards/59255742) | `59255742` | [Scripts/c59255742.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59255742.lua) | 70 |
| [Favorite HERO Flame Wingman](/examples/cards/13243124) | `13243124` | [Scripts/c13243124.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13243124.lua) | 66 |
| [Spirit Illusion](/examples/cards/71939275) | `71939275` | [Scripts/c71939275.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71939275.lua) | 65 |
| Performapal Odd-Eyes Dissolver | `46136942` | [Scripts/c46136942.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46136942.lua) | 57 |
| Galaxy-Eyes Photon Dragon | `93717133` | [Scripts/c93717133.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93717133.lua) | 56 |
| All-Eyes Phantom Dragon | `70335319` | [Scripts/c70335319.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70335319.lua) | 55 |
| Arcana Force EX - The Light Ruler | `5861892` | [Scripts/c5861892.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5861892.lua) | 55 |
| Supreme King Z-ARC - Synchro Universe | `48654267` | [Scripts/c48654267.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48654267.lua) | 54 |
| Hecahands Mankibuel | `18321034` | [Scripts/c18321034.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18321034.lua) | 53 |
| Mirror Barrier | `95915457` | [Scripts/c95915457.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95915457.lua) | 52 |
| Gilti-Gearfried the Magical Steel Knight | `49161188` | [Scripts/c49161188.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49161188.lua) | 51 |
| TiSolfachord Beautia | `54387923` | [Scripts/c54387923.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54387923.lua) | 50 |
| Supreme King Dragon Odd-Eyes | `96733134` | [Scripts/c96733134.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96733134.lua) | 50 |
| Courageous Crimson Chevalier Bradamante | `91479482` | [Scripts/c91479482.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c91479482.lua) | 50 |
| Alien Mother | `24104865` | [Scripts/c24104865.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24104865.lua) | 50 |
| Predaplant Chimerafflesia | `25586143` | [Scripts/c25586143.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25586143.lua) | 49 |
| Magikey Deity - Ashtartu | `26988374` | [Scripts/c26988374.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c26988374.lua) | 49 |
| Life Extreme | `36148308` | [Scripts/c36148308.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36148308.lua) | 49 |
| Myutant Blast | `79072916` | [Scripts/c79072916.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c79072916.lua) | 49 |
| Infernoid Attondel | `88301393` | [Scripts/c88301393.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88301393.lua) | 49 |
| Gussari @Ignister | `55762976` | [Scripts/c55762976.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55762976.lua) | 49 |
| Infinitrack Earth Slicer | `97584719` | [Scripts/c97584719.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97584719.lua) | 49 |
| Magikey Mechmusket - Batosbuster | `19489718` | [Scripts/c19489718.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c19489718.lua) | 48 |
| Mirage Swordsman | `73936388` | [Scripts/c73936388.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c73936388.lua) | 48 |
| ...and 329 more |  |  |  |

## Script Examples

### Goyo Emperor (`59255742`)

Source: [Scripts/c59255742.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59255742.lua)

```lua
function c59255742.spcon(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	local bc=c:GetBattleTarget()
	if not c:IsRelateToBattle() or c:IsFacedown() then return false end
	return bc:IsLocation(LOCATION_GRAVE) and bc:IsType(TYPE_MONSTER)
```

### Favorite HERO Flame Wingman (`13243124`)

Source: [Scripts/c13243124.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13243124.lua)

```lua
function s.atkcon(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	local bc=c:GetBattleTarget()
	return bc and bc:IsFaceup() and bc:IsAttackAbove(2200)
end
```

### Spirit Illusion (`71939275`)

Source: [Scripts/c71939275.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71939275.lua)

```lua
function s.atkcon(e,tp,eg,ep,ev,re,r,rp)
	local ec=e:GetHandler():GetEquipTarget()
	local tc=ec:GetBattleTarget()
	e:SetLabelObject(tc)
	return not ec:IsAttack(0) and tc and tc:IsFaceup()
```
