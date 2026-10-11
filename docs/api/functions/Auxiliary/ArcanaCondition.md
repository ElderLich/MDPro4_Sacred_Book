# Auxiliary.ArcanaCondition

## Signature

```lua
Auxiliary.ArcanaCondition(Effect e) -> bool
```

## Description

Arcana Force condition helper that checks whether the handler has a stored Arcana coin-result flag.

## Parameters

- `e` `Effect`

## Returns

- `bool`

## Source

- `Utilities/utility.lua:304`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **3** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.ArcanaCondition) with `Auxiliary.ArcanaCondition`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Arcana Force 0 - The Fool | `62892347` | [Scripts/c62892347.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62892347.lua) | 3 |
| Arcana Force I - The Magician | `8396952` | [Scripts/c8396952.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8396952.lua) | 1 |
| Arcana Force IV - The Emperor | `61175706` | [Scripts/c61175706.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61175706.lua) | 1 |

## Script Examples

### Arcana Force 0 - The Fool (`62892347`)

Source: [Scripts/c62892347.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62892347.lua)

```lua
	e3:SetRange(LOCATION_MZONE)
	e3:SetTargetRange(LOCATION_ONFIELD,LOCATION_ONFIELD)
	e3:SetCondition(aux.ArcanaCondition)
	e3:SetTarget(c62892347.distg)
	c:RegisterEffect(e3)
```

### Arcana Force I - The Magician (`8396952`)

Source: [Scripts/c8396952.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8396952.lua)

```lua
	e1:SetCode(EVENT_CHAIN_SOLVED)
	e1:SetRange(LOCATION_MZONE)
	e1:SetCondition(aux.ArcanaCondition)
	e1:SetOperation(c8396952.speop)
	c:RegisterEffect(e1)
```

### Arcana Force IV - The Emperor (`61175706`)

Source: [Scripts/c61175706.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61175706.lua)

```lua
	e1:SetRange(LOCATION_MZONE)
	e1:SetTargetRange(LOCATION_MZONE,0)
	e1:SetCondition(aux.ArcanaCondition)
	e1:SetTarget(c61175706.atktg)
	e1:SetValue(c61175706.atkval)
```
