# Duel.SynchroSummon

## Signature

```lua
Duel.SynchroSummon(int player, Card c, [Card|nil tuner], [Group|nil mg], [int minc], [int maxc]) -> void
```

## Description

Let the player player to tuner as the adjustment \[mg for the material\] on the c cohomology summon procedures

## Parameters

- `player` `int`
- `c` `Card`
- `tuner` `Card|nil` optional
- `mg` `Group|nil` optional
- `minc` `int` optional - default: 0
- `maxc` `int` optional - default: 0

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4867`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **74** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.SynchroSummon`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Accel Synchro Stardust Dragon](/examples/cards/30983281) | `30983281` | [Scripts/c30983281.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30983281.lua) | 69 |
| [Yummy★Snatchy](/examples/cards/30581601) | `30581601` | [Scripts/c30581601.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30581601.lua) | 61 |
| Supreme King Dragon Lightwurm | `41908872` | [Scripts/c41908872.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41908872.lua) | 59 |
| Saiba the Soldier Swordsmith | `36608728` | [Scripts/c36608728.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36608728.lua) | 57 |
| Kewl Tune Remix | `88170262` | [Scripts/c88170262.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88170262.lua) | 54 |
| R-Genex Turing | `61052897` | [Scripts/c61052897.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61052897.lua) | 54 |
| Naturia Blessing | `34813545` | [Scripts/c34813545.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34813545.lua) | 54 |
| Melffy Pinny | `34800281` | [Scripts/c34800281.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34800281.lua) | 53 |
| Daigusto Laplampilica | `76937326` | [Scripts/c76937326.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76937326.lua) | 52 |
| Kewl Tune B2B | `65961304` | [Scripts/c65961304.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65961304.lua) | 52 |
| Performapal Odd-Eyes Synchron | `82224646` | [Scripts/c82224646.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82224646.lua) | 51 |
| Accel Synchron | `37675907` | [Scripts/c37675907.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37675907.lua) | 50 |
| Stand Up Centur-Ion! | `41371602` | [Scripts/c41371602.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41371602.lua) | 49 |
| Mathmech Superfactorial | `87804365` | [Scripts/c87804365.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87804365.lua) | 49 |
| Superheavy Samurai Fist | `71386411` | [Scripts/c71386411.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71386411.lua) | 48 |
| Elfnote Power Patron | `12375297` | [Scripts/c12375297.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12375297.lua) | 48 |
| Ukiyoe-P.U.N.K. Sharakusai | `13258285` | [Scripts/c13258285.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13258285.lua) | 48 |
| Re-dyce-cle | `85704698` | [Scripts/c85704698.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85704698.lua) | 48 |
| Magicolloidal Sol | `67694706` | [Scripts/c67694706.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67694706.lua) | 47 |
| Garden Rose Flora | `76524506` | [Scripts/c76524506.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76524506.lua) | 47 |
| X-Saber Bruno | `45462306` | [Scripts/c45462306.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45462306.lua) | 47 |
| Crystron Tristaros | `99471856` | [Scripts/c99471856.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c99471856.lua) | 46 |
| Speedroid Gum Prize | `70939418` | [Scripts/c70939418.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70939418.lua) | 46 |
| Shooting Riser Dragon | `68431965` | [Scripts/c68431965.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c68431965.lua) | 46 |
| ...and 50 more |  |  |  |

## Script Examples

### Accel Synchro Stardust Dragon (`30983281`)

Source: [Scripts/c30983281.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30983281.lua)

```lua
		e1:SetOwnerPlayer(tp)
		sg:GetFirst():RegisterEffect(e1,true)
		Duel.SynchroSummon(tp,sg:GetFirst(),nil)
	end
end
```

### Yummy★Snatchy (`30581601`)

Source: [Scripts/c30581601.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30581601.lua)

```lua
		Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SMATERIAL)
		local tg=mg:SelectSubGroup(tp,s.syncheck,false,2,#mg,tp,sc)
		Duel.SynchroSummon(tp,sc,nil,tg,#tg-1,#tg-1)
	end
end
```

### Supreme King Dragon Lightwurm (`41908872`)

Source: [Scripts/c41908872.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41908872.lua)

```lua
			local sc=g:Select(tp,1,1,nil):GetFirst()
			if g1:IsContains(sc) then
				Duel.SynchroSummon(tp,sc,nil)
			else
				Duel.XyzSummon(tp,sc,nil)
```
