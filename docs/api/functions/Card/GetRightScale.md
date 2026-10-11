# Card.GetRightScale

## Signature

```lua
Card.GetRightScale(Card c) -> int
```

## Description

Returns c's current right Pendulum Scale value.
While c is in a Pendulum Zone, the core applies EFFECT_UPDATE_RSCALE and EFFECT_CHANGE_RSCALE modifiers. Outside a Pendulum Zone, it returns the card-data right scale.

## Parameters

- `c` `Card`

## Returns

- `int` - Current right Pendulum Scale value.

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3466`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **9** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.GetRightScale) with `Card.GetRightScale`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Pendulum Evolution](/examples/cards/55795155) | `55795155` | [Scripts/c55795155.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55795155.lua) | 2 |
| Zefraath | `29432356` | [Scripts/c29432356.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29432356.lua) | 1 |
| PenduLuMoon | `66150724` | [Scripts/c66150724.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66150724.lua) | 2 |
| Harmonic Oscillation | `31531170` | [Scripts/c31531170.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31531170.lua) | 2 |
| Performapal Popperup | `11481610` | [Scripts/c11481610.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11481610.lua) | 1 |
| Dharma-Eye Magician | `88757791` | [Scripts/c88757791.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88757791.lua) | 1 |
| Metrognome | `26638543` | [Scripts/c26638543.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c26638543.lua) | 2 |
| Pendulum Scale | `17885118` | [Scripts/c17885118.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17885118.lua) | 2 |
| Zefra Path | `5255013` | [Scripts/c5255013.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5255013.lua) | 1 |

## Script Examples

### Pendulum Evolution (`55795155`)

Source: [Scripts/c55795155.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55795155.lua)

```lua
		local eset={e1}
		local lscale=lpz:GetLeftScale()
		local rscale=rpz:GetRightScale()
		if lscale>rscale then lscale,rscale=rscale,lscale end
		local g=Duel.GetFieldGroup(tp,loc,0)
```

### Zefraath (`29432356`)

Source: [Scripts/c29432356.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29432356.lua)

```lua
		local e2=e1:Clone()
		e2:SetCode(EFFECT_CHANGE_RSCALE)
		e2:SetValue(tc:GetRightScale())
		c:RegisterEffect(e2)
	end
```

### PenduLuMoon (`66150724`)

Source: [Scripts/c66150724.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66150724.lua)

```lua
		if not lc or not rc then return false end
		local lsc=lc:GetLeftScale()
		local rsc=rc:GetRightScale()
		if lsc>rsc then lsc,rsc=rsc,lsc end
		return Duel.IsExistingMatchingCard(c66150724.thfilter2,tp,LOCATION_EXTRA,0,1,nil,lsc,rsc)
```
