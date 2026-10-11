# Auxiliary.UrsarcticExCostFilter

## Signature

```lua
Auxiliary.UrsarcticExCostFilter(Card c, int tp) -> bool
```

## Description

Replacement-cost filter for the shared Ursarctic Special Summon effect. It accepts cards in the Graveyard that can be banished as cost through effect code 16471775 or 89264428.

## Parameters

- `c` `Card`
- `tp` `int`

## Returns

- `bool` - true if c can be banished as an Ursarctic replacement cost.

## Source

- `Utilities/utility.lua:961`
