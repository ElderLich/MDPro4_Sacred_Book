# Card.IsRelateToChain

## Signature

```lua
Card.IsRelateToChain(Card c, [int chainc]) -> bool
```

## Description

Check if c is linked to chained chainc
Note: Each launch into the effect of chain, the effect of launching the card, and the effect of the specified object
(With Duel.SetTargetCard or Duel.SelectTarget specified, including the take and not take objects)
Will automatically establish contact with that effect, once the departure, contact will be reset

## Parameters

- `c` `Card`
- `chainc` `int` optional - default: 0

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3563`
