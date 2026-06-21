# Auxiliary.AddRitualProcEqual

## Signature

```lua
Auxiliary.AddRitualProcEqual(Card c, function filter, any summon_location, any grave_filter, any mat_filter, Effect pause, any extra_operation, any extra_target) -> void
```

## Description

Add a ritual summon effect to c
Filter for the ritual monster to meet the conditions, the material level must be equal to the ritual monster level

## Parameters

- `c` `Card`
- `filter` `function`
- `summon_location` `any`
- `grave_filter` `any`
- `mat_filter` `any`
- `pause` `Effect`
- `extra_operation` `any`
- `extra_target` `any`

## Source

- `Utilities/procedure.lua:1914`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.AddRitualProcEqual`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Super Soldier Ritual | `14094090` | [Scripts/c14094090.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c14094090.lua) | 28 |

## Script Examples

### Super Soldier Ritual (`14094090`)

Source: [Scripts/c14094090.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c14094090.lua)

```lua
--超戦士の儀式
function c14094090.initial_effect(c)
	aux.AddRitualProcEqual(c,c14094090.ritual_filter)
	--spsummon
	local e1=Effect.CreateEffect(c)
```
