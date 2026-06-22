# Duel.ConfirmDecktop

## Signature

```lua
Duel.ConfirmDecktop(int player, int count) -> void
```

## Description

Reveals up to count cards from the top of player's Main Deck to the client.
count is clamped to the remaining Deck size. The function yields for the reveal wait and returns no Lua values.

## Parameters

- `player` `int`
- `count` `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4890`
