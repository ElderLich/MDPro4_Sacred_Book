# Card.IsAbleToHandAsCost

## Signature

```lua
Card.IsAbleToHandAsCost(Card c) -> bool
```

## Description

Checks whether c can be returned to the hand as a cost.
This uses c's actual return destination and returns false when the card would go somewhere other than the player's hand, such as the Extra Deck.

## Parameters

- `c` `Card`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3589`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **37** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.IsAbleToHandAsCost`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Astrolasma Urania | `18738846` | [Scripts/c18738846.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18738846.lua) | 55 |
| Sauravis, Dragon Sage of the Voiceless Voice | `88284599` | [Scripts/c88284599.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88284599.lua) | 51 |
| Gouki The Master Ogre | `30286474` | [Scripts/c30286474.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30286474.lua) | 51 |
| Whisker Blitzclique | `85523502` | [Scripts/c85523502.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85523502.lua) | 50 |
| Cyber Jormungardr | `19715246` | [Scripts/c19715246.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c19715246.lua) | 49 |
| Grapha, Dragon Lord of Dark World | `34230233` | [Scripts/c34230233.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34230233.lua) | 49 |
| Mind Shuffle | `24749710` | [Scripts/c24749710.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24749710.lua) | 47 |
| Swap Frog | `9126351` | [Scripts/c9126351.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9126351.lua) | 47 |
| Blitzclique - Breakaway | `64049762` | [Scripts/c64049762.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c64049762.lua) | 47 |
| Battlewasp - Sachi the Ceremonial Bow | `71456737` | [Scripts/c71456737.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71456737.lua) | 45 |
| U.A. Libero Spiker | `11637481` | [Scripts/c11637481.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11637481.lua) | 45 |
| Reign-Beaux, Overking of Dark World | `41406613` | [Scripts/c41406613.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41406613.lua) | 44 |
| U.A. Midfielder | `72491806` | [Scripts/c72491806.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c72491806.lua) | 44 |
| Blitzclique - Return Stroke | `23526128` | [Scripts/c23526128.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23526128.lua) | 43 |
| U.A. Blockbacker | `34614289` | [Scripts/c34614289.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34614289.lua) | 41 |
| Altergeist Silquitous | `89538537` | [Scripts/c89538537.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c89538537.lua) | 38 |
| U.A. Goalkeeper | `9485511` | [Scripts/c9485511.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9485511.lua) | 36 |
| U.A. Perfect Ace | `82419869` | [Scripts/c82419869.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82419869.lua) | 36 |
| Artifact Chakram | `8873112` | [Scripts/c8873112.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8873112.lua) | 35 |
| Performapal Sky Pupil | `122520` | [Scripts/c122520.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c122520.lua) | 34 |
| U.A. Rival Rebounder | `17264592` | [Scripts/c17264592.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17264592.lua) | 34 |
| U.A. Playmaker | `98229575` | [Scripts/c98229575.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c98229575.lua) | 34 |
| Altergeist Dragvirion | `21187631` | [Scripts/c21187631.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21187631.lua) | 34 |
| Garum the Storm Vassal | `22382087` | [Scripts/c22382087.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22382087.lua) | 33 |
| ...and 13 more |  |  |  |

## Script Examples

### Astrolasma Urania (`18738846`)

Source: [Scripts/c18738846.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18738846.lua)

```lua
end
function s.spfilter(c,tp)
	return c:IsAbleToHandAsCost() and Duel.GetMZoneCount(tp,c)>0
end
function s.spcon(e,c)
```

### Sauravis, Dragon Sage of the Voiceless Voice (`88284599`)

Source: [Scripts/c88284599.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88284599.lua)

```lua
function s.cost(e,tp,eg,ep,ev,re,r,rp,chk)
	local c=e:GetHandler()
	if chk==0 then return c:IsAbleToHandAsCost() end
	Duel.SendtoHand(c,nil,REASON_COST)
end
```

### Gouki The Master Ogre (`30286474`)

Source: [Scripts/c30286474.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30286474.lua)

```lua
end
function c30286474.costfilter(c,g)
	return c:IsFaceup() and c:IsSetCard(0xfc) and g:IsContains(c) and c:IsAbleToHandAsCost()
end
function c30286474.distg(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
```
