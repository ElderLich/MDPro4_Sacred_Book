# Auxiliary.RegisterMergedDelayedEvent

## Signature

```lua
Auxiliary.RegisterMergedDelayedEvent(Card c, int code, int event, [Group|nil g]) -> void
```

## Description

Registers global listeners that merge multiple occurrences of event into one EVENT_CUSTOM+code event. The merged event is raised immediately outside a Chain, or at Chain End while in a Chain.

## Parameters

- `c` `Card`
- `code` `int`
- `event` `int`
- `g` `Group|nil` optional - Optional storage group; a kept-alive group is created when omitted.

## Source

- `Utilities/utility.lua:1650`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **11** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.RegisterMergedDelayedEvent) with `Auxiliary.RegisterMergedDelayedEvent`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Shadow Severing Strike | `57232301` | [Scripts/c57232301.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57232301.lua) | 1 |
| Heart of the Blue-Eyes | `54475145` | [Scripts/c54475145.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54475145.lua) | 2 |
| Red-Eyes Retro Dragon | `53485634` | [Scripts/c53485634.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53485634.lua) | 1 |
| Ghost Mourner &amp; Moonlit Chill | `52038441` | [Scripts/c52038441.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52038441.lua) | 1 |
| Maiden of Blue Tears | `99176254` | [Scripts/c99176254.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c99176254.lua) | 1 |
| Ebon Sun | `96029570` | [Scripts/c96029570.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96029570.lua) | 2 |
| Shining Sarcophagus | `79791878` | [Scripts/c79791878.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c79791878.lua) | 1 |
| Battlewasp Wind | `67441879` | [Scripts/c67441879.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67441879.lua) | 2 |
| Time Engine | `15216188` | [Scripts/c15216188.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15216188.lua) | 1 |
| Antidote Nurse | `31539614` | [Scripts/c31539614.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31539614.lua) | 1 |
| Monarchic Perfection | `59983249` | [Scripts/c59983249.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59983249.lua) | 1 |

## Script Examples

### Shadow Severing Strike (`57232301`)

Source: [Scripts/c57232301.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57232301.lua)

```lua
	c:RegisterEffect(e2)
	local g=Group.CreateGroup()
	aux.RegisterMergedDelayedEvent(c,id,EVENT_REMOVE,g)
	--tohand
	local e3=Effect.CreateEffect(c)
```

### Heart of the Blue-Eyes (`54475145`)

Source: [Scripts/c54475145.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54475145.lua)

```lua
	e3:SetOperation(s.spop)
	c:RegisterEffect(e3)
	aux.RegisterMergedDelayedEvent(c,id,EVENT_SUMMON_SUCCESS)
	aux.RegisterMergedDelayedEvent(c,id,EVENT_SPSUMMON_SUCCESS)
	if not s.global_check then
```

### Red-Eyes Retro Dragon (`53485634`)

Source: [Scripts/c53485634.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53485634.lua)

```lua
	e1:SetOperation(c53485634.spop)
	c:RegisterEffect(e1)
	aux.RegisterMergedDelayedEvent(c,53485634,EVENT_TO_GRAVE)
	--extra summon
	local e2=Effect.CreateEffect(c)
```
