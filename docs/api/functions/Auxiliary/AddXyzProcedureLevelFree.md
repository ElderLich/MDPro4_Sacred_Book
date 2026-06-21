# Auxiliary.AddXyzProcedureLevelFree

## Signature

```lua
Auxiliary.AddXyzProcedureLevelFree(Card c, [function|nil f], [function|nil gf], int minc, int maxc, [function alterf], [string alterdesc], [function alterop]) -> void
```

## Description

Add an Xyz Summon procedure for c
Use minc \[to maxc\] monsters satisfying condition f, and within the group satisfying condition gf, for overlay; f is a required condition, gf is an additional condition
Or overlay on a single monster (typically an Xyz Monster)
alterf is the condition this monster must satisfy, desc is the description, op is the operation required during overlay (e.g., Number F0: Utopic Future)

## Parameters

- `c` `Card`
- `f` `function|nil` optional
- `gf` `function|nil` optional
- `minc` `int`
- `maxc` `int`
- `alterf` `function` optional
- `alterdesc` `string` optional
- `alterop` `function` optional

## Source

- `Utilities/procedure.lua:700`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **13** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.AddXyzProcedureLevelFree`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Exosisters Magnifica | `59242457` | [Scripts/c59242457.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59242457.lua) | 56 |
| Number 93: Utopia Kaiser | `23187256` | [Scripts/c23187256.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23187256.lua) | 52 |
| Disaster, Dragon Ruler of All Apocalypses | `67359907` | [Scripts/c67359907.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67359907.lua) | 51 |
| Number 100: Numeron Dragon | `57314798` | [Scripts/c57314798.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57314798.lua) | 45 |
| Rilliona, the Wondrous Magistus Witch Wardrobe | `74689476` | [Scripts/c74689476.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74689476.lua) | 44 |
| Eclipse Twins | `45852939` | [Scripts/c45852939.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45852939.lua) | 44 |
| Number F0: Utopic Future Zexal | `41522092` | [Scripts/c41522092.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41522092.lua) | 43 |
| Number S0: Utopic ZEXAL | `52653092` | [Scripts/c52653092.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52653092.lua) | 36 |
| Gigantic Spright | `54498517` | [Scripts/c54498517.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54498517.lua) | 35 |
| Virtual World Dragon - Longlong | `61641818` | [Scripts/c61641818.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61641818.lua) | 35 |
| Number F0: Utopic Draco Future | `26973555` | [Scripts/c26973555.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c26973555.lua) | 33 |
| Number F0: Utopic Future | `65305468` | [Scripts/c65305468.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65305468.lua) | 29 |
| Number F0: Utopic Future Slash | `43490025` | [Scripts/c43490025.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43490025.lua) | 29 |

## Script Examples

### Exosisters Magnifica (`59242457`)

Source: [Scripts/c59242457.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59242457.lua)

```lua
	--xyz summon
	c:EnableReviveLimit()
	aux.AddXyzProcedureLevelFree(c,c59242457.mfilter,nil,2,2)
	--spsummon condition
	local e1=Effect.CreateEffect(c)
```

### Number 93: Utopia Kaiser (`23187256`)

Source: [Scripts/c23187256.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23187256.lua)

```lua
	--xyz summon
	c:EnableReviveLimit()
	aux.AddXyzProcedureLevelFree(c,c23187256.mfilter,c23187256.xyzcheck,2,99)
	--spsummon
	local e2=Effect.CreateEffect(c)
```

### Disaster, Dragon Ruler of All Apocalypses (`67359907`)

Source: [Scripts/c67359907.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67359907.lua)

```lua
	--xyz summon
	c:EnableReviveLimit()
	aux.AddXyzProcedureLevelFree(c,s.mfilter,nil,2,2)
	--material
	local e1=Effect.CreateEffect(c)
```
