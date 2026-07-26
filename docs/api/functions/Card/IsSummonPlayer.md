# Card.IsSummonPlayer

## Signature

```lua
Card.IsSummonPlayer(Card c, int player) -> bool
```

## Description

Checks whether player was the player who Summoned c.

## Parameters

- `c` `Card`
- `player` `int`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3506`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **254** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.IsSummonPlayer`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Goyo Emperor](/examples/cards/59255742) | `59255742` | [Scripts/c59255742.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59255742.lua) | 70 |
| [D/D Count Surveyor](/examples/cards/5997110) | `5997110` | [Scripts/c5997110.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5997110.lua) | 63 |
| [D/D/D/D Super-Dimensional Sovereign Emperor Zero Paradox](/examples/cards/97417863) | `97417863` | [Scripts/c97417863.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97417863.lua) | 62 |
| [Chef de Nouvelles](/examples/cards/29251488) | `29251488` | [Scripts/c29251488.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29251488.lua) | 60 |
| Starving Venom Wing Dragon | `5148778` | [Scripts/c5148778.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5148778.lua) | 60 |
| Artmage Pact -Awakening- | `23599634` | [Scripts/c23599634.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23599634.lua) | 60 |
| Trickstar Light Arena | `63492244` | [Scripts/c63492244.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63492244.lua) | 59 |
| Plunder Patrollship Jord | `85969517` | [Scripts/c85969517.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85969517.lua) | 58 |
| Flame Swordsrealm | `73714736` | [Scripts/c73714736.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c73714736.lua) | 58 |
| Amazement Administrator Arlekino | `94821366` | [Scripts/c94821366.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c94821366.lua) | 57 |
| Awakening of the Sacred Beasts | `53701259` | [Scripts/c53701259.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53701259.lua) | 57 |
| Union Activation | `38527680` | [Scripts/c38527680.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38527680.lua) | 57 |
| Lunalight Masquerade | `2344618` | [Scripts/c2344618.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2344618.lua) | 57 |
| GMX - VELOX | `82706696` | [Scripts/c82706696.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82706696.lua) | 56 |
| Magellanica, the Deep Sea City | `26534688` | [Scripts/c26534688.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c26534688.lua) | 56 |
| Theia, the Primal Being | `85687952` | [Scripts/c85687952.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85687952.lua) | 56 |
| Veda Kalarcanum | `40785230` | [Scripts/c40785230.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40785230.lua) | 55 |
| Melffy Rabbys | `46955132` | [Scripts/c46955132.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46955132.lua) | 55 |
| Gunkan Sushipyard Seaside Supper Spot | `62200831` | [Scripts/c62200831.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62200831.lua) | 54 |
| PSY-Framegear Alpha | `75425043` | [Scripts/c75425043.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75425043.lua) | 54 |
| Megalith Anastasis | `29876299` | [Scripts/c29876299.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29876299.lua) | 54 |
| Fabled Realm's Revival | `57775790` | [Scripts/c57775790.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57775790.lua) | 54 |
| Gagaga Girl - Cell Phone Subtraction | `48393693` | [Scripts/c48393693.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48393693.lua) | 53 |
| Jurrac Volcano | `89948817` | [Scripts/c89948817.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c89948817.lua) | 53 |
| ...and 230 more |  |  |  |

## Script Examples

### Goyo Emperor (`59255742`)

Source: [Scripts/c59255742.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59255742.lua)

```lua
end
function c59255742.filter(c,tp)
	return c:IsSummonPlayer(1-tp) and c:IsControlerCanBeChanged(true)
end
function c59255742.target(e,tp,eg,ep,ev,re,r,rp,chk)
```

### D/D Count Surveyor (`5997110`)

Source: [Scripts/c5997110.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5997110.lua)

```lua
end
function s.rlcfilter(c,tp)
	return c:IsFaceup() and c:IsSetCard(0x10af) and c:IsSummonPlayer(tp) and c:IsSummonType(SUMMON_TYPE_PENDULUM)
end
function s.rlcon(e,tp,eg,ep,ev,re,r,rp)
```

### D/D/D/D Super-Dimensional Sovereign Emperor Zero Paradox (`97417863`)

Source: [Scripts/c97417863.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97417863.lua)

```lua
end
function c97417863.cfilter(c,tp)
	return c:IsSummonPlayer(tp) and c:IsSummonType(SUMMON_TYPE_PENDULUM) and c:IsFaceup()
end
function c97417863.spcon(e,tp,eg,ep,ev,re,r,rp)
```
