# GetID

## Signature

```lua
GetID() -> table,int,int
```

## Description

Returns the current script's table, card code, and string offset. The offset is 1 for regular card IDs and 100 for large custom IDs.

## Returns

- `table` - The current script table.
- `int` - The current card code.
- `int` - String ID offset, 1 or 100.

## Source

- `Utilities/utility.lua:8`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
