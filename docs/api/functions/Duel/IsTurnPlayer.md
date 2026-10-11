# Duel.IsTurnPlayer

## Signature

```lua
Duel.IsTurnPlayer(int playerid) -> bool
```

## Description

Returns whether playerid is the current turn player.

## Parameters

- `playerid` `int`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4848`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **9** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.IsTurnPlayer) with `Duel.IsTurnPlayer`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| D/D Extra Surveyor | `74387963` | [Scripts/c74387963.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74387963.lua) | 1 |
| Trirealm Rift Territory - Valvols | `33700664` | [Scripts/c33700664.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33700664.lua) | 1 |
| Volcanic Doomfire | `32543380` | [Scripts/c32543380.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32543380.lua) | 1 |
| Thunderforce Attack | `42469671` | [Scripts/c42469671.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42469671.lua) | 1 |
| Hieratic Seal From the Ashes | `53670497` | [Scripts/c53670497.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53670497.lua) | 2 |
| Mask of Dispel | `20765952` | [Scripts/c20765952.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20765952.lua) | 1 |
| White Aura Bihamut | `89907227` | [Scripts/c89907227.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c89907227.lua) | 1 |
| Evil HERO Malicious Fiend | `86676862` | [Scripts/c86676862.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c86676862.lua) | 1 |
| Ultimate Tyranno | `15894048` | [Scripts/c15894048.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15894048.lua) | 1 |

## Script Examples

### D/D Extra Surveyor (`74387963`)

Source: [Scripts/c74387963.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74387963.lua)

```lua
function s.dacon(e,tp,eg,ep,ev,re,r,rp)
	return eg:IsExists(s.sfilter,1,nil,tp) and not eg:IsContains(e:GetHandler())
		and aux.bpcon(e,tp,eg,ep,ev,re,r,rp) and Duel.IsTurnPlayer(tp)
end
function s.dafilter(c)
```

### Trirealm Rift Territory - Valvols (`33700664`)

Source: [Scripts/c33700664.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33700664.lua)

```lua
	return Duel.IsExistingMatchingCard(s.cfilter,e:GetHandlerPlayer(),LOCATION_MZONE,0,1,nil)
		and Duel.GetMatchingGroupCount(aux.TRUE,e:GetHandlerPlayer(),LOCATION_DECK,0,nil)==0
		and Duel.IsTurnPlayer(e:GetHandlerPlayer())
end
```

### Volcanic Doomfire (`32543380`)

Source: [Scripts/c32543380.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32543380.lua)

```lua
end
function c32543380.bpcon(e)
	return Duel.IsTurnPlayer(1-e:GetHandlerPlayer()) and Duel.IsBattlePhase()
end
function c32543380.atklimit(e,c)
```
