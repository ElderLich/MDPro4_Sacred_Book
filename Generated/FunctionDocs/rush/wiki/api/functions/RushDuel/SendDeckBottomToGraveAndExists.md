# RushDuel.SendDeckBottomToGraveAndExists

Alias: `RD.SendDeckBottomToGraveAndExists`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.SendDeckBottomToGraveAndExists(any player, any card_count, any filter, any count, any expect) -> any
```

## Description

Rush Duel helper declared in `RDAction.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
操作: 从卡组下面把卡送去墓地
```

## Parameters

- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `card_count` `any`: Type and behavior are not yet reviewed; see the source.
- `filter` `any`: Type and behavior are not yet reviewed; see the source.
- `count` `any`: Type and behavior are not yet reviewed; see the source.
- `expect` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAction.lua:308`

```lua
function RushDuel.SendDeckBottomToGraveAndExists(player, card_count, filter, count, expect)
    local dg = RushDuel.GetDeckBottomGroup(player, card_count)
    if #dg == 0 then
        return false
    end
    Duel.DisableShuffleCheck()
    return Duel.SendtoGrave(dg, REASON_EFFECT) ~= 0 and RushDuel.IsOperatedGroupExists(filter, count, expect)
end
```
