# Card.GetFieldID

## Signature

```lua
Card.GetFieldID(Card c) -> int
```

## Description

Returns c's current field ID, the core timestamp assigned when c moved to its current place.
Smaller values are older. This differs from Card.GetRealFieldID, which tracks the real field ID used by battle-state checks.

## Parameters

- `c` `Card`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3477`
