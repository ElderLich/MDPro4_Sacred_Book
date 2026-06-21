# Auxiliary.FCheckMixRepSelected

## Signature

```lua
Auxiliary.FCheckMixRepSelected(Card c, ... any) -> bool
```

## Description

Selection-recursion helper for mixed-repeat Fusion Materials; it delegates to Auxiliary.FCheckMixRepTemplate using the selected-material condition.

## Parameters

- `c` `Card`
- `...` `any`

## Returns

- `bool` - true if the selected-material recursion can succeed.

## Source

- `Utilities/procedure.lua:1153`
