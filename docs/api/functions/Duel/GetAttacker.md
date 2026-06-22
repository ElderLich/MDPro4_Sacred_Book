# Duel.GetAttacker

## Signature

```lua
Duel.GetAttacker() -> Card
```

## Description

Returns the monster that is currently attacking, or nil if there is no current attacker.

## Returns

- `Card`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4957`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **857** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.GetAttacker`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Prank-Kids Weather Washer](/examples/cards/44509529) | `44509529` | [Scripts/c44509529.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44509529.lua) | 65 |
| [Light End Sublimation Dragon](/examples/cards/35614780) | `35614780` | [Scripts/c35614780.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35614780.lua) | 61 |
| Red-Eyes Slash Dragon | `21140872` | [Scripts/c21140872.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21140872.lua) | 60 |
| K9-X Forced Release | `53792930` | [Scripts/c53792930.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53792930.lua) | 58 |
| Performapal Odd-Eyes Dissolver | `46136942` | [Scripts/c46136942.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46136942.lua) | 57 |
| Number 99: Utopia Dragonar | `95134948` | [Scripts/c95134948.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95134948.lua) | 57 |
| Ursarctic Quint Charge | `15758127` | [Scripts/c15758127.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15758127.lua) | 56 |
| Number 38: Hope Harbinger Dragon Titanic Galaxy | `63767246` | [Scripts/c63767246.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63767246.lua) | 56 |
| All-Eyes Phantom Dragon | `70335319` | [Scripts/c70335319.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70335319.lua) | 55 |
| Nirvana High Paladin | `80896940` | [Scripts/c80896940.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80896940.lua) | 55 |
| Favorite Hero | `11881272` | [Scripts/c11881272.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11881272.lua) | 55 |
| Genex Ally Triforce | `52709508` | [Scripts/c52709508.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52709508.lua) | 55 |
| Gladiator Beast Gaiodiaz | `90957527` | [Scripts/c90957527.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90957527.lua) | 54 |
| Magnet Warrior Sigma Minus | `87814728` | [Scripts/c87814728.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87814728.lua) | 54 |
| Megaroid City | `44139064` | [Scripts/c44139064.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44139064.lua) | 53 |
| PSY-Framegear Beta | `2810642` | [Scripts/c2810642.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2810642.lua) | 53 |
| Salamangreat Sanctuary | `1295111` | [Scripts/c1295111.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1295111.lua) | 53 |
| D/D/D Super Doom King Bright Armageddon | `72402069` | [Scripts/c72402069.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c72402069.lua) | 52 |
| Shura the Combat Star | `32615065` | [Scripts/c32615065.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32615065.lua) | 52 |
| Cubic Rebirth | `71442223` | [Scripts/c71442223.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71442223.lua) | 52 |
| X-Saber Gottoms | `8252010` | [Scripts/c8252010.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8252010.lua) | 52 |
| Armed Dragon LV10 White | `84425220` | [Scripts/c84425220.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84425220.lua) | 52 |
| Mementomictlan | `43338320` | [Scripts/c43338320.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43338320.lua) | 52 |
| K9-LC Release Restraint | `27308231` | [Scripts/c27308231.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27308231.lua) | 52 |
| ...and 833 more |  |  |  |

## Script Examples

### Prank-Kids Weather Washer (`44509529`)

Source: [Scripts/c44509529.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44509529.lua)

```lua
end
function c44509529.actcon(e)
	local a=Duel.GetAttacker()
	return a and a:IsControler(e:GetHandlerPlayer()) and a:IsSetCard(0x120)
end
```

### Light End Sublimation Dragon (`35614780`)

Source: [Scripts/c35614780.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35614780.lua)

```lua
end
function s.atkcon(e,tp,eg,ep,ev,re,r,rp)
	return Duel.GetAttacker():IsControler(1-tp)
end
function s.atktg(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Red-Eyes Slash Dragon (`21140872`)

Source: [Scripts/c21140872.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21140872.lua)

```lua
end
function c21140872.eqcon(e)
	return Duel.GetAttacker():IsSetCard(0x3b)
end
function c21140872.eqfilter(c,tp)
```
