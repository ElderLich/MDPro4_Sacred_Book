# Auxiliary.FossilFusionLimit

## Signature

```lua
Auxiliary.FossilFusionLimit(Effect e, Effect se, int sp, int st) -> bool
```

## Description

Special Summon restriction value for Fossil Fusion effects; allows Fossil Fusion's summon value, Fossil Fusion itself, or non-Extra Deck handlers.

## Parameters

- `e` `Effect`
- `se` `Effect`
- `sp` `int`
- `st` `int`

## Returns

- `bool` - true if the Summon matches Fossil Fusion conditions.

## Source

- `Utilities/procedure.lua:2327`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **8** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.FossilFusionLimit) with `Auxiliary.FossilFusionLimit`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Fossil Machine Skull Buggy | `10040267` | [Scripts/c10040267.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10040267.lua) | 1 |
| Fossil Machine Skull Wagon | `83656563` | [Scripts/c83656563.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c83656563.lua) | 1 |
| Fossil Warrior Skull King | `96897184` | [Scripts/c96897184.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96897184.lua) | 1 |
| Fossil Warrior Skull Knight | `59531356` | [Scripts/c59531356.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59531356.lua) | 1 |
| Fossil Dragon Skullgar | `12015000` | [Scripts/c12015000.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12015000.lua) | 1 |
| Fossil Machine Skull Convoy | `57157964` | [Scripts/c57157964.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57157964.lua) | 1 |
| Fossil Dragon Skullgios | `21225115` | [Scripts/c21225115.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21225115.lua) | 1 |
| Fossil Warrior Skull Bone | `86520461` | [Scripts/c86520461.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c86520461.lua) | 1 |

## Script Examples

### Fossil Machine Skull Buggy (`10040267`)

Source: [Scripts/c10040267.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10040267.lua)

```lua
	e1:SetProperty(EFFECT_FLAG_CANNOT_DISABLE+EFFECT_FLAG_UNCOPYABLE)
	e1:SetCode(EFFECT_SPSUMMON_CONDITION)
	e1:SetValue(aux.FossilFusionLimit)
	c:RegisterEffect(e1)
	--damage
```

### Fossil Machine Skull Wagon (`83656563`)

Source: [Scripts/c83656563.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c83656563.lua)

```lua
	e1:SetProperty(EFFECT_FLAG_CANNOT_DISABLE+EFFECT_FLAG_UNCOPYABLE)
	e1:SetCode(EFFECT_SPSUMMON_CONDITION)
	e1:SetValue(aux.FossilFusionLimit)
	c:RegisterEffect(e1)
	--extra attack
```

### Fossil Warrior Skull King (`96897184`)

Source: [Scripts/c96897184.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96897184.lua)

```lua
	e1:SetProperty(EFFECT_FLAG_CANNOT_DISABLE+EFFECT_FLAG_UNCOPYABLE)
	e1:SetCode(EFFECT_SPSUMMON_CONDITION)
	e1:SetValue(aux.FossilFusionLimit)
	c:RegisterEffect(e1)
	--pierce
```
