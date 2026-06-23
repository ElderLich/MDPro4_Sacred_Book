# Card.GetLeftScale

## Signature

```lua
Card.GetLeftScale(Card c) -> int
```

## Description

Returns c's current left Pendulum Scale value.
While c is in a Pendulum Zone, the core applies EFFECT_UPDATE_LSCALE and EFFECT_CHANGE_LSCALE modifiers. Outside a Pendulum Zone, it returns the card-data left scale.

## Parameters

- `c` `Card`

## Returns

- `int` - Current left Pendulum Scale value.

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3413`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **26** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.GetLeftScale`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Astrograph Sorcerer, the Star Magician](/examples/cards/48171151) | `48171151` | [Scripts/c48171151.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48171151.lua) | 80 |
| [Pendulum Evolution](/examples/cards/55795155) | `55795155` | [Scripts/c55795155.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55795155.lua) | 77 |
| [D/D/D/D Super-Dimensional Sovereign Emperor Zero Paradox](/examples/cards/97417863) | `97417863` | [Scripts/c97417863.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97417863.lua) | 62 |
| Performage Ball Balancer | `92530005` | [Scripts/c92530005.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92530005.lua) | 51 |
| Zefraath | `29432356` | [Scripts/c29432356.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29432356.lua) | 49 |
| PenduLuMoon | `66150724` | [Scripts/c66150724.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66150724.lua) | 48 |
| Speedroid Passinglider | `26420373` | [Scripts/c26420373.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c26420373.lua) | 47 |
| Performage Wind Drainer | `70417076` | [Scripts/c70417076.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70417076.lua) | 46 |
| D/D Savant Kepler | `11609969` | [Scripts/c11609969.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11609969.lua) | 44 |
| Solving for Pendulum | `5208118` | [Scripts/c5208118.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5208118.lua) | 44 |
| Harmonic Oscillation | `31531170` | [Scripts/c31531170.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31531170.lua) | 44 |
| D/D Savant Galilei | `74605254` | [Scripts/c74605254.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74605254.lua) | 43 |
| Performapal Popperup | `11481610` | [Scripts/c11481610.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11481610.lua) | 43 |
| D/D Scale Surveyor | `42382265` | [Scripts/c42382265.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42382265.lua) | 41 |
| Dharma-Eye Magician | `88757791` | [Scripts/c88757791.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88757791.lua) | 41 |
| Soul Pendulum | `34884015` | [Scripts/c34884015.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34884015.lua) | 41 |
| Wisdom-Eye Magician | `72714461` | [Scripts/c72714461.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c72714461.lua) | 40 |
| Metrognome | `26638543` | [Scripts/c26638543.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c26638543.lua) | 34 |
| Pendulum Scale | `17885118` | [Scripts/c17885118.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17885118.lua) | 34 |
| Performapal Parrotrio | `56675280` | [Scripts/c56675280.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56675280.lua) | 31 |
| Zefra Path | `5255013` | [Scripts/c5255013.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5255013.lua) | 27 |
| Performapal Trumpanda | `32787239` | [Scripts/c32787239.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32787239.lua) | 24 |
| Pendulum Shift | `69982329` | [Scripts/c69982329.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c69982329.lua) | 23 |
| Mild Turkey | `47558785` | [Scripts/c47558785.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c47558785.lua) | 21 |
| ...and 2 more |  |  |  |

## Script Examples

### Astrograph Sorcerer, the Star Magician (`48171151`)

Source: [Scripts/c48171151.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48171151.lua)

```lua
end
function s.pfilter(c,tp)
	return c:IsType(TYPE_PENDULUM) and not c:IsCode(id) and c:GetLeftScale()==1
		and not c:IsForbidden() and c:CheckUniqueOnField(tp)
end
```

### Pendulum Evolution (`55795155`)

Source: [Scripts/c55795155.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55795155.lua)

```lua
		Duel.RegisterEffect(e1,tp)
		local eset={e1}
		local lscale=lpz:GetLeftScale()
		local rscale=rpz:GetRightScale()
		if lscale>rscale then lscale,rscale=rscale,lscale end
```

### D/D/D/D Super-Dimensional Sovereign Emperor Zero Paradox (`97417863`)

Source: [Scripts/c97417863.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97417863.lua)

```lua
	local pg=Duel.GetFieldGroup(tp,LOCATION_PZONE,0)
	if #pg==0 then return false end
	local pval=pg:GetSum(Card.GetLeftScale)
	local g=eg:Filter(c97417863.cfilter,nil,tp)
	local lv=g:GetSum(Card.GetLevel)
```
