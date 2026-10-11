# Card.GetBattleTarget

## Signature

```lua
Card.GetBattleTarget(Card c) -> Card|nil
```

## Description

Returns the monster currently battling c, or nil if c is not the current attacker or attack target.

## Parameters

- `c` `Card`

## Returns

- `Card|nil` - The monster battling c, or nil.

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3708`

## Guided Examples

Learn how to use this function in context:

- [Battle Participants And Timing](/learn/battle-participants-and-timing)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **356** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.GetBattleTarget) with `Card.GetBattleTarget`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Goyo Emperor](/examples/cards/59255742) | `59255742` | [Scripts/c59255742.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59255742.lua) | 3 |
| [Favorite HERO Flame Wingman](/examples/cards/13243124) | `13243124` | [Scripts/c13243124.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13243124.lua) | 1 |
| [Spirit Illusion](/examples/cards/71939275) | `71939275` | [Scripts/c71939275.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71939275.lua) | 1 |
| Performapal Odd-Eyes Dissolver | `46136942` | [Scripts/c46136942.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46136942.lua) | 1 |
| Galaxy-Eyes Photon Dragon | `93717133` | [Scripts/c93717133.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93717133.lua) | 1 |
| All-Eyes Phantom Dragon | `70335319` | [Scripts/c70335319.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70335319.lua) | 1 |
| Arcana Force EX - The Light Ruler | `5861892` | [Scripts/c5861892.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5861892.lua) | 1 |
| Supreme King Z-ARC - Synchro Universe | `48654267` | [Scripts/c48654267.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48654267.lua) | 2 |
| Hecahands Mankibuel | `18321034` | [Scripts/c18321034.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18321034.lua) | 1 |
| Mirror Barrier | `95915457` | [Scripts/c95915457.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95915457.lua) | 2 |
| Gilti-Gearfried the Magical Steel Knight | `49161188` | [Scripts/c49161188.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49161188.lua) | 1 |
| TiSolfachord Beautia | `54387923` | [Scripts/c54387923.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54387923.lua) | 3 |
| Supreme King Dragon Odd-Eyes | `96733134` | [Scripts/c96733134.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96733134.lua) | 1 |
| Courageous Crimson Chevalier Bradamante | `91479482` | [Scripts/c91479482.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c91479482.lua) | 1 |
| Blue-Eyes Toon Ultimate Dragon | `71808988` | [Scripts/c71808988.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71808988.lua) | 1 |
| Alien Mother | `24104865` | [Scripts/c24104865.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24104865.lua) | 1 |
| Predaplant Chimerafflesia | `25586143` | [Scripts/c25586143.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25586143.lua) | 1 |
| Magikey Deity - Ashtartu | `26988374` | [Scripts/c26988374.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c26988374.lua) | 1 |
| Life Extreme | `36148308` | [Scripts/c36148308.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36148308.lua) | 2 |
| Myutant Blast | `79072916` | [Scripts/c79072916.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c79072916.lua) | 3 |
| Infernoid Attondel | `88301393` | [Scripts/c88301393.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88301393.lua) | 1 |
| Gussari @Ignister | `55762976` | [Scripts/c55762976.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55762976.lua) | 1 |
| Infinitrack Earth Slicer | `97584719` | [Scripts/c97584719.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97584719.lua) | 1 |
| Magikey Mechmusket - Batosbuster | `19489718` | [Scripts/c19489718.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c19489718.lua) | 1 |
| ...and 332 more |  |  |  |

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
