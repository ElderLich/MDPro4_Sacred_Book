# Auxiliary.AddFusionProcShaddoll

## Signature

```lua
Auxiliary.AddFusionProcShaddoll(Card c, int attr) -> void
```

## Description

Registers the Shaddoll Fusion Material procedure requiring one Shaddoll material and one material with attr as Fusion Attribute.

## Parameters

- `c` `Card`
- `attr` `int`

## Source

- `Utilities/procedure.lua:1342`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **7** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.AddFusionProcShaddoll`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Reeshaddoll Wendikuruhu | `8852158` | [Scripts/c8852158.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8852158.lua) | 43 |
| El Shaddoll Shekhinaga | `74822425` | [Scripts/c74822425.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74822425.lua) | 40 |
| El Shaddoll Construct | `20366274` | [Scripts/c20366274.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20366274.lua) | 38 |
| El Shaddoll Grysta | `48424886` | [Scripts/c48424886.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48424886.lua) | 37 |
| El Shaddoll Wendigo | `74009824` | [Scripts/c74009824.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74009824.lua) | 31 |
| El Shaddoll Winda | `94977269` | [Scripts/c94977269.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c94977269.lua) | 30 |
| El Shaddoll Anoyatyllis | `19261966` | [Scripts/c19261966.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c19261966.lua) | 30 |

## Script Examples

### Reeshaddoll Wendikuruhu (`8852158`)

Source: [Scripts/c8852158.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8852158.lua)

```lua
	c:EnableReviveLimit()
	--fusion
	aux.AddFusionProcShaddoll(c,ATTRIBUTE_WIND)
	--cannot spsummon
	local e1=Effect.CreateEffect(c)
```

### El Shaddoll Shekhinaga (`74822425`)

Source: [Scripts/c74822425.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74822425.lua)

```lua
	--fusion material
	c:EnableReviveLimit()
	aux.AddFusionProcShaddoll(c,ATTRIBUTE_EARTH)
	--cannot spsummon
	local e2=Effect.CreateEffect(c)
```

### El Shaddoll Construct (`20366274`)

Source: [Scripts/c20366274.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20366274.lua)

```lua
	--fusion material
	c:EnableReviveLimit()
	aux.AddFusionProcShaddoll(c,ATTRIBUTE_LIGHT)
	--cannot spsummon
	local e2=Effect.CreateEffect(c)
```
