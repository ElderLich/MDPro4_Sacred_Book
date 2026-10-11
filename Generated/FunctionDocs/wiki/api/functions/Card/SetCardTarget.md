# Card.SetCardTarget

## Signature

```lua
Card.SetCardTarget(Card c1, Card c2) -> void
```

## Description

Registers c2 as a persistent card target of c1.
This stores a card-target relation used by functions such as Card.GetCardTarget and by related-card disable checks; it is separate from Duel.SelectTarget's Chain target list.

## Parameters

- `c1` `Card`
- `c2` `Card`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3591`
