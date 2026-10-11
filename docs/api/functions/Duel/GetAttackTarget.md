# Duel.GetAttackTarget

## Signature

```lua
Duel.GetAttackTarget() -> Card
```

## Description

Returns the monster currently being attacked, or nil for a direct attack.

## Returns

- `Card`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4958`

## Guided Examples

Learn how to use this function in context:

- [Battle Participants And Timing](/learn/battle-participants-and-timing)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **659** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.GetAttackTarget) with `Duel.GetAttackTarget`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Trirealm Rift Judgment | `65195679` | [Scripts/c65195679.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65195679.lua) | 1 |
| K9-X Forced Release | `53792930` | [Scripts/c53792930.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53792930.lua) | 1 |
| Number 99: Utopia Dragonar | `95134948` | [Scripts/c95134948.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95134948.lua) | 1 |
| Number 38: Hope Harbinger Dragon Titanic Galaxy | `63767246` | [Scripts/c63767246.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63767246.lua) | 1 |
| All-Eyes Phantom Dragon | `70335319` | [Scripts/c70335319.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70335319.lua) | 1 |
| Darkuriboh | `1035143` | [Scripts/c1035143.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1035143.lua) | 2 |
| Genex Ally Triforce | `52709508` | [Scripts/c52709508.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52709508.lua) | 1 |
| Gladiator Beast Gaiodiaz | `90957527` | [Scripts/c90957527.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90957527.lua) | 1 |
| Magnet Warrior Sigma Minus | `87814728` | [Scripts/c87814728.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87814728.lua) | 1 |
| Megaroid City | `44139064` | [Scripts/c44139064.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44139064.lua) | 2 |
| Borrelcode Dragon | `67288539` | [Scripts/c67288539.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67288539.lua) | 1 |
| Salamangreat Sanctuary | `1295111` | [Scripts/c1295111.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1295111.lua) | 1 |
| Shura the Combat Star | `32615065` | [Scripts/c32615065.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32615065.lua) | 2 |
| Cubic Rebirth | `71442223` | [Scripts/c71442223.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71442223.lua) | 1 |
| Witchcrafter Madame Verre | `21522601` | [Scripts/c21522601.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21522601.lua) | 4 |
| X-Saber Gottoms | `8252010` | [Scripts/c8252010.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8252010.lua) | 1 |
| Mementomictlan | `43338320` | [Scripts/c43338320.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43338320.lua) | 1 |
| K9-LC Release Restraint | `27308231` | [Scripts/c27308231.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27308231.lua) | 1 |
| Red Cocoon | `2542230` | [Scripts/c2542230.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2542230.lua) | 1 |
| Performage Ball Balancer | `92530005` | [Scripts/c92530005.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92530005.lua) | 1 |
| Infernoid Piaty | `25811989` | [Scripts/c25811989.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25811989.lua) | 1 |
| Raidraptor - Last Strix | `97219708` | [Scripts/c97219708.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97219708.lua) | 1 |
| Mechanical Mechanic | `22106558` | [Scripts/c22106558.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22106558.lua) | 2 |
| White Knight Lord | `14732294` | [Scripts/c14732294.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c14732294.lua) | 1 |
| ...and 635 more |  |  |  |

## Script Examples

### Trirealm Rift Judgment (`65195679`)

Source: [Scripts/c65195679.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65195679.lua)

```lua
	if Duel.GetMatchingGroupCount(aux.TRUE,e:GetHandlerPlayer(),LOCATION_DECK,0,nil)>0 then return end
	local a=Duel.GetAttacker()
	local d=Duel.GetAttackTarget()
	if not d then return false end
	if not a:IsControler(tp) then a,d=d,a end
```

### K9-X Forced Release (`53792930`)

Source: [Scripts/c53792930.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53792930.lua)

```lua
end
function s.checkop(e,tp,eg,ep,ev,re,r,rp)
	local at=Duel.GetAttackTarget()
	local ar=Duel.GetAttacker()
	if at and at:IsSetCard(0x1cb) then
```

### Number 99: Utopia Dragonar (`95134948`)

Source: [Scripts/c95134948.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95134948.lua)

```lua
	local tc=eg:GetFirst()
	local p=tc:GetControler()
	if Duel.GetAttackTarget()~=nil then return end
	if tc:GetFlagEffect(95134948)==0 then
		tc:RegisterFlagEffect(95134948,RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END,0,1)
```
