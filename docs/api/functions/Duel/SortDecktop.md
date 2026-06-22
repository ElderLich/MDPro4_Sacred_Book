# Duel.SortDecktop

## Signature

```lua
Duel.SortDecktop(int sort_player, int target_player, int count) -> void
```

## Description

Lets sort_player reorder the top count cards of target_player's Main Deck.
Both players must be valid and count must be at least 1. If count is larger than the remaining Deck size, the processor only sorts the available top cards.

## Parameters

- `sort_player` `int`
- `target_player` `int`
- `count` `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4893`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **59** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.SortDecktop`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Flower Cardian Peony with Butterfly](/examples/cards/57261568) | `57261568` | [Scripts/c57261568.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57261568.lua) | 62 |
| Purrely | `25550531` | [Scripts/c25550531.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25550531.lua) | 56 |
| Materiactor Meltthrough | `66059345` | [Scripts/c66059345.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66059345.lua) | 53 |
| Loris, Lady of Lament | `50699850` | [Scripts/c50699850.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50699850.lua) | 51 |
| Destiny HERO - Dominance | `69394324` | [Scripts/c69394324.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c69394324.lua) | 50 |
| Shadowreaver Knight 21 | `95506252` | [Scripts/c95506252.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95506252.lua) | 50 |
| Materiactor Meltdown | `38669664` | [Scripts/c38669664.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38669664.lua) | 49 |
| Magikey Mechmusket - Batosbuster | `19489718` | [Scripts/c19489718.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c19489718.lua) | 48 |
| Adamancipator Risen - Leonite | `47674738` | [Scripts/c47674738.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c47674738.lua) | 48 |
| Adamancipator Risen - Raptite | `73079836` | [Scripts/c73079836.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c73079836.lua) | 45 |
| Speedroid Fuki-Modoshi Piper | `50482813` | [Scripts/c50482813.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50482813.lua) | 45 |
| Wannabee! | `3248469` | [Scripts/c3248469.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3248469.lua) | 45 |
| Hydralander Orbit | `93953933` | [Scripts/c93953933.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93953933.lua) | 44 |
| GMX Chairman Kimridge | `56034579` | [Scripts/c56034579.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56034579.lua) | 44 |
| Morphtronic Smartfon | `15521027` | [Scripts/c15521027.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15521027.lua) | 43 |
| Pot of Prosperity | `84211599` | [Scripts/c84211599.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84211599.lua) | 43 |
| Way Where There's a Will | `91880660` | [Scripts/c91880660.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c91880660.lua) | 42 |
| Sylvan Lotuswain | `73136204` | [Scripts/c73136204.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c73136204.lua) | 42 |
| Recardination | `73271204` | [Scripts/c73271204.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c73271204.lua) | 42 |
| Dark Magical Circle | `47222536` | [Scripts/c47222536.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c47222536.lua) | 41 |
| SPYRAL GEAR - Drone | `4474060` | [Scripts/c4474060.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4474060.lua) | 41 |
| Orea, the Sylvan High Arbiter | `95239444` | [Scripts/c95239444.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95239444.lua) | 39 |
| Adamancipator Risen - Dragite | `9464441` | [Scripts/c9464441.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9464441.lua) | 39 |
| Votis | `75311421` | [Scripts/c75311421.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75311421.lua) | 39 |
| ...and 35 more |  |  |  |

## Script Examples

### Flower Cardian Peony with Butterfly (`57261568`)

Source: [Scripts/c57261568.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57261568.lua)

```lua
			Duel.ConfirmCards(tp,g)
			local opt=Duel.SelectOption(tp,aux.Stringid(57261568,1),aux.Stringid(57261568,2))
			Duel.SortDecktop(tp,1-tp,ct)
			if opt==1 then
				for i=1,ct do
```

### Purrely (`25550531`)

Source: [Scripts/c25550531.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25550531.lua)

```lua
	end
	if ct<=1 then return end
	Duel.SortDecktop(p,p,ct)
	for i=1,ct do
		local mg=Duel.GetDecktopGroup(p,1)
```

### Materiactor Meltthrough (`66059345`)

Source: [Scripts/c66059345.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66059345.lua)

```lua
	local g=Duel.GetDecktopGroup(tp,6)
	if g:GetCount()>0 then
		Duel.SortDecktop(tp,tp,g:GetCount())
	end
end
```
