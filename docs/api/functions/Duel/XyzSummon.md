# Duel.XyzSummon

## Signature

```lua
Duel.XyzSummon(int player, Card c, [Group|nil mg], [int min], [int max]) -> void
```

## Description

Let the player player \[from the mg\] \[choose min-max a material\] on the c to call the excess procedure
Mg is not empty and min is 0 mg directly to all the excess material

## Parameters

- `player` `int`
- `c` `Card`
- `mg` `Group|nil` optional
- `min` `int` optional - default: 0
- `max` `int` optional - default: 0

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4868`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **30** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.XyzSummon`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Barian's Chaos Draw](/examples/cards/97769122) | `97769122` | [Scripts/c97769122.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97769122.lua) | 63 |
| [Bujinki Ahashima](/examples/cards/71095768) | `71095768` | [Scripts/c71095768.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71095768.lua) | 62 |
| Supreme King Dragon Lightwurm | `41908872` | [Scripts/c41908872.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41908872.lua) | 59 |
| Gagaga Girl - Cell Phone Subtraction | `48393693` | [Scripts/c48393693.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48393693.lua) | 53 |
| Salamangreat Zebroid X | `44161893` | [Scripts/c44161893.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44161893.lua) | 51 |
| Fire King Sanctuary | `65305978` | [Scripts/c65305978.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65305978.lua) | 51 |
| Chronomaly Esperanza Glyph | `50797682` | [Scripts/c50797682.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50797682.lua) | 51 |
| Numbers Last Hope | `4606229` | [Scripts/c4606229.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4606229.lua) | 50 |
| Mathmech Superfactorial | `87804365` | [Scripts/c87804365.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87804365.lua) | 49 |
| Gazer Shark | `23536866` | [Scripts/c23536866.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23536866.lua) | 49 |
| Shining Hope Road | `62829077` | [Scripts/c62829077.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62829077.lua) | 48 |
| Magicolloidal Sol | `67694706` | [Scripts/c67694706.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67694706.lua) | 47 |
| Magikey Locking | `40493210` | [Scripts/c40493210.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40493210.lua) | 46 |
| Ryzeal Plasma Hole | `33787730` | [Scripts/c33787730.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33787730.lua) | 46 |
| Exosister Returnia | `197042` | [Scripts/c197042.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c197042.lua) | 46 |
| Reincarnation Unveiling Mail | `68663427` | [Scripts/c68663427.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c68663427.lua) | 45 |
| Artifacts Unleashed | `56611470` | [Scripts/c56611470.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56611470.lua) | 45 |
| The Phantom Knights of Umbrage Veil | `85257384` | [Scripts/c85257384.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85257384.lua) | 44 |
| Full-Armored Xyz | `39733924` | [Scripts/c39733924.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39733924.lua) | 44 |
| Here There Be Dragons | `4575541` | [Scripts/c4575541.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4575541.lua) | 44 |
| Pendulum Xyz | `46005939` | [Scripts/c46005939.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46005939.lua) | 44 |
| Gagaga Magician - Gagaga Magic | `12908094` | [Scripts/c12908094.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12908094.lua) | 42 |
| K9-ØØ Lupis | `91025875` | [Scripts/c91025875.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c91025875.lua) | 42 |
| Halfway to Forever | `20285786` | [Scripts/c20285786.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20285786.lua) | 42 |
| ...and 6 more |  |  |  |

## Script Examples

### Barian's Chaos Draw (`97769122`)

Source: [Scripts/c97769122.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97769122.lua)

```lua
		local fg=Duel.GetMatchingGroup(c97769122.filter2,tp,LOCATION_MZONE,0,nil)
		local sg=fg:SelectSubGroup(tp,c97769122.gselect,false,1,7,xyz,g)
		Duel.XyzSummon(tp,xyz,sg)
	end
end
```

### Bujinki Ahashima (`71095768`)

Source: [Scripts/c71095768.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71095768.lua)

```lua
			Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SPSUMMON)
			local xyz=xyzg:Select(tp,1,1,nil):GetFirst()
			Duel.XyzSummon(tp,xyz,sg)
		end
	end
```

### Supreme King Dragon Lightwurm (`41908872`)

Source: [Scripts/c41908872.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41908872.lua)

```lua
				Duel.SynchroSummon(tp,sc,nil)
			else
				Duel.XyzSummon(tp,sc,nil)
			end
		end
```
