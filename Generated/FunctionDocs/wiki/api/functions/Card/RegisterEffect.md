# Card.RegisterEffect

## Signature

```lua
Card.RegisterEffect(Card c, Effect e, [bool forced]) -> int|nil
```

## Description

Registers effect e to card c and returns the generated effect field ID.
Registration also makes c the effect handler. If the card is unaffected by the current reason effect, registration can fail unless forced is true.

## Parameters

- `c` `Card`
- `e` `Effect`
- `forced` `bool` optional

## Returns

- `int|nil`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3603`
