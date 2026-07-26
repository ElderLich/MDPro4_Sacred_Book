# Card.IsXyzType

## Signature

```lua
Card.IsXyzType(Card c, int type) -> bool
```

## Description

Checks whether c's type while used as Xyz Material contains type.

## Parameters

- `c` `Card`
- `type` `int`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3488`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **24** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.IsXyzType`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Number 93: Utopia Kaiser | `23187256` | [Scripts/c23187256.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23187256.lua) | 1 |
| Disaster, Dragon Ruler of All Apocalypses | `67359907` | [Scripts/c67359907.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67359907.lua) | 1 |
| Pendulum Dimension | `84274024` | [Scripts/c84274024.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84274024.lua) | 1 |
| Exstellarknight Constellar Ptolemy Ω7 | `6195332` | [Scripts/c6195332.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6195332.lua) | 1 |
| Oracle of Zefra | `32354768` | [Scripts/c32354768.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32354768.lua) | 1 |
| Odd-Eyes Rebellion Xyz Dragon | `30095833` | [Scripts/c30095833.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30095833.lua) | 1 |
| Number 100: Numeron Dragon | `57314798` | [Scripts/c57314798.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57314798.lua) | 1 |
| Digital Bug Corebage | `58600555` | [Scripts/c58600555.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58600555.lua) | 1 |
| Rilliona, the Wondrous Magistus Witch Wardrobe | `74689476` | [Scripts/c74689476.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74689476.lua) | 1 |
| Number F0: Utopic Future Zexal | `41522092` | [Scripts/c41522092.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41522092.lua) | 1 |
| Supreme King Dragon Dark Rebellion | `42160203` | [Scripts/c42160203.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42160203.lua) | 1 |
| Vola-Chemicritter Methydraco | `38026562` | [Scripts/c38026562.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38026562.lua) | 1 |
| Timestar Magician | `47349116` | [Scripts/c47349116.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c47349116.lua) | 1 |
| Number S0: Utopic ZEXAL | `52653092` | [Scripts/c52653092.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52653092.lua) | 1 |
| Right-Hand Shark | `11845050` | [Scripts/c11845050.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11845050.lua) | 1 |
| Majester Paladin, the Ascending Dracoslayer | `88722973` | [Scripts/c88722973.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88722973.lua) | 1 |
| Virtual World Dragon - Longlong | `61641818` | [Scripts/c61641818.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61641818.lua) | 1 |
| Number F0: Utopic Draco Future | `26973555` | [Scripts/c26973555.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c26973555.lua) | 1 |
| Digital Bug Rhinosebus | `85004150` | [Scripts/c85004150.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85004150.lua) | 1 |
| Left-Hand Shark | `47840168` | [Scripts/c47840168.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c47840168.lua) | 1 |
| Number F0: Utopic Future | `65305468` | [Scripts/c65305468.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65305468.lua) | 1 |
| Number F0: Utopic Future Slash | `43490025` | [Scripts/c43490025.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43490025.lua) | 1 |
| Number 21: Frozen Lady Justice | `57707471` | [Scripts/c57707471.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57707471.lua) | 1 |
| Thunder End Dragon | `698785` | [Scripts/c698785.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c698785.lua) | 1 |

## Script Examples

### Number 93: Utopia Kaiser (`23187256`)

Source: [Scripts/c23187256.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23187256.lua)

```lua
aux.xyz_number[23187256]=93
function c23187256.mfilter(c,xyzc)
	return c:IsXyzType(TYPE_XYZ) and c:IsSetCard(0x48) and c:GetOverlayCount()>0
end
function c23187256.xyzcheck(g)
```

### Disaster, Dragon Ruler of All Apocalypses (`67359907`)

Source: [Scripts/c67359907.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67359907.lua)

```lua
end
function s.mfilter(c,xyzc)
	return c:IsXyzType(TYPE_XYZ) and c:IsRank(7)
end
function s.matfilter(c)
```

### Pendulum Dimension (`84274024`)

Source: [Scripts/c84274024.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84274024.lua)

```lua
	if c:IsType(TYPE_FUSION) and g:IsExists(Card.IsFusionType,1,nil,TYPE_PENDULUM)
		or c:IsType(TYPE_SYNCHRO) and g:IsExists(Card.IsSynchroType,1,nil,TYPE_PENDULUM)
		or c:IsType(TYPE_XYZ) and g:IsExists(Card.IsXyzType,1,nil,TYPE_PENDULUM) then
		c:RegisterFlagEffect(84274024,RESET_EVENT+0x4fe0000+RESET_PHASE+PHASE_END,0,1)
	end
```
