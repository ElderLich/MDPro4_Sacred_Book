# Auxiliary.mzctcheckrel

## Signature

```lua
Auxiliary.mzctcheckrel(Group g, int tp, [int reason]) -> bool
```

## Description

Checks whether releasing group g by reason leaves a Monster Zone and g is a valid release group for tp.

## Parameters

- `g` `Group`
- `tp` `int`
- `reason` `int` optional - default: REASON_COST

## Returns

- `bool`

## Source

- `Utilities/utility.lua:1171`
