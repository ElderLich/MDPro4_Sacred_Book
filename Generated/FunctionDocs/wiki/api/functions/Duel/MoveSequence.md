# Duel.MoveSequence

## Signature

```lua
Duel.MoveSequence(Card c, int seq) -> void
```

## Description

Moves c to sequence seq within its current controller and location if c is affected by the resolving reason effect.
The core raises EVENT_MOVE for the moved card and returns no Lua values.

## Parameters

- `c` `Card`
- `seq` `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4884`
