# Auxiliary.NegateMonsterFilter

## Signature

```lua
Auxiliary.NegateMonsterFilter(Card c) -> bool
```

## Description

Filter for effects that negate a face-up monster, such as Infinite Impermanence: c must be face-up, not already disabled, and be or originally be an Effect Monster.

## Parameters

- `c` `Card`

## Returns

- `bool` - true if c is a valid face-up monster to have its effects negated.

## Source

- `Utilities/utility.lua:747`
