# Duel.Draw

## Signature

```lua
Duel.Draw(int player, int count, int reason) -> int
```

## Description

Let the player play the count card with the reason, and return the number of cards actually drawn
If the reason contains REASON_RULE the draw is not affected by the "can not draw" effect

## Parameters

- `player` `int`
- `count` `int`
- `reason` `int`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4900`
