# Auxiliary.AddSynchroMixProcedure

## Signature

```lua
Auxiliary.AddSynchroMixProcedure(Card c, [function|nil f1], [function|nil f2], [function|nil f3], [function|nil f4], int minc, int maxc, [function gc]) -> void
```

## Description

Add a Synchro Summon procedure for c
f1, f2, f3 are filter conditions satisfied by 1 card each, f4 is a filter condition satisfied by minc \[to maxc\] cards
At least one of f1, f2, f3, f4 must be a Tuner condition
If f2 and f3 are nil, equivalent to aux.AddSynchroProcedure(c, f1, f4, minc\[, maxc\])

## Parameters

- `c` `Card`
- `f1` `function|nil` optional
- `f2` `function|nil` optional
- `f3` `function|nil` optional
- `f4` `function|nil` optional
- `minc` `int`
- `maxc` `int`
- `gc` `function` optional

## Source

- `Utilities/procedure.lua:135`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **35** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.AddSynchroMixProcedure`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Shooting Majestic Star Dragon](/examples/cards/40939228) | `40939228` | [Scripts/c40939228.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40939228.lua) | 62 |
| Red Nova Dragon - Burning Soul | `65541655` | [Scripts/c65541655.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65541655.lua) | 57 |
| Kewl Tune Crackle | `39576656` | [Scripts/c39576656.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39576656.lua) | 56 |
| Nirvana High Paladin | `80896940` | [Scripts/c80896940.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80896940.lua) | 55 |
| Kewl Tune Remix | `88170262` | [Scripts/c88170262.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88170262.lua) | 54 |
| Red Hypernova Dragon | `30698243` | [Scripts/c30698243.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30698243.lua) | 53 |
| Kewl Tune B2B | `65961304` | [Scripts/c65961304.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65961304.lua) | 52 |
| X-Saber Gottoms | `8252010` | [Scripts/c8252010.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8252010.lua) | 52 |
| Commander Souza, Swordmaster | `72867001` | [Scripts/c72867001.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c72867001.lua) | 51 |
| Majestic Star Dragon | `7841112` | [Scripts/c7841112.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7841112.lua) | 49 |
| Red Supernova Dragon | `99585850` | [Scripts/c99585850.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c99585850.lua) | 48 |
| Kewl Tune RS | `15665977` | [Scripts/c15665977.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15665977.lua) | 48 |
| Crystal Clear Wing Over Synchro Dragon | `84343351` | [Scripts/c84343351.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84343351.lua) | 47 |
| Mannadium Prime-Heart | `90465153` | [Scripts/c90465153.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90465153.lua) | 47 |
| Chaos Angel | `22850702` | [Scripts/c22850702.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22850702.lua) | 47 |
| Blue-Eyes Ultimate Spirit Dragon | `89604813` | [Scripts/c89604813.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c89604813.lua) | 44 |
| Lollipo★Yummy Way | `93192592` | [Scripts/c93192592.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93192592.lua) | 44 |
| Vylon Omega | `93157004` | [Scripts/c93157004.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93157004.lua) | 44 |
| Ghoti of the Deep Beyond | `72309040` | [Scripts/c72309040.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c72309040.lua) | 44 |
| Hot Red Dragon Archfiend King Calamity | `62242678` | [Scripts/c62242678.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62242678.lua) | 43 |
| Majestic Red Dragon | `67030233` | [Scripts/c67030233.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67030233.lua) | 43 |
| Cupsy★Yummy Way | `31603289` | [Scripts/c31603289.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31603289.lua) | 43 |
| Judgment, the Dragon of Heaven | `41659072` | [Scripts/c41659072.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41659072.lua) | 43 |
| Cooky★Yummy Way | `67098897` | [Scripts/c67098897.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67098897.lua) | 42 |
| ...and 11 more |  |  |  |

## Script Examples

### Shooting Majestic Star Dragon (`40939228`)

Source: [Scripts/c40939228.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40939228.lua)

```lua
	aux.AddCodeList(c,44508094)
	--synchro summon
	aux.AddSynchroMixProcedure(c,aux.Tuner(Card.IsCode,21159309),nil,nil,aux.NonTuner(nil),1,99,c40939228.syncheck)
	c:EnableReviveLimit()
	--special summon condition
```

### Red Nova Dragon - Burning Soul (`65541655`)

Source: [Scripts/c65541655.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65541655.lua)

```lua
	aux.AddCodeList(c,70902743)
	--synchro summon
	aux.AddSynchroMixProcedure(c,aux.Tuner(nil),aux.Tuner(nil),nil,aux.NonTuner(nil),1,1)
	c:EnableReviveLimit()
	--cannot special summon
```

### Kewl Tune Crackle (`39576656`)

Source: [Scripts/c39576656.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39576656.lua)

```lua
	aux.AddMaterialCodeList(c,43904702)
	--synchro summon
	aux.AddSynchroMixProcedure(c,aux.FilterBoolFunction(Card.IsCode,43904702),nil,nil,aux.Tuner(nil),1,99)
	c:EnableReviveLimit()
	--remove extra
```
