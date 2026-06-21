# Auxiliary.SynMixHandCheck

## Signature

```lua
Auxiliary.SynMixHandCheck(Group g, int tp, Card syncard) -> bool
```

## Description

Checks whether selected hand Synchro Materials are allowed by a material that grants hand Synchro use, including filter and count limits.

## Parameters

- `g` `Group`
- `tp` `int`
- `syncard` `Card`

## Returns

- `bool` - true if hand Synchro Materials in g are legal.

## Source

- `Utilities/procedure.lua:396`
