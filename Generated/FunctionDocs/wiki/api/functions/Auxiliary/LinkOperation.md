# Auxiliary.LinkOperation

## Signature

```lua
Auxiliary.LinkOperation(function|nil f, int minct, int maxct, function|nil gf) -> function
```

## Description

Returns the operation function for Link Summon procedures; it sets the materials, consumes extra-material count limits, and sends the materials to the Graveyard.

## Parameters

- `f` `function|nil`
- `minct` `int`
- `maxct` `int`
- `gf` `function|nil`

## Returns

- `function` - Operation function for a Link Summon procedure.

## Source

- `Utilities/procedure.lua:2263`
