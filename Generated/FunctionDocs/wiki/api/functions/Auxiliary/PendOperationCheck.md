# Auxiliary.PendOperationCheck

## Signature

```lua
Auxiliary.PendOperationCheck(int ft1, int ft2, int ft) -> function
```

## Description

Returns a group check that enforces the hand, Extra Deck, and total Monster Zone limits for a Pendulum Summon selection.
The returned function counts selected Extra Deck cards separately from non-Extra Deck cards before accepting the subgroup.

## Parameters

- `ft1` `int` - Maximum selected monsters from non-Extra Deck locations, usually the hand.
- `ft2` `int` - Maximum selected monsters from the face-up Extra Deck.
- `ft` `int` - Maximum total selected monsters.

## Returns

- `function` - Group check for Pendulum Summon zone limits.

## Source

- `Utilities/procedure.lua:2026`
