# Auxiliary.EnableExtraDeckSummonCountLimit

## Signature

```lua
Auxiliary.EnableExtraDeckSummonCountLimit() -> void
```

## Description

Initializes the shared Extra Deck Summon count table with one count for each player and registers a global Draw Phase Start reset. The helper only manages the counter; individual card scripts still check and decrement it.

## Source

- `Utilities/utility.lua:482`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **5** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.EnableExtraDeckSummonCountLimit`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Numbers Last Hope | `4606229` | [Scripts/c4606229.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4606229.lua) | 1 |
| Mystical Celtic Sage | `50073633` | [Scripts/c50073633.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50073633.lua) | 1 |
| Additional Mirror Level 7 | `23812568` | [Scripts/c23812568.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23812568.lua) | 1 |
| Fury of Fire | `92345028` | [Scripts/c92345028.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92345028.lua) | 1 |
| Squeaknight | `38783169` | [Scripts/c38783169.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38783169.lua) | 1 |

## Script Examples

### Numbers Last Hope (`4606229`)

Source: [Scripts/c4606229.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4606229.lua)

```lua
local s,id,o=GetID()
function s.initial_effect(c)
	aux.EnableExtraDeckSummonCountLimit()
	--Activate
	local e1=Effect.CreateEffect(c)
```

### Mystical Celtic Sage (`50073633`)

Source: [Scripts/c50073633.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50073633.lua)

```lua
local s,id,o=GetID()
function s.initial_effect(c)
	aux.EnableExtraDeckSummonCountLimit()
	aux.AddCodeList(c,33599853)
	--special summon
```

### Additional Mirror Level 7 (`23812568`)

Source: [Scripts/c23812568.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23812568.lua)

```lua
--アディショナル・ミラー・レベル7
function c23812568.initial_effect(c)
	aux.EnableExtraDeckSummonCountLimit()
	--Activate
	local e1=Effect.CreateEffect(c)
```
