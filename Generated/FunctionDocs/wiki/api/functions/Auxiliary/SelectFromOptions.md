# Auxiliary.SelectFromOptions

## Signature

```lua
Auxiliary.SelectFromOptions(int tp, ... table) -> any|nil
```

## Description

Filters option tables by their condition, calls Duel.SelectOption with the available option labels, and returns the selected table's custom value or original index.
Each option is {condition, option\[, value\]}. If no condition is true, the helper returns nil. Its default index return is 1-based, unlike Duel.SelectOption's 0-based return.

## Parameters

- `tp` `int`
- `...` `table`

## Returns

- `any|nil` - Selected option value or 1-based option index; nil if no option is available.

## Source

- `Utilities/utility.lua:152`
