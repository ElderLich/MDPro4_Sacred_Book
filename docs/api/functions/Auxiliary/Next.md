# Auxiliary.Next

## Signature

```lua
Auxiliary.Next(Group g) -> function
```

## Description

Returns an iterator over g for generic for loops, using Group.GetFirst and Group.GetNext internally.

## Parameters

- `g` `Group`

## Returns

- `function` - Iterator function for generic for loops.

## Source

- `Utilities/utility.lua:82`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **311** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.Next) with `Auxiliary.Next`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Levia-Dragoon - Daedalus](/examples/cards/78579058) | `78579058` | [Scripts/c78579058.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c78579058.lua) | 1 |
| [Azure Ocean Dragon Lord - Neo-Daedalus Rage](/examples/cards/41570943) | `41570943` | [Scripts/c41570943.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c41570943.lua) | 1 |
| [Goyo Emperor](/examples/cards/59255742) | `59255742` | [Scripts/c59255742.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c59255742.lua) | 1 |
| [D/D/D Alfred the Divine Sage King](/examples/cards/11852093) | `11852093` | [Scripts/c11852093.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c11852093.lua) | 1 |
| [Destratification Dino Stratiae](/examples/cards/3841104) | `3841104` | [Scripts/c3841104.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c3841104.lua) | 1 |
| [GMX 55th Experiment Report](/examples/cards/38984832) | `38984832` | [Scripts/c38984832.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c38984832.lua) | 1 |
| [D/D/D/D Dimensional King Arc Crisis](/examples/cards/71398055) | `71398055` | [Scripts/c71398055.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c71398055.lua) | 1 |
| [Enlightenment Dragon](/examples/cards/46186135) | `46186135` | [Scripts/c46186135.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c46186135.lua) | 1 |
| [Ultimate Crystal Rainbow Dragon Overdrive](/examples/cards/84544192) | `84544192` | [Scripts/c84544192.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c84544192.lua) | 1 |
| [GMX Associate Noma](/examples/cards/83528184) | `83528184` | [Scripts/c83528184.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c83528184.lua) | 1 |
| [Kewl Tune Crackle](/examples/cards/39576656) | `39576656` | [Scripts/c39576656.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c39576656.lua) | 1 |
| [Ashened to Endlessness](/examples/cards/34813443) | `34813443` | [Scripts/c34813443.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c34813443.lua) | 1 |
| [Radiant Typhoon Varuroon, the Marine Eidolon](/examples/cards/39341885) | `39341885` | [Scripts/c39341885.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c39341885.lua) | 1 |
| Starving Venom Wing Dragon | `5148778` | [Scripts/c5148778.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c5148778.lua) | 1 |
| Flowering Etoile the Melodious Magnificat | `83793721` | [Scripts/c83793721.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c83793721.lua) | 2 |
| Regenesis Birth | `27781371` | [Scripts/c27781371.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c27781371.lua) | 1 |
| Chaos Magical Hats | `2372506` | [Scripts/c2372506.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c2372506.lua) | 1 |
| Gouki Sheik Ogre | `7382007` | [Scripts/c7382007.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c7382007.lua) | 1 |
| Hunting Horn | `55421040` | [Scripts/c55421040.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c55421040.lua) | 1 |
| Vanquish Soul Trinity Burst | `53330789` | [Scripts/c53330789.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c53330789.lua) | 1 |
| Grandpa Demetto | `44190146` | [Scripts/c44190146.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c44190146.lua) | 1 |
| S:P Little Knight | `29301450` | [Scripts/c29301450.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c29301450.lua) | 2 |
| Enneacraft - Atori.MAR | `54842941` | [Scripts/c54842941.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c54842941.lua) | 1 |
| Phantom Knights' Rank-Up-Magic Force | `88504133` | [Scripts/c88504133.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c88504133.lua) | 2 |
| ...and 287 more |  |  |  |

## Script Examples

### Levia-Dragoon - Daedalus (`78579058`)

Source: [Scripts/c78579058.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c78579058.lua)

```lua
end
function s.LExtraMaterialCount(mg,lc,tp)
	for tc in aux.Next(mg) do
		local le={tc:IsHasEffect(EFFECT_EXTRA_LINK_MATERIAL,tp)}
		for _,te in pairs(le) do
```

### Azure Ocean Dragon Lord - Neo-Daedalus Rage (`41570943`)

Source: [Scripts/c41570943.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c41570943.lua)

```lua
end
function s.LExtraMaterialCount(mg,lc,tp)
	for tc in aux.Next(mg) do
		local le={tc:IsHasEffect(EFFECT_EXTRA_LINK_MATERIAL,tp)}
		for _,te in pairs(le) do
```

### Goyo Emperor (`59255742`)

Source: [Scripts/c59255742.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c59255742.lua)

```lua
		local e1=e2:GetLabelObject()
		local tg=e1:GetLabelObject()
		for tc in aux.Next(tg) do
			tc:ResetFlagEffect(59255742)
		end
```
