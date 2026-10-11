# RushDuel.TargetDraw

Alias: `RD.TargetDraw`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.TargetDraw(int player, int count) -> void
```

## Description

Stores the target player and draw count on the current chain link and declares CATEGORY_DRAW operation information. This helper does not draw cards or check deck availability.

## Parameters

- `player` `int`: Drawing player.
- `count` `int`: Number to draw.

## Returns

No return values.

## Source

`Rush/Utilities/RDTarget.lua:5`

```lua
function RushDuel.TargetDraw(player, count)
    Duel.SetTargetPlayer(player)
    Duel.SetTargetParam(count)
    Duel.SetOperationInfo(0, CATEGORY_DRAW, nil, 0, player, count)
end
```

## Guided Examples

Learn how to use this function in context:

- [Rush Duel Scripting](/learn/rush-duel-scripting)

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **160** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.TargetDraw) with `RushDuel.TargetDraw`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Elemental Circulation](/examples/rush-cards/120263030) | `120263030` | [Rush/Scripts/c120263030.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120263030.lua) | 1 |
| [Ember the Ultra Assistant](/examples/rush-cards/120283035) | `120283035` | [Rush/Scripts/c120283035.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120283035.lua) | 1 |
| [Gold Rush](/examples/rush-cards/120247059) | `120247059` | [Rush/Scripts/c120247059.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120247059.lua) | 1 |
| [Nobody Phantom Thief](/examples/rush-cards/120244060) | `120244060` | [Rush/Scripts/c120244060.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120244060.lua) | 1 |
| [Nobody Phantom Thief](/examples/rush-cards/120273005) | `120273005` | [Rush/Scripts/c120273005.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120273005.lua) | 1 |
| [Moonforce Timo](/examples/rush-cards/120300015) | `120300015` | [Rush/Scripts/c120300015.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300015.lua) | 1 |
| [Dimension Oper](/examples/rush-cards/120309025) | `120309025` | [Rush/Scripts/c120309025.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120309025.lua) | 1 |
| [Preferlyre](/examples/rush-cards/120283046) | `120283046` | [Rush/Scripts/c120283046.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120283046.lua) | 1 |
| [Lovely Rabbit](/examples/rush-cards/120300018) | `120300018` | [Rush/Scripts/c120300018.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300018.lua) | 1 |
| [Mystic Dealer](/examples/rush-cards/120105006) | `120105006` | [Rush/Scripts/c120105006.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120105006.lua) | 1 |
| Icelyn the Super Assistant | `120254064` | [Rush/Scripts/c120254064.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120254064.lua) | 1 |
| Daigyakutenno Megami | `120203019` | [Rush/Scripts/c120203019.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120203019.lua) | 1 |
| Fusionic Revivern | `120109030` | [Rush/Scripts/c120109030.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120109030.lua) | 1 |
| Abysslayer Quintiamat | `120257021` | [Rush/Scripts/c120257021.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120257021.lua) | 1 |
| Under Dealer | `120290015` | [Rush/Scripts/c120290015.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290015.lua) | 1 |
| Lostream Shell | `120309039` | [Rush/Scripts/c120309039.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120309039.lua) | 1 |
| Goe Goe the Rumored Ninja | `120306029` | [Rush/Scripts/c120306029.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120306029.lua) | 1 |
| Harpie Regina | `120247008` | [Rush/Scripts/c120247008.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120247008.lua) | 1 |
| Spell Extraction | `120246085` | [Rush/Scripts/c120246085.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120246085.lua) | 1 |
| Excutie Leya Frontier | `120293069` | [Rush/Scripts/c120293069.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120293069.lua) | 1 |
| Boost Rescue | `120222065` | [Rush/Scripts/c120222065.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120222065.lua) | 1 |
| Moonforce Piyopi | `120300011` | [Rush/Scripts/c120300011.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300011.lua) | 1 |
| The Secret of Manifestation | `120257051` | [Rush/Scripts/c120257051.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120257051.lua) | 1 |
| Legendary Scout | `120271047` | [Rush/Scripts/c120271047.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120271047.lua) | 1 |
| ...and 136 more |  |  |  |

## Script Examples

### Elemental Circulation (`120263030`)

Source: [Rush/Scripts/c120263030.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120263030.lua)

```lua
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsPlayerCanDraw(tp,3) end
	RD.TargetDraw(tp,3)
end
function cm.activate(e,tp,eg,ep,ev,re,r,rp)
```

### Ember the Ultra Assistant (`120283035`)

Source: [Rush/Scripts/c120283035.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120283035.lua)

```lua
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsPlayerCanDraw(tp,1) end
	RD.TargetDraw(tp,1)
end
function cm.operation(e,tp,eg,ep,ev,re,r,rp)
```

### Gold Rush (`120247059`)

Source: [Rush/Scripts/c120247059.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120247059.lua)

```lua
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsPlayerCanDraw(tp,3) end
	RD.TargetDraw(tp,3)
end
function cm.activate(e,tp,eg,ep,ev,re,r,rp)
```
