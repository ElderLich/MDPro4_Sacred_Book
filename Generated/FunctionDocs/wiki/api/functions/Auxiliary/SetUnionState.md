# Auxiliary.SetUnionState

## Signature

```lua
Auxiliary.SetUnionState(Card c) -> void
```

## Description

Applies the equipped Union state to c after it becomes equipped.
If c has an EFFECT_UNION_LIMIT effect, this registers the matching EFFECT_EQUIP_LIMIT and EFFECT_UNION_STATUS reset effects. Old Union cards also receive EFFECT_OLDUNION_STATUS.

## Parameters

- `c` `Card`

## Source

- `Utilities/utility.lua:312`
