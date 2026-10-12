# Card.IsNotTuner

## Signature

```lua
Card.IsNotTuner(Card c, Card scard) -> bool
```

## Description

Checks whether c is treated as a non-Tuner for Synchro Monster scard.

## Parameters

- `c` `Card`
- `scard` `Card`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3560`

## Guided Examples

Learn how to use this function in context:

- [Synchro Procedure Guide](/learn/synchro-procedure)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **10** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.IsNotTuner) with `Card.IsNotTuner`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Shooting Majestic Star Dragon](/examples/cards/40939228) | `40939228` | [Scripts/c40939228.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c40939228.lua) | 1 |
| Cupid Pitch | `21915012` | [Scripts/c21915012.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c21915012.lua) | 1 |
| Red Hypernova Dragon | `30698243` | [Scripts/c30698243.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c30698243.lua) | 1 |
| Chaos Angel | `22850702` | [Scripts/c22850702.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c22850702.lua) | 1 |
| T.G. Cyber Magician | `64910482` | [Scripts/c64910482.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c64910482.lua) | 2 |
| Lollipo★Yummy Way | `93192592` | [Scripts/c93192592.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c93192592.lua) | 1 |
| Ghoti of the Deep Beyond | `72309040` | [Scripts/c72309040.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c72309040.lua) | 1 |
| Cupsy★Yummy Way | `31603289` | [Scripts/c31603289.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c31603289.lua) | 1 |
| Cooky★Yummy Way | `67098897` | [Scripts/c67098897.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c67098897.lua) | 1 |
| Vagnawa the Moon-Eating Dragon | `9839115` | [Scripts/c9839115.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c9839115.lua) | 1 |

## Script Examples

### Shooting Majestic Star Dragon (`40939228`)

Source: [Scripts/c40939228.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c40939228.lua)

```lua
c40939228.material_type=TYPE_SYNCHRO
function c40939228.cfilter(c,syncard)
	return c:IsRace(RACE_DRAGON) and c:IsSynchroType(TYPE_SYNCHRO) and c:IsNotTuner(syncard)
end
function c40939228.syncheck(g,syncard)
```

### Cupid Pitch (`21915012`)

Source: [Scripts/c21915012.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c21915012.lua)

```lua
	end
	if #mg>1 then
		local tg=g-(g:Filter(Card.IsNotTuner,nil,c))
		if #tg>0 then
			tc=tg:GetFirst()
```

### Red Hypernova Dragon (`30698243`)

Source: [Scripts/c30698243.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c30698243.lua)

```lua
function s.mgcheck(c,mg,syncard)
	local rg=mg-c
	if c:IsNotTuner(syncard) and c:IsSynchroType(TYPE_SYNCHRO) then
		return rg:FilterCount(Card.IsTuner,nil,syncard)==4
	else
```
