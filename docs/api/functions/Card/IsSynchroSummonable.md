# Card.IsSynchroSummonable

## Signature

```lua
Card.IsSynchroSummonable(Card c, [Card|nil tuner], [Group mg]) -> bool
```

## Description

Checks whether c can be Synchro Summoned with tuner and the available material group mg.
If tuner is nil, this behaves like the regular Special Summon procedure check for c.

## Parameters

- `c` `Card`
- `tuner` `Card|nil` optional
- `mg` `Group` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3576`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **75** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.IsSynchroSummonable`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Accel Synchro Stardust Dragon](/examples/cards/30983281) | `30983281` | [Scripts/c30983281.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30983281.lua) | 69 |
| [Yummy★Snatchy](/examples/cards/30581601) | `30581601` | [Scripts/c30581601.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30581601.lua) | 61 |
| Supreme King Dragon Lightwurm | `41908872` | [Scripts/c41908872.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41908872.lua) | 59 |
| Saiba the Soldier Swordsmith | `36608728` | [Scripts/c36608728.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36608728.lua) | 57 |
| Kewl Tune Remix | `88170262` | [Scripts/c88170262.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88170262.lua) | 54 |
| R-Genex Turing | `61052897` | [Scripts/c61052897.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61052897.lua) | 54 |
| Naturia Blessing | `34813545` | [Scripts/c34813545.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34813545.lua) | 54 |
| Melffy Pinny | `34800281` | [Scripts/c34800281.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34800281.lua) | 53 |
| Daigusto Laplampilica | `76937326` | [Scripts/c76937326.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76937326.lua) | 52 |
| Kewl Tune B2B | `65961304` | [Scripts/c65961304.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65961304.lua) | 52 |
| Performapal Odd-Eyes Synchron | `82224646` | [Scripts/c82224646.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82224646.lua) | 51 |
| Accel Synchron | `37675907` | [Scripts/c37675907.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37675907.lua) | 50 |
| Stand Up Centur-Ion! | `41371602` | [Scripts/c41371602.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41371602.lua) | 49 |
| Mathmech Superfactorial | `87804365` | [Scripts/c87804365.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87804365.lua) | 49 |
| Superheavy Samurai Fist | `71386411` | [Scripts/c71386411.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71386411.lua) | 48 |
| Elfnote Power Patron | `12375297` | [Scripts/c12375297.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12375297.lua) | 48 |
| Ukiyoe-P.U.N.K. Sharakusai | `13258285` | [Scripts/c13258285.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13258285.lua) | 48 |
| Re-dyce-cle | `85704698` | [Scripts/c85704698.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85704698.lua) | 48 |
| Magicolloidal Sol | `67694706` | [Scripts/c67694706.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67694706.lua) | 47 |
| Garden Rose Flora | `76524506` | [Scripts/c76524506.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76524506.lua) | 47 |
| X-Saber Bruno | `45462306` | [Scripts/c45462306.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45462306.lua) | 47 |
| Crystron Tristaros | `99471856` | [Scripts/c99471856.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c99471856.lua) | 46 |
| Speedroid Gum Prize | `70939418` | [Scripts/c70939418.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70939418.lua) | 46 |
| Shooting Riser Dragon | `68431965` | [Scripts/c68431965.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c68431965.lua) | 46 |
| ...and 51 more |  |  |  |

## Script Examples

### Accel Synchro Stardust Dragon (`30983281`)

Source: [Scripts/c30983281.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30983281.lua)

```lua
end
function c30983281.syncheck(g,tp,syncard)
	return aux.SynMixHandCheck(g,tp,syncard) and syncard:IsSynchroSummonable(nil,g,#g-1,#g-1)
end
function c30983281.synfilter(c,tp,mg)
```

### Yummy★Snatchy (`30581601`)

Source: [Scripts/c30581601.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30581601.lua)

```lua
end
function s.syncheck(g,tp,syncard)
	return g:IsExists(s.mfilter,1,nil) and aux.SynMixHandCheck(g,tp,syncard) and syncard:IsSynchroSummonable(nil,g,#g-1,#g-1)
end
function s.scfilter(c,tp,mg)
```

### Supreme King Dragon Lightwurm (`41908872`)

Source: [Scripts/c41908872.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41908872.lua)

```lua
end
function c41908872.scfilter(c)
	return c:IsSetCard(0x20f8) and c:IsSynchroSummonable(nil)
end
function c41908872.xyzfilter(c)
```
