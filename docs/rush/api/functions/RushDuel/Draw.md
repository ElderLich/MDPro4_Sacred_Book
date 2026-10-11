# RushDuel.Draw

Alias: `RD.Draw`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.Draw([int player], [int count]) -> int
```

## Description

Draws with REASON_EFFECT using the supplied player/count, or the current chain's target player/parameter when arguments are omitted. Pair RD.TargetDraw(tp, count) in targeting with RD.Draw() in resolution.

## Parameters

- `player` `int` (optional): Player; defaults to CHAININFO_TARGET_PLAYER.
- `count` `int` (optional): Count; defaults to CHAININFO_TARGET_PARAM.

## Returns

- `int`: Result returned by Duel.Draw.

## Source

`Rush/Utilities/RDTarget.lua:34`

```lua
function RushDuel.Draw(player, count)
    local p, d = Duel.GetChainInfo(0, CHAININFO_TARGET_PLAYER, CHAININFO_TARGET_PARAM)
    return Duel.Draw(player or p, count or d, REASON_EFFECT)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **150** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.Draw) with `RushDuel.Draw`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Elemental Circulation](/examples/rush-cards/120263030) | `120263030` | [Rush/Scripts/c120263030.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120263030.lua) | 1 |
| [Ember the Ultra Assistant](/examples/rush-cards/120283035) | `120283035` | [Rush/Scripts/c120283035.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120283035.lua) | 1 |
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
| Dimension Pramma | `120309026` | [Rush/Scripts/c120309026.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120309026.lua) | 1 |
| Spell Extraction | `120246085` | [Rush/Scripts/c120246085.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120246085.lua) | 1 |
| Excutie Leya Frontier | `120293069` | [Rush/Scripts/c120293069.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120293069.lua) | 1 |
| Moonforce Piyopi | `120300011` | [Rush/Scripts/c120300011.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300011.lua) | 1 |
| The Secret of Manifestation | `120257051` | [Rush/Scripts/c120257051.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120257051.lua) | 1 |
| Legendary Scout | `120271047` | [Rush/Scripts/c120271047.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120271047.lua) | 1 |
| Straynge Magician | `120109032` | [Rush/Scripts/c120109032.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120109032.lua) | 1 |
| ...and 126 more |  |  |  |

## Script Examples

### Elemental Circulation (`120263030`)

Source: [Rush/Scripts/c120263030.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120263030.lua)

```lua
end
function cm.activate(e,tp,eg,ep,ev,re,r,rp)
	if RD.Draw()~=0 then
		RD.SelectAndDoAction(HINTMSG_TOGRAVE,Card.IsAbleToGrave,tp,LOCATION_HAND,0,1,1,nil,function(g)
			Duel.BreakEffect()
```

### Ember the Ultra Assistant (`120283035`)

Source: [Rush/Scripts/c120283035.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120283035.lua)

```lua
end
function cm.operation(e,tp,eg,ep,ev,re,r,rp)
	if RD.Draw()~=0 and Duel.IsExistingMatchingCard(cm.exfilter,tp,LOCATION_GRAVE,0,1,nil) then
		local sg,og=RD.SendDeckTopToGraveAndCanSelect(tp,2,aux.Stringid(m,1),HINTMSG_ATOHAND,aux.NecroValleyFilter(cm.thfilter),1,1)
		if sg:GetCount()>0 then
```

### Nobody Phantom Thief (`120244060`)

Source: [Rush/Scripts/c120244060.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120244060.lua)

```lua
end
function cm.activate(e,tp,eg,ep,ev,re,r,rp)
	if RD.Draw()~=0 then
		RD.SelectAndDoAction(HINTMSG_TOGRAVE,cm.filter,tp,LOCATION_HAND,0,1,99,nil,function(g)
			Duel.BreakEffect()
```
