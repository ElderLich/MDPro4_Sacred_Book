# Auxiliary.covcheck

## Signature

```lua
Auxiliary.covcheck(Card c) -> bool|nil
```

## Description

Returns true for a printed Monster Card, or for a non-monster whose recorded Special Summon reason effect belongs to itself. Used when deciding whether an original-value calculation remains meaningful after a self-summoned Trap leaves the field.

## Parameters

- `c` `Card`

## Returns

- `bool|nil` - May return nil when there is no recorded Special Summon reason effect; use as a predicate.

## Source

- `Utilities/utility.lua:2070`
