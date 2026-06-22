# Duel.CheckReleaseGroupEx

## Signature

```lua
Duel.CheckReleaseGroupEx(int player, [function|nil f], int count, int reason, bool use_hand, [Card|Group|nil ex], ... any) -> bool
```

## Description

Checks whether player can release at least count cards matching f, excluding ex, with an explicit reason and optional hand releases.
Extra arguments after ex are passed to f after the Card argument.

## Parameters

- `player` `int`
- `f` `function|nil` optional
- `count` `int`
- `reason` `int`
- `use_hand` `bool`
- `ex` `Card|Group|nil` optional
- `...` `any`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4978`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **115** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.CheckReleaseGroupEx`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Odd-Eyes Arcray Dragon](/examples/cards/6218704) | `6218704` | [Scripts/c6218704.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6218704.lua) | 62 |
| [Flower Cardian Peony with Butterfly](/examples/cards/57261568) | `57261568` | [Scripts/c57261568.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57261568.lua) | 62 |
| [Flower Cardian Willow with Calligrapher](/examples/cards/89818984) | `89818984` | [Scripts/c89818984.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c89818984.lua) | 61 |
| [Cyber Pharos](/examples/cards/29719112) | `29719112` | [Scripts/c29719112.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29719112.lua) | 61 |
| Vaylantz Genesis Grand Duke | `76075139` | [Scripts/c76075139.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76075139.lua) | 60 |
| Kuribeh | `34419588` | [Scripts/c34419588.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34419588.lua) | 57 |
| Clown Crew Malabarisme | `83232904` | [Scripts/c83232904.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c83232904.lua) | 56 |
| Abyssrhine, the Atlantean Spirit | `17080584` | [Scripts/c17080584.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17080584.lua) | 53 |
| Cyberdark End Dragon | `37542782` | [Scripts/c37542782.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37542782.lua) | 53 |
| Tensei Ryu-Ge Anva | `56322832` | [Scripts/c56322832.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56322832.lua) | 52 |
| Rainbow Overdragon | `37440988` | [Scripts/c37440988.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37440988.lua) | 52 |
| Egyptian God Slime | `42166000` | [Scripts/c42166000.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42166000.lua) | 52 |
| LaSolfachord Angelia | `27993919` | [Scripts/c27993919.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27993919.lua) | 51 |
| Dawn Angel Kambi | `12500059` | [Scripts/c12500059.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12500059.lua) | 51 |
| Hrimnir the Divine Follower | `49904658` | [Scripts/c49904658.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49904658.lua) | 51 |
| Clown Crew Finale | `84031736` | [Scripts/c84031736.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84031736.lua) | 50 |
| Fabled Levilazebul | `21281085` | [Scripts/c21281085.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21281085.lua) | 50 |
| Toon Black Luster Soldier | `28711704` | [Scripts/c28711704.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28711704.lua) | 50 |
| Hieratic Dragon of Nebthet | `31516413` | [Scripts/c31516413.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31516413.lua) | 50 |
| Blue-Eyes Tyrant Dragon | `11443677` | [Scripts/c11443677.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11443677.lua) | 49 |
| Hieratic Dragon of Su | `3300267` | [Scripts/c3300267.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3300267.lua) | 49 |
| Gizmek Yata, the Gleaming Vanguard | `13224603` | [Scripts/c13224603.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13224603.lua) | 47 |
| Fallen Angel of the Golden Land | `43143567` | [Scripts/c43143567.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43143567.lua) | 47 |
| Silent Swordsman | `15180041` | [Scripts/c15180041.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15180041.lua) | 47 |
| ...and 91 more |  |  |  |

## Script Examples

### Odd-Eyes Arcray Dragon (`6218704`)

Source: [Scripts/c6218704.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6218704.lua)

```lua
function c6218704.hspcon(e,c)
	if c==nil then return true end
	return c:IsFacedown() and Duel.CheckReleaseGroupEx(c:GetControler(),c6218704.hspfilter,1,REASON_SPSUMMON,false,nil,c:GetControler(),c)
end
function c6218704.hsptg(e,tp,eg,ep,ev,re,r,rp,chk,c)
```

### Flower Cardian Peony with Butterfly (`57261568`)

Source: [Scripts/c57261568.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57261568.lua)

```lua
	if c==nil then return true end
	local tp=c:GetControler()
	return Duel.CheckReleaseGroupEx(tp,c57261568.hspfilter,1,REASON_SPSUMMON,false,nil,tp)
end
function c57261568.hsptg(e,tp,eg,ep,ev,re,r,rp,chk,c)
```

### Flower Cardian Willow with Calligrapher (`89818984`)

Source: [Scripts/c89818984.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c89818984.lua)

```lua
	if c==nil then return true end
	local tp=c:GetControler()
	return Duel.CheckReleaseGroupEx(tp,c89818984.hspfilter,1,REASON_SPSUMMON,false,nil,tp)
end
function c89818984.hsptg(e,tp,eg,ep,ev,re,r,rp,chk,c)
```
