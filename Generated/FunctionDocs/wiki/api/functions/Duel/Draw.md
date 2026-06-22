# Duel.Draw

## Signature

```lua
Duel.Draw(int player, int count, int reason) -> int
```

## Description

Makes player draw up to count cards for reason and returns the number actually drawn.
When reason includes REASON_RULE, effects that prevent drawing are ignored.

## Parameters

- `player` `int`
- `count` `int`
- `reason` `int`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4900`
