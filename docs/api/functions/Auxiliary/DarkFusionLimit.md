# Auxiliary.DarkFusionLimit

## Signature

```lua
Auxiliary.DarkFusionLimit(Effect e, Effect se, int sp, int st) -> bool
```

## Description

Special Summon restriction value for Evil HERO/Dark Fusion effects; allows Dark Fusion itself, the Dark Fusion summon value, or Fusion Summons while the player is affected by effect code 72043279.

## Parameters

- `e` `Effect`
- `se` `Effect`
- `sp` `int`
- `st` `int`

## Returns

- `bool` - true if the Summon matches Dark Fusion conditions.

## Source

- `Utilities/procedure.lua:2321`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **10** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.DarkFusionLimit) with `Auxiliary.DarkFusionLimit`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Evil HERO Inferno Wing - Backfire | `59893882` | [Scripts/c59893882.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c59893882.lua) | 1 |
| Evil HERO Darkest Knight | `86282581` | [Scripts/c86282581.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c86282581.lua) | 1 |
| Evil HERO Neos Lord | `13708888` | [Scripts/c13708888.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c13708888.lua) | 1 |
| Evil HERO Malicious Bane | `86165817` | [Scripts/c86165817.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c86165817.lua) | 1 |
| Evil HERO Dark Gaia | `58332301` | [Scripts/c58332301.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c58332301.lua) | 1 |
| Evil HERO Lightning Golem | `21947653` | [Scripts/c21947653.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c21947653.lua) | 1 |
| Evil HERO Inferno Wing | `22160245` | [Scripts/c22160245.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c22160245.lua) | 1 |
| Evil HERO Wild Cyclone | `13293158` | [Scripts/c13293158.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c13293158.lua) | 1 |
| Evil HERO Infernal Sniper | `50282757` | [Scripts/c50282757.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c50282757.lua) | 1 |
| Evil HERO Malicious Fiend | `86676862` | [Scripts/c86676862.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c86676862.lua) | 1 |

## Script Examples

### Evil HERO Inferno Wing - Backfire (`59893882`)

Source: [Scripts/c59893882.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c59893882.lua)

```lua
	e1:SetProperty(EFFECT_FLAG_CANNOT_DISABLE+EFFECT_FLAG_UNCOPYABLE)
	e1:SetCode(EFFECT_SPSUMMON_CONDITION)
	e1:SetValue(aux.DarkFusionLimit)
	c:RegisterEffect(e1)
	--to hand
```

### Evil HERO Darkest Knight (`86282581`)

Source: [Scripts/c86282581.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c86282581.lua)

```lua
	e1:SetProperty(EFFECT_FLAG_CANNOT_DISABLE+EFFECT_FLAG_UNCOPYABLE)
	e1:SetCode(EFFECT_SPSUMMON_CONDITION)
	e1:SetValue(aux.DarkFusionLimit)
	c:RegisterEffect(e1)
	--atk down
```

### Evil HERO Neos Lord (`13708888`)

Source: [Scripts/c13708888.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c13708888.lua)

```lua
	e1:SetProperty(EFFECT_FLAG_CANNOT_DISABLE+EFFECT_FLAG_UNCOPYABLE)
	e1:SetCode(EFFECT_SPSUMMON_CONDITION)
	e1:SetValue(aux.DarkFusionLimit)
	c:RegisterEffect(e1)
	--gain control
```
