# Auxiliary.ExceptThisCard

## Signature

```lua
Auxiliary.ExceptThisCard(Effect e) -> Card|nil
```

## Description

Returns e's handler while that card is still related to the current Chain; otherwise returns nil.

## Parameters

- `e` `Effect`

## Returns

- `Card|nil` - e's handler if it is still related to the current Chain; otherwise nil.

## Source

- `Utilities/utility.lua:1179`
