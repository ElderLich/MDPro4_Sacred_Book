# Duel.SelectEffectYesNo

## Signature

```lua
Duel.SelectEffectYesNo(int player, Card c, [int desc]) -> bool
```

## Description

Let players choose whether to launch the card player c effect

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

- Detected in **263** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.SelectEffectYesNo`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Camelot, Realm of Noble Knights and Noble Arms](/examples/cards/15635751) | `15635751` | [Scripts/c15635751.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15635751.lua) | 61 |
| Gravity Balance | `37930737` | [Scripts/c37930737.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37930737.lua) | 60 |
| Edge Imp Scythe | `29280589` | [Scripts/c29280589.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29280589.lua) | 56 |
| Number 4: Stealth Kragen | `67557908` | [Scripts/c67557908.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67557908.lua) | 55 |
| Ojama Pajama | `75884822` | [Scripts/c75884822.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75884822.lua) | 55 |
| Jurrac Volcano | `89948817` | [Scripts/c89948817.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c89948817.lua) | 53 |
| Masterking Archfiend | `35606858` | [Scripts/c35606858.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35606858.lua) | 53 |
| Laevateinn the Burning Blade | `6260560` | [Scripts/c6260560.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6260560.lua) | 53 |
| Sea Lancer | `22842214` | [Scripts/c22842214.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22842214.lua) | 53 |
| Zebufera, Vaalmonican Hallow Heathen | `2815176` | [Scripts/c2815176.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2815176.lua) | 52 |
| Dual Avatar Feet - Armored Un-Gyo | `7631534` | [Scripts/c7631534.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7631534.lua) | 52 |
| Thunder Dragon Titan | `41685633` | [Scripts/c41685633.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41685633.lua) | 52 |
| Altergeist Memorygant | `23790299` | [Scripts/c23790299.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23790299.lua) | 52 |
| Lost World | `17228908` | [Scripts/c17228908.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17228908.lua) | 51 |
| Dream Tower of Princess Nemleria | `18458255` | [Scripts/c18458255.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18458255.lua) | 51 |
| Fire King Sanctuary | `65305978` | [Scripts/c65305978.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65305978.lua) | 51 |
| Salamandra Fusion | `9102835` | [Scripts/c9102835.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9102835.lua) | 51 |
| Commander Souza, Swordmaster | `72867001` | [Scripts/c72867001.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c72867001.lua) | 51 |
| Stealth Kragen Spawn | `94942656` | [Scripts/c94942656.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c94942656.lua) | 51 |
| Odd-Eyes Lancer Dragon | `83347294` | [Scripts/c83347294.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c83347294.lua) | 51 |
| Solfachord Solfegia | `84693918` | [Scripts/c84693918.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84693918.lua) | 50 |
| Magician of Hope | `67865534` | [Scripts/c67865534.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67865534.lua) | 50 |
| Hidden Village of Ninjitsu Arts | `26232916` | [Scripts/c26232916.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c26232916.lua) | 50 |
| Goblin's Crazy Beast | `71100270` | [Scripts/c71100270.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71100270.lua) | 50 |
| ...and 239 more |  |  |  |

## Script Examples

### Camelot, Realm of Noble Knights and Noble Arms (`15635751`)

Source: [Scripts/c15635751.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15635751.lua)

```lua
		and #g>0 end
	local c=e:GetHandler()
	if Duel.SelectEffectYesNo(tp,c,96) then
		Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_DESREPLACE)
		local tc=g:Select(tp,1,1,nil):GetFirst()
```

### Gravity Balance (`37930737`)

Source: [Scripts/c37930737.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37930737.lua)

```lua
function c37930737.reptg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return e:GetHandler():IsAbleToRemove() and eg:IsExists(c37930737.repfilter,1,nil,tp) end
	return Duel.SelectEffectYesNo(tp,e:GetHandler(),96)
end
function c37930737.repval(e,c)
```

### Edge Imp Scythe (`29280589`)

Source: [Scripts/c29280589.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29280589.lua)

```lua
function c29280589.reptg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return e:GetHandler():IsAbleToRemove() and eg:IsExists(c29280589.repfilter,1,nil,tp) end
	if Duel.SelectEffectYesNo(tp,e:GetHandler(),96) then
		Duel.Remove(e:GetHandler(),POS_FACEUP,REASON_EFFECT)
		return true
```
