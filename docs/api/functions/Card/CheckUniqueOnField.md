# Card.CheckUniqueOnField

## Signature

```lua
Card.CheckUniqueOnField(Card c, int check_player, [int check_location], [Card|nil icard]) -> bool
```

## Description

Checks whether c can coexist on check_player's field under the current unique-on-field rules.
check_location defaults to LOCATION_ONFIELD and is masked to on-field locations. icard can be supplied as an ignored card when testing a pending move.

## Parameters

- `c` `Card` - Card being tested against unique-on-field restrictions.
- `check_player` `int` - Player whose field is checked for a uniqueness conflict.
- `check_location` `int` optional - On-field location mask to check; default: LOCATION_ONFIELD. The core masks this value to LOCATION_ONFIELD.
- `icard` `Card|nil` optional - Optional card ignored during the check, useful when testing a pending replacement or move.

## Returns

- `bool` - True if c can coexist under the unique-on-field rules for the requested player and location.

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3713`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **197** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.CheckUniqueOnField) with `Card.CheckUniqueOnField`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Astrograph Sorcerer, the Starfrost Magician](/examples/cards/48171151) | `48171151` | [Scripts/c48171151.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c48171151.lua) | 1 |
| [D/D/D Alfred the Divine Sage King](/examples/cards/11852093) | `11852093` | [Scripts/c11852093.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c11852093.lua) | 1 |
| [Pere-Zenet Em Heru](/examples/cards/46273941) | `46273941` | [Scripts/c46273941.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c46273941.lua) | 1 |
| [Am Duazenet](/examples/cards/45151304) | `45151304` | [Scripts/c45151304.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c45151304.lua) | 1 |
| [Shining Draw](/examples/cards/35906693) | `35906693` | [Scripts/c35906693.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c35906693.lua) | 1 |
| [Plunder Patroll Shipshape Ships Shipping](/examples/cards/44227727) | `44227727` | [Scripts/c44227727.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c44227727.lua) | 1 |
| [Radiant Typhoon Varuroon, the Marine Eidolon](/examples/cards/39341885) | `39341885` | [Scripts/c39341885.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c39341885.lua) | 3 |
| [Camelot, Realm of Noble Knights and Noble Arms](/examples/cards/15635751) | `15635751` | [Scripts/c15635751.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c15635751.lua) | 1 |
| [Yummy★Snatchy](/examples/cards/30581601) | `30581601` | [Scripts/c30581601.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c30581601.lua) | 1 |
| Red-Eyes Slash Dragon | `21140872` | [Scripts/c21140872.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c21140872.lua) | 1 |
| Power Tool Braver Dragon | `63265554` | [Scripts/c63265554.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c63265554.lua) | 1 |
| DoomZ XII Zero - Drastea | `92472273` | [Scripts/c92472273.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c92472273.lua) | 1 |
| Seven Stars Slash - Army Annihilator Hagun | `65114115` | [Scripts/c65114115.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c65114115.lua) | 1 |
| Zoroa, the Magistus Verethragna | `37260677` | [Scripts/c37260677.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c37260677.lua) | 1 |
| Emperor Charles the Great | `97864322` | [Scripts/c97864322.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c97864322.lua) | 2 |
| Inzektor Picofalena | `97273514` | [Scripts/c97273514.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c97273514.lua) | 1 |
| Dreaming Nemleria | `70155677` | [Scripts/c70155677.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c70155677.lua) | 1 |
| Yummy☆Surprise | `29369059` | [Scripts/c29369059.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c29369059.lua) | 1 |
| Sosei Ryu-Ge Mistva | `92487128` | [Scripts/c92487128.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c92487128.lua) | 1 |
| Spirit Poacher | `85150300` | [Scripts/c85150300.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c85150300.lua) | 1 |
| The Continuing Epic of Charles | `11802691` | [Scripts/c11802691.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c11802691.lua) | 3 |
| Angelechy Problem | `17782288` | [Scripts/c17782288.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c17782288.lua) | 1 |
| Dragunity Arma Gram | `53184342` | [Scripts/c53184342.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c53184342.lua) | 1 |
| Chaos Allure Queen | `29925614` | [Scripts/c29925614.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c29925614.lua) | 1 |
| ...and 173 more |  |  |  |

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

### D/D/D Alfred the Divine Sage King (`11852093`)

Source: [Scripts/c11852093.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c11852093.lua)

```lua
end
function s.tffilter(c,tp)
	return c:IsType(TYPE_SPELL+TYPE_TRAP) and c:IsType(TYPE_CONTINUOUS) and c:IsSetCard(0xae) and c:IsFaceupEx() and not c:IsForbidden() and c:CheckUniqueOnField(tp)
end
function s.mfilter(c)
```

### Pere-Zenet Em Heru (`46273941`)

Source: [Scripts/c46273941.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c46273941.lua)

```lua
end
function s.eqfilter(c,tp)
	return c:IsType(TYPE_NORMAL) and c:CheckUniqueOnField(tp) and not c:IsForbidden()
end
function s.spop(e,tp,eg,ep,ev,re,r,rp)
```
