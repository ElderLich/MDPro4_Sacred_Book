# Duel.AnnounceAttribute

## Signature

```lua
Duel.AnnounceAttribute(int player, int count, int available) -> int
```

## Description

Lets player declare count Attributes from the available Attribute bitmask and returns the selected Attribute bitmask.
available should be a bitwise combination of ATTRIBUTE_* constants.

## Parameters

- `player` `int`
- `count` `int`
- `available` `int`

## Returns

- `int` - Selected Attribute bitmask.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5030`
