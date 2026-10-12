# Card.IsForbidden

## Signature

```lua
Card.IsForbidden(Card c) -> bool
```

## Description

Checks whether c currently has STATUS_FORBIDDEN.

## Parameters

- `c` `Card`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3680`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **277** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.IsForbidden) with `Card.IsForbidden`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Astrograph Sorcerer, the Starfrost Magician](/examples/cards/48171151) | `48171151` | [Scripts/c48171151.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c48171151.lua) | 1 |
| [Astrograph Sorcerer](/examples/cards/76794549) | `76794549` | [Scripts/c76794549.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c76794549.lua) | 1 |
| [D/D/D Alfred the Divine Sage King](/examples/cards/11852093) | `11852093` | [Scripts/c11852093.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c11852093.lua) | 1 |
| [Pere-Zenet Em Heru](/examples/cards/46273941) | `46273941` | [Scripts/c46273941.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c46273941.lua) | 1 |
| [Am Duazenet](/examples/cards/45151304) | `45151304` | [Scripts/c45151304.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c45151304.lua) | 1 |
| [Shining Draw](/examples/cards/35906693) | `35906693` | [Scripts/c35906693.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c35906693.lua) | 1 |
| [Plunder Patroll Shipshape Ships Shipping](/examples/cards/44227727) | `44227727` | [Scripts/c44227727.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c44227727.lua) | 1 |
| [Odd-Eyes Arcray Dragon](/examples/cards/6218704) | `6218704` | [Scripts/c6218704.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c6218704.lua) | 1 |
| [Chronograph Sorcerer](/examples/cards/12289247) | `12289247` | [Scripts/c12289247.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c12289247.lua) | 1 |
| [Radiant Typhoon Varuroon, the Marine Eidolon](/examples/cards/39341885) | `39341885` | [Scripts/c39341885.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c39341885.lua) | 3 |
| [Camelot, Realm of Noble Knights and Noble Arms](/examples/cards/15635751) | `15635751` | [Scripts/c15635751.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c15635751.lua) | 1 |
| [Yummy★Snatchy](/examples/cards/30581601) | `30581601` | [Scripts/c30581601.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c30581601.lua) | 1 |
| Aroma Blend | `25861589` | [Scripts/c25861589.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c25861589.lua) | 1 |
| Red-Eyes Slash Dragon | `21140872` | [Scripts/c21140872.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c21140872.lua) | 1 |
| Plunder Patrollship Jord | `85969517` | [Scripts/c85969517.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c85969517.lua) | 2 |
| Power Tool Braver Dragon | `63265554` | [Scripts/c63265554.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c63265554.lua) | 1 |
| Amazement Administrator Arlekino | `94821366` | [Scripts/c94821366.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c94821366.lua) | 1 |
| DoomZ XII Zero - Drastea | `92472273` | [Scripts/c92472273.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c92472273.lua) | 1 |
| Seven Stars Slash - Army Annihilator Hagun | `65114115` | [Scripts/c65114115.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c65114115.lua) | 1 |
| Zoroa, the Magistus Verethragna | `37260677` | [Scripts/c37260677.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c37260677.lua) | 1 |
| D/D/D Deviser King Deus Machinex | `46593546` | [Scripts/c46593546.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c46593546.lua) | 1 |
| Emperor Charles the Great | `97864322` | [Scripts/c97864322.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c97864322.lua) | 2 |
| Inzektor Picofalena | `97273514` | [Scripts/c97273514.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c97273514.lua) | 1 |
| Dreaming Nemleria | `70155677` | [Scripts/c70155677.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c70155677.lua) | 1 |
| ...and 253 more |  |  |  |

## Script Examples

### Astrograph Sorcerer, the Starfrost Magician (`48171151`)

Source: [Scripts/c48171151.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c48171151.lua)

```lua
function s.pfilter(c,tp)
	return c:IsType(TYPE_PENDULUM) and not c:IsCode(id) and c:GetLeftScale()==1
		and not c:IsForbidden() and c:CheckUniqueOnField(tp)
end
function s.ptg(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Astrograph Sorcerer (`76794549`)

Source: [Scripts/c76794549.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c76794549.lua)

```lua
end
function c76794549.rpfilter(c,e,tp)
	return c:IsCode(94415058) and (not c:IsForbidden()
		or (Duel.GetLocationCount(tp,LOCATION_MZONE)>0 and c:IsCanBeSpecialSummoned(e,0,tp,false,false)))
end
```

### D/D/D Alfred the Divine Sage King (`11852093`)

Source: [Scripts/c11852093.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c11852093.lua)

```lua
end
function s.tffilter(c,tp)
	return c:IsType(TYPE_SPELL+TYPE_TRAP) and c:IsType(TYPE_CONTINUOUS) and c:IsSetCard(0xae) and c:IsFaceupEx() and not c:IsForbidden() and c:CheckUniqueOnField(tp)
end
function s.mfilter(c)
```
