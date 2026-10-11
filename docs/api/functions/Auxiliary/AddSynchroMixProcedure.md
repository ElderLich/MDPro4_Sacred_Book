# Auxiliary.AddSynchroMixProcedure

## Signature

```lua
Auxiliary.AddSynchroMixProcedure(Card c, function|nil f1, function|nil f2, function|nil f3, function|nil f4, int minc, int maxc, [function gc]) -> void
```

## Description

Registers a mixed Synchro Summon procedure requiring up to three fixed material filters plus f4 repeated between minc and maxc times.
The helper creates an Extra Deck EFFECT_SPSUMMON_PROC with SUMMON_TYPE_SYNCHRO, checks the exact Synchro Level total, and handles mandatory material, hand Synchro, tuner-limit, and optional group-check rules.
The maximum count is capped by c's Level after subtracting any required fixed materials.

## Parameters

- `c` `Card`
- `f1` `function|nil`
- `f2` `function|nil`
- `f3` `function|nil`
- `f4` `function|nil`
- `minc` `int`
- `maxc` `int`
- `gc` `function` optional

## Source

- `Utilities/procedure.lua:135`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **35** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.AddSynchroMixProcedure) with `Auxiliary.AddSynchroMixProcedure`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Shooting Majestic Star Dragon](/examples/cards/40939228) | `40939228` | [Scripts/c40939228.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40939228.lua) | 1 |
| [Kewl Tune Crackle](/examples/cards/39576656) | `39576656` | [Scripts/c39576656.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39576656.lua) | 1 |
| Red Nova Dragon - Burning Soul | `65541655` | [Scripts/c65541655.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65541655.lua) | 1 |
| Nirvana High Paladin | `80896940` | [Scripts/c80896940.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80896940.lua) | 1 |
| Kewl Tune Remix | `88170262` | [Scripts/c88170262.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88170262.lua) | 1 |
| Red Hypernova Dragon | `30698243` | [Scripts/c30698243.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30698243.lua) | 1 |
| Kewl Tune B2B | `65961304` | [Scripts/c65961304.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65961304.lua) | 1 |
| X-Saber Gottoms | `8252010` | [Scripts/c8252010.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8252010.lua) | 1 |
| Commander Souza, Swordmaster | `72867001` | [Scripts/c72867001.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c72867001.lua) | 1 |
| Majestic Star Dragon | `7841112` | [Scripts/c7841112.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7841112.lua) | 1 |
| Red Supernova Dragon | `99585850` | [Scripts/c99585850.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c99585850.lua) | 1 |
| Kewl Tune RS | `15665977` | [Scripts/c15665977.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15665977.lua) | 1 |
| Crystal Clear Wing Over Synchro Dragon | `84343351` | [Scripts/c84343351.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84343351.lua) | 1 |
| Mannadium Prime-Heart | `90465153` | [Scripts/c90465153.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90465153.lua) | 1 |
| Chaos Angel | `22850702` | [Scripts/c22850702.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22850702.lua) | 1 |
| Blue-Eyes Ultimate Spirit Dragon | `89604813` | [Scripts/c89604813.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c89604813.lua) | 1 |
| Lollipo★Yummy Way | `93192592` | [Scripts/c93192592.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93192592.lua) | 1 |
| Vylon Omega | `93157004` | [Scripts/c93157004.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93157004.lua) | 1 |
| Ghoti of the Deep Beyond | `72309040` | [Scripts/c72309040.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c72309040.lua) | 1 |
| Hot Red Dragon Archfiend King Calamity | `62242678` | [Scripts/c62242678.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62242678.lua) | 1 |
| Majestic Red Dragon | `67030233` | [Scripts/c67030233.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67030233.lua) | 1 |
| Cupsy★Yummy Way | `31603289` | [Scripts/c31603289.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31603289.lua) | 1 |
| Judgment, the Dragon of Heaven | `41659072` | [Scripts/c41659072.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41659072.lua) | 1 |
| Cooky★Yummy Way | `67098897` | [Scripts/c67098897.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67098897.lua) | 1 |
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

### Kewl Tune Crackle (`39576656`)

Source: [Scripts/c39576656.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39576656.lua)

```lua
	aux.AddMaterialCodeList(c,43904702)
	--synchro summon
	aux.AddSynchroMixProcedure(c,aux.FilterBoolFunction(Card.IsCode,43904702),nil,nil,aux.Tuner(nil),1,99)
	c:EnableReviveLimit()
	--remove extra
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
