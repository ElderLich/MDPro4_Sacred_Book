# Card.IsTuner

## Signature

```lua
Card.IsTuner(Card c, Card scard) -> bool
```

## Description

Checks whether c is a Tuner monster for scard.
Besides TYPE_TUNER, this also checks effects that can make c be treated as a Tuner.

## Parameters

- `c` `Card`
- `scard` `Card`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3561`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **15** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.IsTuner) with `Card.IsTuner`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Nirvana High Paladin | `80896940` | [Scripts/c80896940.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80896940.lua) | 1 |
| Cupid Pitch | `21915012` | [Scripts/c21915012.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21915012.lua) | 1 |
| Red Hypernova Dragon | `30698243` | [Scripts/c30698243.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30698243.lua) | 1 |
| Majestic Star Dragon | `7841112` | [Scripts/c7841112.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7841112.lua) | 2 |
| Crystal Clear Wing Over Synchro Dragon | `84343351` | [Scripts/c84343351.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84343351.lua) | 1 |
| Chaos Angel | `22850702` | [Scripts/c22850702.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22850702.lua) | 1 |
| Lollipo★Yummy Way | `93192592` | [Scripts/c93192592.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93192592.lua) | 1 |
| Ghoti of the Deep Beyond | `72309040` | [Scripts/c72309040.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c72309040.lua) | 1 |
| Majestic Red Dragon | `67030233` | [Scripts/c67030233.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67030233.lua) | 2 |
| Cupsy★Yummy Way | `31603289` | [Scripts/c31603289.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31603289.lua) | 1 |
| Cooky★Yummy Way | `67098897` | [Scripts/c67098897.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67098897.lua) | 1 |
| Junora the Power Patron of Tuning | `5914858` | [Scripts/c5914858.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5914858.lua) | 1 |
| Vagnawa the Moon-Eating Dragon | `9839115` | [Scripts/c9839115.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9839115.lua) | 1 |
| Ib the World Chalice Justiciar | `94677445` | [Scripts/c94677445.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c94677445.lua) | 1 |
| Cyber Slash Harpie Lady | `63261835` | [Scripts/c63261835.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63261835.lua) | 1 |

## Script Examples

### Nirvana High Paladin (`80896940`)

Source: [Scripts/c80896940.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80896940.lua)

```lua
c80896940.material_type=TYPE_SYNCHRO
function c80896940.matfilter1(c,syncard)
	return c:IsTuner(syncard) or (c:IsType(TYPE_PENDULUM) and c:IsSummonType(SUMMON_TYPE_PENDULUM))
end
function c80896940.indcon(e,tp,eg,ep,ev,re,r,rp)
```

### Cupid Pitch (`21915012`)

Source: [Scripts/c21915012.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21915012.lua)

```lua
function c21915012.valcheck(e,c)
	local g=c:GetMaterial()
	local mg=g:Filter(Card.IsTuner,nil,c)
	local tc=mg:GetFirst()
	if not tc then
```

### Red Hypernova Dragon (`30698243`)

Source: [Scripts/c30698243.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30698243.lua)

```lua
	local rg=mg-c
	if c:IsNotTuner(syncard) and c:IsSynchroType(TYPE_SYNCHRO) then
		return rg:FilterCount(Card.IsTuner,nil,syncard)==4
	else
		return false
```
