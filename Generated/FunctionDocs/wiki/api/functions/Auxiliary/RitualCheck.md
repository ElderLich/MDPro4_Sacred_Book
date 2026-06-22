# Auxiliary.RitualCheck

## Signature

```lua
Auxiliary.RitualCheck(Group g, int tp, Card c, int lv, string greater_or_equal) -> bool
```

## Description

Ritual material group predicate that checks zone availability, the requested Greater/Equal level rule, custom mat_group_check, and RCheckAdditional.

## Parameters

- `g` `Group`
- `tp` `int`
- `c` `Card`
- `lv` `int`
- `greater_or_equal` `string`

## Returns

- `bool`

## Source

- `Utilities/procedure.lua:1786`
