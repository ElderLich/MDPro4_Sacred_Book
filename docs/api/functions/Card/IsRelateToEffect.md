# Card.IsRelateToEffect

## Signature

```lua
Card.IsRelateToEffect(Card c, Effect e) -> bool
```

## Description

Check whether c is associated with effect e
Note: Each launch into the effect of chain, the effect of launching the card, and the effect of the specified object
(With Duel.SetTargetCard or Duel.SelectTarget specified, including the take and not take objects)

## Parameters

- `c` `Card`
- `e` `Effect`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3562`
