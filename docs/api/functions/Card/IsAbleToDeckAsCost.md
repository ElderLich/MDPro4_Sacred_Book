# Card.IsAbleToDeckAsCost

## Signature

```lua
Card.IsAbleToDeckAsCost(Card c) -> bool
```

## Description

Checks whether c can be returned to the Deck as a cost.

## Parameters

- `c` `Card`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3645`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **78** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.IsAbleToDeckAsCost) with `Card.IsAbleToDeckAsCost`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Pendulum Evolution](/examples/cards/55795155) | `55795155` | [Scripts/c55795155.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55795155.lua) | 1 |
| [Yomagna the Fire Phantom](/examples/cards/17350692) | `17350692` | [Scripts/c17350692.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17350692.lua) | 1 |
| Anubis the Last Judge | `60411677` | [Scripts/c60411677.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60411677.lua) | 1 |
| Shimmering Shatterer of the Sacred Beasts | `3441553` | [Scripts/c3441553.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3441553.lua) | 1 |
| Possessed Destiny - Wynn | `60516416` | [Scripts/c60516416.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60516416.lua) | 1 |
| Sauravis, Dragon Sage of the Voiceless Voice | `88284599` | [Scripts/c88284599.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88284599.lua) | 1 |
| Black Chaos | `98684220` | [Scripts/c98684220.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c98684220.lua) | 1 |
| Sweet Dreams, Nemleria | `44843954` | [Scripts/c44843954.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44843954.lua) | 1 |
| Exosister Irene | `79858629` | [Scripts/c79858629.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c79858629.lua) | 1 |
| Kyoro Ryu-Ge Kaiva | `93509766` | [Scripts/c93509766.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93509766.lua) | 2 |
| Blitzclique Alternator | `59921227` | [Scripts/c59921227.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59921227.lua) | 1 |
| Gladiator Beast Lanista | `2067935` | [Scripts/c2067935.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2067935.lua) | 1 |
| Heavy Beetrooper Mighty Neptune | `14357527` | [Scripts/c14357527.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c14357527.lua) | 1 |
| Ryu-Ge Realm - Sea Spires | `28669235` | [Scripts/c28669235.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28669235.lua) | 1 |
| Gladiator Beast Gistel | `26582143` | [Scripts/c26582143.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c26582143.lua) | 1 |
| Kairo Ryu-Ge Emva | `20904475` | [Scripts/c20904475.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20904475.lua) | 1 |
| Palm Ryzeal | `61116514` | [Scripts/c61116514.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61116514.lua) | 1 |
| Ryu-Ge Realm - Wyrm Winds | `55154344` | [Scripts/c55154344.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55154344.lua) | 1 |
| Ryu-Ge End | `90664684` | [Scripts/c90664684.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90664684.lua) | 1 |
| Gladiator Beast Attorix | `52502677` | [Scripts/c52502677.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52502677.lua) | 1 |
| Cielo, the Veil of Raise Moon | `75934716` | [Scripts/c75934716.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75934716.lua) | 1 |
| Rescue-ACE Quick Attacker | `47425162` | [Scripts/c47425162.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c47425162.lua) | 1 |
| Gladiator Beast Darius | `25924653` | [Scripts/c25924653.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25924653.lua) | 1 |
| Nouvelles Restaurant "At Table" | `15388353` | [Scripts/c15388353.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15388353.lua) | 1 |
| ...and 54 more |  |  |  |

## Script Examples

### Pendulum Evolution (`55795155`)

Source: [Scripts/c55795155.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55795155.lua)

```lua
end
function c55795155.cfilter(c,tp)
	return c:IsType(TYPE_PENDULUM) and c:IsAbleToDeckAsCost()
		and Duel.IsExistingMatchingCard(c55795155.thfilter,tp,LOCATION_DECK,0,1,nil,c:GetCode())
end
```

### Yomagna the Fire Phantom (`17350692`)

Source: [Scripts/c17350692.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17350692.lua)

```lua
end
function s.sprfilter(c)
	return c:IsAbleToDeckAsCost() or c:IsAbleToExtraAsCost()
end
function s.gcheck(g)
```

### Anubis the Last Judge (`60411677`)

Source: [Scripts/c60411677.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60411677.lua)

```lua
end
function s.sprfilter(c)
	return (c:IsCode(29762407) or c:IsType(TYPE_TRAP)) and c:IsAbleToDeckAsCost()
end
function s.sprcon(e,c)
```
