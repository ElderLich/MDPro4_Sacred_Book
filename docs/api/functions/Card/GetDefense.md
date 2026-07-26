# Card.GetDefense

## Signature

```lua
Card.GetDefense(Card c) -> int
```

## Description

Returns c's current DEF. Unknown or negative DEF values are clamped to 0 by this binding.

## Parameters

- `c` `Card`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3446`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **121** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.GetDefense`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Duel Link Dragon, the Duel Dragon | `60025883` | [Scripts/c60025883.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60025883.lua) | 1 |
| Amaze Attraction Wonder Wheel | `93473606` | [Scripts/c93473606.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93473606.lua) | 1 |
| Nemleria Louve | `57296396` | [Scripts/c57296396.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57296396.lua) | 1 |
| Gladiator Beast Gaiodiaz | `90957527` | [Scripts/c90957527.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90957527.lua) | 2 |
| Millennium-Eyes Restrict | `41578483` | [Scripts/c41578483.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41578483.lua) | 2 |
| Melffy Staring Contest | `76981308` | [Scripts/c76981308.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76981308.lua) | 1 |
| Gilti-Gearfried the Magical Steel Knight | `49161188` | [Scripts/c49161188.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49161188.lua) | 2 |
| Mythical Beast Medusa | `54965929` | [Scripts/c54965929.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54965929.lua) | 1 |
| Floowandereeze &amp; Empen | `80611581` | [Scripts/c80611581.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80611581.lua) | 1 |
| Cherubini, Ebon Angel of the Burning Abyss | `58699500` | [Scripts/c58699500.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58699500.lua) | 1 |
| Dimension Reflector | `54297661` | [Scripts/c54297661.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54297661.lua) | 2 |
| Light and Darkness Dragonlord | `19652159` | [Scripts/c19652159.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c19652159.lua) | 1 |
| True Draco Apocalypse | `61529473` | [Scripts/c61529473.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61529473.lua) | 1 |
| Vanquish Soul Dr. Mad Love | `29280200` | [Scripts/c29280200.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29280200.lua) | 2 |
| Victory Viper XX03 | `93130021` | [Scripts/c93130021.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93130021.lua) | 3 |
| Replicard LAD | `1665819` | [Scripts/c1665819.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1665819.lua) | 1 |
| Power Capsule | `54289683` | [Scripts/c54289683.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54289683.lua) | 3 |
| Malacoda, Netherlord of the Burning Abyss | `35330871` | [Scripts/c35330871.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35330871.lua) | 1 |
| Galaxy Brave | `55168550` | [Scripts/c55168550.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55168550.lua) | 1 |
| Psychic Commander | `21454943` | [Scripts/c21454943.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21454943.lua) | 1 |
| Yosenju Oyam | `69838592` | [Scripts/c69838592.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c69838592.lua) | 1 |
| Superheavy Samurai Helper | `44891812` | [Scripts/c44891812.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44891812.lua) | 1 |
| Legendary Secret of the Six Samurai | `15327215` | [Scripts/c15327215.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15327215.lua) | 2 |
| Red-Eyes Fang with Chain | `57135971` | [Scripts/c57135971.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57135971.lua) | 1 |
| ...and 97 more |  |  |  |

## Script Examples

### Duel Link Dragon, the Duel Dragon (`60025883`)

Source: [Scripts/c60025883.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60025883.lua)

```lua
	return c:IsType(TYPE_SYNCHRO) and c:IsAbleToRemoveAsCost()
		and (c:IsSetCard(0xc2) or c:IsRace(RACE_DRAGON) and (c:IsLevel(7) or c:IsLevel(8)))
		and Duel.IsPlayerCanSpecialSummonMonster(tp,60025884,0,TYPES_TOKEN_MONSTER,c:GetAttack(),c:GetDefense(),c:GetLevel(),c:GetRace(),c:GetAttribute())
end
function c60025883.spcost(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Amaze Attraction Wonder Wheel (`93473606`)

Source: [Scripts/c93473606.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93473606.lua)

```lua
	if ec and c:IsRelateToEffect(e) then
		local atk=ec:GetAttack()
		local def=ec:GetDefense()
		local e1=Effect.CreateEffect(c)
		e1:SetType(EFFECT_TYPE_SINGLE)
```

### Nemleria Louve (`57296396`)

Source: [Scripts/c57296396.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57296396.lua)

```lua
end
function s.atkfilter(c)
	return c:IsFaceup() and (c:GetAttack()>0 or c:GetDefense()>0)
end
function s.stattg(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
```
