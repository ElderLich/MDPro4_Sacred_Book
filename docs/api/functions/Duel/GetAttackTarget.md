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

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **658** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.GetAttackTarget`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| K9-X Forced Release | `53792930` | [Scripts/c53792930.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53792930.lua) | 58 |
| Number 99: Utopia Dragonar | `95134948` | [Scripts/c95134948.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95134948.lua) | 57 |
| Number 38: Hope Harbinger Dragon Titanic Galaxy | `63767246` | [Scripts/c63767246.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63767246.lua) | 56 |
| All-Eyes Phantom Dragon | `70335319` | [Scripts/c70335319.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70335319.lua) | 55 |
| Darkuriboh | `1035143` | [Scripts/c1035143.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1035143.lua) | 55 |
| Genex Ally Triforce | `52709508` | [Scripts/c52709508.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52709508.lua) | 55 |
| Gladiator Beast Gaiodiaz | `90957527` | [Scripts/c90957527.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90957527.lua) | 54 |
| Magnet Warrior Sigma Minus | `87814728` | [Scripts/c87814728.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87814728.lua) | 54 |
| Megaroid City | `44139064` | [Scripts/c44139064.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44139064.lua) | 53 |
| Borrelcode Dragon | `67288539` | [Scripts/c67288539.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67288539.lua) | 53 |
| Salamangreat Sanctuary | `1295111` | [Scripts/c1295111.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1295111.lua) | 53 |
| Shura the Combat Star | `32615065` | [Scripts/c32615065.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32615065.lua) | 52 |
| Cubic Rebirth | `71442223` | [Scripts/c71442223.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71442223.lua) | 52 |
| X-Saber Gottoms | `8252010` | [Scripts/c8252010.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8252010.lua) | 52 |
| Mementomictlan | `43338320` | [Scripts/c43338320.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43338320.lua) | 52 |
| K9-LC Release Restraint | `27308231` | [Scripts/c27308231.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27308231.lua) | 52 |
| Red Cocoon | `2542230` | [Scripts/c2542230.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2542230.lua) | 52 |
| Performage Ball Balancer | `92530005` | [Scripts/c92530005.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92530005.lua) | 51 |
| Infernoid Piaty | `25811989` | [Scripts/c25811989.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25811989.lua) | 51 |
| Raidraptor - Last Strix | `97219708` | [Scripts/c97219708.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97219708.lua) | 50 |
| Mechanical Mechanic | `22106558` | [Scripts/c22106558.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22106558.lua) | 50 |
| VARefar, the Judge of Ball | `19743887` | [Scripts/c19743887.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c19743887.lua) | 50 |
| Charming Resort Staff | `64753157` | [Scripts/c64753157.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c64753157.lua) | 50 |
| Borreload Dragon | `31833038` | [Scripts/c31833038.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31833038.lua) | 50 |
| ...and 634 more |  |  |  |

## Script Examples

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

### Number 38: Hope Harbinger Dragon Titanic Galaxy (`63767246`)

Source: [Scripts/c63767246.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63767246.lua)

```lua
end
function c63767246.cbcon(e,tp,eg,ep,ev,re,r,rp)
	return Duel.GetTurnPlayer()~=tp and Duel.GetAttackTarget()~=e:GetHandler()
end
function c63767246.cbcost(e,tp,eg,ep,ev,re,r,rp,chk)
```
