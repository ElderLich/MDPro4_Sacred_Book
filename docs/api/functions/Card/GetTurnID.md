# Card.GetTurnID

## Signature

```lua
Card.GetTurnID(Card c) -> int
```

## Description

Returns c's stored turn ID.
The core updates this value when the card is added to a location, so scripts commonly compare it with Duel.GetTurnCount() for same-turn timing checks.

## Parameters

- `c` `Card`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3479`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **51** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.GetTurnID`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Unchained Enma Lord Yama | `94014327` | [Scripts/c94014327.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c94014327.lua) | 52 |
| Cubic Mandala | `8837932` | [Scripts/c8837932.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8837932.lua) | 49 |
| Xyz Double Back | `57836546` | [Scripts/c57836546.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57836546.lua) | 49 |
| Diabrocken the Ominous Specter | `6083904` | [Scripts/c6083904.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6083904.lua) | 48 |
| Borrelguard Dragon | `68987122` | [Scripts/c68987122.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c68987122.lua) | 47 |
| Laundry Trap | `79371769` | [Scripts/c79371769.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c79371769.lua) | 45 |
| Vampire Scarlet Scourge | `79523365` | [Scripts/c79523365.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c79523365.lua) | 45 |
| Vampire Red Baron | `6917479` | [Scripts/c6917479.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6917479.lua) | 45 |
| Recovery Sorcerer | `76232522` | [Scripts/c76232522.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76232522.lua) | 45 |
| Vampire Fraulein | `6039967` | [Scripts/c6039967.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6039967.lua) | 44 |
| D/D/D Wave King Caesar | `3758046` | [Scripts/c3758046.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3758046.lua) | 44 |
| Fire Phoenix @Ignister | `24882256` | [Scripts/c24882256.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24882256.lua) | 43 |
| Officiating Reverie | `49828011` | [Scripts/c49828011.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49828011.lua) | 43 |
| Arkbrave Dragon | `33282498` | [Scripts/c33282498.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33282498.lua) | 40 |
| Number 92: Heart-eartH Dragon | `97403510` | [Scripts/c97403510.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97403510.lua) | 39 |
| Vampire Grimson | `33438666` | [Scripts/c33438666.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33438666.lua) | 39 |
| Kuribohrn | `78355370` | [Scripts/c78355370.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78355370.lua) | 38 |
| Dark Nephthys | `38107923` | [Scripts/c38107923.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38107923.lua) | 36 |
| Ixeep, Omen of the Ghoti | `3137279` | [Scripts/c3137279.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3137279.lua) | 36 |
| Battle of Sleeping Spirits | `46570372` | [Scripts/c46570372.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46570372.lua) | 36 |
| Number iC1000: Numerounius Numerounia | `15862758` | [Scripts/c15862758.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15862758.lua) | 35 |
| Fusion Recycling Plant | `22829942` | [Scripts/c22829942.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22829942.lua) | 35 |
| D.D. Telepon | `51701885` | [Scripts/c51701885.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c51701885.lua) | 34 |
| High Tide on Fire Island | `32542011` | [Scripts/c32542011.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32542011.lua) | 33 |
| ...and 27 more |  |  |  |

## Script Examples

### Unchained Enma Lord Yama (`94014327`)

Source: [Scripts/c94014327.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c94014327.lua)

```lua
end
function s.spfilter(c,e,tp,cid)
	return c:IsReason(REASON_DESTROY) and c:GetTurnID()==cid and c:IsRace(RACE_FIEND) and c:IsCanBeSpecialSummoned(e,0,tp,false,false)
end
function s.sptg(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
```

### Cubic Mandala (`8837932`)

Source: [Scripts/c8837932.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8837932.lua)

```lua
end
function c8837932.spfilter(c,e,tp,tid)
	return c:IsReason(REASON_DESTROY) and c:IsType(TYPE_MONSTER) and c:GetTurnID()==tid
		and c:IsCanBeSpecialSummoned(e,0,tp,false,false,POS_FACEUP,1-tp) and Duel.IsCanAddCounter(tp,0x1038,1,c)
end
```

### Xyz Double Back (`57836546`)

Source: [Scripts/c57836546.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57836546.lua)

```lua
function c57836546.filter1(c,e,tp,turn)
	return c:IsType(TYPE_XYZ) and c:IsReason(REASON_DESTROY) and c:IsPreviousControler(tp) and c:IsPreviousLocation(LOCATION_MZONE)
		and c:IsPreviousPosition(POS_FACEUP) and c:GetTurnID()==turn and c:IsCanBeSpecialSummoned(e,0,tp,false,false)
		and Duel.IsExistingTarget(c57836546.filter2,tp,LOCATION_GRAVE,0,1,c,e,tp,c:GetAttack())
end
```
