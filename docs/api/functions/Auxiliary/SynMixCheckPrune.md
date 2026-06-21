# Auxiliary.SynMixCheckPrune

## Signature

```lua
Auxiliary.SynMixCheckPrune(Group sg, Group sg1, Card syncard) -> bool
```

## Description

Pruning check for mixed Synchro searches; returns true once the selected materials' minimum Synchro Level total reaches syncard's Level.

## Parameters

- `sg` `Group`
- `sg1` `Group`
- `syncard` `Card`

## Returns

- `bool` - true if the branch can be pruned by minimum Synchro Level total.

## Source

- `Utilities/procedure.lua:376`
