# Card.IsLinkAttribute

## Signature

```lua
Card.IsLinkAttribute(Card c, int attribute, [int player]) -> bool
```

## Description

Checks whether c's Attribute while used as Link Material contains attribute.
player defaults to the current reason player. The core uses c:GetLinkAttribute(player), so Link Material Attribute-changing effects are included.

## Parameters

- `c` `Card`
- `attribute` `int`
- `player` `int` optional - default: current reason player

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3499`
