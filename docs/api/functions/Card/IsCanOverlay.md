# Card.IsCanOverlay

## Signature

```lua
Card.IsCanOverlay(Card c, [int player]) -> bool
```

## Description

Checks whether c can be used as Xyz Material by player.
player defaults to the current reason player. The core rejects Tokens, forbidden cards in invalid states, and cards controlled by the other player that cannot change control.

## Parameters

- `c` `Card`
- `player` `int` optional - default: current reason player

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3693`

## Guided Examples

Learn how to use this function in context:

- [Xyz Procedure Guide](/learn/xyz-procedure)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **177** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.IsCanOverlay) with `Card.IsCanOverlay`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Performage Cup Tricker](/examples/cards/6812770) | `6812770` | [Scripts/c6812770.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6812770.lua) | 1 |
| Jupredo the Shademachine Power Patron | `43871165` | [Scripts/c43871165.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43871165.lua) | 1 |
| Number 101: Silent Honor ARK - Soul Asylum | `2419596` | [Scripts/c2419596.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2419596.lua) | 2 |
| Super Quantal Mech Ship Magnacarrier | `10424147` | [Scripts/c10424147.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10424147.lua) | 2 |
| DoomZ XII Zero - Drastea | `92472273` | [Scripts/c92472273.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92472273.lua) | 2 |
| D/D/D Deviser King Deus Machinex | `46593546` | [Scripts/c46593546.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46593546.lua) | 1 |
| Number 38: Hope Harbinger Dragon Titanic Galaxy | `63767246` | [Scripts/c63767246.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63767246.lua) | 1 |
| Purrely | `25550531` | [Scripts/c25550531.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25550531.lua) | 2 |
| Odd-Eyes Rebellion Dragon Overlord | `98452268` | [Scripts/c98452268.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c98452268.lua) | 1 |
| Number 4: Stealth Kragen | `67557908` | [Scripts/c67557908.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67557908.lua) | 1 |
| Purrely Sharely!? | `10780049` | [Scripts/c10780049.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10780049.lua) | 1 |
| Squeeze, the Full Moon of Raise Moon - JACKPOT! | `9484285` | [Scripts/c9484285.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9484285.lua) | 1 |
| Madolche Dessert | `51650038` | [Scripts/c51650038.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c51650038.lua) | 2 |
| Materiactor Meltthrough | `66059345` | [Scripts/c66059345.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66059345.lua) | 1 |
| The Phantom Knights' Rank-Up-Magic Launch | `3298689` | [Scripts/c3298689.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3298689.lua) | 2 |
| Time Thief Redoer | `55285840` | [Scripts/c55285840.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55285840.lua) | 1 |
| Numeron Chaos Ritual | `41850466` | [Scripts/c41850466.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41850466.lua) | 2 |
| Bujincident | `11221418` | [Scripts/c11221418.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11221418.lua) | 2 |
| Zoodiac Combo | `73881652` | [Scripts/c73881652.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c73881652.lua) | 1 |
| Disaster, Dragon Ruler of All Apocalypses | `67359907` | [Scripts/c67359907.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67359907.lua) | 2 |
| Doll House | `67331360` | [Scripts/c67331360.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67331360.lua) | 1 |
| Stealth Kragen Spawn | `94942656` | [Scripts/c94942656.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c94942656.lua) | 1 |
| The Glitter of Raise Moon | `9362643` | [Scripts/c9362643.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9362643.lua) | 2 |
| Magician of Hope | `67865534` | [Scripts/c67865534.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67865534.lua) | 2 |
| ...and 153 more |  |  |  |

## Script Examples

### Performage Cup Tricker (`6812770`)

Source: [Scripts/c6812770.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6812770.lua)

```lua
	local c=e:GetHandler()
	if chkc then return chkc:IsLocation(LOCATION_MZONE) and chkc:IsControler(tp) and s.ovfilter(chkc) and chkc~=c end
	if chk==0 then return Duel.IsExistingTarget(s.ovfilter,tp,LOCATION_MZONE,0,1,c) and c:IsCanOverlay() end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_TARGET)
	Duel.SelectTarget(tp,s.ovfilter,tp,LOCATION_MZONE,0,1,1,c)
```

### Jupredo the Shademachine Power Patron (`43871165`)

Source: [Scripts/c43871165.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43871165.lua)

```lua
end
function s.matfilter(c)
	return c:IsCanOverlay()
end
function s.spop(e,tp,eg,ep,ev,re,r,rp)
```

### Number 101: Silent Honor ARK - Soul Asylum (`2419596`)

Source: [Scripts/c2419596.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2419596.lua)

```lua
end
function s.filter2(c)
	return c:IsCanOverlay()
end
function s.target1(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
```
