# Auxiliary.PlaceCardsOnDeckBottom

## Signature

```lua
Auxiliary.PlaceCardsOnDeckBottom(int p, Group g, [int reason]) -> int
```

## Description

Sends g to the top of the Deck by reason, lets p order cards that reached either Deck, moves them to the bottom, and returns the number of operated cards.

## Parameters

- `p` `int`
- `g` `Group`
- `reason` `int` optional - Defaults to REASON_EFFECT.

## Returns

- `int` - The number of operated cards.

## Source

- `Utilities/utility.lua:1617`
