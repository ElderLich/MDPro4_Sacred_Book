# Auxiliary.GCheckAdditional

## Signature

```lua
Auxiliary.GCheckAdditional(Group sg, Card|nil c, Group g) -> bool
```

## Description

Global additional subgroup-check hook used by Group.CheckSubGroup and related selection helpers.
The default implementation returns true. Summon and selection procedures temporarily replace this function to enforce extra group constraints, then restore it.

## Parameters

- `sg` `Group`
- `c` `Card|nil`
- `g` `Group`

## Returns

- `bool`

## Source

- `Utilities/utility.lua:56`
