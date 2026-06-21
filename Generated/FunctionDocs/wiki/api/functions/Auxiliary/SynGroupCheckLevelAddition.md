# Auxiliary.SynGroupCheckLevelAddition

## Signature

```lua
Auxiliary.SynGroupCheckLevelAddition(Card syncard) -> function
```

## Description

Returns a group check for Synchro material selection that keeps the sum of the selected materials' minimum Synchro Levels at or below syncard's Level.

## Parameters

- `syncard` `Card`

## Returns

- `function` - Group check for Synchro material Level pruning.

## Source

- `Utilities/procedure.lua:463`
