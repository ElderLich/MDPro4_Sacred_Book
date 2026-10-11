# Card.IsSpecialSummonableCard

## Signature

```lua
Card.IsSpecialSummonableCard(Card c) -> bool
```

## Description

Checks whether c can be Special Summoned by a proper procedure.
c must have an available Special Summon procedure. This is useful for cards that look for monsters in the GY that already satisfy their revive-limit requirements and still have a legal procedure-style Special Summon path.

## Parameters

- `c` `Card` - Card being checked.

## Returns

- `bool` - True if c has an available proper Special Summon procedure in the current game state.

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3628`
