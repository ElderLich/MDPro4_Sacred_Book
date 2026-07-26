# Duel.Summon

## Signature

```lua
Duel.Summon(int player, Card c, bool ignore_count, [Effect|nil e], [int min], [int zone]) -> void
```

## Description

Makes player Normal Summon c, not Set it, optionally by effect e and requiring at least min Tributes.
If e is nil, regular Normal Summon rules are used. If ignore_count is true, the once-per-turn Normal Summon limit is ignored.

## Parameters

- `player` `int`
- `c` `Card`
- `ignore_count` `bool`
- `e` `Effect|nil` optional
- `min` `int` optional - default: 0
- `zone` `int` optional - default: 0x1f

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4865`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **98** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.Summon`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Ehther the Heavenly Monarch](/examples/cards/96570609) | `96570609` | [Scripts/c96570609.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96570609.lua) | 1 |
| [Aiwass the Spirit of the Law](/examples/cards/84288367) | `84288367` | [Scripts/c84288367.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84288367.lua) | 1 |
| Clown Crew Soiree Operations | `70058649` | [Scripts/c70058649.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70058649.lua) | 1 |
| Tails of the Fairy Tails | `82119326` | [Scripts/c82119326.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82119326.lua) | 1 |
| Union Activation | `38527680` | [Scripts/c38527680.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38527680.lua) | 1 |
| Kuribeh | `34419588` | [Scripts/c34419588.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34419588.lua) | 1 |
| Ojamatch | `38395123` | [Scripts/c38395123.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38395123.lua) | 1 |
| Clown Crew Biancaviso | `82159583` | [Scripts/c82159583.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82159583.lua) | 1 |
| Argostars - Giantslaying | `30964246` | [Scripts/c30964246.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30964246.lua) | 1 |
| Rahamu, Envoy of the Sacred Tome | `53904087` | [Scripts/c53904087.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53904087.lua) | 1 |
| Ritual Beast Ulti-Kimunfalcos | `58811192` | [Scripts/c58811192.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58811192.lua) | 1 |
| Doodle Beast - Tyranno | `67725394` | [Scripts/c67725394.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67725394.lua) | 1 |
| Primite Imperial Dragon | `81418467` | [Scripts/c81418467.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81418467.lua) | 1 |
| Bahalutiya, the Grand Radiance | `53318263` | [Scripts/c53318263.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53318263.lua) | 1 |
| Hi-Speedroid Rubber Band Shooter | `72813401` | [Scripts/c72813401.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c72813401.lua) | 1 |
| Floowandereeze &amp; Empen | `80611581` | [Scripts/c80611581.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80611581.lua) | 1 |
| Exosister Betrayal | `52335937` | [Scripts/c52335937.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52335937.lua) | 1 |
| Gizmek Yata, the Gleaming Vanguard | `13224603` | [Scripts/c13224603.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13224603.lua) | 1 |
| Repair Genex Controller | `8173184` | [Scripts/c8173184.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8173184.lua) | 1 |
| Electrode Beast Cation | `21291696` | [Scripts/c21291696.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21291696.lua) | 1 |
| Miasma Necromancer | `69176851` | [Scripts/c69176851.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c69176851.lua) | 1 |
| Fairy Tale Tails | `91957038` | [Scripts/c91957038.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c91957038.lua) | 1 |
| Gagaga Illusion | `73496100` | [Scripts/c73496100.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c73496100.lua) | 1 |
| True Draco Apocalypse | `61529473` | [Scripts/c61529473.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61529473.lua) | 1 |
| ...and 74 more |  |  |  |

## Script Examples

### Ehther the Heavenly Monarch (`96570609`)

Source: [Scripts/c96570609.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96570609.lua)

```lua
	if pos==0 then return end
	if Duel.SelectPosition(tp,c,pos)==POS_FACEUP_ATTACK then
		Duel.Summon(tp,c,true,nil,1)
	else
		Duel.MSet(tp,c,true,nil,1)
```

### Aiwass the Spirit of the Law (`84288367`)

Source: [Scripts/c84288367.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84288367.lua)

```lua
			if tc then
				Duel.ShuffleHand(tp)
				Duel.Summon(tp,tc,true,nil)
			end
		end
```

### Clown Crew Soiree Operations (`70058649`)

Source: [Scripts/c70058649.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70058649.lua)

```lua
	local tc=g:GetFirst()
	if tc then
		Duel.Summon(tp,tc,true,nil,1)
	end
end
```
