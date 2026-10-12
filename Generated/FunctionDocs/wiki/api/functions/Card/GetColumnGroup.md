# Card.GetColumnGroup

## Signature

```lua
Card.GetColumnGroup(Card c) -> Group
```

## Description

Returns a Group containing cards in the same column as c.
This MDPro4/YGOPro binding only takes c. It uses c's current on-field column, including related Monster Zones, Spell & Trap Zones, and Extra Monster Zone column relationships; if c is not on the field, the returned Group is empty.

## Parameters

- `c` `Card`

## Returns

- `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3478`
