# Auxiliary.AddRitualProcEqual2Code2

## Signature

```lua
Auxiliary.AddRitualProcEqual2Code2(Card c, any code1, any code2, any summon_location, any grave_filter, any mat_filter, Effect pause, any extra_operation, any extra_target) -> void
```

## Description

Add a Ritual Summon effect for c
code1, code2 are the card codes of the Ritual Monsters; the sum of the Levels of the materials must equal the Ritual Monster's Level
Equivalent to: aux.AddRitualProcEqual2(c, aux.FilterBoolFunction(Card.IsCode, code1, code2)), with fit_monster={code1, code2} added

## Parameters

- `c` `Card`
- `code1` `any`
- `code2` `any`
- `summon_location` `any`
- `grave_filter` `any`
- `mat_filter` `any`
- `pause` `Effect`
- `extra_operation` `any`
- `extra_target` `any`

## Source

- `Utilities/procedure.lua:1929`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.AddRitualProcEqual2Code2`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| End of the World | `8198712` | [Scripts/c8198712.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8198712.lua) | 1 |

## Script Examples

### End of the World (`8198712`)

Source: [Scripts/c8198712.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8198712.lua)

```lua
--エンド・オブ・ザ・ワールド
function c8198712.initial_effect(c)
	aux.AddRitualProcEqual2Code2(c,72426662,46427957)
end
```
