# Card.IsCanHaveCounter

## Signature

```lua
Card.IsCanHaveCounter(Card c, int countertype) -> bool
```

## Description

Checks whether c can hold counters of countertype.

## Parameters

- `c` `Card`
- `countertype` `int`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3637`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **9** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.IsCanHaveCounter`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Endymion, the Mighty Master of Magic | `3611830` | [Scripts/c3611830.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3611830.lua) | 56 |
| Reflection of Endymion | `39000945` | [Scripts/c39000945.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39000945.lua) | 53 |
| Magister of Endymion | `66104644` | [Scripts/c66104644.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66104644.lua) | 52 |
| Servant of Endymion | `92559258` | [Scripts/c92559258.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92559258.lua) | 50 |
| Mythical Beast Medusa | `54965929` | [Scripts/c54965929.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54965929.lua) | 48 |
| Mythical Institution | `94599451` | [Scripts/c94599451.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c94599451.lua) | 45 |
| Summer | `97254001` | [Scripts/c97254001.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97254001.lua) | 42 |
| Spring | `60600821` | [Scripts/c60600821.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60600821.lua) | 36 |
| Mythical Bestiary | `38325384` | [Scripts/c38325384.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38325384.lua) | 35 |

## Script Examples

### Endymion, the Mighty Master of Magic (`3611830`)

Source: [Scripts/c3611830.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3611830.lua)

```lua
end
function c3611830.cfilter(c)
	return c:IsCanHaveCounter(0x1)
end
function c3611830.destg(e,tp,eg,ep,ev,re,r,rp,chk)
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
