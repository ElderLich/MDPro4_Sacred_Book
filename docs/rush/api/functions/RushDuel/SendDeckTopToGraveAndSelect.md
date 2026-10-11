# RushDuel.SendDeckTopToGraveAndSelect

Alias: `RD.SendDeckTopToGraveAndSelect`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.SendDeckTopToGraveAndSelect(any player, any count, any hint, any filter, any min, any max, ... any) -> any
```

## Description

Rush Duel helper declared in `RDAction.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
操作: 从卡组上面把卡送去墓地, 并选择被送去墓地的卡片
```

## Parameters

- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `count` `any`: Type and behavior are not yet reviewed; see the source.
- `hint` `any`: Type and behavior are not yet reviewed; see the source.
- `filter` `any`: Type and behavior are not yet reviewed; see the source.
- `min` `any`: Type and behavior are not yet reviewed; see the source.
- `max` `any`: Type and behavior are not yet reviewed; see the source.
- `...` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAction.lua:485`

```lua
function RushDuel.SendDeckTopToGraveAndSelect(player, count, hint, filter, min, max, ...)
    if Duel.DiscardDeck(player, count, REASON_EFFECT) ~= 0 then
        local g = Duel.GetOperatedGroup()
        local mg = g:Filter(filter, nil, ...)
        if #mg >= min then
            local sg = RushDuel.Select(hint, player, mg, nil, false, min, max)
            if sg and #sg > 0 then
                g:Sub(sg)
                return sg, g
            end
        end
        return Group.CreateGroup(), g
    end
    return Group.CreateGroup(), Group.CreateGroup()
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **2** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.SendDeckTopToGraveAndSelect) with `RushDuel.SendDeckTopToGraveAndSelect`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| The Player Returning Alive | `120305036` | [Rush/Scripts/c120305036.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120305036.lua) | 1 |
| Pliage's Clustering Stars | `120305024` | [Rush/Scripts/c120305024.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120305024.lua) | 1 |

## Script Examples

### The Player Returning Alive (`120305036`)

Source: [Rush/Scripts/c120305036.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120305036.lua)

```lua
end
function cm.activate(e,tp,eg,ep,ev,re,r,rp)
	local sg=RD.SendDeckTopToGraveAndSelect(tp,3,HINTMSG_ATOHAND,aux.NecroValleyFilter(cm.thfilter1),1,1)
	if sg:GetCount()>0 then
		Duel.BreakEffect()
```

### Pliage's Clustering Stars (`120305024`)

Source: [Rush/Scripts/c120305024.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120305024.lua)

```lua
end
function cm.activate(e,tp,eg,ep,ev,re,r,rp)
	local sg=RD.SendDeckTopToGraveAndSelect(tp,3,HINTMSG_ATOHAND,aux.NecroValleyFilter(cm.thfilter),2,2)
	if sg:GetCount()>0 then
		Duel.BreakEffect()
```
