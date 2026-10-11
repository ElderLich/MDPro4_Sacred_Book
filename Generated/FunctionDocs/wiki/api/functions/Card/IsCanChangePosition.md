# Card.IsCanChangePosition

## Signature

```lua
Card.IsCanChangePosition(Card c) -> bool
```

## Description

Checks the core's effect-specific position-change capability for c.
In this MDPro3/YGOPro core, that helper returns false for Link Monsters and true for other cards; it does not perform the broader manual battle-position-change checks.

## Parameters

- `c` `Card`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3688`
