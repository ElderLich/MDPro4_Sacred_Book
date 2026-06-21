# Auxiliary.AddThisCardInGraveAlreadyCheck

## Signature

```lua
Auxiliary.AddThisCardInGraveAlreadyCheck(Card c) -> void
```

## Description

Registers a continuous effect on c that records the effect that sent c to the Graveyard.
This lets later Graveyard-condition checks distinguish a card that was already in the Graveyard from one sent there by the currently resolving effect.

## Parameters

- `c` `Card`

## Source

- `Utilities/utility.lua:1548`
