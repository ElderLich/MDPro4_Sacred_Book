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
