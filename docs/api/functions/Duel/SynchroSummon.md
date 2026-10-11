# Duel.SynchroSummon

## Signature

```lua
Duel.SynchroSummon(int player, Card c, [Card|nil tuner], [Group|nil mg], [int minc], [int maxc]) -> void
```

## Description

Performs a Synchro Summon of c for player, optionally requiring tuner and selecting materials from mg.
Use this in an effect operation after checking Card.IsSynchroSummonable; the chosen Synchro Monster's registered procedure still controls material legality.
minc and maxc can restrict the number of non-Tuner materials used by the procedure.

## Parameters

- `player` `int` - Player performing the Synchro Summon.
- `c` `Card` - Synchro Monster to Summon.
- `tuner` `Card|nil` optional - Optional required Tuner material.
- `mg` `Group|nil` optional - Optional material pool to select from.
- `minc` `int` optional - Optional minimum non-Tuner material count override; default: 0.
- `maxc` `int` optional - Optional maximum non-Tuner material count override; default: 0.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4867`

## Guided Examples

Learn how to use this function in context:

- [Synchro Procedure Guide](/learn/synchro-procedure)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **77** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.SynchroSummon) with `Duel.SynchroSummon`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Accel Synchro Stardust Dragon](/examples/cards/30983281) | `30983281` | [Scripts/c30983281.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30983281.lua) | 1 |
| [Yummy★Snatchy](/examples/cards/30581601) | `30581601` | [Scripts/c30581601.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30581601.lua) | 1 |
| Supreme King Dragon Lightwurm | `41908872` | [Scripts/c41908872.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41908872.lua) | 1 |
| Saiba the Soldier Swordsmith | `36608728` | [Scripts/c36608728.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36608728.lua) | 1 |
| Kewl Tune Remix | `88170262` | [Scripts/c88170262.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88170262.lua) | 1 |
| R-Genex Turing | `61052897` | [Scripts/c61052897.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61052897.lua) | 1 |
| Naturia Blessing | `34813545` | [Scripts/c34813545.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34813545.lua) | 1 |
| Melffy Pinny | `34800281` | [Scripts/c34800281.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34800281.lua) | 1 |
| Daigusto Laplampilica | `76937326` | [Scripts/c76937326.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76937326.lua) | 1 |
| Kewl Tune B2B | `65961304` | [Scripts/c65961304.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65961304.lua) | 1 |
| Performapal Odd-Eyes Synchron | `82224646` | [Scripts/c82224646.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82224646.lua) | 1 |
| Accel Synchron | `37675907` | [Scripts/c37675907.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37675907.lua) | 1 |
| Stand Up Centur-Ion! | `41371602` | [Scripts/c41371602.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41371602.lua) | 1 |
| Mathmech Superfactorial | `87804365` | [Scripts/c87804365.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87804365.lua) | 1 |
| Superheavy Samurai Fist | `71386411` | [Scripts/c71386411.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71386411.lua) | 1 |
| Elfnote Power Patron | `12375297` | [Scripts/c12375297.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12375297.lua) | 1 |
| Ukiyoe-P.U.N.K. Sharakusai | `13258285` | [Scripts/c13258285.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13258285.lua) | 1 |
| Re-dyce-cle | `85704698` | [Scripts/c85704698.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85704698.lua) | 1 |
| Magicolloidal Sol | `67694706` | [Scripts/c67694706.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67694706.lua) | 1 |
| Garden Rose Flora | `76524506` | [Scripts/c76524506.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76524506.lua) | 1 |
| X-Saber Bruno | `45462306` | [Scripts/c45462306.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45462306.lua) | 1 |
| Crystron Rion | `66938505` | [Scripts/c66938505.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66938505.lua) | 1 |
| Crystron Tristaros | `99471856` | [Scripts/c99471856.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c99471856.lua) | 1 |
| Speedroid Gum Prize | `70939418` | [Scripts/c70939418.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70939418.lua) | 1 |
| ...and 53 more |  |  |  |

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
