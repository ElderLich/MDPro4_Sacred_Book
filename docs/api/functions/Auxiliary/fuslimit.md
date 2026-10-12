# Auxiliary.fuslimit

## Signature

```lua
Auxiliary.fuslimit(Effect e, Effect se, int sp, int st) -> bool
```

## Description

Special Summon condition helper that returns true when summon type st contains SUMMON_TYPE_FUSION.

## Parameters

- `e` `Effect`
- `se` `Effect`
- `sp` `int`
- `st` `int`

## Returns

- `bool`

## Source

- `Utilities/procedure.lua:2289`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **89** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.fuslimit) with `Auxiliary.fuslimit`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| El Shaddoll Meshachrer | `32467459` | [Scripts/c32467459.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c32467459.lua) | 1 |
| Dragon Master Magia | `12381100` | [Scripts/c12381100.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c12381100.lua) | 1 |
| Divine Serpent Apophis | `97800311` | [Scripts/c97800311.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c97800311.lua) | 1 |
| Cyberdark End Dragon | `37542782` | [Scripts/c37542782.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c37542782.lua) | 1 |
| Predaplant Daredevil | `82370493` | [Scripts/c82370493.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c82370493.lua) | 1 |
| Thunder Dragon Titan | `41685633` | [Scripts/c41685633.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c41685633.lua) | 1 |
| Rainbow Overdragon | `37440988` | [Scripts/c37440988.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c37440988.lua) | 1 |
| Egyptian God Slime | `42166000` | [Scripts/c42166000.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c42166000.lua) | 1 |
| Supreme King Z-ARC | `13331639` | [Scripts/c13331639.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c13331639.lua) | 1 |
| Blue-Eyes Tyrant Dragon | `11443677` | [Scripts/c11443677.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c11443677.lua) | 1 |
| Nerva the Power Patron of Creation | `53589300` | [Scripts/c53589300.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c53589300.lua) | 1 |
| Hecahands Jauzah | `67021206` | [Scripts/c67021206.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c67021206.lua) | 1 |
| Elemental HERO Sunrise | `22908820` | [Scripts/c22908820.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c22908820.lua) | 1 |
| Snake-Eyes Doomed Dragon | `58071334` | [Scripts/c58071334.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c58071334.lua) | 1 |
| Elemental HERO Flame Wingman - Infernal Rage | `93347961` | [Scripts/c93347961.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c93347961.lua) | 1 |
| Armed Neos | `31817415` | [Scripts/c31817415.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c31817415.lua) | 1 |
| Greedy Venom Fusion Dragon | `51570882` | [Scripts/c51570882.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c51570882.lua) | 1 |
| Elemental HERO Thunder Giant - Voltic Thunder | `19222426` | [Scripts/c19222426.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c19222426.lua) | 1 |
| Light and Darkness Dragonlord | `19652159` | [Scripts/c19652159.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c19652159.lua) | 1 |
| Cyberdarkness Dragon | `18967507` | [Scripts/c18967507.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c18967507.lua) | 1 |
| Elemental HERO Grandmerge | `36841733` | [Scripts/c36841733.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c36841733.lua) | 1 |
| Prank-Kids Battle Butler | `81997228` | [Scripts/c81997228.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c81997228.lua) | 1 |
| Fullmetalfoes Alkahest | `77693536` | [Scripts/c77693536.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c77693536.lua) | 1 |
| Invoked Elysium | `11270236` | [Scripts/c11270236.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c11270236.lua) | 1 |
| ...and 65 more |  |  |  |

## Script Examples

### El Shaddoll Meshachrer (`32467459`)

Source: [Scripts/c32467459.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c32467459.lua)

```lua
	e1:SetProperty(EFFECT_FLAG_CANNOT_DISABLE+EFFECT_FLAG_UNCOPYABLE)
	e1:SetCode(EFFECT_SPSUMMON_CONDITION)
	e1:SetValue(aux.fuslimit)
	c:RegisterEffect(e1)
	--immune
```

### Dragon Master Magia (`12381100`)

Source: [Scripts/c12381100.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c12381100.lua)

```lua
	e0:SetProperty(EFFECT_FLAG_CANNOT_DISABLE+EFFECT_FLAG_UNCOPYABLE)
	e0:SetCode(EFFECT_SPSUMMON_CONDITION)
	e0:SetValue(aux.fuslimit)
	c:RegisterEffect(e0)
	local e1=Effect.CreateEffect(c)
```

### Divine Serpent Apophis (`97800311`)

Source: [Scripts/c97800311.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c97800311.lua)

```lua
	e1:SetProperty(EFFECT_FLAG_CANNOT_DISABLE+EFFECT_FLAG_UNCOPYABLE)
	e1:SetCode(EFFECT_SPSUMMON_CONDITION)
	e1:SetValue(aux.fuslimit)
	c:RegisterEffect(e1)
	--spsummon
```
