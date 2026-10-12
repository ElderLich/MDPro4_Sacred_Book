# RushDuel.RevealDeckTopAndSelect

Alias: `RD.RevealDeckTopAndSelect`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.RevealDeckTopAndSelect(any player, any count, any hint, any filter, any min, any max, ... any) -> any
```

## Description

Rush Duel helper declared in `RDAction.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
操作: 翻开卡组并选择卡
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

`Rush/Utilities/RDAction.lua:427`

```lua
function RushDuel.RevealDeckTopAndSelect(player, count, hint, filter, min, max, ...)
    Duel.ConfirmDecktop(player, count)
    local g = Duel.GetDecktopGroup(player, count)
    local mg = g:Filter(filter, nil, ...)
    if #mg >= min then
        local sg = RushDuel.Select(hint, player, mg, nil, false, min, max)
        if sg and #sg > 0 then
            g:Sub(sg)
            return sg, g
        end
    else
        return Group.CreateGroup(), g
    end
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **6** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.RevealDeckTopAndSelect) with `RushDuel.RevealDeckTopAndSelect`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Skysavior Watch](/examples/rush-cards/120235053) | `120235053` | [Rush/Scripts/c120235053.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120235053.lua) | 1 |
| [Miracle Pick](/examples/rush-cards/120253052) | `120253052` | [Rush/Scripts/c120253052.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120253052.lua) | 1 |
| [Pot of Duality](/examples/rush-cards/120271002) | `120271002` | [Rush/Scripts/c120271002.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120271002.lua) | 1 |
| [Crystal Seer](/examples/rush-cards/120109067) | `120109067` | [Rush/Scripts/c120109067.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120109067.lua) | 1 |
| Jointech Digup | `120249047` | [Rush/Scripts/c120249047.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120249047.lua) | 1 |
| Specter of Heaven's End | `120217092` | [Rush/Scripts/c120217092.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120217092.lua) | 1 |

## Script Examples

### Skysavior Watch (`120235053`)

Source: [Rush/Scripts/c120235053.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120235053.lua)

```lua
	local p=Duel.GetChainInfo(0,CHAININFO_TARGET_PLAYER)
	if Duel.GetFieldGroupCount(p,LOCATION_DECK,0)<5 then return end
	local sg,g=RD.RevealDeckTopAndSelect(p,5,HINTMSG_ATOHAND,aux.TRUE,1,1)
	local tc=sg:GetFirst()
	if tc then
```

### Miracle Pick (`120253052`)

Source: [Rush/Scripts/c120253052.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120253052.lua)

```lua
	local p=Duel.GetChainInfo(0,CHAININFO_TARGET_PLAYER)
	if Duel.GetFieldGroupCount(p,LOCATION_DECK,0)<3 then return end
	local sg,g=RD.RevealDeckTopAndSelect(p,3,HINTMSG_ATOHAND,aux.TRUE,1,1)
	local tc=sg:GetFirst()
	if tc then
```

### Pot of Duality (`120271002`)

Source: [Rush/Scripts/c120271002.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120271002.lua)

```lua
	local p=Duel.GetChainInfo(0,CHAININFO_TARGET_PLAYER)
	if Duel.GetFieldGroupCount(p,LOCATION_DECK,0)<3 then return end
	local sg,g=RD.RevealDeckTopAndSelect(p,3,HINTMSG_ATOHAND,aux.TRUE,1,1)
	local tc=sg:GetFirst()
	if tc then
```
