# Duel.GetControl

## Signature

```lua
Duel.GetControl(Card|Group targets, int player, [int reset_phase], [int reset_count], [int zone]) -> bool
```

## Description

Let players get control of the player, the return value indicates success

## Parameters

- `targets` `Card|Group`
- `player` `int`
- `reset_phase` `int` optional - default: 0
- `reset_count` `int` optional - default: 0
- `zone` `int` optional - default: 0xff

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4906`
