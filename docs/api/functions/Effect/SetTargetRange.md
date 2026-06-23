# Effect.SetTargetRange

## Signature

```lua
Effect.SetTargetRange(Effect e, int s_range, int o_range) -> void
```

## Description

Sets e's target range fields and clears EFFECT_FLAG_ABSOLUTE_TARGET.
For most field effects, s_range is the affected locations on the handler's controller's side and o_range is the affected locations on the opponent's side. With EFFECT_FLAG_SPSUM_PARAM, they store Special Summon destination player and position.

## How To Use It

For field effects, target range decides which side and location the effect can apply to.

```lua
e1:SetType(EFFECT_TYPE_FIELD)
e1:SetCode(EFFECT_UPDATE_ATTACK)
e1:SetRange(LOCATION_MZONE)
e1:SetTargetRange(LOCATION_MZONE,0)
```

With normal range handling, the first value is the handler controller's side and the second value is the opponent's side. `SetTargetRange` clears the absolute-target flag. Use `Effect.SetAbsoluteRange` when the ranges must mean player 0 and player 1 regardless of who controls the handler.

For Special Summon procedure effects using `EFFECT_FLAG_SPSUM_PARAM`, these fields store the Summon destination player and allowed position instead of card locations.

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

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **2987** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Effect.SetTargetRange`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Pendulum Evolution](/examples/cards/55795155) | `55795155` | [Scripts/c55795155.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55795155.lua) | 77 |
| [Goyo Emperor](/examples/cards/59255742) | `59255742` | [Scripts/c59255742.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59255742.lua) | 70 |
| [Exciting Melffy Time](/examples/cards/58036097) | `58036097` | [Scripts/c58036097.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58036097.lua) | 69 |
| [Deftero Enneacraft - "alazoneIA"](/examples/cards/92171126) | `92171126` | [Scripts/c92171126.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92171126.lua) | 68 |
| [Gem-Knight Dispersion](/examples/cards/24220368) | `24220368` | [Scripts/c24220368.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24220368.lua) | 66 |
| [Lubellion the Searing Dragon](/examples/cards/70534340) | `70534340` | [Scripts/c70534340.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70534340.lua) | 65 |
| [Hecahands Tartaros](/examples/cards/57809669) | `57809669` | [Scripts/c57809669.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57809669.lua) | 65 |
| [Prank-Kids Weather Washer](/examples/cards/44509529) | `44509529` | [Scripts/c44509529.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44509529.lua) | 65 |
| [Enneacraft - Asta.PIXEA](/examples/cards/28454232) | `28454232` | [Scripts/c28454232.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28454232.lua) | 64 |
| [Odd-Eyes Revolution Dragon](/examples/cards/16306932) | `16306932` | [Scripts/c16306932.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16306932.lua) | 64 |
| [Resurgam Xyz](/examples/cards/49082032) | `49082032` | [Scripts/c49082032.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49082032.lua) | 64 |
| [Tohushaddoll Grysta](/examples/cards/95072744) | `95072744` | [Scripts/c95072744.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95072744.lua) | 64 |
| [Enneacraft - Archa.TAIL](/examples/cards/81237046) | `81237046` | [Scripts/c81237046.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81237046.lua) | 63 |
| [Dark End Evaporation Dragon](/examples/cards/62002838) | `62002838` | [Scripts/c62002838.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62002838.lua) | 63 |
| [Future Fusion Nova](/examples/cards/92058902) | `92058902` | [Scripts/c92058902.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92058902.lua) | 63 |
| [Enneacraft - Atil.SPIA](/examples/cards/71801447) | `71801447` | [Scripts/c71801447.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71801447.lua) | 62 |
| [Enneacraft - Aiza.LEON](/examples/cards/82359538) | `82359538` | [Scripts/c82359538.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82359538.lua) | 62 |
| [Ursarctic Polar Star](/examples/cards/62714453) | `62714453` | [Scripts/c62714453.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62714453.lua) | 62 |
| [Vidolium the Unstable Power Patron of Unity](/examples/cards/70488851) | `70488851` | [Scripts/c70488851.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70488851.lua) | 61 |
| [Starving Venemy Dragon](/examples/cards/93729065) | `93729065` | [Scripts/c93729065.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93729065.lua) | 61 |
| [W:P Fancy Ball](/examples/cards/4993187) | `4993187` | [Scripts/c4993187.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4993187.lua) | 61 |
| [Light End Sublimation Dragon](/examples/cards/35614780) | `35614780` | [Scripts/c35614780.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35614780.lua) | 61 |
| [Yummy★Snatchy](/examples/cards/30581601) | `30581601` | [Scripts/c30581601.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30581601.lua) | 61 |
| [Trickstar Diffusion](/examples/cards/63181559) | `63181559` | [Scripts/c63181559.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63181559.lua) | 61 |
| ...and 2963 more |  |  |  |

## Script Examples

### Pendulum Evolution (`55795155`)

Source: [Scripts/c55795155.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55795155.lua)

```lua
		e1:SetCode(EFFECT_EXTRA_PENDULUM_SUMMON)
		e1:SetProperty(EFFECT_FLAG_PLAYER_TARGET)
		e1:SetTargetRange(1,0)
		e1:SetValue(aux.TRUE)
		e1:SetReset(RESET_PHASE+PHASE_END)
```

### Goyo Emperor (`59255742`)

Source: [Scripts/c59255742.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59255742.lua)

```lua
	e1:SetCode(EFFECT_REMOVE_BRAINWASHING)
	e1:SetProperty(EFFECT_FLAG_SET_AVAILABLE)
	e1:SetTargetRange(LOCATION_MZONE,LOCATION_MZONE)
	e1:SetTarget(aux.TargetEqualFunction(Card.GetFlagEffect,1,59255742))
	e1:SetLabelObject(tg)
```

### Exciting Melffy Time (`58036097`)

Source: [Scripts/c58036097.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58036097.lua)

```lua
	e1:SetType(EFFECT_TYPE_FIELD)
	e1:SetCode(EFFECT_IMMUNE_EFFECT)
	e1:SetTargetRange(LOCATION_MZONE,0)
	e1:SetTarget(s.tg)
	e1:SetValue(s.efilter)
```
