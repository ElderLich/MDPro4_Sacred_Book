# Duel.XyzSummon

## Signature

```lua
Duel.XyzSummon(int player, Card c, [Group|nil materials], [int minc], [int maxc]) -> void
```

## Description

Performs a rule Xyz Summon for player and c using an optional material group and min/max constraints.
Use this in effect operations after checking Card.IsXyzSummonable. The selected Xyz Monster's registered procedure still controls final material legality and overlaying.
The core rejects this during the Damage Step, yields while the summon is processed, and returns no Lua value.

## Parameters

- `player` `int` - Player performing the Xyz Summon.
- `c` `Card` - Xyz Monster to Summon.
- `materials` `Group|nil` optional - Optional material group supplied by the effect.
- `minc` `int` optional - Optional minimum material count override. Defaults to 0.
- `maxc` `int` optional - Optional maximum material count override. Defaults to 0.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4868`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **30** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.XyzSummon`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Barian's Chaos Draw](/examples/cards/97769122) | `97769122` | [Scripts/c97769122.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97769122.lua) | 1 |
| [Bujinki Ahashima](/examples/cards/71095768) | `71095768` | [Scripts/c71095768.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71095768.lua) | 1 |
| Supreme King Dragon Lightwurm | `41908872` | [Scripts/c41908872.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41908872.lua) | 1 |
| Gagaga Girl - Cell Phone Subtraction | `48393693` | [Scripts/c48393693.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48393693.lua) | 1 |
| Salamangreat Zebroid X | `44161893` | [Scripts/c44161893.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44161893.lua) | 1 |
| Fire King Sanctuary | `65305978` | [Scripts/c65305978.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65305978.lua) | 1 |
| Chronomaly Esperanza Glyph | `50797682` | [Scripts/c50797682.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50797682.lua) | 1 |
| Numbers Last Hope | `4606229` | [Scripts/c4606229.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4606229.lua) | 1 |
| Mathmech Superfactorial | `87804365` | [Scripts/c87804365.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87804365.lua) | 1 |
| Gazer Shark | `23536866` | [Scripts/c23536866.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23536866.lua) | 1 |
| Shining Hope Road | `62829077` | [Scripts/c62829077.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62829077.lua) | 1 |
| Magicolloidal Sol | `67694706` | [Scripts/c67694706.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67694706.lua) | 1 |
| Magikey Locking | `40493210` | [Scripts/c40493210.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40493210.lua) | 1 |
| Ryzeal Plasma Hole | `33787730` | [Scripts/c33787730.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33787730.lua) | 1 |
| Exosister Returnia | `197042` | [Scripts/c197042.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c197042.lua) | 1 |
| Reincarnation Unveiling Mail | `68663427` | [Scripts/c68663427.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c68663427.lua) | 1 |
| Artifacts Unleashed | `56611470` | [Scripts/c56611470.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56611470.lua) | 1 |
| The Phantom Knights of Umbrage Veil | `85257384` | [Scripts/c85257384.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85257384.lua) | 1 |
| Full-Armored Xyz | `39733924` | [Scripts/c39733924.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39733924.lua) | 1 |
| Here There Be Dragons | `4575541` | [Scripts/c4575541.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4575541.lua) | 1 |
| Pendulum Xyz | `46005939` | [Scripts/c46005939.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46005939.lua) | 1 |
| Gagaga Magician - Gagaga Magic | `12908094` | [Scripts/c12908094.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12908094.lua) | 1 |
| K9-ØØ Lupis | `91025875` | [Scripts/c91025875.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c91025875.lua) | 1 |
| Halfway to Forever | `20285786` | [Scripts/c20285786.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20285786.lua) | 1 |
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
