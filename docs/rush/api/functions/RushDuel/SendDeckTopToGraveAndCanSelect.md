# RushDuel.SendDeckTopToGraveAndCanSelect

Alias: `RD.SendDeckTopToGraveAndCanSelect`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.SendDeckTopToGraveAndCanSelect(any player, any count, any desc, any hint, any filter, any min, any max, ... any) -> any
```

## Description

Rush Duel helper declared in `RDAction.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
操作: 从卡组上面把卡送去墓地, 并可以选择被送去墓地的卡片
```

## Parameters

- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `count` `any`: Type and behavior are not yet reviewed; see the source.
- `desc` `any`: Type and behavior are not yet reviewed; see the source.
- `hint` `any`: Type and behavior are not yet reviewed; see the source.
- `filter` `any`: Type and behavior are not yet reviewed; see the source.
- `min` `any`: Type and behavior are not yet reviewed; see the source.
- `max` `any`: Type and behavior are not yet reviewed; see the source.
- `...` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAction.lua:501`

```lua
function RushDuel.SendDeckTopToGraveAndCanSelect(player, count, desc, hint, filter, min, max, ...)
    if Duel.DiscardDeck(player, count, REASON_EFFECT) ~= 0 then
        local g = Duel.GetOperatedGroup()
        local mg = g:Filter(filter, nil, ...)
        if #mg >= min then
            local sg = RushDuel.CanSelect(desc, hint, player, mg, nil, min, max)
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

- Detected in **18** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.SendDeckTopToGraveAndCanSelect) with `RushDuel.SendDeckTopToGraveAndCanSelect`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Ember the Ultra Assistant](/examples/rush-cards/120283035) | `120283035` | [Rush/Scripts/c120283035.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120283035.lua) | 1 |
| Lua, the Fairy of Skysavior | `120235021` | [Rush/Scripts/c120235021.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120235021.lua) | 1 |
| Sparkhearts Anesh | `120298022` | [Rush/Scripts/c120298022.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120298022.lua) | 1 |
| Ritche of Hope | `120287072` | [Rush/Scripts/c120287072.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120287072.lua) | 1 |
| Chemipet Chirp | `120261009` | [Rush/Scripts/c120261009.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120261009.lua) | 1 |
| Celeb Rose Wiz | `120253008` | [Rush/Scripts/c120253008.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120253008.lua) | 1 |
| Space Call | `120260018` | [Rush/Scripts/c120260018.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120260018.lua) | 1 |
| Future Aeromancer | `120231054` | [Rush/Scripts/c120231054.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120231054.lua) | 1 |
| Nimble Lemming | `120238020` | [Rush/Scripts/c120238020.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120238020.lua) | 1 |
| Dead Heat the Mad Fiend of Despair | `120301029` | [Rush/Scripts/c120301029.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120301029.lua) | 1 |
| Police Hound of the Blaze Fiends | `120287035` | [Rush/Scripts/c120287035.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120287035.lua) | 1 |
| The Journeying Three Magi | `120304058` | [Rush/Scripts/c120304058.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304058.lua) | 1 |
| Dimension Jump | `120309032` | [Rush/Scripts/c120309032.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120309032.lua) | 1 |
| Balloon Butier | `120277037` | [Rush/Scripts/c120277037.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120277037.lua) | 1 |
| Chaos Femtron | `120260012` | [Rush/Scripts/c120260012.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120260012.lua) | 1 |
| Carrier Manta Ray | `120253019` | [Rush/Scripts/c120253019.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120253019.lua) | 1 |
| Resolve | `120246054` | [Rush/Scripts/c120246054.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120246054.lua) | 1 |
| Delirium Honeyed Words | `120274064` | [Rush/Scripts/c120274064.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120274064.lua) | 1 |

## Script Examples

### Ember the Ultra Assistant (`120283035`)

Source: [Rush/Scripts/c120283035.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120283035.lua)

```lua
function cm.operation(e,tp,eg,ep,ev,re,r,rp)
	if RD.Draw()~=0 and Duel.IsExistingMatchingCard(cm.exfilter,tp,LOCATION_GRAVE,0,1,nil) then
		local sg,og=RD.SendDeckTopToGraveAndCanSelect(tp,2,aux.Stringid(m,1),HINTMSG_ATOHAND,aux.NecroValleyFilter(cm.thfilter),1,1)
		if sg:GetCount()>0 then
			Duel.BreakEffect()
```

### Lua, the Fairy of Skysavior (`120235021`)

Source: [Rush/Scripts/c120235021.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120235021.lua)

```lua
		if not Duel.IsPlayerCanDiscardDeck(tp,1) then return end
		Duel.BreakEffect()
		local sg,og=RD.SendDeckTopToGraveAndCanSelect(tp,3,aux.Stringid(m,1),HINTMSG_ATOHAND,aux.NecroValleyFilter(cm.thfilter),1,1)
		if sg:GetCount()>0 then
			Duel.BreakEffect()
```

### Sparkhearts Anesh (`120298022`)

Source: [Rush/Scripts/c120298022.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120298022.lua)

```lua
end
function cm.operation(e,tp,eg,ep,ev,re,r,rp)
	local sg,og=RD.SendDeckTopToGraveAndCanSelect(tp,3,aux.Stringid(m,2),HINTMSG_ATOHAND,aux.NecroValleyFilter(cm.thfilter),1,1)
	if sg:GetCount()>0 then
		Duel.BreakEffect()
```
