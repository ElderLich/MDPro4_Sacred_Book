# Auxiliary.NegateAnyFilter

## Signature

```lua
Auxiliary.NegateAnyFilter(Card c) -> bool
```

## Description

Filter for effects that negate a face-up card. Trap Monsters only need to be face-up, Spell/Trap Cards must be face-up and not already disabled, and monsters use Auxiliary.NegateMonsterFilter.

## Parameters

- `c` `Card`

## Returns

- `bool` - true if c is a valid card to have its effects negated.

## Source

- `Utilities/utility.lua:755`
