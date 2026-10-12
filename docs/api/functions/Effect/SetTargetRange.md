# Effect.SetTargetRange

## Signature

```lua
Effect.SetTargetRange(Effect e, int s_range, int o_range) -> void
```

## Description

Sets e's target range fields and clears EFFECT_FLAG_ABSOLUTE_TARGET.
For most field effects, s_range is the affected locations on the handler's controller's side and o_range is the affected locations on the opponent's side. With EFFECT_FLAG_SPSUM_PARAM, they store Special Summon destination player and position.
Use Effect.SetAbsoluteRange when the affected sides must be fixed to a specific player instead of relative to the handler.

## How To Use It

Use this for the cards or players affected by a field-like effect, or for special meanings required by certain properties.

```lua
e1:SetRange(LOCATION_MZONE)
e1:SetTargetRange(0,LOCATION_MZONE)
```

The local binding writes `s_range` and `o_range` and clears `EFFECT_FLAG_ABSOLUTE_TARGET`. For absolute player-oriented ranges, use `Effect.SetAbsoluteRange`.

## Related Functions

- [Effect.SetRange](/api/functions/Effect/SetRange)
- [Effect.SetAbsoluteRange](/api/functions/Effect/SetAbsoluteRange)
- [Effect.SetProperty](/api/functions/Effect/SetProperty)

## Parameters

- `e` `Effect` - Effect whose target range fields are being set.
- `s_range` `int` - Usually the handler controller's affected locations. With EFFECT_FLAG_SPSUM_PARAM, this is the allowed Special Summon position.
- `o_range` `int` - Usually the opponent's affected locations. With EFFECT_FLAG_SPSUM_PARAM, this is the destination player value for the Special Summon.

## Source

- `D:\Programs\GitHub\ygopro-core\libeffect.cpp:615`

## Guided Examples

Learn how to use this function in context:

- [Battle Position Effects](/learn/battle-position-effects)
- [Common Script Errors And Debugging](/learn/common-script-errors-and-debugging)
- [Effects That Apply Continuously](/learn/continuous-effects)
- [Continuous Stat Modifiers](/learn/continuous-stat-modifiers)
- [Creation, Building, and Registration of an Effect Object](/learn/effect-object)
- [EFFECT_TYPE Constants and Templates](/learn/effect-types)

::: details More guided lessons (5)

- [Field Spells](/learn/field-spells)
- [First Scripts To Study](/learn/first-scripts)
- [Normal And Continuous Traps](/learn/normal-and-continuous-traps)
- [Special Summon-Only Monster Guide](/learn/special-summon-only-monsters)
- [Tribute Summon Materials](/learn/tribute-summon-materials)

:::

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **3047** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Effect.SetTargetRange) with `Effect.SetTargetRange`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Pendulum Evolution](/examples/cards/55795155) | `55795155` | [Scripts/c55795155.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c55795155.lua) | 2 |
| [Azure Ocean Dragon Lord - Neo-Daedalus Rage](/examples/cards/41570943) | `41570943` | [Scripts/c41570943.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c41570943.lua) | 1 |
| [Goyo Emperor](/examples/cards/59255742) | `59255742` | [Scripts/c59255742.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c59255742.lua) | 1 |
| [Melffy Playtime Surprise](/examples/cards/58036097) | `58036097` | [Scripts/c58036097.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c58036097.lua) | 1 |
| [Deftero Enneacraft - "alazoneIA"](/examples/cards/92171126) | `92171126` | [Scripts/c92171126.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c92171126.lua) | 1 |
| [Gem-Knight Dispersion](/examples/cards/24220368) | `24220368` | [Scripts/c24220368.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c24220368.lua) | 1 |
| [Lubellion the Searing Dragon](/examples/cards/70534340) | `70534340` | [Scripts/c70534340.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c70534340.lua) | 1 |
| [Destratification Dino Stratiae](/examples/cards/3841104) | `3841104` | [Scripts/c3841104.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c3841104.lua) | 1 |
| [Hecahands Tartaros](/examples/cards/57809669) | `57809669` | [Scripts/c57809669.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c57809669.lua) | 2 |
| [Prank-Kids Weather Washer](/examples/cards/44509529) | `44509529` | [Scripts/c44509529.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c44509529.lua) | 1 |
| [Enneacraft - Asta.PIXEA](/examples/cards/28454232) | `28454232` | [Scripts/c28454232.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c28454232.lua) | 2 |
| [Odd-Eyes Revolution Dragon](/examples/cards/16306932) | `16306932` | [Scripts/c16306932.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c16306932.lua) | 1 |
| [Resurgam Xyz](/examples/cards/49082032) | `49082032` | [Scripts/c49082032.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c49082032.lua) | 1 |
| [Tohushaddoll Grysta](/examples/cards/95072744) | `95072744` | [Scripts/c95072744.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c95072744.lua) | 1 |
| [Enneacraft - Archa.TAIL](/examples/cards/81237046) | `81237046` | [Scripts/c81237046.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c81237046.lua) | 2 |
| [Dark End Evaporation Dragon](/examples/cards/62002838) | `62002838` | [Scripts/c62002838.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c62002838.lua) | 1 |
| [Future Fusion Nova](/examples/cards/92058902) | `92058902` | [Scripts/c92058902.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c92058902.lua) | 2 |
| [Enneacraft - Atil.SPIA](/examples/cards/71801447) | `71801447` | [Scripts/c71801447.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c71801447.lua) | 1 |
| [Enneacraft - Aiza.LEON](/examples/cards/82359538) | `82359538` | [Scripts/c82359538.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c82359538.lua) | 1 |
| [Ursarctic Polar Star](/examples/cards/62714453) | `62714453` | [Scripts/c62714453.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c62714453.lua) | 1 |
| [Vidolium the Unstable Power Patron of Unity](/examples/cards/70488851) | `70488851` | [Scripts/c70488851.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c70488851.lua) | 1 |
| [Starving Venemy Dragon](/examples/cards/93729065) | `93729065` | [Scripts/c93729065.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c93729065.lua) | 1 |
| [W:P Fancy Ball](/examples/cards/4993187) | `4993187` | [Scripts/c4993187.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c4993187.lua) | 2 |
| [Cerynemesia, Mystical Beast of the Forest](/examples/cards/43632709) | `43632709` | [Scripts/c43632709.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c43632709.lua) | 1 |
| ...and 3023 more |  |  |  |

## Script Examples

### Pendulum Evolution (`55795155`)

Source: [Scripts/c55795155.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c55795155.lua)

```lua
		e1:SetCode(EFFECT_EXTRA_PENDULUM_SUMMON)
		e1:SetProperty(EFFECT_FLAG_PLAYER_TARGET)
		e1:SetTargetRange(1,0)
		e1:SetValue(aux.TRUE)
		e1:SetReset(RESET_PHASE+PHASE_END)
```

### Azure Ocean Dragon Lord - Neo-Daedalus Rage (`41570943`)

Source: [Scripts/c41570943.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c41570943.lua)

```lua
	e1:SetCode(EFFECT_CANNOT_SPECIAL_SUMMON)
	e1:SetReset(RESET_PHASE+PHASE_END)
	e1:SetTargetRange(1,0)
	Duel.RegisterEffect(e1,tp)
end
```

### Goyo Emperor (`59255742`)

Source: [Scripts/c59255742.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c59255742.lua)

```lua
	e1:SetCode(EFFECT_REMOVE_BRAINWASHING)
	e1:SetProperty(EFFECT_FLAG_SET_AVAILABLE)
	e1:SetTargetRange(LOCATION_MZONE,LOCATION_MZONE)
	e1:SetTarget(aux.TargetEqualFunction(Card.GetFlagEffect,1,59255742))
	e1:SetLabelObject(tg)
```
