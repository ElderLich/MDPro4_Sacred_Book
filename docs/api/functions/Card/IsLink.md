# Card.IsLink

## Signature

```lua
Card.IsLink(Card c, int link1, [int link2], [... int]) -> bool
```

## Description

Checks whether c:GetLink() equals any supplied link value. Nil link arguments are skipped; non-Link cards compare as 0.

## Parameters

- `c` `Card`
- `link1` `int`
- `link2` `int` optional
- `...` `int` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3492`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **37** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.IsLink`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Tri-Brigade Nervall | `14816857` | [Scripts/c14816857.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c14816857.lua) | 2 |
| Tri-Brigade Fraktall | `87209160` | [Scripts/c87209160.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87209160.lua) | 2 |
| Tri-Brigade Kitt | `56196385` | [Scripts/c56196385.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56196385.lua) | 2 |
| Tri-Brigade Kerass | `50810455` | [Scripts/c50810455.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50810455.lua) | 2 |
| V-LAN Hydra | `13536606` | [Scripts/c13536606.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13536606.lua) | 1 |
| Appliancer Test | `66380357` | [Scripts/c66380357.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66380357.lua) | 1 |
| Forge a New Future | `27104921` | [Scripts/c27104921.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27104921.lua) | 2 |
| Tri-Brigade Hammer | `92269002` | [Scripts/c92269002.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92269002.lua) | 2 |
| Yummyusment☆Mignon | `66975205` | [Scripts/c66975205.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66975205.lua) | 1 |
| Marincess Circulation | `83723605` | [Scripts/c83723605.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c83723605.lua) | 1 |
| Lollipo★Yummy Way | `93192592` | [Scripts/c93192592.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93192592.lua) | 2 |
| Cupsy★Yummy Way | `31603289` | [Scripts/c31603289.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31603289.lua) | 2 |
| Cooky★Yummy Way | `67098897` | [Scripts/c67098897.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67098897.lua) | 2 |
| Spright Double Cross | `68250822` | [Scripts/c68250822.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c68250822.lua) | 1 |
| Firewall eXceed Dragon | `21065189` | [Scripts/c21065189.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21065189.lua) | 1 |
| World Chalice Guardragon Almarduke | `95793022` | [Scripts/c95793022.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95793022.lua) | 1 |
| Danmari @Ignister | `66192538` | [Scripts/c66192538.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66192538.lua) | 1 |
| Spright Sprind | `72329844` | [Scripts/c72329844.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c72329844.lua) | 1 |
| Bomber Place | `71750854` | [Scripts/c71750854.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71750854.lua) | 2 |
| Lollipo☆Yummy | `4215180` | [Scripts/c4215180.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4215180.lua) | 1 |
| EM:P Meowmine | `48017189` | [Scripts/c48017189.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48017189.lua) | 1 |
| Cupsy☆Yummy | `31425736` | [Scripts/c31425736.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31425736.lua) | 1 |
| Cooky☆Yummy | `68810435` | [Scripts/c68810435.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c68810435.lua) | 1 |
| Spright Carrot | `2311090` | [Scripts/c2311090.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2311090.lua) | 3 |
| ...and 13 more |  |  |  |

## Script Examples

### Tri-Brigade Nervall (`14816857`)

Source: [Scripts/c14816857.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c14816857.lua)

```lua
end
function c14816857.fselect(g,tg)
	return tg:IsExists(Card.IsLink,1,nil,#g)
end
function c14816857.spfilter(c,e,tp)
```

### Tri-Brigade Fraktall (`87209160`)

Source: [Scripts/c87209160.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87209160.lua)

```lua
end
function c87209160.fselect(g,tg)
	return tg:IsExists(Card.IsLink,1,nil,#g)
end
function c87209160.spfilter(c,e,tp)
```

### Tri-Brigade Kitt (`56196385`)

Source: [Scripts/c56196385.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56196385.lua)

```lua
end
function c56196385.fselect(g,tg)
	return tg:IsExists(Card.IsLink,1,nil,#g)
end
function c56196385.spfilter(c,e,tp)
```
