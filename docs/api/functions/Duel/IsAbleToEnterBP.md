# Duel.IsAbleToEnterBP

## Signature

```lua
Duel.IsAbleToEnterBP() -> bool
```

## Description

Checks whether the current turn player can still enter the Battle Phase.
The core requires the duel to allow first-turn attacks or not be turn 1, the current phase to be before PHASE_BATTLE_START, and the turn player not to be affected by EFFECT_CANNOT_BP.

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5071`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **75** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.IsAbleToEnterBP`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Pendulum Evolution](/examples/cards/55795155) | `55795155` | [Scripts/c55795155.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55795155.lua) | 77 |
| Performage Trapeze Magician | `17016362` | [Scripts/c17016362.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17016362.lua) | 56 |
| Vernusylph of the Thawing Mountains | `9238125` | [Scripts/c9238125.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9238125.lua) | 55 |
| Joyous Melffys | `53054164` | [Scripts/c53054164.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53054164.lua) | 52 |
| H.E.R.O. Flash! | `18482473` | [Scripts/c18482473.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18482473.lua) | 50 |
| Mega Fortress Whale | `96546575` | [Scripts/c96546575.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96546575.lua) | 49 |
| Update Jammer | `88093706` | [Scripts/c88093706.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88093706.lua) | 47 |
| Ukiyoe-P.U.N.K. Rising Carp | `18313046` | [Scripts/c18313046.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18313046.lua) | 46 |
| D/D Defense Soldier | `93317313` | [Scripts/c93317313.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93317313.lua) | 46 |
| Heavy Armored Train Ironwolf | `49121795` | [Scripts/c49121795.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49121795.lua) | 46 |
| Shooting Star Dragon | `24696097` | [Scripts/c24696097.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24696097.lua) | 45 |
| Inzektor Hopper | `52601736` | [Scripts/c52601736.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52601736.lua) | 45 |
| Raidraptor - Revolution Falcon | `81927732` | [Scripts/c81927732.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81927732.lua) | 44 |
| Eclipse Twins | `45852939` | [Scripts/c45852939.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45852939.lua) | 44 |
| Heroic Champion - Claivesolish | `97453744` | [Scripts/c97453744.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97453744.lua) | 43 |
| Diplexer Chimera | `78084378` | [Scripts/c78084378.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78084378.lua) | 43 |
| Double Iris Magician | `49684352` | [Scripts/c49684352.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49684352.lua) | 42 |
| Sunavalon Melias | `44478599` | [Scripts/c44478599.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44478599.lua) | 42 |
| Performage Fire Dancer | `7934362` | [Scripts/c7934362.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7934362.lua) | 41 |
| Duralume, Vaalmonican Heathen Hallow | `76821171` | [Scripts/c76821171.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76821171.lua) | 41 |
| Number 47: Nightmare Shark | `31320433` | [Scripts/c31320433.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31320433.lua) | 41 |
| SPYRAL GEAR - Last Resort | `37433748` | [Scripts/c37433748.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37433748.lua) | 40 |
| Go! - D/D/D Divine Zero King Rage | `40227329` | [Scripts/c40227329.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40227329.lua) | 39 |
| "Infernoble Arms - Hauteclere" | `64867422` | [Scripts/c64867422.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c64867422.lua) | 38 |
| ...and 51 more |  |  |  |

## Script Examples

### Pendulum Evolution (`55795155`)

Source: [Scripts/c55795155.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55795155.lua)

```lua
end
function c55795155.atkcon(e,tp,eg,ep,ev,re,r,rp)
	return Duel.IsAbleToEnterBP()
end
function c55795155.atkfilter(c)
```

### Performage Trapeze Magician (`17016362`)

Source: [Scripts/c17016362.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17016362.lua)

```lua
end
function c17016362.mtcon(e,tp,eg,ep,ev,re,r,rp)
	return Duel.GetCurrentPhase()==PHASE_MAIN1 and Duel.IsAbleToEnterBP()
end
function c17016362.mtcost(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Vernusylph of the Thawing Mountains (`9238125`)

Source: [Scripts/c9238125.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9238125.lua)

```lua
end
function c9238125.atkcon(e,tp,eg,ep,ev,re,r,rp)
	return Duel.IsAbleToEnterBP()
end
function c9238125.atkfilter(c)
```
