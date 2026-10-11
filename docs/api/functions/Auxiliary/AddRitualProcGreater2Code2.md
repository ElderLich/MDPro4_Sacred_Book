# Auxiliary.AddRitualProcGreater2Code2

## Signature

```lua
Auxiliary.AddRitualProcGreater2Code2(Card c, int code1, int code2, [int summon_location], [function|nil grave_filter], [function|nil mat_filter], [bool pause], [function|nil extra_operation], [function|nil extra_target]) -> Effect
```

## Description

Registers code1 and code2 as listed by c, then adds the Greater2 Ritual procedure restricted to Ritual Monsters with either code.

## Parameters

- `c` `Card`
- `code1` `int`
- `code2` `int`
- `summon_location` `int` optional
- `grave_filter` `function|nil` optional
- `mat_filter` `function|nil` optional
- `pause` `bool` optional
- `extra_operation` `function|nil` optional
- `extra_target` `function|nil` optional

## Returns

- `Effect` - The created Ritual Summon effect.

## Source

- `Utilities/procedure.lua:1941`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **3** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.AddRitualProcGreater2Code2) with `Auxiliary.AddRitualProcGreater2Code2`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Cycle of the World | `32828635` | [Scripts/c32828635.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32828635.lua) | 1 |
| Turning of the World | `95612049` | [Scripts/c95612049.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95612049.lua) | 1 |
| Shinobird's Calling | `73055622` | [Scripts/c73055622.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c73055622.lua) | 1 |

## Script Examples

### Cycle of the World (`32828635`)

Source: [Scripts/c32828635.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32828635.lua)

```lua
function c32828635.initial_effect(c)
	aux.AddCodeList(c,8198712,46427957,72426662)
	aux.AddRitualProcGreater2Code2(c,46427957,72426662,nil,nil,c32828635.mfilter)
	--salvage
	local e2=Effect.CreateEffect(c)
```

### Turning of the World (`95612049`)

Source: [Scripts/c95612049.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95612049.lua)

```lua
function c95612049.initial_effect(c)
	--Activate
	local e1=aux.AddRitualProcGreater2Code2(c,46427957,72426662,LOCATION_HAND+LOCATION_DECK,nil,c95612049.mfilter,true)
	e1:SetCountLimit(1,95612049+EFFECT_COUNT_CODE_OATH)
	c:RegisterEffect(e1)
```

### Shinobird's Calling (`73055622`)

Source: [Scripts/c73055622.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c73055622.lua)

```lua
--霊魂の降神
function c73055622.initial_effect(c)
	aux.AddRitualProcGreater2Code2(c,25415052,52900000,nil,c73055622.mfilter)
end
c73055622.has_text_type=TYPE_SPIRIT
```
