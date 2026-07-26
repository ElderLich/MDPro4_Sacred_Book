# Auxiliary.AssaultModeLimit

## Signature

```lua
Auxiliary.AssaultModeLimit(Effect e, Effect se, int sp, int st) -> bool
```

## Description

Special Summon restriction value for /Assault Mode monsters; allows the Assault Mode summon value or effects activated by Assault Mode Activate.

## Parameters

- `e` `Effect`
- `se` `Effect`
- `sp` `int`
- `st` `int`

## Returns

- `bool` - true if the Summon matches /Assault Mode conditions.

## Source

- `Utilities/procedure.lua:2313`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **11** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.AssaultModeLimit`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Doomkaiser Dragon/Assault Mode | `1764972` | [Scripts/c1764972.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1764972.lua) | 1 |
| Red Nova Dragon/Assault Mode | `82323997` | [Scripts/c82323997.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82323997.lua) | 1 |
| Junk Warrior/Assault Mode | `23219323` | [Scripts/c23219323.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23219323.lua) | 1 |
| Black Rose Dragon/Assault Mode | `46985799` | [Scripts/c46985799.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46985799.lua) | 1 |
| T.G. Halberd Cannon/Assault Mode | `47027714` | [Scripts/c47027714.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c47027714.lua) | 1 |
| Crimson Blader/Assault Mode | `50604072` | [Scripts/c50604072.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50604072.lua) | 1 |
| Arcanite Magician/Assault Mode | `14553285` | [Scripts/c14553285.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c14553285.lua) | 1 |
| Colossal Fighter/Assault Mode | `38898779` | [Scripts/c38898779.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38898779.lua) | 1 |
| Hyper Psychic Blaster/Assault Mode | `37169670` | [Scripts/c37169670.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37169670.lua) | 1 |
| Stardust Dragon/Assault Mode | `61257789` | [Scripts/c61257789.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61257789.lua) | 1 |
| Red Dragon Archfiend/Assault Mode | `77336644` | [Scripts/c77336644.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77336644.lua) | 1 |

## Script Examples

### Doomkaiser Dragon/Assault Mode (`1764972`)

Source: [Scripts/c1764972.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1764972.lua)

```lua
	e1:SetType(EFFECT_TYPE_SINGLE)
	e1:SetCode(EFFECT_SPSUMMON_CONDITION)
	e1:SetValue(aux.AssaultModeLimit)
	c:RegisterEffect(e1)
	--Special summon
```

### Red Nova Dragon/Assault Mode (`82323997`)

Source: [Scripts/c82323997.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82323997.lua)

```lua
	e1:SetType(EFFECT_TYPE_SINGLE)
	e1:SetCode(EFFECT_SPSUMMON_CONDITION)
	e1:SetValue(aux.AssaultModeLimit)
	c:RegisterEffect(e1)
	--remove
```

### Junk Warrior/Assault Mode (`23219323`)

Source: [Scripts/c23219323.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23219323.lua)

```lua
	e0:SetType(EFFECT_TYPE_SINGLE)
	e0:SetCode(EFFECT_SPSUMMON_CONDITION)
	e0:SetValue(aux.AssaultModeLimit)
	c:RegisterEffect(e0)
	--atkup
```
