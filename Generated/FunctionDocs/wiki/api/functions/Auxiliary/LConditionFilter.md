# Auxiliary.LConditionFilter

## Signature

```lua
Auxiliary.LConditionFilter(Card c, function|nil f, Card lc, Effect e) -> bool
```

## Description

Regular Link Material filter. The card must be visible or selectable by e, usable as Link Material for lc, and satisfy f when provided.

## Parameters

- `c` `Card`
- `f` `function|nil`
- `lc` `Card`
- `e` `Effect`

## Returns

- `bool` - true if c is regular Link Material.

## Source

- `Utilities/procedure.lua:2143`
