# RushDuel.SendDeckTopToBottom

Alias: `RD.SendDeckTopToBottom`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.SendDeckTopToBottom(any player, any count) -> any
```

## Description

Rush Duel helper declared in `RDFunction.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
将玩家卡组最上面的N张卡移到卡组最下面
```

## Parameters

- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `count` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDFunction.lua:139`

```lua
function RushDuel.SendDeckTopToBottom(player, count)
    for i = 1, count do
        Duel.MoveSequence(Duel.GetDecktopGroup(player, 1):GetFirst(), 1)
    end
end
```
