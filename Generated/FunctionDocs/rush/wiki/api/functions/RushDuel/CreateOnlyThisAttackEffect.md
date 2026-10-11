# RushDuel.CreateOnlyThisAttackEffect

Alias: `RD.CreateOnlyThisAttackEffect`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CreateOnlyThisAttackEffect(any e, any code, any player, any s_range, any o_range, any reset) -> any
```

## Description

Rush Duel helper declared in `RDLimit.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
创建限制: 只能用这张卡进行攻击
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `code` `any`: Type and behavior are not yet reviewed; see the source.
- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `s_range` `any`: Type and behavior are not yet reviewed; see the source.
- `o_range` `any`: Type and behavior are not yet reviewed; see the source.
- `reset` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDLimit.lua:248`

```lua
function RushDuel.CreateOnlyThisAttackEffect(e, code, player, s_range, o_range, reset)
    RushDuel.CreateOnlyThatAttackEffect(e, e:GetHandler(), code, player, s_range, o_range, reset)
end
```
