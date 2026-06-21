# Auxiliary.AddUrsarcticSpSummonEffect

## Signature

```lua
Auxiliary.AddUrsarcticSpSummonEffect(Card c) -> void
```

## Description

Adds the shared Ursarctic hand Quick Effect that Special Summons c during the Main Phase.
The cost releases a Level 7 or higher monster from the hand, or banishes a valid replacement card from the Graveyard.

## Parameters

- `c` `Card`

## Source

- `Utilities/utility.lua:938`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **6** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.AddUrsarcticSpSummonEffect`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Ursarctic Megatanus | `54700519` | [Scripts/c54700519.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54700519.lua) | 27 |
| Ursarctic Megapolar | `28715905` | [Scripts/c28715905.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28715905.lua) | 27 |
| Ursarctic Megabilis | `81108658` | [Scripts/c81108658.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81108658.lua) | 27 |
| Ursarctic Miktanus | `55936191` | [Scripts/c55936191.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55936191.lua) | 25 |
| Ursarctic Mikpolar | `29537493` | [Scripts/c29537493.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29537493.lua) | 22 |
| Ursarctic Mikbilis | `81321206` | [Scripts/c81321206.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81321206.lua) | 22 |

## Script Examples

### Ursarctic Megatanus (`54700519`)

Source: [Scripts/c54700519.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54700519.lua)

```lua
function c54700519.initial_effect(c)
	--spsummon
	local e1=aux.AddUrsarcticSpSummonEffect(c)
	e1:SetDescription(aux.Stringid(54700519,0))
	e1:SetCountLimit(1,54700519)
```

### Ursarctic Megapolar (`28715905`)

Source: [Scripts/c28715905.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28715905.lua)

```lua
function c28715905.initial_effect(c)
	--spsummon
	local e1=aux.AddUrsarcticSpSummonEffect(c)
	e1:SetDescription(aux.Stringid(28715905,0))
	e1:SetCountLimit(1,28715905)
```

### Ursarctic Megabilis (`81108658`)

Source: [Scripts/c81108658.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81108658.lua)

```lua
function c81108658.initial_effect(c)
	--spsummon
	local e1=aux.AddUrsarcticSpSummonEffect(c)
	e1:SetDescription(aux.Stringid(81108658,0))
	e1:SetCountLimit(1,81108658)
```
