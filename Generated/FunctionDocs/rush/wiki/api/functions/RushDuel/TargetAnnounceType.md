# RushDuel.TargetAnnounceType

Alias: `RD.TargetAnnounceType`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.TargetAnnounceType(any player) -> any
```

## Description

Rush Duel helper declared in `RDTarget.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
对玩家效果: 宣言卡片的种类（怪兽·魔法·陷阱）
```

## Parameters

- `player` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDTarget.lua:29`

```lua
function RushDuel.TargetAnnounceType(player)
    Duel.SetTargetParam(Duel.AnnounceType(player))
end
```
