# Duel.GetControl

## Signature

```lua
Duel.GetControl(Card|Group targets, int player, [int reset_phase], [int reset_count], [int zone]) -> int
```

## Description

Moves control of targets to player and returns the number of cards whose control actually changed.
Use reset_phase and reset_count for temporary control, such as PHASE_END, 1. To pass only a zone mask, use 0, 0, zone.
Use Card.IsControlerCanBeChanged in target filters and recheck relation before changing control at resolution.

## How To Use It

Use this when an effect takes control of cards.

For temporary control, pass a phase and count. For permanent control, omit those arguments. If you only need to restrict the destination zone, pass `0,0,zone` before the zone mask.

```lua
local tc=Duel.GetFirstTarget()
if tc and tc:IsRelateToEffect(e) then
    Duel.GetControl(tc,tp,PHASE_END,1)
end
```

The return value is the number of cards that actually changed control, so use `>0` when later logic depends on success.

## Related Functions

- [Card.IsControler](/api/functions/Card/IsControler)
- [Duel.SwapControl](/api/functions/Duel/SwapControl)
- [Duel.CheckLocation](/api/functions/Duel/CheckLocation)

## Parameters

- `targets` `Card|Group`
- `player` `int`
- `reset_phase` `int` optional - default: 0
- `reset_count` `int` optional - default: 0
- `zone` `int` optional - default: 0xff

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4906`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **159** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.GetControl) with `Duel.GetControl`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Goyo Emperor](/examples/cards/59255742) | `59255742` | [Scripts/c59255742.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59255742.lua) | 1 |
| [Tellusion the Magna Warrior](/examples/cards/24431911) | `24431911` | [Scripts/c24431911.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24431911.lua) | 1 |
| Enlilgirsu, the Orcust Mekk-Knight | `74820316` | [Scripts/c74820316.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74820316.lua) | 1 |
| R.B. Lambda Blade | `17188206` | [Scripts/c17188206.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17188206.lua) | 1 |
| Phara the Primordial Goddess | `82344137` | [Scripts/c82344137.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82344137.lua) | 1 |
| Eternal Bond | `45283341` | [Scripts/c45283341.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45283341.lua) | 1 |
| Possessed Destiny - Wynn | `60516416` | [Scripts/c60516416.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60516416.lua) | 1 |
| Borreload Dragon | `31833038` | [Scripts/c31833038.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31833038.lua) | 1 |
| Fabled Levilazebul | `21281085` | [Scripts/c21281085.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21281085.lua) | 1 |
| Primite Howl | `41488249` | [Scripts/c41488249.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41488249.lua) | 1 |
| Vanquish Soul Hollie Sue | `93156774` | [Scripts/c93156774.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93156774.lua) | 1 |
| Distrust Paranoia | `81965543` | [Scripts/c81965543.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81965543.lua) | 1 |
| Amaze Attraction Viking Vortex | `97182396` | [Scripts/c97182396.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97182396.lua) | 1 |
| Hecahands Xeno | `94410955` | [Scripts/c94410955.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c94410955.lua) | 1 |
| Evil Lord - Zorc | `73320394` | [Scripts/c73320394.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c73320394.lua) | 1 |
| Chaotic Elements | `92221402` | [Scripts/c92221402.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92221402.lua) | 1 |
| SPYRAL MISSION - Recapture | `39373426` | [Scripts/c39373426.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39373426.lua) | 1 |
| Ancient Warriors Saga - Deception and Betrayal | `45115956` | [Scripts/c45115956.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45115956.lua) | 1 |
| Angelechy Enlisted | `81797573` | [Scripts/c81797573.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81797573.lua) | 1 |
| Altergeist Adminia | `61470213` | [Scripts/c61470213.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61470213.lua) | 1 |
| Time Thief Double Barrel | `91135480` | [Scripts/c91135480.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c91135480.lua) | 1 |
| Borreload Liberator Dragon | `27096833` | [Scripts/c27096833.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27096833.lua) | 1 |
| Metaphys Horus | `36898537` | [Scripts/c36898537.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36898537.lua) | 1 |
| Tragoedia | `98777036` | [Scripts/c98777036.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c98777036.lua) | 1 |
| ...and 135 more |  |  |  |

## Script Examples

### Goyo Emperor (`59255742`)

Source: [Scripts/c59255742.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59255742.lua)

```lua
	local g=Duel.GetChainInfo(0,CHAININFO_TARGET_CARDS):Filter(Card.IsRelateToEffect,nil,e)
	if Duel.GetLocationCount(tp,LOCATION_MZONE)<g:GetCount() then return end
	Duel.GetControl(g,tp)
end
function c59255742.ctcon(e,tp,eg,ep,ev,re,r,rp)
```

### Tellusion the Magna Warrior (`24431911`)

Source: [Scripts/c24431911.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24431911.lua)

```lua
		if e:GetLabel()==1 and tc:IsControlerCanBeChanged()
			and Duel.SelectYesNo(tp,aux.Stringid(id,3)) then
			Duel.GetControl(tc,tp)
		else
			Duel.Destroy(tc,REASON_EFFECT)
```

### Enlilgirsu, the Orcust Mekk-Knight (`74820316`)

Source: [Scripts/c74820316.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74820316.lua)

```lua
			if cg:GetCount()>0 then
				Duel.HintSelection(cg)
				Duel.GetControl(cg:GetFirst(),tp)
			end
		end
```
