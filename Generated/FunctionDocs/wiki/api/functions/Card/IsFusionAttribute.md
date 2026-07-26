# Card.IsFusionAttribute

## Signature

```lua
Card.IsFusionAttribute(Card c, int attribute, [int player]) -> bool
```

## Description

Checks whether c's Attribute while used as Fusion Material contains attribute.
player defaults to the current reason player. The core uses c:GetFusionAttribute(player), so Fusion Material Attribute-changing effects are included.

## Parameters

- `c` `Card`
- `attribute` `int`
- `player` `int` optional - default: current reason player

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3498`
