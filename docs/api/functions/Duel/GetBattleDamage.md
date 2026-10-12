# Duel.GetBattleDamage

## Signature

```lua
Duel.GetBattleDamage(int player) -> int
```

## Description

Returns the battle damage currently recorded for player.

## Parameters

- `player` `int`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4922`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **22** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.GetBattleDamage) with `Duel.GetBattleDamage`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Dinomorphia Reversion | `28292031` | [Scripts/c28292031.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c28292031.lua) | 1 |
| Giant Ballpark | `58012707` | [Scripts/c58012707.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c58012707.lua) | 2 |
| Heavy Metal Raiders | `3113667` | [Scripts/c3113667.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c3113667.lua) | 1 |
| Marincess Crown Tail | `54569495` | [Scripts/c54569495.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c54569495.lua) | 1 |
| Gouki Octostretch | `85008676` | [Scripts/c85008676.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c85008676.lua) | 1 |
| Boo-Boo Game | `27923575` | [Scripts/c27923575.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c27923575.lua) | 1 |
| Advanced Dark | `12644061` | [Scripts/c12644061.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c12644061.lua) | 1 |
| Smoke Mosquito | `28427869` | [Scripts/c28427869.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c28427869.lua) | 1 |
| Dinomorphia Sonic | `52807032` | [Scripts/c52807032.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c52807032.lua) | 1 |
| Destiny HERO - Dynatag | `37780349` | [Scripts/c37780349.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c37780349.lua) | 1 |
| Dinomorphia Intact | `7336745` | [Scripts/c7336745.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c7336745.lua) | 1 |
| Donyoribo @Ignister | `14146794` | [Scripts/c14146794.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c14146794.lua) | 1 |
| Dinomorphia Shell | `25419323` | [Scripts/c25419323.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c25419323.lua) | 1 |
| Rescue Interlacer | `63009228` | [Scripts/c63009228.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c63009228.lua) | 1 |
| Spirit Force | `16674846` | [Scripts/c16674846.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c16674846.lua) | 1 |
| Kuribon | `47432275` | [Scripts/c47432275.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c47432275.lua) | 1 |
| Power Wall | `76403456` | [Scripts/c76403456.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c76403456.lua) | 2 |
| Arcana Force XIV - Temperance | `60953118` | [Scripts/c60953118.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c60953118.lua) | 1 |
| Chthonian Soldier | `50916353` | [Scripts/c50916353.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c50916353.lua) | 1 |
| Kuriboh | `40640057` | [Scripts/c40640057.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c40640057.lua) | 1 |
| Defense Draw | `24268052` | [Scripts/c24268052.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c24268052.lua) | 1 |
| Nutrient Z | `29389368` | [Scripts/c29389368.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c29389368.lua) | 1 |

## Script Examples

### Dinomorphia Reversion (`28292031`)

Source: [Scripts/c28292031.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c28292031.lua)

```lua
end
function c28292031.damcon(e,tp,eg,ep,ev,re,r,rp)
	return Duel.GetLP(tp)<=2000 and Duel.GetBattleDamage(tp)>0
end
function c28292031.damop(e,tp,eg,ep,ev,re,r,rp)
```

### Giant Ballpark (`58012707`)

Source: [Scripts/c58012707.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c58012707.lua)

```lua
end
function c58012707.dmcon(e,tp,eg,ep,ev,re,r,rp)
	return Duel.GetBattleDamage(tp)>0 or Duel.GetBattleDamage(1-tp)>0
end
function c58012707.tgfilter(c)
```

### Heavy Metal Raiders (`3113667`)

Source: [Scripts/c3113667.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c3113667.lua)

```lua
	local tc=a:GetBattleTarget()
	if tc and tc:IsControler(1-tp) then a,tc=tc,a end
	local dam=Duel.GetBattleDamage(tp)
	if not tc or dam<=0 then return 1 end
	local e1=Effect.CreateEffect(e:GetHandler())
```
