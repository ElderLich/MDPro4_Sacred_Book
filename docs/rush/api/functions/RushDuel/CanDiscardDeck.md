# RushDuel.CanDiscardDeck

Alias: `RD.CanDiscardDeck`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CanDiscardDeck(any desc, any player, any min, any max, any break_effect, any target_player) -> any
```

## Description

Rush Duel helper declared in `RDAction.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
可选操作: 盲堆
```

## Parameters

- `desc` `any`: Type and behavior are not yet reviewed; see the source.
- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `min` `any`: Type and behavior are not yet reviewed; see the source.
- `max` `any`: Type and behavior are not yet reviewed; see the source.
- `break_effect` `any`: Type and behavior are not yet reviewed; see the source.
- `target_player` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAction.lua:580`

```lua
function RushDuel.CanDiscardDeck(desc, player, min, max, break_effect, target_player)
    target_player = target_player or player
    if Duel.IsPlayerCanDiscardDeck(target_player, min) and Duel.SelectYesNo(player, desc) then
        if break_effect then
            Duel.BreakEffect()
        end
        max = max or min
        local ct = Duel.GetFieldGroupCount(target_player, LOCATION_DECK, 0)
        local ops = {}
        for i = min, math.min(max, ct) do
            if Duel.IsPlayerCanDiscardDeck(target_player, i) then
                table.insert(ops, i)
            end
        end
        local count = 0
        if #ops == 1 then
            count = table.remove(ops)
        elseif #ops > 1 then
            Duel.Hint(HINT_SELECTMSG, player, HINTMSG_OPERATE_COUNT)
            count = Duel.AnnounceNumber(player, table.unpack(ops))
        end
        return Duel.DiscardDeck(target_player, count, REASON_EFFECT)
    end
    return 0
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **9** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CanDiscardDeck) with `RushDuel.CanDiscardDeck`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Sea Star Trooper | `120199022` | [Rush/Scripts/c120199022.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120199022.lua) | 1 |
| Psychicomposition | `120246069` | [Rush/Scripts/c120246069.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120246069.lua) | 1 |
| Cocoon King Beetle | `120277039` | [Rush/Scripts/c120277039.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120277039.lua) | 1 |
| Flash Voltchick | `120246005` | [Rush/Scripts/c120246005.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120246005.lua) | 1 |
| Baron Wight | `120271057` | [Rush/Scripts/c120271057.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120271057.lua) | 1 |
| Dragons Boost Fusion | `120244049` | [Rush/Scripts/c120244049.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120244049.lua) | 1 |
| Endless Partner | `120300050` | [Rush/Scripts/c120300050.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300050.lua) | 1 |
| Psychic Burial | `120160004` | [Rush/Scripts/c120160004.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120160004.lua) | 1 |
| Root of Despair | `120301033` | [Rush/Scripts/c120301033.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120301033.lua) | 1 |

## Script Examples

### Sea Star Trooper (`120199022`)

Source: [Rush/Scripts/c120199022.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120199022.lua)

```lua
	RD.SelectAndDoAction(HINTMSG_TODECK,aux.NecroValleyFilter(cm.tdfilter),tp,0,LOCATION_GRAVE,1,1,nil,function(g)
		if RD.SendToDeckAndExists(g,e,tp,REASON_EFFECT) and Duel.IsExistingMatchingCard(cm.exfilter,tp,LOCATION_ONFIELD,0,1,nil) then
			RD.CanDiscardDeck(aux.Stringid(m,1),tp,2)
		end
	end)
```

### Psychicomposition (`120246069`)

Source: [Rush/Scripts/c120246069.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120246069.lua)

```lua
	RD.SelectAndDoAction(HINTMSG_ATOHAND,aux.NecroValleyFilter(cm.filter),tp,LOCATION_GRAVE,0,1,1,nil,function(g)
		if RD.SendToHandAndExists(g,e,tp,REASON_EFFECT,cm.exfilter,1,nil) then
			RD.CanDiscardDeck(aux.Stringid(m,1),tp,3)
		end
	end)
```

### Cocoon King Beetle (`120277039`)

Source: [Rush/Scripts/c120277039.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120277039.lua)

```lua
function cm.operation(e,tp,eg,ep,ev,re,r,rp)
	if RD.Draw()~=0 and Duel.IsExistingMatchingCard(cm.exfilter,tp,LOCATION_GRAVE,0,2,nil) then
		RD.CanDiscardDeck(aux.Stringid(m,1),tp,3,3,true)
	end
end
```
