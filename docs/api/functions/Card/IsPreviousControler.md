# Card.IsPreviousControler

## Signature

```lua
Card.IsPreviousControler(Card c, int player) -> bool
```

## Description

Check if card c's previous controller was player

## Parameters

- `c` `Card`
- `player` `int`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3608`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **761** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.IsPreviousControler`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Astrograph Sorcerer, the Star Magician](/examples/cards/48171151) | `48171151` | [Scripts/c48171151.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48171151.lua) | 80 |
| [Astrograph Sorcerer](/examples/cards/76794549) | `76794549` | [Scripts/c76794549.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76794549.lua) | 71 |
| [Mementotlan Fusion](/examples/cards/66518509) | `66518509` | [Scripts/c66518509.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66518509.lua) | 67 |
| [Aiwass the Spirit of the Law](/examples/cards/84288367) | `84288367` | [Scripts/c84288367.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84288367.lua) | 64 |
| [Teleport Fusion](/examples/cards/36494597) | `36494597` | [Scripts/c36494597.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36494597.lua) | 64 |
| [D/D/D/D Super-Dimensional Sovereign Emperor Zero Paradox](/examples/cards/97417863) | `97417863` | [Scripts/c97417863.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97417863.lua) | 62 |
| [Bujinki Ahashima](/examples/cards/71095768) | `71095768` | [Scripts/c71095768.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71095768.lua) | 62 |
| [Chronograph Sorcerer](/examples/cards/12289247) | `12289247` | [Scripts/c12289247.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12289247.lua) | 61 |
| [Cyber Pharos](/examples/cards/29719112) | `29719112` | [Scripts/c29719112.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29719112.lua) | 61 |
| D/D Extra Surveyor | `74387963` | [Scripts/c74387963.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74387963.lua) | 60 |
| Flowering Etoile the Melodious Magnificat | `83793721` | [Scripts/c83793721.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c83793721.lua) | 60 |
| Fossil Fusion | `59419719` | [Scripts/c59419719.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59419719.lua) | 60 |
| Supreme King Dragon Lightwurm | `41908872` | [Scripts/c41908872.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41908872.lua) | 59 |
| Performapal Celestial Magician | `58092907` | [Scripts/c58092907.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58092907.lua) | 58 |
| Cyberse Reminder | `56337500` | [Scripts/c56337500.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56337500.lua) | 58 |
| Mementotlan Shleepy | `50042011` | [Scripts/c50042011.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50042011.lua) | 58 |
| S:P Little Knight | `29301450` | [Scripts/c29301450.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29301450.lua) | 58 |
| Dragon Master Magia | `12381100` | [Scripts/c12381100.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12381100.lua) | 57 |
| Windwitch - Crystal Bell | `25793414` | [Scripts/c25793414.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25793414.lua) | 57 |
| Seven Stars Slash - Army Annihilator Hagun | `65114115` | [Scripts/c65114115.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65114115.lua) | 57 |
| Berserkion the Electromagna Warrior | `42901635` | [Scripts/c42901635.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42901635.lua) | 56 |
| Performage Trapeze Magician | `17016362` | [Scripts/c17016362.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17016362.lua) | 56 |
| Number 38: Hope Harbinger Dragon Titanic Galaxy | `63767246` | [Scripts/c63767246.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63767246.lua) | 56 |
| Abyss-steam | `63941169` | [Scripts/c63941169.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63941169.lua) | 56 |
| ...and 737 more |  |  |  |

## Script Examples

### Astrograph Sorcerer, the Star Magician (`48171151`)

Source: [Scripts/c48171151.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48171151.lua)

```lua
end
function s.desfilter(c,tp)
	return c:IsPreviousControler(tp) and c:IsPreviousPosition(POS_FACEUP) and c:IsReason(REASON_BATTLE+REASON_EFFECT)
		and c:GetOriginalType()&TYPE_MONSTER~=0 and c:IsPreviousLocation(LOCATION_ONFIELD)
end
```

### Astrograph Sorcerer (`76794549`)

Source: [Scripts/c76794549.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76794549.lua)

```lua
function c76794549.spcfilter(c,tp)
	return c:IsReason(REASON_BATTLE+REASON_EFFECT)
		and c:IsPreviousControler(tp) and c:IsPreviousLocation(LOCATION_ONFIELD)
end
function c76794549.regcon(e,tp,eg,ep,ev,re,r,rp)
```

### Mementotlan Fusion (`66518509`)

Source: [Scripts/c66518509.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66518509.lua)

```lua
function s.regop(e,tp,eg,ep,ev,re,r,rp)
	local g=eg:Filter(s.spcfilter,nil)
	if g:IsExists(Card.IsPreviousControler,1,nil,0) then
		Duel.RegisterFlagEffect(0,id,RESET_PHASE+PHASE_END,EFFECT_FLAG_OATH,1)
	end
```
