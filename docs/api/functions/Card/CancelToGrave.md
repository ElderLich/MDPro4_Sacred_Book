# Card.CancelToGrave

## Signature

```lua
Card.CancelToGrave(Card c, [bool cancel]) -> void
```

## Description

Cancels the confirmed-to-Graveyard state for c. If cancel is false, sets that state again.
This state is used for non-continuous Spell/Trap Cards activated on the field before they leave the field; while set, they cannot return to the hand or Deck and are sent to the Graveyard when the Chain ends.
Use this helper to keep such cards on the field, as with Swords of Revealing Light or Scrap-Iron Scarecrow.

## Parameters

- `c` `Card`
- `cancel` `bool` optional - default: true

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3651`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **114** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.CancelToGrave`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Salamandra with Chain](/examples/cards/62091148) | `62091148` | [Scripts/c62091148.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62091148.lua) | 81 |
| [Converging Wishes](/examples/cards/20007374) | `20007374` | [Scripts/c20007374.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20007374.lua) | 64 |
| [Graydle Split](/examples/cards/75361204) | `75361204` | [Scripts/c75361204.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75361204.lua) | 64 |
| Number 38: Hope Harbinger Dragon Titanic Galaxy | `63767246` | [Scripts/c63767246.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63767246.lua) | 56 |
| Amaze Attraction Wonder Wheel | `93473606` | [Scripts/c93473606.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93473606.lua) | 55 |
| Max Metalmorph | `89812483` | [Scripts/c89812483.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c89812483.lua) | 53 |
| The Phantom Knights' Rank-Up-Magic Launch | `3298689` | [Scripts/c3298689.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3298689.lua) | 52 |
| Amaze Attraction Thrill Train | `36591747` | [Scripts/c36591747.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36591747.lua) | 52 |
| Scrap-Iron Sacred Statue | `85520170` | [Scripts/c85520170.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85520170.lua) | 52 |
| Red Cocoon | `2542230` | [Scripts/c2542230.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2542230.lua) | 52 |
| Mirror Barrier | `95915457` | [Scripts/c95915457.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95915457.lua) | 52 |
| Hyper-Rank-Up-Magic Ultimate Force | `87818869` | [Scripts/c87818869.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87818869.lua) | 51 |
| Shichi-Go-San | `11035075` | [Scripts/c11035075.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11035075.lua) | 51 |
| Gergonne's End | `59490397` | [Scripts/c59490397.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59490397.lua) | 51 |
| Malefic Force | `68721020` | [Scripts/c68721020.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c68721020.lua) | 51 |
| Limit Code | `86607583` | [Scripts/c86607583.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c86607583.lua) | 51 |
| Goblin's Crazy Beast | `71100270` | [Scripts/c71100270.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71100270.lua) | 50 |
| Amaze Attraction Cyclo-Coaster | `66984907` | [Scripts/c66984907.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66984907.lua) | 50 |
| DoomZ Destruction | `80320877` | [Scripts/c80320877.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80320877.lua) | 50 |
| Epurrely Beauty | `98049934` | [Scripts/c98049934.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c98049934.lua) | 49 |
| Laevatein, Generaider Boss of Shadows | `74615388` | [Scripts/c74615388.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74615388.lua) | 49 |
| Assault Spirits | `87043568` | [Scripts/c87043568.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87043568.lua) | 49 |
| Goblin Biker Grand Pileup | `90946420` | [Scripts/c90946420.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90946420.lua) | 48 |
| Epurrely Plump | `24434049` | [Scripts/c24434049.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24434049.lua) | 48 |
| ...and 90 more |  |  |  |

## Script Examples

### Salamandra with Chain (`62091148`)

Source: [Scripts/c62091148.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62091148.lua)

```lua
	if cid~=e:GetLabel() then return end
	if e:GetOwner():IsRelateToChain(ev) then
		e:GetOwner():CancelToGrave(false)
	end
end
```

### Converging Wishes (`20007374`)

Source: [Scripts/c20007374.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20007374.lua)

```lua
	if cid~=e:GetLabel() then return end
	if e:GetOwner():IsRelateToChain(ev) then
		e:GetOwner():CancelToGrave(false)
	end
end
```

### Graydle Split (`75361204`)

Source: [Scripts/c75361204.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75361204.lua)

```lua
	if cid~=e:GetLabel() then return end
	if e:GetOwner():IsRelateToChain(ev) then
		e:GetOwner():CancelToGrave(false)
	end
end
```
