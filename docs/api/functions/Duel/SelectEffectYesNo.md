# Duel.SelectEffectYesNo

## Signature

```lua
Duel.SelectEffectYesNo(int player, Card c, [int desc]) -> bool
```

## Description

Asks player whether to use c's effect with description id desc, defaulting to 95.

## Parameters

- `player` `int`
- `c` `Card`
- `desc` `int` optional - default: 95

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5022`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **270** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.SelectEffectYesNo) with `Duel.SelectEffectYesNo`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Am Duazenet](/examples/cards/45151304) | `45151304` | [Scripts/c45151304.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45151304.lua) | 1 |
| [Camelot, Realm of Noble Knights and Noble Arms](/examples/cards/15635751) | `15635751` | [Scripts/c15635751.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15635751.lua) | 1 |
| [Revendread Origin](/examples/cards/94666032) | `94666032` | [Scripts/c94666032.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c94666032.lua) | 1 |
| Gravity Balance | `37930737` | [Scripts/c37930737.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37930737.lua) | 1 |
| Number 101: Silent Honor ARK - Soul Asylum | `2419596` | [Scripts/c2419596.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2419596.lua) | 1 |
| Edge Imp Scythe | `29280589` | [Scripts/c29280589.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29280589.lua) | 1 |
| Number 4: Stealth Kragen | `67557908` | [Scripts/c67557908.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67557908.lua) | 1 |
| Ojama Pajama | `75884822` | [Scripts/c75884822.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75884822.lua) | 1 |
| Jurrac Volcano | `89948817` | [Scripts/c89948817.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c89948817.lua) | 1 |
| Sleepy Scapegoats | `3129527` | [Scripts/c3129527.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3129527.lua) | 1 |
| Masterking Archfiend | `35606858` | [Scripts/c35606858.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35606858.lua) | 2 |
| Laevateinn the Burning Blade | `6260560` | [Scripts/c6260560.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6260560.lua) | 1 |
| Sea Lancer | `22842214` | [Scripts/c22842214.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22842214.lua) | 1 |
| Zebufera, Vaalmonican Hallow Heathen | `2815176` | [Scripts/c2815176.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2815176.lua) | 1 |
| Dual Avatar Feet - Armored Un-Gyo | `7631534` | [Scripts/c7631534.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7631534.lua) | 1 |
| Unchained Firelord of Yama | `94014327` | [Scripts/c94014327.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c94014327.lua) | 1 |
| Thunder Dragon Titan | `41685633` | [Scripts/c41685633.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41685633.lua) | 1 |
| Altergeist Memorygant | `23790299` | [Scripts/c23790299.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23790299.lua) | 1 |
| Lost World | `17228908` | [Scripts/c17228908.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17228908.lua) | 1 |
| Dream Tower of Princess Nemleria | `18458255` | [Scripts/c18458255.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18458255.lua) | 1 |
| Fire King Sanctuary | `65305978` | [Scripts/c65305978.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65305978.lua) | 1 |
| Salamandra Fusion | `9102835` | [Scripts/c9102835.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9102835.lua) | 1 |
| Commander Souza, Swordmaster | `72867001` | [Scripts/c72867001.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c72867001.lua) | 1 |
| Stealth Kragen Spawn | `94942656` | [Scripts/c94942656.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c94942656.lua) | 1 |
| ...and 246 more |  |  |  |

## Script Examples

### Am Duazenet (`45151304`)

Source: [Scripts/c45151304.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45151304.lua)

```lua
function s.reptg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return e:GetHandler():IsAbleToRemove() and eg:IsExists(s.repfilter,1,nil,tp) end
	return Duel.SelectEffectYesNo(tp,e:GetHandler(),96)
end
function s.repval(e,c)
```

### Camelot, Realm of Noble Knights and Noble Arms (`15635751`)

Source: [Scripts/c15635751.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15635751.lua)

```lua
		and #g>0 end
	local c=e:GetHandler()
	if Duel.SelectEffectYesNo(tp,c,96) then
		Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_DESREPLACE)
		local tc=g:Select(tp,1,1,nil):GetFirst()
```

### Revendread Origin (`94666032`)

Source: [Scripts/c94666032.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c94666032.lua)

```lua
function c94666032.reptg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return e:GetHandler():IsAbleToRemove() and eg:IsExists(c94666032.repfilter,1,nil,tp) end
	return Duel.SelectEffectYesNo(tp,e:GetHandler(),96)
end
function c94666032.repval(e,c)
```
