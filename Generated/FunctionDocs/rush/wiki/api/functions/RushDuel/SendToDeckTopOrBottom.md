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
