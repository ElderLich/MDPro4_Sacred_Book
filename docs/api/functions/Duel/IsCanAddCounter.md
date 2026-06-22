# Duel.IsCanAddCounter

## Signature

```lua
Duel.IsCanAddCounter(int player, [int countertype], [int count], [Card c]) -> bool
```

## Description

With only player, checks whether player is not forbidden from placing counters.
With countertype, count, and c, checks whether player can place that many counters of countertype on c.

## Parameters

- `player` `int`
- `countertype` `int` optional
- `count` `int` optional
- `c` `Card` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4876`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **24** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.IsCanAddCounter`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Endymion, the Mighty Master of Magic | `3611830` | [Scripts/c3611830.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3611830.lua) | 56 |
| Reflection of Endymion | `39000945` | [Scripts/c39000945.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39000945.lua) | 53 |
| Magister of Endymion | `66104644` | [Scripts/c66104644.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66104644.lua) | 52 |
| Cubic Rebirth | `71442223` | [Scripts/c71442223.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71442223.lua) | 52 |
| Limit Code | `86607583` | [Scripts/c86607583.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c86607583.lua) | 51 |
| Servant of Endymion | `92559258` | [Scripts/c92559258.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92559258.lua) | 50 |
| Cubic Mandala | `8837932` | [Scripts/c8837932.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8837932.lua) | 49 |
| Mythical Beast Medusa | `54965929` | [Scripts/c54965929.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54965929.lua) | 48 |
| Forge a New Future | `27104921` | [Scripts/c27104921.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27104921.lua) | 47 |
| Summer Schoolwork Successful! | `77751766` | [Scripts/c77751766.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77751766.lua) | 45 |
| Link Turret | `55034079` | [Scripts/c55034079.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55034079.lua) | 42 |
| Ursarctic Radiation | `32692693` | [Scripts/c32692693.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32692693.lua) | 42 |
| Apocavities | `28531163` | [Scripts/c28531163.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28531163.lua) | 40 |
| Gouki Cage Match | `85638822` | [Scripts/c85638822.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85638822.lua) | 40 |
| Mythical Bestiary | `38325384` | [Scripts/c38325384.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38325384.lua) | 35 |
| Kaiju Capture Mission | `81057455` | [Scripts/c81057455.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81057455.lua) | 35 |
| War Rock Ordeal | `71331215` | [Scripts/c71331215.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71331215.lua) | 33 |
| Linkbelt Wall Dragon | `63092423` | [Scripts/c63092423.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63092423.lua) | 32 |
| Okiku's Dish Count | `89086647` | [Scripts/c89086647.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c89086647.lua) | 32 |
| Pitch-Black Power Stone | `34029630` | [Scripts/c34029630.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34029630.lua) | 32 |
| Battlewasp - Nest | `25221249` | [Scripts/c25221249.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25221249.lua) | 30 |
| Double Payback | `5914184` | [Scripts/c5914184.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5914184.lua) | 30 |
| Cauldron of the Old Man | `91740879` | [Scripts/c91740879.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c91740879.lua) | 29 |
| Gadget Box | `8025950` | [Scripts/c8025950.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8025950.lua) | 27 |

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
