# Auxiliary.ndcon

## Signature

```lua
Auxiliary.ndcon(int tp, Effect re) -> bool
```

## Description

Condition helper for effects that negate an activation and return the activating card to the Deck. It accepts Spell/Trap activations, unrelated cards, or related cards that can be returned to the Deck.

## Parameters

- `tp` `int`
- `re` `Effect`

## Returns

- `bool` - true if the activation can be negated and the card can be returned to the Deck if needed.

## Source

- `Utilities/utility.lua:1482`
