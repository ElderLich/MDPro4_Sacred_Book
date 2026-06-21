# Card.IsRelateToEffect

## Signature

```lua
Card.IsRelateToEffect(Card c, Effect e) -> bool
```

## Description

Checks whether c is still related to effect e.
When an effect enters the Chain, its handler and cards selected with Duel.SetTargetCard or Duel.SelectTarget are related to that effect. That relation is normally lost once the card leaves its expected place.

## Parameters

- `c` `Card`
- `e` `Effect`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3562`
