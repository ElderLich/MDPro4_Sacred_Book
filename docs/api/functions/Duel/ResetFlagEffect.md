# Duel.ResetFlagEffect

## Signature

```lua
Duel.ResetFlagEffect(int player, int code) -> void
```

## Description

Resets all player flag effects with code for player.
This clears matching player markers manually; card markers use Card.ResetFlagEffect.

## How To Use It

Use this to manually clear all matching player markers.

```lua
Duel.ResetFlagEffect(tp,id)
```

This only removes player flag effects for the requested player and code. Card markers use `Card.ResetFlagEffect`.

## Related Functions

- [Duel.RegisterFlagEffect](/api/functions/Duel/RegisterFlagEffect)
- [Duel.GetFlagEffect](/api/functions/Duel/GetFlagEffect)

## Parameters

- `player` `int` - Player whose matching flag effects are reset.
- `code` `int` - Flag-effect code to clear.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4855`

## Guided Examples

Learn how to use this function in context:

- [Flag Effects](/learn/flag-effects)
- [Reset Flags And Effect Duration](/learn/reset-flags-and-duration)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **28** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.ResetFlagEffect) with `Duel.ResetFlagEffect`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Ghostrick Renovation](/examples/cards/61818176) | `61818176` | [Scripts/c61818176.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61818176.lua) | 1 |
| Artmage Pact -Awakening- | `23599634` | [Scripts/c23599634.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23599634.lua) | 2 |
| Echelon of the Fire Kings | `38798785` | [Scripts/c38798785.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38798785.lua) | 2 |
| Beyond the Pendulum | `22125101` | [Scripts/c22125101.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22125101.lua) | 1 |
| Favorite Hero | `11881272` | [Scripts/c11881272.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11881272.lua) | 2 |
| Jurrac Volcano | `89948817` | [Scripts/c89948817.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c89948817.lua) | 1 |
| Clown Crew Meteor | `93172951` | [Scripts/c93172951.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93172951.lua) | 2 |
| Odd-Eyes Pendulum Dragon, Four Heavenly Dragons | `75787708` | [Scripts/c75787708.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75787708.lua) | 1 |
| Heart of the Blue-Eyes | `54475145` | [Scripts/c54475145.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54475145.lua) | 1 |
| Sweet Dreams, Nemleria | `44843954` | [Scripts/c44843954.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44843954.lua) | 2 |
| Numeron Wall | `42352091` | [Scripts/c42352091.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42352091.lua) | 2 |
| PenduLuMoon | `66150724` | [Scripts/c66150724.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66150724.lua) | 1 |
| Dragonroid | `9069157` | [Scripts/c9069157.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9069157.lua) | 1 |
| Raise Moon Starter Squeeze | `47605577` | [Scripts/c47605577.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c47605577.lua) | 2 |
| Arcana Force V - The Hierophant | `3376703` | [Scripts/c3376703.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3376703.lua) | 2 |
| The Legendary Fisherman III | `44968687` | [Scripts/c44968687.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44968687.lua) | 1 |
| Trap Tracks | `70825459` | [Scripts/c70825459.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70825459.lua) | 1 |
| Ghost Sister &amp; Spooky Dogwood | `60643553` | [Scripts/c60643553.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60643553.lua) | 1 |
| Trap Trick | `80101899` | [Scripts/c80101899.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80101899.lua) | 1 |
| Spell Wall | `84117021` | [Scripts/c84117021.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84117021.lua) | 2 |
| Mulcharmy Purulia | `84192580` | [Scripts/c84192580.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84192580.lua) | 1 |
| Mulcharmy Fuwalos | `42141493` | [Scripts/c42141493.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42141493.lua) | 1 |
| Mulcharmy Meowls | `87126721` | [Scripts/c87126721.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87126721.lua) | 1 |
| Metaverse | `89208725` | [Scripts/c89208725.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c89208725.lua) | 2 |
| ...and 4 more |  |  |  |

## Script Examples

### Ghostrick Renovation (`61818176`)

Source: [Scripts/c61818176.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61818176.lua)

```lua
		if e:GetLabel()==1 then Duel.RegisterFlagEffect(tp,15248873,RESET_CHAIN,0,1) end
		local g=Duel.GetMatchingGroup(c61818176.actfilter,tp,LOCATION_HAND+LOCATION_DECK,0,nil,tp)
		Duel.ResetFlagEffect(tp,15248873)
		if g:GetCount()>0 and Duel.SelectYesNo(tp,aux.Stringid(61818176,1)) then
			Duel.BreakEffect()
```

### Artmage Pact -Awakening- (`23599634`)

Source: [Scripts/c23599634.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23599634.lua)

```lua
end
function s.resetop(e,tp,eg,ep,ev,re,r,rp)
	Duel.ResetFlagEffect(tp,id)
	e:Reset()
end
```

### Echelon of the Fire Kings (`38798785`)

Source: [Scripts/c38798785.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38798785.lua)

```lua
		Duel.SetChainLimitTillChainEnd(s.efun)
	end
	Duel.ResetFlagEffect(tp,id)
end
function s.resetop(e,tp,eg,ep,ev,re,r,rp)
```
