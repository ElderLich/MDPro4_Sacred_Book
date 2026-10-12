# Auxiliary.AddRitualProcEqualCode

## Signature

```lua
Auxiliary.AddRitualProcEqualCode(Card c, int code1, [int summon_location], [function grave_filter], [function mat_filter], [bool pause], [function extra_operation], [function extra_target]) -> Effect
```

## Description

Creates a Ritual Summon activation effect for Ritual Monster code1.
The selected materials' Ritual Levels must exactly equal the Ritual Monster's original Level, and optional Graveyard material, material filter, and extra callbacks are forwarded to the shared Ritual procedure.

## Parameters

- `c` `Card`
- `code1` `int`
- `summon_location` `int` optional - default: LOCATION_HAND
- `grave_filter` `function` optional
- `mat_filter` `function` optional
- `pause` `bool` optional
- `extra_operation` `function` optional
- `extra_target` `function` optional

## Returns

- `Effect` - Created Ritual Summon activation effect.

## Source

- `Utilities/procedure.lua:1917`

## Guided Examples

Learn how to use this function in context:

- [Ritual Procedure Guide](/learn/ritual-procedure)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **3** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.AddRitualProcEqualCode) with `Auxiliary.AddRitualProcEqualCode`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Dawn of the Herald | `27383110` | [Scripts/c27383110.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c27383110.lua) | 1 |
| Luminous Dragon Ritual | `34834619` | [Scripts/c34834619.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c34834619.lua) | 1 |
| Amorphous Persona | `23160024` | [Scripts/c23160024.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c23160024.lua) | 1 |

## Script Examples

### Dawn of the Herald (`27383110`)

Source: [Scripts/c27383110.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c27383110.lua)

```lua
function c27383110.initial_effect(c)
	--Activate
	aux.AddRitualProcEqualCode(c,44665365,nil,nil,nil,false,c27383110.extraop)
	--salvage
	local e2=Effect.CreateEffect(c)
```

### Luminous Dragon Ritual (`34834619`)

Source: [Scripts/c34834619.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c34834619.lua)

```lua
--光子竜降臨
function c34834619.initial_effect(c)
	aux.AddRitualProcEqualCode(c,85346853)
	--spsummon
	local e1=Effect.CreateEffect(c)
```

### Amorphous Persona (`23160024`)

Source: [Scripts/c23160024.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c23160024.lua)

```lua
	c:RegisterEffect(e4)
	--ritural
	local e5=aux.AddRitualProcEqualCode(c,98287529,nil,nil,c23160024.mfilter,true)
	e5:SetType(EFFECT_TYPE_IGNITION)
	e5:SetCode(0)
```
