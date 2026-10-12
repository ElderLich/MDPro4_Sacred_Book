# Auxiliary.AddRitualProcEqual

## Signature

```lua
Auxiliary.AddRitualProcEqual(Card c, function filter, any summon_location, any grave_filter, any mat_filter, Effect pause, any extra_operation, any extra_target) -> void
```

## Description

Creates a Ritual Summon activation effect whose selected materials' Ritual Levels must exactly equal the Ritual Monster's original Level.

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

## Guided Examples

Learn how to use this function in context:

- [Ritual Procedure Guide](/learn/ritual-procedure)
- [Ritual Summon Choices](/learn/ritual-summon-choices)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.AddRitualProcEqual) with `Auxiliary.AddRitualProcEqual`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Super Soldier Ritual](/examples/cards/14094090) | `14094090` | [Scripts/c14094090.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c14094090.lua) | 1 |

## Script Examples

### Super Soldier Ritual (`14094090`)

Source: [Scripts/c14094090.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c14094090.lua)

```lua
--超戦士の儀式
function c14094090.initial_effect(c)
	aux.AddRitualProcEqual(c,c14094090.ritual_filter)
	--spsummon
	local e1=Effect.CreateEffect(c)
```
