# Card.IsCanAddCounter

## Signature

```lua
Card.IsCanAddCounter(Card c, int countertype, int count, [bool singly], [int loc]) -> bool
```

## Description

Checks whether the current reason player can place count counters of countertype on c.
When loc is 0, c must currently be face-up on the field. When loc is nonzero, the counter permit range is checked against loc instead. If singly is true, counter limits are tested as current count + 1 rather than current count + count.

## Parameters

- `c` `Card`
- `countertype` `int`
- `count` `int`
- `singly` `bool` optional - default: false
- `loc` `int` optional - default: 0

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3690`

## Guided Examples

Learn how to use this function in context:

- [Counters](/learn/counters)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **82** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.IsCanAddCounter) with `Card.IsCanAddCounter`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Limit Code | `86607583` | [Scripts/c86607583.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c86607583.lua) | 1 |
| Servant of Endymion | `92559258` | [Scripts/c92559258.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92559258.lua) | 4 |
| Mythical Beast Medusa | `54965929` | [Scripts/c54965929.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54965929.lua) | 1 |
| Combat Wheel | `12501230` | [Scripts/c12501230.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12501230.lua) | 2 |
| Mythical Beast Jackal | `91182675` | [Scripts/c91182675.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c91182675.lua) | 1 |
| Zushin the Sleeping Giant | `67547370` | [Scripts/c67547370.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67547370.lua) | 1 |
| Alien Shocktrooper M-Frame | `74974229` | [Scripts/c74974229.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74974229.lua) | 2 |
| Chaos Core | `54040484` | [Scripts/c54040484.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54040484.lua) | 2 |
| Cubic Wave | `35058588` | [Scripts/c35058588.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35058588.lua) | 2 |
| Predaplant Longinephila | `44994712` | [Scripts/c44994712.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44994712.lua) | 3 |
| Signal Warrior | `9634146` | [Scripts/c9634146.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9634146.lua) | 1 |
| Super B.E.S. Metal Slave | `41516133` | [Scripts/c41516133.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41516133.lua) | 1 |
| B.E.S. Derringer Core | `5121528` | [Scripts/c5121528.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5121528.lua) | 1 |
| Cosmic Fortress Gol'gar | `68319538` | [Scripts/c68319538.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c68319538.lua) | 2 |
| Aiza the Dragoness of Deranged Devotion | `63378869` | [Scripts/c63378869.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63378869.lua) | 3 |
| Beat Cop from the Underworld | `99011763` | [Scripts/c99011763.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c99011763.lua) | 3 |
| Starving Venemy Lethal Dose Dragon | `22070401` | [Scripts/c22070401.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22070401.lua) | 1 |
| Predaplanning | `44536921` | [Scripts/c44536921.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44536921.lua) | 2 |
| Summer | `97254001` | [Scripts/c97254001.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97254001.lua) | 1 |
| Ninjitsu Art of Mosquito Marching | `68441986` | [Scripts/c68441986.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c68441986.lua) | 1 |
| Borreload Savage Dragon | `27548199` | [Scripts/c27548199.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27548199.lua) | 1 |
| Cosmic Horror Gangi'el | `51192573` | [Scripts/c51192573.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c51192573.lua) | 3 |
| Ice Master | `32750510` | [Scripts/c32750510.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32750510.lua) | 4 |
| Blackwing - Auster the South Wind | `17465972` | [Scripts/c17465972.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17465972.lua) | 2 |
| ...and 58 more |  |  |  |

## Script Examples

### Limit Code (`86607583`)

Source: [Scripts/c86607583.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c86607583.lua)

```lua
	local c=e:GetHandler()
	local ct=Duel.GetMatchingGroupCount(c86607583.cfilter,tp,LOCATION_GRAVE,0,nil)
	if c:IsRelateToEffect(e) and ct>0 and c:IsCanAddCounter(0x47,ct) then
		c:AddCounter(0x47,ct)
		Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SPSUMMON)
```

### Servant of Endymion (`92559258`)

Source: [Scripts/c92559258.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92559258.lua)

```lua
function c92559258.countertg2(e,tp,eg,ep,ev,re,r,rp,chk)
	local c=e:GetHandler()
	if chk==0 then return c:IsCanAddCounter(0x1,1) end
	local g=Duel.GetMatchingGroup(Card.IsCanAddCounter,tp,LOCATION_ONFIELD,0,c,0x1,1)
	g:AddCard(c)
```

### Mythical Beast Medusa (`54965929`)

Source: [Scripts/c54965929.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54965929.lua)

```lua
		local tc=Duel.GetFirstTarget()
		if tc:IsRelateToEffect(e) and Duel.SpecialSummon(tc,0,tp,tp,false,false,POS_FACEUP)~=0
			and tc:IsCanAddCounter(0x1,1) then
			tc:AddCounter(0x1,1)
		end
```
