# Auxiliary.NegateEffectMonsterFilter

## Signature

```lua
Auxiliary.NegateEffectMonsterFilter(Card c) -> bool
```

## Description

Filter for effects that negate an Effect Monster, such as Effect Veiler: c must be face-up, not already disabled, and currently an Effect Monster.

## Parameters

- `c` `Card`

## Returns

- `bool` - true if c is a valid Effect Monster to have its effects negated.

## Source

- `Utilities/utility.lua:748`
