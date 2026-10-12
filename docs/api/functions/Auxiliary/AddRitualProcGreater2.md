# Auxiliary.AddRitualProcGreater2

## Signature

```lua
Auxiliary.AddRitualProcGreater2(Card c, function filter, [int summon_location], [function|nil grave_filter], [function|nil mat_filter], [bool pause], [function|nil extra_operation], [function|nil extra_target]) -> Effect
```

## Description

Adds a Ritual Summon effect for c that uses the Ritual Monster's current Level and requires materials whose total Level is greater than or equal to it.

## Parameters

- `c` `Card`
- `filter` `function`
- `summon_location` `int` optional
- `grave_filter` `function|nil` optional
- `mat_filter` `function|nil` optional
- `pause` `bool` optional
- `extra_operation` `function|nil` optional
- `extra_target` `function|nil` optional

## Returns

- `Effect` - The created Ritual Summon effect.

## Source

- `Utilities/procedure.lua:1934`

## Guided Examples

Learn how to use this function in context:

- [Ritual Procedure Guide](/learn/ritual-procedure)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **22** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.AddRitualProcGreater2) with `Auxiliary.AddRitualProcGreater2`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Mitsurugi Mirror](/examples/cards/49721684) | `49721684` | [Scripts/c49721684.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c49721684.lua) | 1 |
| [Revendread Origin](/examples/cards/94666032) | `94666032` | [Scripts/c94666032.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c94666032.lua) | 1 |
| [Recette de Viande (Meat Recipe)](/examples/cards/14166715) | `14166715` | [Scripts/c14166715.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c14166715.lua) | 1 |
| Megalith Aratron | `25726386` | [Scripts/c25726386.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c25726386.lua) | 1 |
| Megalith Phul | `78990927` | [Scripts/c78990927.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c78990927.lua) | 1 |
| Megalith Bethor | `99628747` | [Scripts/c99628747.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c99628747.lua) | 1 |
| Prayers of the Voiceless Voice | `52472775` | [Scripts/c52472775.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c52472775.lua) | 1 |
| Impcantation Inception | `86758915` | [Scripts/c86758915.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c86758915.lua) | 1 |
| Saffira, Dragon Queen of the Voiceless Voice | `51296484` | [Scripts/c51296484.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c51296484.lua) | 1 |
| Clown Crew Rehearsal | `20448151` | [Scripts/c20448151.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c20448151.lua) | 1 |
| Code Igniter | `5088741` | [Scripts/c5088741.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c5088741.lua) | 1 |
| Cynet Ritual | `34767865` | [Scripts/c34767865.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c34767865.lua) | 1 |
| Light and Darkness Ritual | `33599853` | [Scripts/c33599853.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c33599853.lua) | 1 |
| Libromancer Magigirl | `82128978` | [Scripts/c82128978.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c82128978.lua) | 1 |
| Libromancer First Appearance | `18890039` | [Scripts/c18890039.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c18890039.lua) | 1 |
| Megalith Phaleg | `63233638` | [Scripts/c63233638.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c63233638.lua) | 1 |
| Libromancer Bonded | `41085464` | [Scripts/c41085464.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c41085464.lua) | 1 |
| Machine Angel Ritual | `39996157` | [Scripts/c39996157.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c39996157.lua) | 1 |
| Dogmatikamacabre | `60921537` | [Scripts/c60921537.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c60921537.lua) | 1 |
| Recette de Poisson (Fish Recipe) | `87778106` | [Scripts/c87778106.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c87778106.lua) | 1 |
| Mikanko Kagura | `16310544` | [Scripts/c16310544.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c16310544.lua) | 1 |
| Rebirth of Nephthys | `23459650` | [Scripts/c23459650.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c23459650.lua) | 1 |

## Script Examples

### Mitsurugi Mirror (`49721684`)

Source: [Scripts/c49721684.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c49721684.lua)

```lua
	aux.AddCodeList(c,13332685,19899073,55397172)
	--Activate
	local e1=aux.AddRitualProcGreater2(c,s.spfilter,LOCATION_HAND+LOCATION_GRAVE,nil,s.mfilter,true)
	e1:SetCountLimit(1,id)
	c:RegisterEffect(e1)
```

### Revendread Origin (`94666032`)

Source: [Scripts/c94666032.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c94666032.lua)

```lua
function c94666032.initial_effect(c)
	aux.AddCodeList(c,4388680)
	aux.AddRitualProcGreater2(c,c94666032.filter,LOCATION_HAND+LOCATION_GRAVE,c94666032.mfilter)
	--destroy replace
	local e2=Effect.CreateEffect(c)
```

### Recette de Viande (Meat Recipe) (`14166715`)

Source: [Scripts/c14166715.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c14166715.lua)

```lua
function s.initial_effect(c)
	aux.AddCodeList(c,53618197)
	aux.AddRitualProcGreater2(c,s.filter,LOCATION_HAND,nil,nil,false,s.extraop)
end
function s.filter(c,e,tp)
```
