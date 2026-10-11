# RushDuel.FilterToHandConfirm

Alias: `RD.FilterToHandConfirm`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.FilterToHandConfirm(any card, any player) -> any
```

## Description

Rush Duel helper declared in `RDAction.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
过滤需要给对方确认的卡
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `player` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAction.lua:273`

```lua
function RushDuel.FilterToHandConfirm(card, player)
    return card:IsControler(player) and card:IsPreviousLocation(LOCATION_DECK + LOCATION_GRAVE + LOCATION_REMOVED)
end
```
