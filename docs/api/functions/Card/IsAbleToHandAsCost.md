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

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3644`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **41** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.IsAbleToHandAsCost) with `Card.IsAbleToHandAsCost`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Astrazma Urania | `18738846` | [Scripts/c18738846.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c18738846.lua) | 1 |
| Sauravis, Dragon Sage of the Voiceless Voice | `88284599` | [Scripts/c88284599.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c88284599.lua) | 1 |
| Gouki The Master Ogre | `30286474` | [Scripts/c30286474.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c30286474.lua) | 1 |
| Whisker Blitzclique | `85523502` | [Scripts/c85523502.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c85523502.lua) | 1 |
| Cyber Jormungardr | `19715246` | [Scripts/c19715246.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c19715246.lua) | 1 |
| Grapha, Dragon Lord of Dark World | `34230233` | [Scripts/c34230233.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c34230233.lua) | 1 |
| Mind Shuffle | `24749710` | [Scripts/c24749710.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c24749710.lua) | 1 |
| Swap Frog | `9126351` | [Scripts/c9126351.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c9126351.lua) | 2 |
| Blitzclique - Breakaway | `64049762` | [Scripts/c64049762.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c64049762.lua) | 1 |
| Yoa the Plague Deity Ashtra | `1710647` | [Scripts/c1710647.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c1710647.lua) | 1 |
| Battlewasp - Sachi the Ceremonial Bow | `71456737` | [Scripts/c71456737.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c71456737.lua) | 1 |
| U.A. Libero Spiker | `11637481` | [Scripts/c11637481.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c11637481.lua) | 1 |
| Kuzuha the Bewitching Deity Ashtra | `65325949` | [Scripts/c65325949.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c65325949.lua) | 1 |
| Akasuna the Battle Ashtra | `38331244` | [Scripts/c38331244.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c38331244.lua) | 1 |
| Mikumari the Sealing Deity Ashtra | `38114652` | [Scripts/c38114652.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c38114652.lua) | 1 |
| Reign-Beaux, Overking of Dark World | `41406613` | [Scripts/c41406613.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c41406613.lua) | 1 |
| U.A. Midfielder | `72491806` | [Scripts/c72491806.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c72491806.lua) | 1 |
| Blitzclique Return Stroke | `23526128` | [Scripts/c23526128.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c23526128.lua) | 1 |
| U.A. Blockbacker | `34614289` | [Scripts/c34614289.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c34614289.lua) | 1 |
| Altergeist Silquitous | `89538537` | [Scripts/c89538537.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c89538537.lua) | 1 |
| U.A. Goalkeeper | `9485511` | [Scripts/c9485511.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c9485511.lua) | 1 |
| U.A. Perfect Ace | `82419869` | [Scripts/c82419869.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c82419869.lua) | 1 |
| Artifact Chakram | `8873112` | [Scripts/c8873112.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c8873112.lua) | 1 |
| Performapal Sky Pupil | `122520` | [Scripts/c122520.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c122520.lua) | 1 |
| ...and 17 more |  |  |  |

## Script Examples

### Astrazma Urania (`18738846`)

Source: [Scripts/c18738846.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c18738846.lua)

```lua
end
function s.spfilter(c,tp)
	return c:IsAbleToHandAsCost() and Duel.GetMZoneCount(tp,c)>0
end
function s.spcon(e,c)
```

### Sauravis, Dragon Sage of the Voiceless Voice (`88284599`)

Source: [Scripts/c88284599.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c88284599.lua)

```lua
function s.cost(e,tp,eg,ep,ev,re,r,rp,chk)
	local c=e:GetHandler()
	if chk==0 then return c:IsAbleToHandAsCost() end
	Duel.SendtoHand(c,nil,REASON_COST)
end
```

### Gouki The Master Ogre (`30286474`)

Source: [Scripts/c30286474.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c30286474.lua)

```lua
end
function c30286474.costfilter(c,g)
	return c:IsFaceup() and c:IsSetCard(0xfc) and g:IsContains(c) and c:IsAbleToHandAsCost()
end
function c30286474.distg(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
```
