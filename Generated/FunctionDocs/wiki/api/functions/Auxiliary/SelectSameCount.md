# Auxiliary.SelectSameCount

## Signature

```lua
Auxiliary.SelectSameCount(int tp, Group g1, Group g2, [int min], [int max], [Card|Group except]) -> Group
```

## Description

Select the same number of cards from each group.

## Parameters

- `tp` `int`
- `g1` `Group`
- `g2` `Group`
- `min` `int` optional - Cards to select from each group, minimum
- `max` `int` optional - Cards to select from each group, maximum
- `except` `Card|Group` optional

## Returns

- `Group`

## Source

- `Utilities/utility.lua:1421`
