# Card.GetFieldID

## Signature

```lua
Card.GetFieldID(Card c) -> int
```

## Description

Returns c's current field ID, the core timestamp assigned when c moved to its current place.
Smaller values are older. The core refreshes this value when the card gains a new field identity, such as entering the field or changing controller. This differs from Card.GetRealFieldID, which tracks the real field ID used by battle-state checks.

## Parameters

- `c` `Card` - Card whose current field ID is returned.

## Returns

- `int` - Current field ID assigned by the core for c's current field identity.

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3480`
