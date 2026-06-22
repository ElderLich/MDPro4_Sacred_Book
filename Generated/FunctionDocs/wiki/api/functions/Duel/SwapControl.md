# Duel.SwapControl

## Signature

```lua
Duel.SwapControl(Card|Group targets1, Card|Group targets2, [int reset_phase], [int reset_count]) -> bool
```

## Description

Swaps control between two Cards or between two Groups and returns whether the swap processor succeeded.
reset_phase and reset_count are optional temporary-control reset settings.

## Parameters

- `targets1` `Card|Group`
- `targets2` `Card|Group`
- `reset_phase` `int` optional - default: 0
- `reset_count` `int` optional - default: 0

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4907`
