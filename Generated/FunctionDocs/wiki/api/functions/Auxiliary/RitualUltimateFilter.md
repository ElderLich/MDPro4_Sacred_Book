# Auxiliary.RitualUltimateFilter

## Signature

```lua
Auxiliary.RitualUltimateFilter(Card c, function|nil filter, Effect e, int tp, Group m1, Group|nil m2, function level_function, string greater_or_equal, bool|nil chk) -> bool
```

## Description

Checks whether c is a valid Ritual Monster that can be Ritual Summoned with the available material groups and the selected Equal or Greater level rule.

## Parameters

- `c` `Card`
- `filter` `function|nil`
- `e` `Effect`
- `tp` `int`
- `m1` `Group`
- `m2` `Group|nil`
- `level_function` `function`
- `greater_or_equal` `string`
- `chk` `bool|nil`

## Returns

- `bool` - true if c can be Ritual Summoned.

## Source

- `Utilities/procedure.lua:1825`
