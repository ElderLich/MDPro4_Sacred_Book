# Duel.IsCanAddCounter

## Signature

```lua
Duel.IsCanAddCounter(int player, [int countertype], [int count], [Card c]) -> bool
```

## Description

With only player, checks whether player is not forbidden from placing counters.
With countertype, count, and c, checks player-wide counter placement restrictions for that card target. It does not replace Card.IsCanAddCounter; use the Card check when you need to confirm the card's permit, face-up state, location, and counter limit.

## Parameters

- `player` `int` - Player attempting to place counters.
- `countertype` `int` optional - Counter type to test when the card-target overload is used.
- `count` `int` optional - Number of counters to test when the card-target overload is used.
- `c` `Card` optional - Card target passed to player-level counter-placement restriction effects.

## Returns

- `bool` - true when the player-level placement check passes; this does not by itself prove c can hold or receive the counters.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4876`

## Guided Examples

Learn how to use this function in context:

- [Counters](/learn/counters)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **24** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.IsCanAddCounter) with `Duel.IsCanAddCounter`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Endymion, the Mighty Master of Magic | `3611830` | [Scripts/c3611830.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3611830.lua) | 1 |
| Reflection of Endymion | `39000945` | [Scripts/c39000945.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39000945.lua) | 2 |
| Magister of Endymion | `66104644` | [Scripts/c66104644.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66104644.lua) | 2 |
| Cubic Rebirth | `71442223` | [Scripts/c71442223.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71442223.lua) | 1 |
| Limit Code | `86607583` | [Scripts/c86607583.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c86607583.lua) | 1 |
| Servant of Endymion | `92559258` | [Scripts/c92559258.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92559258.lua) | 2 |
| Cubic Mandala | `8837932` | [Scripts/c8837932.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8837932.lua) | 1 |
| Mythical Beast Medusa | `54965929` | [Scripts/c54965929.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54965929.lua) | 1 |
| Forge a New Future | `27104921` | [Scripts/c27104921.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27104921.lua) | 1 |
| Summer Schoolwork Successful! | `77751766` | [Scripts/c77751766.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77751766.lua) | 1 |
| Link Turret | `55034079` | [Scripts/c55034079.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55034079.lua) | 1 |
| Ursarctic Radiation | `32692693` | [Scripts/c32692693.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32692693.lua) | 1 |
| Apocavities | `28531163` | [Scripts/c28531163.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28531163.lua) | 1 |
| Gouki Cage Match | `85638822` | [Scripts/c85638822.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85638822.lua) | 1 |
| Mythical Bestiary | `38325384` | [Scripts/c38325384.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38325384.lua) | 1 |
| Kaiju Capture Mission | `81057455` | [Scripts/c81057455.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81057455.lua) | 1 |
| War Rock Ordeal | `71331215` | [Scripts/c71331215.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71331215.lua) | 1 |
| Linkbelt Wall Dragon | `63092423` | [Scripts/c63092423.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63092423.lua) | 1 |
| Okiku's Dish Count | `89086647` | [Scripts/c89086647.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c89086647.lua) | 1 |
| Pitch-Black Power Stone | `34029630` | [Scripts/c34029630.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34029630.lua) | 1 |
| Battlewasp - Nest | `25221249` | [Scripts/c25221249.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25221249.lua) | 1 |
| Double Payback | `5914184` | [Scripts/c5914184.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5914184.lua) | 1 |
| Cauldron of the Old Man | `91740879` | [Scripts/c91740879.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c91740879.lua) | 1 |
| Gadget Box | `8025950` | [Scripts/c8025950.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8025950.lua) | 1 |

## Script Examples

### Endymion, the Mighty Master of Magic (`3611830`)

Source: [Scripts/c3611830.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3611830.lua)

```lua
	local c=e:GetHandler()
	if chk==0 then return Duel.GetLocationCount(tp,LOCATION_MZONE)>0 and c:IsCanBeSpecialSummoned(e,0,tp,false,false)
		and Duel.IsCanAddCounter(tp,0x1,1,c) end
	local g=Duel.GetMatchingGroup(nil,tp,LOCATION_ONFIELD,LOCATION_ONFIELD,nil)
	Duel.SetOperationInfo(0,CATEGORY_DESTROY,g,1,0,0)
```

### Reflection of Endymion (`39000945`)

Source: [Scripts/c39000945.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39000945.lua)

```lua
end
function c39000945.spfilter(c,e,tp)
	return c:IsCanHaveCounter(0x1) and Duel.IsCanAddCounter(tp,0x1,1,c) and c:IsCanBeSpecialSummoned(e,0,tp,false,false)
end
function c39000945.sptg(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Magister of Endymion (`66104644`)

Source: [Scripts/c66104644.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66104644.lua)

```lua
end
function c66104644.spfilter(c,e,tp)
	return c:IsFaceup() and c:IsCanHaveCounter(0x1) and Duel.IsCanAddCounter(tp,0x1,1,c)
		and c:IsCanBeSpecialSummoned(e,0,tp,false,false) and Duel.GetLocationCountFromEx(tp,tp,nil,c)>0
end
```
