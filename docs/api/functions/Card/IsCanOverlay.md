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

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3641`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **169** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.IsCanOverlay`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Performage Cup Tricker](/examples/cards/6812770) | `6812770` | [Scripts/c6812770.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6812770.lua) | 65 |
| [Jupredo the Shademachine Power Patron](/examples/cards/43871165) | `43871165` | [Scripts/c43871165.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43871165.lua) | 60 |
| Super Quantal Mech Ship Magnacarrier | `10424147` | [Scripts/c10424147.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10424147.lua) | 57 |
| DoomZ XII Zero - Drastea | `92472273` | [Scripts/c92472273.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92472273.lua) | 57 |
| D/D/D Deviser King Deus Machinex | `46593546` | [Scripts/c46593546.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46593546.lua) | 56 |
| Number 38: Hope Harbinger Dragon Titanic Galaxy | `63767246` | [Scripts/c63767246.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63767246.lua) | 56 |
| Purrely | `25550531` | [Scripts/c25550531.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25550531.lua) | 56 |
| Odd-Eyes Rebellion Dragon Overlord | `98452268` | [Scripts/c98452268.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c98452268.lua) | 55 |
| Number 4: Stealth Kragen | `67557908` | [Scripts/c67557908.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67557908.lua) | 55 |
| Purrely Sharely!? | `10780049` | [Scripts/c10780049.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10780049.lua) | 55 |
| Madolche Dessert | `51650038` | [Scripts/c51650038.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c51650038.lua) | 53 |
| Materiactor Meltthrough | `66059345` | [Scripts/c66059345.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66059345.lua) | 53 |
| The Phantom Knights' Rank-Up-Magic Launch | `3298689` | [Scripts/c3298689.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3298689.lua) | 52 |
| Time Thief Redoer | `55285840` | [Scripts/c55285840.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55285840.lua) | 52 |
| Numeron Chaos Ritual | `41850466` | [Scripts/c41850466.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41850466.lua) | 52 |
| Bujincident | `11221418` | [Scripts/c11221418.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11221418.lua) | 52 |
| Zoodiac Combo | `73881652` | [Scripts/c73881652.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c73881652.lua) | 52 |
| Disaster, Dragon Ruler of All Apocalypses | `67359907` | [Scripts/c67359907.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67359907.lua) | 51 |
| Doll House | `67331360` | [Scripts/c67331360.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67331360.lua) | 51 |
| Stealth Kragen Spawn | `94942656` | [Scripts/c94942656.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c94942656.lua) | 51 |
| Magician of Hope | `67865534` | [Scripts/c67865534.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67865534.lua) | 50 |
| Sacred Noble Knight of King Custennin | `78876707` | [Scripts/c78876707.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78876707.lua) | 50 |
| Goblin's Crazy Beast | `71100270` | [Scripts/c71100270.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71100270.lua) | 50 |
| Galaxy Cleric | `28770951` | [Scripts/c28770951.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28770951.lua) | 50 |
| ...and 145 more |  |  |  |

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

### Super Quantal Mech Ship Magnacarrier (`10424147`)

Source: [Scripts/c10424147.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10424147.lua)

```lua
end
function c10424147.spfilter3(c,e)
	return (c:IsLocation(LOCATION_GRAVE) or c:IsFaceup()) and c:IsSetCard(0x20dc) and c:IsType(TYPE_XYZ) and c:IsCanBeEffectTarget(e) and c:IsCanOverlay()
end
function c10424147.spfilter4(c,e,tp)
```
