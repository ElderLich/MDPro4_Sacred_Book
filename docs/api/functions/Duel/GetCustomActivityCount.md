# Duel.GetCustomActivityCount

## Signature

```lua
Duel.GetCustomActivityCount(int counter_id, int player, int activity_type) -> int
```

## Description

Counter number counter_id count, the number of players to return to the following (currently up to 1)
The activity_type is of the following type
ACTIVITY_SUMMON call (not including the usual call set)
ACTIVITY_NORMALSUMMON usually called (including the usual call set)
ACTIVITY_SPSUMMON Special call
ACTIVITY_FLIPSUMMON Reverse call
ACTIVITY_CHAIN ​​Activates the effect

## Parameters

- `counter_id` `int`
- `player` `int`
- `activity_type` `int`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5069`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **172** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.GetCustomActivityCount`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Deftero Enneacraft - "alazoneIA"](/examples/cards/92171126) | `92171126` | [Scripts/c92171126.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92171126.lua) | 68 |
| [Enneacraft - Asta.PIXEA](/examples/cards/28454232) | `28454232` | [Scripts/c28454232.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28454232.lua) | 64 |
| [Tohushaddoll Grysta](/examples/cards/95072744) | `95072744` | [Scripts/c95072744.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95072744.lua) | 64 |
| [Enneacraft - Archa.TAIL](/examples/cards/81237046) | `81237046` | [Scripts/c81237046.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81237046.lua) | 63 |
| [Enneacraft - Atil.SPIA](/examples/cards/71801447) | `71801447` | [Scripts/c71801447.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71801447.lua) | 62 |
| [Enneacraft - Aiza.LEON](/examples/cards/82359538) | `82359538` | [Scripts/c82359538.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82359538.lua) | 62 |
| Cyberse Reminder | `56337500` | [Scripts/c56337500.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56337500.lua) | 58 |
| Enneacraft - Atori.MAR | `54842941` | [Scripts/c54842941.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54842941.lua) | 57 |
| Number 99: Utopia Dragonar | `95134948` | [Scripts/c95134948.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95134948.lua) | 57 |
| Hi-Speedroid Cork Shooter | `23361526` | [Scripts/c23361526.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23361526.lua) | 56 |
| Xtra HERO Cross Crusader | `58004362` | [Scripts/c58004362.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58004362.lua) | 56 |
| Dreaming Nemleria | `70155677` | [Scripts/c70155677.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70155677.lua) | 55 |
| Thunder Dragonlord | `5206415` | [Scripts/c5206415.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5206415.lua) | 54 |
| Megaroid City | `44139064` | [Scripts/c44139064.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44139064.lua) | 53 |
| Chaos Emperor Dragon - Envoy of the End | `82301904` | [Scripts/c82301904.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82301904.lua) | 53 |
| Ekto Enneacraft - "tromarIA" | `29570824` | [Scripts/c29570824.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29570824.lua) | 52 |
| Enato Enneacraft - "oknirIA" | `55965529` | [Scripts/c55965529.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55965529.lua) | 52 |
| Masked HERO Furnace | `58288218` | [Scripts/c58288218.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58288218.lua) | 52 |
| Branded Fusion | `44362883` | [Scripts/c44362883.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44362883.lua) | 52 |
| Trito Enneacraft - "exapatisIA" | `44716748` | [Scripts/c44716748.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44716748.lua) | 51 |
| Proto Enneacraft - "orgIA" | `56187077` | [Scripts/c56187077.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56187077.lua) | 51 |
| Dream Tower of Princess Nemleria | `18458255` | [Scripts/c18458255.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18458255.lua) | 51 |
| Dawn Angel Kambi | `12500059` | [Scripts/c12500059.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12500059.lua) | 51 |
| Absorb Fusion | `71422989` | [Scripts/c71422989.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71422989.lua) | 51 |
| ...and 148 more |  |  |  |

## Script Examples

### Deftero Enneacraft - "alazoneIA" (`92171126`)

Source: [Scripts/c92171126.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92171126.lua)

```lua
function s.spcost(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return not e:GetHandler():IsPublic()
		and Duel.GetCustomActivityCount(id,tp,ACTIVITY_SPSUMMON)==0 end
	local e1=Effect.CreateEffect(e:GetHandler())
	e1:SetType(EFFECT_TYPE_FIELD)
```

### Enneacraft - Asta.PIXEA (`28454232`)

Source: [Scripts/c28454232.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28454232.lua)

```lua
function s.spcost(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return not e:GetHandler():IsPublic()
		and Duel.GetCustomActivityCount(id,tp,ACTIVITY_SPSUMMON)==0 end
	local e1=Effect.CreateEffect(e:GetHandler())
	e1:SetType(EFFECT_TYPE_FIELD)
```

### Tohushaddoll Grysta (`95072744`)

Source: [Scripts/c95072744.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95072744.lua)

```lua
end
function s.fspcost(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.GetCustomActivityCount(id,tp,ACTIVITY_SPSUMMON)==0 end
	local e1=Effect.CreateEffect(e:GetHandler())
	e1:SetType(EFFECT_TYPE_FIELD)
```
