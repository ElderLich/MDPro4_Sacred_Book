# Duel.IsBattlePhase

## Signature

```lua
Duel.IsBattlePhase() -> bool
```

## Description

Returns whether the current phase is the Battle Phase.

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4953`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **23** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.IsBattlePhase) with `Duel.IsBattlePhase`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Yummy★Snatchy](/examples/cards/30581601) | `30581601` | [Scripts/c30581601.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30581601.lua) | 1 |
| Hunting Horn | `55421040` | [Scripts/c55421040.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55421040.lua) | 2 |
| Crystron Halqifibrax Prism | `65400671` | [Scripts/c65400671.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65400671.lua) | 1 |
| Witchcrafter Pupils | `69964858` | [Scripts/c69964858.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c69964858.lua) | 1 |
| Snake-Eyes Vengeance Dragon | `79415624` | [Scripts/c79415624.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c79415624.lua) | 1 |
| Hyper-Rank-Up-Magic Ultimate Force | `87818869` | [Scripts/c87818869.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87818869.lua) | 1 |
| Crossmind Archfiend | `52644170` | [Scripts/c52644170.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52644170.lua) | 1 |
| X-Saber Bruno | `45462306` | [Scripts/c45462306.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45462306.lua) | 1 |
| Master Peace, the True Dracoverlord | `12800564` | [Scripts/c12800564.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12800564.lua) | 1 |
| Borreload Liberator Dragon | `27096833` | [Scripts/c27096833.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27096833.lua) | 1 |
| Regenesis Overlord | `47082621` | [Scripts/c47082621.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c47082621.lua) | 1 |
| Legendary Lord Six Samurai - Kizan | `42209438` | [Scripts/c42209438.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42209438.lua) | 1 |
| Volcanic Doomfire | `32543380` | [Scripts/c32543380.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32543380.lua) | 1 |
| Faisan, Hunting Scout of the Deep Forest | `86038337` | [Scripts/c86038337.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c86038337.lua) | 1 |
| Champion's Pulse | `46001505` | [Scripts/c46001505.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46001505.lua) | 1 |
| The Great Gallant Bandit | `24203749` | [Scripts/c24203749.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24203749.lua) | 1 |
| Assist★Yummy! | `86762958` | [Scripts/c86762958.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c86762958.lua) | 1 |
| Sky Striker Mecha - Adil Saber | `61151074` | [Scripts/c61151074.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61151074.lua) | 1 |
| Regenesis Lord | `22812963` | [Scripts/c22812963.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22812963.lua) | 1 |
| Dark Ceruvim Irisfil | `64626565` | [Scripts/c64626565.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c64626565.lua) | 1 |
| Full-Speed Warrior | `17201951` | [Scripts/c17201951.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17201951.lua) | 1 |
| Evil HERO Malicious Fiend | `86676862` | [Scripts/c86676862.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c86676862.lua) | 1 |
| Ultimate Tyranno | `15894048` | [Scripts/c15894048.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15894048.lua) | 1 |

## Script Examples

### Yummy★Snatchy (`30581601`)

Source: [Scripts/c30581601.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30581601.lua)

```lua
end
function s.sccon(e,tp,eg,ep,ev,re,r,rp)
	return Duel.IsMainPhase() or Duel.GetTurnPlayer()~=tp and Duel.IsBattlePhase()
end
function s.sccost(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Hunting Horn (`55421040`)

Source: [Scripts/c55421040.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55421040.lua)

```lua
		return res
	end
	if Duel.IsBattlePhase() then
		e:SetCategory(CATEGORY_SPECIAL_SUMMON+CATEGORY_FUSION_SUMMON+CATEGORY_ATKCHANGE)
	else
```

### Crystron Halqifibrax Prism (`65400671`)

Source: [Scripts/c65400671.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65400671.lua)

```lua
end
function s.spcon(e,tp,eg,ep,ev,re,r,rp)
	return Duel.GetTurnPlayer()~=tp and (Duel.IsMainPhase() or Duel.IsBattlePhase())
end
function s.sptg(e,tp,eg,ep,ev,re,r,rp,chk)
```
