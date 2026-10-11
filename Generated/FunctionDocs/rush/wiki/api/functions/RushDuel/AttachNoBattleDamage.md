# RushDuel.AttachNoBattleDamage

Alias: `RD.AttachNoBattleDamage`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AttachNoBattleDamage(any e, any card, any desc, any reset, any forced) -> any
```

## Description

Rush Duel helper declared in `RDAttach.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
赋予: 战斗不会让双方受到伤害
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `desc` `any`: Type and behavior are not yet reviewed; see the source.
- `reset` `any`: Type and behavior are not yet reviewed; see the source.
- `forced` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAttach.lua:104`

```lua
function RushDuel.AttachNoBattleDamage(e, card, desc, reset, forced)
    local e1 =  RushDuel.CreateSingleEffect(e, desc, card, EFFECT_AVOID_BATTLE_DAMAGE, 1, reset, forced)
    local e2 =  RushDuel.CreateSingleEffect(e, desc, card, EFFECT_NO_BATTLE_DAMAGE, 1, reset, forced)
    return e1, e2
end
```
