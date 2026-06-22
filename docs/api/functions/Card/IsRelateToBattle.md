# Card.IsRelateToBattle

## Signature

```lua
Card.IsRelateToBattle(Card c) -> bool
```

## Description

Checks whether c is still related to the current battle, usually during the Damage Step or shortly after damage calculation.

## Parameters

- `c` `Card`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3565`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **565** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.IsRelateToBattle`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Goyo Emperor](/examples/cards/59255742) | `59255742` | [Scripts/c59255742.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59255742.lua) | 70 |
| [Converging Wishes](/examples/cards/20007374) | `20007374` | [Scripts/c20007374.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20007374.lua) | 64 |
| [Light End Sublimation Dragon](/examples/cards/35614780) | `35614780` | [Scripts/c35614780.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35614780.lua) | 61 |
| Performapal Odd-Eyes Dissolver | `46136942` | [Scripts/c46136942.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46136942.lua) | 57 |
| Number 99: Utopia Dragonar | `95134948` | [Scripts/c95134948.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95134948.lua) | 57 |
| Sea Stealth Attack | `19089195` | [Scripts/c19089195.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c19089195.lua) | 57 |
| Galaxy-Eyes Photon Dragon | `93717133` | [Scripts/c93717133.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93717133.lua) | 56 |
| Nirvana High Paladin | `80896940` | [Scripts/c80896940.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80896940.lua) | 55 |
| Favorite Hero | `11881272` | [Scripts/c11881272.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11881272.lua) | 55 |
| Arcana Force EX - The Light Ruler | `5861892` | [Scripts/c5861892.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5861892.lua) | 55 |
| Gladiator Beast Gaiodiaz | `90957527` | [Scripts/c90957527.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90957527.lua) | 54 |
| Chevreuil, Hunting Scout of the Deep Forest | `13023431` | [Scripts/c13023431.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13023431.lua) | 54 |
| Megaroid City | `44139064` | [Scripts/c44139064.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44139064.lua) | 53 |
| Vulcan Dragni the Cubic King | `77387463` | [Scripts/c77387463.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77387463.lua) | 53 |
| Shura the Combat Star | `32615065` | [Scripts/c32615065.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32615065.lua) | 52 |
| X-Saber Gottoms | `8252010` | [Scripts/c8252010.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8252010.lua) | 52 |
| Mirror Barrier | `95915457` | [Scripts/c95915457.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95915457.lua) | 52 |
| Gilti-Gearfried the Magical Steel Knight | `49161188` | [Scripts/c49161188.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49161188.lua) | 51 |
| TiSolfachord Beautia | `54387923` | [Scripts/c54387923.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54387923.lua) | 50 |
| Mechanical Mechanic | `22106558` | [Scripts/c22106558.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22106558.lua) | 50 |
| Geira Guile the Cubic King | `40392714` | [Scripts/c40392714.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40392714.lua) | 50 |
| Courageous Crimson Chevalier Bradamante | `91479482` | [Scripts/c91479482.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c91479482.lua) | 50 |
| ZW - Dragonic Halberd | `2896663` | [Scripts/c2896663.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2896663.lua) | 50 |
| Speedroid Colonel Clackers | `65155517` | [Scripts/c65155517.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65155517.lua) | 49 |
| ...and 541 more |  |  |  |

## Script Examples

### Goyo Emperor (`59255742`)

Source: [Scripts/c59255742.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59255742.lua)

```lua
	local c=e:GetHandler()
	local bc=c:GetBattleTarget()
	if not c:IsRelateToBattle() or c:IsFacedown() then return false end
	return bc:IsLocation(LOCATION_GRAVE) and bc:IsType(TYPE_MONSTER)
end
```

### Converging Wishes (`20007374`)

Source: [Scripts/c20007374.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20007374.lua)

```lua
	local c=e:GetHandler()
	local ec=c:GetEquipTarget()
	if not ec:IsRelateToBattle() then return end
	Duel.ChainAttack()
	local e1=Effect.CreateEffect(c)
```

### Light End Sublimation Dragon (`35614780`)

Source: [Scripts/c35614780.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35614780.lua)

```lua
		e2:SetCode(EFFECT_UPDATE_DEFENSE)
		c:RegisterEffect(e2)
		if not c:IsHasEffect(EFFECT_REVERSE_UPDATE) and bc:IsControler(1-tp) and bc:IsFaceup() and bc:IsRelateToBattle() then
			local e3=Effect.CreateEffect(c)
			e3:SetType(EFFECT_TYPE_SINGLE)
```
