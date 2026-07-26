# Auxiliary.ChangeBattleDamage

## Signature

```lua
Auxiliary.ChangeBattleDamage(int player, any value) -> void
```

## Description

Returns a value function for EFFECT_CHANGE_BATTLE_DAMAGE. player=0 changes damage taken by the effect owner, player=1 changes damage taken by the opponent; otherwise it returns -1 to keep the damage unchanged.

## Parameters

- `player` `int`
- `value` `any`

## Source

- `Utilities/utility.lua:726`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **51** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.ChangeBattleDamage`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Odd-Eyes Pendulum Dragon of the Four Heavenly Dragons | `75787708` | [Scripts/c75787708.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75787708.lua) | 1 |
| Supreme King Dragon Odd-Eyes | `96733134` | [Scripts/c96733134.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96733134.lua) | 1 |
| Void Imagination | `31444249` | [Scripts/c31444249.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31444249.lua) | 1 |
| Junk Warrior/Assault Mode | `23219323` | [Scripts/c23219323.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23219323.lua) | 1 |
| X-Krawler Neurogos | `66393507` | [Scripts/c66393507.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66393507.lua) | 1 |
| Arsenal Audit | `49652661` | [Scripts/c49652661.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49652661.lua) | 1 |
| Number 62: Galaxy-Eyes Prime Photon Dragon | `31801517` | [Scripts/c31801517.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31801517.lua) | 1 |
| Pitknight Filly | `25919316` | [Scripts/c25919316.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25919316.lua) | 1 |
| Transcendosaurus Drillygnathus | `30128445` | [Scripts/c30128445.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30128445.lua) | 1 |
| Raijin the Breakbolt Star | `99991455` | [Scripts/c99991455.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c99991455.lua) | 1 |
| Double Iris Magician | `49684352` | [Scripts/c49684352.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49684352.lua) | 1 |
| Galaxy-Eyes Antimatter Dragon | `92517928` | [Scripts/c92517928.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92517928.lua) | 1 |
| Gogogo Golem - Golden Form | `2948263` | [Scripts/c2948263.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2948263.lua) | 1 |
| Chobham Armor Dragon | `27352108` | [Scripts/c27352108.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27352108.lua) | 1 |
| Xyz Armor Fortress | `20145685` | [Scripts/c20145685.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20145685.lua) | 1 |
| Infernity Doom Archfiend | `38904695` | [Scripts/c38904695.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38904695.lua) | 1 |
| Azamina Ilia Silvia | `46396218` | [Scripts/c46396218.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46396218.lua) | 1 |
| Crusadia Maximus | `81524756` | [Scripts/c81524756.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81524756.lua) | 1 |
| Beelzeus of the Diabolic Dragons | `8763963` | [Scripts/c8763963.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8763963.lua) | 1 |
| U.A. Powered Jersey | `35884610` | [Scripts/c35884610.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35884610.lua) | 1 |
| Tri-Gate Wizard | `32617464` | [Scripts/c32617464.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32617464.lua) | 1 |
| Odd-Eyes Pendulum Dragon | `16178681` | [Scripts/c16178681.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16178681.lua) | 1 |
| Dragunity Pilum | `52977572` | [Scripts/c52977572.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52977572.lua) | 1 |
| Pegasus Wing | `72083436` | [Scripts/c72083436.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c72083436.lua) | 1 |
| ...and 27 more |  |  |  |

## Script Examples

### Odd-Eyes Pendulum Dragon of the Four Heavenly Dragons (`75787708`)

Source: [Scripts/c75787708.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75787708.lua)

```lua
	e3:SetCode(EFFECT_CHANGE_INVOLVING_BATTLE_DAMAGE)
	e3:SetCondition(s.atkcon)
	e3:SetValue(aux.ChangeBattleDamage(1,DOUBLE_DAMAGE))
	c:RegisterEffect(e3)
	--to hand
```

### Supreme King Dragon Odd-Eyes (`96733134`)

Source: [Scripts/c96733134.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96733134.lua)

```lua
	e3:SetTargetRange(LOCATION_MZONE,0)
	e3:SetTarget(c96733134.damtg)
	e3:SetValue(aux.ChangeBattleDamage(1,DOUBLE_DAMAGE))
	c:RegisterEffect(e3)
	--special summon
```

### Void Imagination (`31444249`)

Source: [Scripts/c31444249.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31444249.lua)

```lua
	e3:SetTargetRange(LOCATION_MZONE,0)
	e3:SetTarget(c31444249.rdtg)
	e3:SetValue(aux.ChangeBattleDamage(1,HALF_DAMAGE))
	c:RegisterEffect(e3)
	--spsummon
```
