# Auxiliary.dscon

## Signature

```lua
Auxiliary.dscon(Effect e, int tp, Group eg, int ep, any ev, Effect re, any r, int rp) -> void
```

## Description

Condition for Quick Effects that change ATK/DEF; true outside the Damage Phase, or during the Damage Phase before damage calculation has been performed.

## Parameters

- `e` `Effect`
- `tp` `int`
- `eg` `Group`
- `ep` `int`
- `ev` `any`
- `re` `Effect`
- `r` `any`
- `rp` `int`

## Source

- `Utilities/utility.lua:810`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **266** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.dscon`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Salamandra with Chain](/examples/cards/62091148) | `62091148` | [Scripts/c62091148.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62091148.lua) | 81 |
| [Resurgam Xyz](/examples/cards/49082032) | `49082032` | [Scripts/c49082032.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49082032.lua) | 64 |
| [Graydle Split](/examples/cards/75361204) | `75361204` | [Scripts/c75361204.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75361204.lua) | 64 |
| [Penetration Fusion](/examples/cards/8778267) | `8778267` | [Scripts/c8778267.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8778267.lua) | 62 |
| Kuribeh | `34419588` | [Scripts/c34419588.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34419588.lua) | 57 |
| Amaze Attraction Wonder Wheel | `93473606` | [Scripts/c93473606.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93473606.lua) | 55 |
| Nemleria Louve | `57296396` | [Scripts/c57296396.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57296396.lua) | 55 |
| Clear Wing Fast Dragon | `90036274` | [Scripts/c90036274.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90036274.lua) | 54 |
| World Legacy Collapse | `36197902` | [Scripts/c36197902.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36197902.lua) | 53 |
| Marincess Cascade | `27012990` | [Scripts/c27012990.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27012990.lua) | 53 |
| Shura the Combat Star | `32615065` | [Scripts/c32615065.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32615065.lua) | 52 |
| Altergeist Memorygant | `23790299` | [Scripts/c23790299.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23790299.lua) | 52 |
| Raviel, Lord of Phantasms - Shimmering Scraper | `28651380` | [Scripts/c28651380.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28651380.lua) | 51 |
| Borreload Dragon | `31833038` | [Scripts/c31833038.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31833038.lua) | 50 |
| Firewall Dragon Singularity | `21637210` | [Scripts/c21637210.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21637210.lua) | 50 |
| Amazement Abomination Arlekino | `31600845` | [Scripts/c31600845.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31600845.lua) | 49 |
| Mythical Beast Medusa | `54965929` | [Scripts/c54965929.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54965929.lua) | 48 |
| Combat Wheel | `12501230` | [Scripts/c12501230.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12501230.lua) | 48 |
| Dinomorphia Rexterm | `92798873` | [Scripts/c92798873.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92798873.lua) | 48 |
| Envoy of Chaos | `38695361` | [Scripts/c38695361.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38695361.lua) | 48 |
| Blitzclique - Alternator | `59921227` | [Scripts/c59921227.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59921227.lua) | 48 |
| Materiactor Exareptor | `37426272` | [Scripts/c37426272.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37426272.lua) | 48 |
| Tyrant Wing | `57470761` | [Scripts/c57470761.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57470761.lua) | 48 |
| Bujin Regalia - The Jewel | `63049052` | [Scripts/c63049052.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63049052.lua) | 48 |
| ...and 242 more |  |  |  |

## Script Examples

### Salamandra with Chain (`62091148`)

Source: [Scripts/c62091148.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62091148.lua)

```lua
	e1:SetHintTiming(TIMING_DAMAGE_STEP)
	e1:SetProperty(EFFECT_FLAG_CARD_TARGET+EFFECT_FLAG_DAMAGE_STEP)
	e1:SetCondition(aux.dscon)
	e1:SetCost(s.cost)
	e1:SetTarget(s.target)
```

### Resurgam Xyz (`49082032`)

Source: [Scripts/c49082032.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49082032.lua)

```lua
	e1:SetCode(EVENT_FREE_CHAIN)
	e1:SetHintTiming(0,TIMINGS_CHECK_MONSTER+TIMING_END_PHASE+TIMING_DAMAGE_STEP)
	e1:SetCondition(aux.dscon)
	c:RegisterEffect(e1)
	--atkup
```

### Graydle Split (`75361204`)

Source: [Scripts/c75361204.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75361204.lua)

```lua
	e1:SetHintTiming(TIMING_DAMAGE_STEP)
	e1:SetProperty(EFFECT_FLAG_CARD_TARGET+EFFECT_FLAG_DAMAGE_STEP)
	e1:SetCondition(aux.dscon)
	e1:SetCost(c75361204.cost)
	e1:SetTarget(c75361204.target)
```
