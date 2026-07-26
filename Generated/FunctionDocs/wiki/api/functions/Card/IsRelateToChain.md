# Card.IsRelateToChain

## Signature

```lua
Card.IsRelateToChain(Card c, [int chainc]) -> bool
```

## Description

Checks whether c is still related to chainc.
The activating card and cards selected as targets with Duel.SetTargetCard or Duel.SelectTarget automatically become related to that Chain. The relation is lost when the card leaves the expected place.

## Parameters

- `c` `Card`
- `chainc` `int` optional - default: 0

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3566`
