# Auxiliary.SelectSameCount

## Signature

```lua
Auxiliary.SelectSameCount(int tp, Group g1, Group g2, [int min], [int max], [Card|Group|nil except]) -> Group|nil
```

## Description

Lets tp build a selection that contains the same number of cards from g1 and g2.
except is removed from both groups before selection. The result can be nil if min is greater than the computed max.

## Parameters

- `tp` `int`
- `g1` `Group`
- `g2` `Group`
- `min` `int` optional - default: 1
- `max` `int` optional - default: min(#g1, #g2, 127)
- `except` `Card|Group|nil` optional

## Returns

- `Group|nil`

## Source

- `Utilities/utility.lua:1424`
