# Duel.IsMainPhase

## Signature

```lua
Duel.IsMainPhase() -> bool
```

## Description

Returns whether the current phase is a Main Phase.

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4952`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **75** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.IsMainPhase`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Astrograph Sorcerer, the Star Magician](/examples/cards/48171151) | `48171151` | [Scripts/c48171151.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48171151.lua) | 80 |
| [Invoked Sorath](/examples/cards/43989315) | `43989315` | [Scripts/c43989315.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43989315.lua) | 66 |
| [Magnet Bonding](/examples/cards/65514302) | `65514302` | [Scripts/c65514302.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65514302.lua) | 65 |
| [Teleport Fusion](/examples/cards/36494597) | `36494597` | [Scripts/c36494597.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36494597.lua) | 64 |
| [Artmage Masterwork -Succession-](/examples/cards/37517035) | `37517035` | [Scripts/c37517035.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37517035.lua) | 62 |
| [W:P Fancy Ball](/examples/cards/4993187) | `4993187` | [Scripts/c4993187.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4993187.lua) | 61 |
| [Yummy★Snatchy](/examples/cards/30581601) | `30581601` | [Scripts/c30581601.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30581601.lua) | 61 |
| Ecclesia and the Dark Dragon | `78397661` | [Scripts/c78397661.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78397661.lua) | 59 |
| Dracotail Mululu | `7375867` | [Scripts/c7375867.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7375867.lua) | 58 |
| K9-X Forced Release | `53792930` | [Scripts/c53792930.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53792930.lua) | 58 |
| Clown Crew Soiree Operations | `70058649` | [Scripts/c70058649.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70058649.lua) | 57 |
| Saiba the Soldier Swordsmith | `36608728` | [Scripts/c36608728.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36608728.lua) | 57 |
| Artmage Power Patron | `23829452` | [Scripts/c23829452.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23829452.lua) | 56 |
| R.B. Lambda Blade | `17188206` | [Scripts/c17188206.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17188206.lua) | 56 |
| Gem-Knight Master Diamond Dispersion | `25342956` | [Scripts/c25342956.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25342956.lua) | 55 |
| Heroic Champion - Magnum Excalibur | `14301396` | [Scripts/c14301396.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c14301396.lua) | 55 |
| Dracotail Faimena | `1498449` | [Scripts/c1498449.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1498449.lua) | 55 |
| Chevreuil, Hunting Scout of the Deep Forest | `13023431` | [Scripts/c13023431.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13023431.lua) | 54 |
| R.B. Shepherd's Crook | `80071619` | [Scripts/c80071619.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80071619.lua) | 54 |
| Galaxy-Eyes Photon Change Dragon | `54725177` | [Scripts/c54725177.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54725177.lua) | 53 |
| Borrelshroud Dragon | `66452432` | [Scripts/c66452432.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66452432.lua) | 53 |
| Crystron Halqifibrax Prism | `65400671` | [Scripts/c65400671.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65400671.lua) | 53 |
| Laevateinn the Burning Blade | `6260560` | [Scripts/c6260560.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6260560.lua) | 53 |
| Clown Crew Biancaviso | `82159583` | [Scripts/c82159583.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82159583.lua) | 52 |
| ...and 51 more |  |  |  |

## Script Examples

### Astrograph Sorcerer, the Star Magician (`48171151`)

Source: [Scripts/c48171151.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48171151.lua)

```lua
end
function s.fspcon(e,tp,eg,ep,ev,re,r,rp)
	return Duel.IsMainPhase()
end
function s.filter0(c,e)
```

### Invoked Sorath (`43989315`)

Source: [Scripts/c43989315.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43989315.lua)

```lua
end
function s.spcon(e,tp,eg,ep,ev,re,r,rp)
	return Duel.IsMainPhase()
end
function s.spfilter(c,e,tp)
```

### Magnet Bonding (`65514302`)

Source: [Scripts/c65514302.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65514302.lua)

```lua
end
function s.condition(e,tp,eg,ep,ev,re,r,rp)
	return Duel.IsMainPhase()
end
function s.thfilter1(c)
```
