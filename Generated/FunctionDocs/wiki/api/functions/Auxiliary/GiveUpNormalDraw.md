# Auxiliary.GiveUpNormalDraw

## Signature

```lua
Auxiliary.GiveUpNormalDraw(Effect e, int tp, [int property]) -> void
```

## Description

Makes tp give up the normal draw for the current Draw Phase by setting EFFECT_DRAW_COUNT to 0 and registering FLAG_ID_NO_NORMAL_DRAW.

## Parameters

- `e` `Effect`
- `tp` `int`
- `property` `int` optional

## Source

- `Utilities/utility.lua:1867`
