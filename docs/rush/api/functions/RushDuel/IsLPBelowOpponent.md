# RushDuel.IsLPBelowOpponent

Alias: `RD.IsLPBelowOpponent`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsLPBelowOpponent(any player, any lp) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 玩家的LP比对方少 lp 以上
```

## Parameters

- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `lp` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:69`

```lua
function RushDuel.IsLPBelowOpponent(player, lp)
    return Duel.GetLP(player) <= Duel.GetLP(1 - player) - (lp or 0)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **19** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.IsLPBelowOpponent) with `RushDuel.IsLPBelowOpponent`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Supreme Machine Magnum Overlord \[L\]](/examples/rush-cards/120150001) | `120150001` | [Rush/Scripts/c120150001.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120150001.lua) | 1 |
| CAN - Melo:D | `120203010` | [Rush/Scripts/c120203010.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120203010.lua) | 1 |
| Art Angel Metal Position | `120228014` | [Rush/Scripts/c120228014.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120228014.lua) | 1 |
| Sneezing Greedizauls | `120151008` | [Rush/Scripts/c120151008.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120151008.lua) | 1 |
| Cosmic Sucker | `120294021` | [Rush/Scripts/c120294021.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120294021.lua) | 1 |
| Fiery Infernleon | `120205019` | [Rush/Scripts/c120205019.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120205019.lua) | 1 |
| Dian Keto the Cleaning Prodigy | `120260065` | [Rush/Scripts/c120260065.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120260065.lua) | 1 |
| 300 Light Year Red Cape | `120222051` | [Rush/Scripts/c120222051.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120222051.lua) | 1 |
| Requiem Strike Back | `120277060` | [Rush/Scripts/c120277060.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120277060.lua) | 1 |
| Romanpick | `120130023` | [Rush/Scripts/c120130023.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120130023.lua) | 1 |
| The Perfect Dragiastar | `120283026` | [Rush/Scripts/c120283026.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120283026.lua) | 1 |
| Metal Megaleon | `120205020` | [Rush/Scripts/c120205020.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120205020.lua) | 1 |
| Telepathic Agent | `120140030` | [Rush/Scripts/c120140030.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120140030.lua) | 1 |
| Light and Flame | `120249054` | [Rush/Scripts/c120249054.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120249054.lua) | 1 |
| Tribute Lock | `120213028` | [Rush/Scripts/c120213028.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120213028.lua) | 1 |
| Inside Out Roll | `120151044` | [Rush/Scripts/c120151044.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120151044.lua) | 1 |
| My Patience Has Run Out! | `120246067` | [Rush/Scripts/c120246067.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120246067.lua) | 1 |
| Supreme Marine Fortress Magnum Overbase | `120199042` | [Rush/Scripts/c120199042.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120199042.lua) | 1 |
| Folder Blitz the Infinite Dream | `120140028` | [Rush/Scripts/c120140028.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120140028.lua) | 1 |

## Script Examples

### Supreme Machine Magnum Overlord [L] (`120150001`)

Source: [Rush/Scripts/c120150001.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120150001.lua)

```lua
--Atk Up
function cm.condition(e,tp,eg,ep,ev,re,r,rp)
	return RD.MaximumMode(e) and RD.IsLPBelowOpponent(tp,1)
end
cm.cost=RD.CostSendHandToGrave(Card.IsAbleToGraveAsCost,1,1)
```

### CAN - Melo:D (`120203010`)

Source: [Rush/Scripts/c120203010.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120203010.lua)

```lua
function cm.operation(e,tp,eg,ep,ev,re,r,rp)
	RD.SelectAndDoAction(HINTMSG_TODECK,cm.tdfilter,tp,0,LOCATION_ONFIELD,1,1,nil,function(g)
		if RD.SendToDeckAndExists(g,e,tp,REASON_EFFECT) and RD.IsLPBelowOpponent(tp,1) then
			RD.CanSelectAndDoAction(aux.Stringid(m,1),HINTMSG_ATOHAND,aux.NecroValleyFilter(cm.thfilter),tp,LOCATION_GRAVE,0,1,1,nil,function(sg)
				RD.SendToHandAndExists(sg,e,tp,REASON_EFFECT)
```

### Art Angel Metal Position (`120228014`)

Source: [Rush/Scripts/c120228014.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120228014.lua)

```lua
end
function cm.condition(e,tp,eg,ep,ev,re,r,rp)
	return RD.IsLPBelowOpponent(tp,1)
end
cm.cost=RD.CostSendMZoneToGrave(cm.costfilter,1,1,true)
```
