# Auxiliary.AddBanishRedirect

## Signature

```lua
Auxiliary.AddBanishRedirect(Card c, [function condition]) -> void
```

## Description

If this face-up card would leave the field, banish it instead.

## Parameters

- `c` `Card`
- `condition` `function` optional

## Source

- `Utilities/utility.lua:1932`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **10** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.AddBanishRedirect`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Floowandereeze & Toccan | `17827173` | [Scripts/c17827173.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17827173.lua) | 42 |
| Exodius the Ultimate Forbidden Lord | `13893596` | [Scripts/c13893596.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13893596.lua) | 42 |
| Floowandereeze & Stri | `80433039` | [Scripts/c80433039.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80433039.lua) | 41 |
| Shell of Chaos | `77312273` | [Scripts/c77312273.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77312273.lua) | 39 |
| Core of Chaos | `3806388` | [Scripts/c3806388.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3806388.lua) | 39 |
| Dark Magician of Chaos | `40737112` | [Scripts/c40737112.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40737112.lua) | 39 |
| Floowandereeze & Eglen | `54334420` | [Scripts/c54334420.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54334420.lua) | 37 |
| Floowandereeze & Robina | `18940725` | [Scripts/c18940725.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18940725.lua) | 37 |
| Anchamoufrite | `52296675` | [Scripts/c52296675.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52296675.lua) | 30 |
| Cockadoodledoo | `42338879` | [Scripts/c42338879.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42338879.lua) | 14 |

## Script Examples

### Floowandereeze & Toccan (`17827173`)

Source: [Scripts/c17827173.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17827173.lua)

```lua
	c:RegisterEffect(e1)
	--redirect
	aux.AddBanishRedirect(c)
	--to hand(self)
	local e3=Effect.CreateEffect(c)
```

### Exodius the Ultimate Forbidden Lord (`13893596`)

Source: [Scripts/c13893596.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13893596.lua)

```lua
	c:RegisterEffect(e4)
	--redirect
	aux.AddBanishRedirect(c)
end
function c13893596.cfilter(c)
```

### Floowandereeze & Stri (`80433039`)

Source: [Scripts/c80433039.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80433039.lua)

```lua
	c:RegisterEffect(e1)
	--redirect
	aux.AddBanishRedirect(c)
	--to hand(self)
	local e3=Effect.CreateEffect(c)
```
