# Card.GetOriginalType

## Signature

```lua
Card.GetOriginalType(Card c) -> int
```

## Description

Returns c's original card-data type bitmask, not its current modified type.

## Parameters

- `c` `Card`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3451`

## Guided Examples

Learn how to use this function in context:

- [Applying The Latest Engine And Script Changes](/learn/engine-updates)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **175** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.GetOriginalType) with `Card.GetOriginalType`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Astrograph Sorcerer, the Starfrost Magician](/examples/cards/48171151) | `48171151` | [Scripts/c48171151.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c48171151.lua) | 1 |
| [D/D/D Alfred the Divine Sage King](/examples/cards/11852093) | `11852093` | [Scripts/c11852093.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c11852093.lua) | 1 |
| [Favorite HERO Flame Wingman](/examples/cards/13243124) | `13243124` | [Scripts/c13243124.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c13243124.lua) | 1 |
| [GMX Associate Noma](/examples/cards/83528184) | `83528184` | [Scripts/c83528184.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c83528184.lua) | 1 |
| Fiendsmith Kyrie | `26434972` | [Scripts/c26434972.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c26434972.lua) | 1 |
| D/D Extra Surveyor | `74387963` | [Scripts/c74387963.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c74387963.lua) | 1 |
| Vaylantz Genesis Grand Duke | `76075139` | [Scripts/c76075139.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c76075139.lua) | 1 |
| Mementotlan Shleepy | `50042011` | [Scripts/c50042011.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c50042011.lua) | 1 |
| Zoroa, the Magistus Verethragna | `37260677` | [Scripts/c37260677.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c37260677.lua) | 1 |
| D/D/D Deviser King Deus Machinex | `46593546` | [Scripts/c46593546.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c46593546.lua) | 1 |
| Emperor Charles the Great | `97864322` | [Scripts/c97864322.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c97864322.lua) | 2 |
| Angello Vaalmonica | `3048768` | [Scripts/c3048768.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c3048768.lua) | 1 |
| Spirit Poacher | `85150300` | [Scripts/c85150300.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c85150300.lua) | 1 |
| Metaltron XII, the True Dracombatant | `57761191` | [Scripts/c57761191.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c57761191.lua) | 2 |
| Angelechy Problem | `17782288` | [Scripts/c17782288.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c17782288.lua) | 2 |
| Dimonno Vaalmonica | `30432463` | [Scripts/c30432463.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c30432463.lua) | 1 |
| Crystron Halqifibrax Prism | `65400671` | [Scripts/c65400671.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c65400671.lua) | 1 |
| Capsule Monster Chess | `24056179` | [Scripts/c24056179.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c24056179.lua) | 1 |
| Millennium-Eyes Restrict | `41578483` | [Scripts/c41578483.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c41578483.lua) | 1 |
| Enneacraft Reverth | `80015408` | [Scripts/c80015408.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c80015408.lua) | 1 |
| Zebufera, Vaalmonican Hallow Heathen | `2815176` | [Scripts/c2815176.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c2815176.lua) | 1 |
| Emblema Salvation | `61950680` | [Scripts/c61950680.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c61950680.lua) | 1 |
| Cynet Backdoor | `43839002` | [Scripts/c43839002.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c43839002.lua) | 1 |
| Performage Ball Balancer | `92530005` | [Scripts/c92530005.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c92530005.lua) | 1 |
| ...and 151 more |  |  |  |

## Script Examples

### Astrograph Sorcerer, the Starfrost Magician (`48171151`)

Source: [Scripts/c48171151.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c48171151.lua)

```lua
function s.desfilter(c,tp)
	return c:IsPreviousControler(tp) and c:IsPreviousPosition(POS_FACEUP) and c:IsReason(REASON_BATTLE+REASON_EFFECT)
		and c:GetOriginalType()&TYPE_MONSTER~=0 and c:IsPreviousLocation(LOCATION_ONFIELD)
end
function s.spcon1(e,tp,eg,ep,ev,re,r,rp)
```

### D/D/D Alfred the Divine Sage King (`11852093`)

Source: [Scripts/c11852093.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c11852093.lua)

```lua
end
function s.spfilter1(c,e)
	return (c:IsLocation(LOCATION_MZONE) or c:IsFaceupEx() and c:GetOriginalType()&TYPE_MONSTER~=0)
		and c:IsCanBeFusionMaterial() and c:IsAbleToDeck() and not c:IsImmuneToEffect(e)
end
```

### Favorite HERO Flame Wingman (`13243124`)

Source: [Scripts/c13243124.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c13243124.lua)

```lua
end
function s.cfilter(c)
	return (c:IsPreviousLocation(LOCATION_MZONE) or c:GetOriginalType()&TYPE_MONSTER~=0)
		and c:IsReason(REASON_BATTLE)
end
```
