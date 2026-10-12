# RushDuel.SendToDeckTopOrBottom

Alias: `RD.SendToDeckTopOrBottom`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.SendToDeckTopOrBottom(any target, any effect, any player, any reason, any top_desc, any bottom_desc) -> any
```

## Description

Rush Duel helper declared in `RDAction.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
操作: 返回卡组上面或下面 (排序)
```

## Parameters

- `target` `any`: Type and behavior are not yet reviewed; see the source.
- `effect` `any`: Type and behavior are not yet reviewed; see the source.
- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `reason` `any`: Type and behavior are not yet reviewed; see the source.
- `top_desc` `any`: Type and behavior are not yet reviewed; see the source.
- `bottom_desc` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAction.lua:416`

```lua
function RushDuel.SendToDeckTopOrBottom(target, effect, player, reason, top_desc, bottom_desc)
    local sequence = Duel.SelectOption(player, top_desc, bottom_desc)
    if sequence == 0 then
	    RD.NeedShuffleHand[player + 1] = true
        return RushDuel.SendToDeckTop(target, effect, player, reason)
    else
        return RushDuel.SendToDeckBottom(target, effect, player, reason)
    end
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **5** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.SendToDeckTopOrBottom) with `RushDuel.SendToDeckTopOrBottom`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Spice Cross Secret Recipe](/examples/rush-cards/120261060) | `120261060` | [Rush/Scripts/c120261060.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120261060.lua) | 1 |
| Piercing Dragon Bunker Strike | `120130022` | [Rush/Scripts/c120130022.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120130022.lua) | 1 |
| Cybersepice Nutmeg | `120261018` | [Rush/Scripts/c120261018.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120261018.lua) | 1 |
| Psyquip da Capo | `120264052` | [Rush/Scripts/c120264052.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120264052.lua) | 1 |
| Spice Cross Mix | `120261055` | [Rush/Scripts/c120261055.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120261055.lua) | 1 |

## Script Examples

### Spice Cross Secret Recipe (`120261060`)

Source: [Rush/Scripts/c120261060.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120261060.lua)

```lua
			RD.CanSelectAndDoAction(aux.Stringid(m,1),HINTMSG_TODECK,aux.NecroValleyFilter(Card.IsAbleToDeck),tp,0,LOCATION_GRAVE,1,1,nil,function(g)
				Duel.BreakEffect()
				RD.SendToDeckTopOrBottom(g,e,tp,REASON_EFFECT,aux.Stringid(m,2),aux.Stringid(m,3))
			end)
		end
```

### Piercing Dragon Bunker Strike (`120130022`)

Source: [Rush/Scripts/c120130022.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120130022.lua)

```lua
	RD.SelectAndDoAction(HINTMSG_TODECK,Card.IsAbleToDeck,p,LOCATION_HAND,0,ct,ct,nil,function(g)
		Duel.BreakEffect()
		RD.SendToDeckTopOrBottom(g,e,p,REASON_EFFECT,aux.Stringid(m,1),aux.Stringid(m,2))
	end)
end
```

### Cybersepice Nutmeg (`120261018`)

Source: [Rush/Scripts/c120261018.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120261018.lua)

```lua
	RD.CanSelectAndDoAction(aux.Stringid(m,2),HINTMSG_TODECK,filter,tp,LOCATION_GRAVE,LOCATION_GRAVE,1,1,nil,function(g)
		Duel.BreakEffect()
		RD.SendToDeckTopOrBottom(g,e,tp,REASON_EFFECT,aux.Stringid(m,3),aux.Stringid(m,4))
	end)
end
```
