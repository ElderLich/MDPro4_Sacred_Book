# Auxiliary.AddRitualProcEqualCode

## Signature

```lua
Auxiliary.AddRitualProcEqualCode(Card c, any code1, any summon_location, any grave_filter, any mat_filter, Effect pause, any extra_operation, any extra_target) -> void
```

## Description

Add a Ritual Summon effect for c
code is the card code of the Ritual Monster; the sum of the Ritual Levels of the materials must equal the original Level of the Ritual Monster
Equivalent to: aux.AddRitualProcEqual(c, aux.FilterBoolFunction(Card.IsCode, code)), with fit_monster=code added

## Parameters

- `c` `Card`
- `code1` `any`
- `summon_location` `any`
- `grave_filter` `any`
- `mat_filter` `any`
- `pause` `Effect`
- `extra_operation` `any`
- `extra_target` `any`

## Source

- `Utilities/procedure.lua:1917`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **3** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.AddRitualProcEqualCode`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Dawn of the Herald | `27383110` | [Scripts/c27383110.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27383110.lua) | 39 |
| Luminous Dragon Ritual | `34834619` | [Scripts/c34834619.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34834619.lua) | 33 |
| Amorphous Persona | `23160024` | [Scripts/c23160024.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23160024.lua) | 28 |

## Script Examples

### Dawn of the Herald (`27383110`)

Source: [Scripts/c27383110.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27383110.lua)

```lua
function c27383110.initial_effect(c)
	--Activate
	aux.AddRitualProcEqualCode(c,44665365,nil,nil,nil,false,c27383110.extraop)
	--salvage
	local e2=Effect.CreateEffect(c)
```

### Luminous Dragon Ritual (`34834619`)

Source: [Scripts/c34834619.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34834619.lua)

```lua
--光子竜降臨
function c34834619.initial_effect(c)
	aux.AddRitualProcEqualCode(c,85346853)
	--spsummon
	local e1=Effect.CreateEffect(c)
```

### Amorphous Persona (`23160024`)

Source: [Scripts/c23160024.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23160024.lua)

```lua
	c:RegisterEffect(e4)
	--ritural
	local e5=aux.AddRitualProcEqualCode(c,98287529,nil,nil,c23160024.mfilter,true)
	e5:SetType(EFFECT_TYPE_IGNITION)
	e5:SetCode(0)
```
