# Card.GetOriginalRank

## Signature

```lua
Card.GetOriginalRank(Card c) -> int
```

## Description

Returns c's printed Rank from card data, or 0 if c is not an Xyz Monster.

## Parameters

- `c` `Card`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3414`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **9** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.GetOriginalRank`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Zaborg the Mega Monarch | `87602890` | [Scripts/c87602890.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87602890.lua) | 50 |
| Clown Crew Finale | `84031736` | [Scripts/c84031736.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84031736.lua) | 50 |
| Steel Star Regulator | `32986898` | [Scripts/c32986898.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32986898.lua) | 47 |
| Voloferniges, the Darkest Dragon Doomrider | `38694052` | [Scripts/c38694052.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38694052.lua) | 46 |
| Abduction | `21846145` | [Scripts/c21846145.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21846145.lua) | 37 |
| F.A. Turbo Charger | `75059201` | [Scripts/c75059201.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75059201.lua) | 28 |
| F.A. Hang On Mach | `93449450` | [Scripts/c93449450.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93449450.lua) | 28 |
| F.A. Whip Crosser | `49655592` | [Scripts/c49655592.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49655592.lua) | 27 |
| F.A. Sonic Meister | `67045745` | [Scripts/c67045745.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67045745.lua) | 21 |

## Script Examples

### Zaborg the Mega Monarch (`87602890`)

Source: [Scripts/c87602890.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87602890.lua)

```lua
		local lv=tc:GetOriginalLevel()
		if tc:IsType(TYPE_XYZ) then
			lv=tc:GetOriginalRank()
		end
		Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_TOGRAVE)
```

### Clown Crew Finale (`84031736`)

Source: [Scripts/c84031736.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84031736.lua)

```lua
	if c:GetOriginalLevel()>0 then
		return c:GetOriginalLevel()
	elseif c:GetOriginalRank()>0 then
		return c:GetOriginalRank()
	elseif c:GetLink()>0 then
```

### Steel Star Regulator (`32986898`)

Source: [Scripts/c32986898.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32986898.lua)

```lua
		local lk
		if tc:IsType(TYPE_XYZ) then
			lk=tc:GetOriginalRank()
		else
			lk=tc:GetOriginalLevel()
```
