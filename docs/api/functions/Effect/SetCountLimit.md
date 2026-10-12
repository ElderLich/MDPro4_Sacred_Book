# Effect.SetCountLimit

## Signature

```lua
Effect.SetCountLimit(Effect e, int count, [int code]) -> void
```

## Description

Sets how many times e can be used before its count limit is spent.
If count is 0, the core treats it as 1. Effects that share a nonzero code share the same usage count for the checked player.
EFFECT_COUNT_CODE_OATH uses oath-style rollback on negated activations and failed procedure attempts; EFFECT_COUNT_CODE_DUEL uses the duel-long count map; EFFECT_COUNT_CODE_SINGLE shares usage by handler instance; EFFECT_COUNT_CODE_CHAIN uses the chain count map.
Use flag effects for custom reminders or activity markers; use SetCountLimit for engine-managed use counts.

## How To Use It

Use `SetCountLimit` for once-per-turn and shared-count restrictions.

A normal hard once per turn usually uses the card id as the shared code:

```lua
e1:SetCountLimit(1,id)
```

Effects with the same nonzero code share the same count. Special flags such as `EFFECT_COUNT_CODE_OATH`, `EFFECT_COUNT_CODE_DUEL`, `EFFECT_COUNT_CODE_SINGLE`, and `EFFECT_COUNT_CODE_CHAIN` change how that count is scoped. If `count` is 0, MDPro4 stores it as 1.

## Related Functions

- [Effect.CheckCountLimit](/api/functions/Effect/CheckCountLimit)
- [Effect.UseCountLimit](/api/functions/Effect/UseCountLimit)
- [Card.RegisterFlagEffect](/api/functions/Card/RegisterFlagEffect)

## Parameters

- `e` `Effect` - Effect whose count limit is set.
- `count` `int` - Maximum uses before the count is spent; 0 is normalized to 1 by the core.
- `code` `int` optional - Shared count-limit code. Effects with the same nonzero code share usage for the checked player; combine a card id with EFFECT_COUNT_CODE_OATH, EFFECT_COUNT_CODE_DUEL, or EFFECT_COUNT_CODE_SINGLE when that special behavior is needed. Passing exactly EFFECT_COUNT_CODE_CHAIN stores it together with EFFECT_COUNT_CODE_SINGLE in this core.

## Source

- `D:\Programs\GitHub\ygopro-core\libeffect.cpp:617`

## Guided Examples

Learn how to use this function in context:

- [Activation Legality](/learn/activation-legality)
- [Common Script Errors And Debugging](/learn/common-script-errors-and-debugging)
- [Count Limits And Once Per Turn](/learn/count-limits)
- [Creation, Building, and Registration of an Effect Object](/learn/effect-object)
- [Normal And Continuous Traps](/learn/normal-and-continuous-traps)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **8020** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Effect.SetCountLimit) with `Effect.SetCountLimit`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Salamandra with Chain](/examples/cards/62091148) | `62091148` | [Scripts/c62091148.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c62091148.lua) | 2 |
| [Astrograph Sorcerer, the Starfrost Magician](/examples/cards/48171151) | `48171151` | [Scripts/c48171151.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c48171151.lua) | 3 |
| [Artmage Non-Finito](/examples/cards/74631897) | `74631897` | [Scripts/c74631897.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c74631897.lua) | 1 |
| [Pendulum Evolution](/examples/cards/55795155) | `55795155` | [Scripts/c55795155.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c55795155.lua) | 3 |
| [Levia-Dragoon - Daedalus](/examples/cards/78579058) | `78579058` | [Scripts/c78579058.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c78579058.lua) | 2 |
| [Lady's Dragonmaid](/examples/cards/48658295) | `48658295` | [Scripts/c48658295.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c48658295.lua) | 2 |
| [Azure Ocean Dragon Lord - Neo-Daedalus Rage](/examples/cards/41570943) | `41570943` | [Scripts/c41570943.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c41570943.lua) | 1 |
| [Eternal Favorite](/examples/cards/87532344) | `87532344` | [Scripts/c87532344.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c87532344.lua) | 2 |
| [Surprise Fusion](/examples/cards/35167375) | `35167375` | [Scripts/c35167375.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c35167375.lua) | 1 |
| [Astrograph Sorcerer](/examples/cards/76794549) | `76794549` | [Scripts/c76794549.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c76794549.lua) | 1 |
| [Spellbook of the Grand Circle](/examples/cards/11911336) | `11911336` | [Scripts/c11911336.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c11911336.lua) | 2 |
| [Accel Synchro Stardust Dragon](/examples/cards/30983281) | `30983281` | [Scripts/c30983281.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c30983281.lua) | 2 |
| [Melffy Playtime Surprise](/examples/cards/58036097) | `58036097` | [Scripts/c58036097.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c58036097.lua) | 2 |
| [Ashtraja Susanoo](/examples/cards/17020474) | `17020474` | [Scripts/c17020474.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c17020474.lua) | 2 |
| [Deftero Enneacraft - "alazoneIA"](/examples/cards/92171126) | `92171126` | [Scripts/c92171126.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c92171126.lua) | 2 |
| [Destiny HERO - Destro-Dogma](/examples/cards/25158975) | `25158975` | [Scripts/c25158975.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c25158975.lua) | 3 |
| [Yomagna the Fire Phantom](/examples/cards/17350692) | `17350692` | [Scripts/c17350692.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c17350692.lua) | 2 |
| [Fiendsmith's Sequence](/examples/cards/49867899) | `49867899` | [Scripts/c49867899.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c49867899.lua) | 2 |
| [D/D/D Alfred the Divine Sage King](/examples/cards/11852093) | `11852093` | [Scripts/c11852093.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c11852093.lua) | 2 |
| [El Shaddoll Apkallone](/examples/cards/50907446) | `50907446` | [Scripts/c50907446.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c50907446.lua) | 2 |
| [Mementotlan Fusion](/examples/cards/66518509) | `66518509` | [Scripts/c66518509.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c66518509.lua) | 2 |
| [Meteoroa Drytron](/examples/cards/24166324) | `24166324` | [Scripts/c24166324.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c24166324.lua) | 2 |
| [Favorite HERO Flame Wingman](/examples/cards/13243124) | `13243124` | [Scripts/c13243124.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c13243124.lua) | 2 |
| [Mixousia the Confounder](/examples/cards/80843006) | `80843006` | [Scripts/c80843006.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c80843006.lua) | 3 |
| ...and 7996 more |  |  |  |

## Script Examples

### Salamandra with Chain (`62091148`)

Source: [Scripts/c62091148.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c62091148.lua)

```lua
	e2:SetRange(LOCATION_GRAVE)
	e2:SetHintTiming(0,TIMINGS_CHECK_MONSTER)
	e2:SetCountLimit(1,id)
	e2:SetCost(aux.bfgcost)
	e2:SetTarget(s.sptg)
```

### Astrograph Sorcerer, the Starfrost Magician (`48171151`)

Source: [Scripts/c48171151.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c48171151.lua)

```lua
	e1:SetType(EFFECT_TYPE_IGNITION)
	e1:SetRange(LOCATION_PZONE)
	e1:SetCountLimit(1,id)
	e1:SetTarget(s.ptg)
	e1:SetOperation(s.pop)
```

### Artmage Non-Finito (`74631897`)

Source: [Scripts/c74631897.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c74631897.lua)

```lua
	e5:SetRange(LOCATION_MZONE)
	e5:SetHintTiming(0,TIMINGS_CHECK_MONSTER+TIMING_END_PHASE)
	e5:SetCountLimit(1)
	e5:SetCondition(s.fspcon)
	e5:SetTarget(s.fsptg)
```
