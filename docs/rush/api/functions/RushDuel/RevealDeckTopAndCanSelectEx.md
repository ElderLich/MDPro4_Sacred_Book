# RushDuel.RevealDeckTopAndCanSelectEx

Alias: `RD.RevealDeckTopAndCanSelectEx`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.RevealDeckTopAndCanSelectEx(any player, any count, any exg, any desc, any hint, any filter, any min, any max, ... any) -> any
```

## Description

Rush Duel helper declared in `RDAction.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
操作: 翻开卡组并可以选择卡(包含额外的卡片组)
```

## Parameters

- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `count` `any`: Type and behavior are not yet reviewed; see the source.
- `exg` `any`: Type and behavior are not yet reviewed; see the source.
- `desc` `any`: Type and behavior are not yet reviewed; see the source.
- `hint` `any`: Type and behavior are not yet reviewed; see the source.
- `filter` `any`: Type and behavior are not yet reviewed; see the source.
- `min` `any`: Type and behavior are not yet reviewed; see the source.
- `max` `any`: Type and behavior are not yet reviewed; see the source.
- `...` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAction.lua:470`

```lua
function RushDuel.RevealDeckTopAndCanSelectEx(player, count, exg, desc, hint, filter, min, max, ...)
    Duel.ConfirmDecktop(player, count)
    local g = Duel.GetDecktopGroup(player, count)
    local mg = g:Filter(filter, nil, ...)
    mg:Merge(exg)
    if #mg >= min then
        local sg = RushDuel.CanSelect(desc, hint, player, mg, nil, min, max)
        if sg and #sg > 0 then
            g:Sub(sg)
            return sg, g
        end
    end
    return Group.CreateGroup(), g
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **2** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.RevealDeckTopAndCanSelectEx) with `RushDuel.RevealDeckTopAndCanSelectEx`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| One for One | `120307015` | [Rush/Scripts/c120307015.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120307015.lua) | 1 |
| Chaos Ceremonial Object | `120293040` | [Rush/Scripts/c120293040.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120293040.lua) | 1 |

## Script Examples

### One for One (`120307015`)

Source: [Rush/Scripts/c120307015.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120307015.lua)

```lua
	if Duel.GetFieldGroupCount(tp,LOCATION_DECK,0)<4 then return end
	local mg=Duel.GetMatchingGroup(aux.NecroValleyFilter(cm.spfilter),tp,LOCATION_GRAVE,0,nil,e,tp)
	local sg=RD.RevealDeckTopAndCanSelectEx(tp,4,mg,aux.Stringid(m,1),HINTMSG_SPSUMMON,cm.spfilter,1,1,e,tp)
	if sg:GetCount()>0 then
		Duel.SpecialSummon(sg,0,tp,tp,false,false,POS_FACEUP)
```

### Chaos Ceremonial Object (`120293040`)

Source: [Rush/Scripts/c120293040.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120293040.lua)

```lua
	if Duel.GetFieldGroupCount(tp,LOCATION_DECK,0)<3 then return end
	local mg=Duel.GetMatchingGroup(aux.NecroValleyFilter(cm.filter),tp,LOCATION_GRAVE,0,nil)
	local sg,g=RD.RevealDeckTopAndCanSelectEx(tp,3,mg,aux.Stringid(m,1),HINTMSG_ATOHAND,cm.filter,1,1)
	if sg:GetCount()>0 then
		Duel.DisableShuffleCheck()
```
