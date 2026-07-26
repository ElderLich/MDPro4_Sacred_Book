# Auxiliary.evospcon

## Signature

```lua
Auxiliary.evospcon(Effect e, int tp, Group eg, int ep, int ev, Effect re, int r, int rp) -> bool
```

## Description

Special Summon condition helper for Evolsaur-style effects and set 0x304e monster Special Summons.

## Parameters

- `e` `Effect`
- `tp` `int`
- `eg` `Group`
- `ep` `int`
- `ev` `int`
- `re` `Effect`
- `r` `int`
- `rp` `int`

## Returns

- `bool`

## Source

- `Utilities/utility.lua:914`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **7** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.evospcon`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Evolsaur Cerato | `80651316` | [Scripts/c80651316.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80651316.lua) | 1 |
| Evolsaur Pelta | `16480084` | [Scripts/c16480084.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16480084.lua) | 1 |
| Evolsaur Vulcano | `54266211` | [Scripts/c54266211.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54266211.lua) | 1 |
| Evolsaur Darwino | `39672388` | [Scripts/c39672388.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39672388.lua) | 1 |
| Evolsaur Elias | `23234094` | [Scripts/c23234094.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23234094.lua) | 1 |
| Evolsaur Diplo | `17045014` | [Scripts/c17045014.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17045014.lua) | 1 |
| Evolsaur Terias | `69633792` | [Scripts/c69633792.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c69633792.lua) | 1 |

## Script Examples

### Evolsaur Cerato (`80651316`)

Source: [Scripts/c80651316.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80651316.lua)

```lua
	e1:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_TRIGGER_F)
	e1:SetCode(EVENT_SPSUMMON_SUCCESS)
	e1:SetCondition(aux.evospcon)
	e1:SetOperation(c80651316.atkop)
	c:RegisterEffect(e1)
```

### Evolsaur Pelta (`16480084`)

Source: [Scripts/c16480084.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16480084.lua)

```lua
	e1:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_TRIGGER_F)
	e1:SetCode(EVENT_SPSUMMON_SUCCESS)
	e1:SetCondition(aux.evospcon)
	e1:SetOperation(c16480084.operation)
	c:RegisterEffect(e1)
```

### Evolsaur Vulcano (`54266211`)

Source: [Scripts/c54266211.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54266211.lua)

```lua
	e1:SetProperty(EFFECT_FLAG_CARD_TARGET+EFFECT_FLAG_DAMAGE_STEP)
	e1:SetCode(EVENT_SPSUMMON_SUCCESS)
	e1:SetCondition(aux.evospcon)
	e1:SetTarget(c54266211.sptg)
	e1:SetOperation(c54266211.spop)
```
