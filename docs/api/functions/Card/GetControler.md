# Card.GetControler

## Signature

```lua
Card.GetControler(Card c) -> int
```

## Description

Returns c's current controller.

## Parameters

- `c` `Card`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3456`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **1228** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.GetControler`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Artmage Non-Finito](/examples/cards/74631897) | `74631897` | [Scripts/c74631897.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74631897.lua) | 78 |
| [Lady's Dragonmaid](/examples/cards/48658295) | `48658295` | [Scripts/c48658295.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48658295.lua) | 75 |
| [Goyo Emperor](/examples/cards/59255742) | `59255742` | [Scripts/c59255742.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59255742.lua) | 70 |
| [Ghostrick Renovation](/examples/cards/61818176) | `61818176` | [Scripts/c61818176.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61818176.lua) | 65 |
| [Ursarctic Polari](/examples/cards/27693363) | `27693363` | [Scripts/c27693363.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27693363.lua) | 65 |
| [Odd-Eyes Revolution Dragon](/examples/cards/16306932) | `16306932` | [Scripts/c16306932.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16306932.lua) | 64 |
| [D/D/D/D Dimensional King Arc Crisis](/examples/cards/71398055) | `71398055` | [Scripts/c71398055.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71398055.lua) | 63 |
| [Odd-Eyes Arcray Dragon](/examples/cards/6218704) | `6218704` | [Scripts/c6218704.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6218704.lua) | 62 |
| [Enlightenment Dragon](/examples/cards/46186135) | `46186135` | [Scripts/c46186135.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46186135.lua) | 62 |
| [Flower Cardian Peony with Butterfly](/examples/cards/57261568) | `57261568` | [Scripts/c57261568.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57261568.lua) | 62 |
| [Ultimate Crystal Rainbow Dragon Overdrive](/examples/cards/84544192) | `84544192` | [Scripts/c84544192.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84544192.lua) | 62 |
| [Tellusion the Magna Warrior](/examples/cards/24431911) | `24431911` | [Scripts/c24431911.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24431911.lua) | 62 |
| [Ursarctic Polar Star](/examples/cards/62714453) | `62714453` | [Scripts/c62714453.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62714453.lua) | 62 |
| [Vidolium the Unstable Power Patron of Unity](/examples/cards/70488851) | `70488851` | [Scripts/c70488851.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70488851.lua) | 61 |
| [DoSolfachord Coolia](/examples/cards/80776622) | `80776622` | [Scripts/c80776622.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80776622.lua) | 61 |
| [W:P Fancy Ball](/examples/cards/4993187) | `4993187` | [Scripts/c4993187.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4993187.lua) | 61 |
| [Flower Cardian Willow with Calligrapher](/examples/cards/89818984) | `89818984` | [Scripts/c89818984.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c89818984.lua) | 61 |
| [Cyber Pharos](/examples/cards/29719112) | `29719112` | [Scripts/c29719112.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29719112.lua) | 61 |
| Vaylantz Genesis Grand Duke | `76075139` | [Scripts/c76075139.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76075139.lua) | 60 |
| Hunting Horn | `55421040` | [Scripts/c55421040.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55421040.lua) | 59 |
| Chaos Emperor, the Dragon of Armageddon | `4538826` | [Scripts/c4538826.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4538826.lua) | 58 |
| A-to-Z-Dragon Buster Cannon | `65172015` | [Scripts/c65172015.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65172015.lua) | 58 |
| K9-X Forced Release | `53792930` | [Scripts/c53792930.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53792930.lua) | 58 |
| Revolution Cyber Dragon | `66664203` | [Scripts/c66664203.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66664203.lua) | 58 |
| ...and 1204 more |  |  |  |

## Script Examples

### Artmage Non-Finito (`74631897`)

Source: [Scripts/c74631897.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74631897.lua)

```lua
function s.spcon(e,c)
	if c==nil then return true end
	local tp=c:GetControler()
	if Duel.GetFlagEffect(tp,id)>0 then return false end
	local rg=s.getrg(tp,c)
```

### Lady's Dragonmaid (`48658295`)

Source: [Scripts/c48658295.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48658295.lua)

```lua
function s.spcon(e,c)
	if c==nil then return true end
	local tp=c:GetControler()
	local fg=Duel.GetMatchingGroup(s.fusfilter,tp,LOCATION_ONFIELD+LOCATION_GRAVE,0,nil)
	return fg:CheckSubGroup(s.fselect,2,2)
```

### Goyo Emperor (`59255742`)

Source: [Scripts/c59255742.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59255742.lua)

```lua
end
function c59255742.ctfilter(c)
	return c:GetControler()~=c:GetOwner()
end
function c59255742.cttg(e,tp,eg,ep,ev,re,r,rp,chk)
```
