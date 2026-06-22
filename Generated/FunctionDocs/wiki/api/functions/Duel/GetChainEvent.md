# Duel.GetChainEvent

## Signature

```lua
Duel.GetChainEvent(int count) -> Group,int,int,Effect,int,int
```

## Description

Returns the event group, event player, event value, reason effect, reason, and reason player stored on Chain Link count.

## Parameters

- `count` `int`

## Returns

- `Group` - Event cards.
- `int` - Event player.
- `int` - Event value.
- `Effect` - Reason effect.
- `int` - Reason flags.
- `int` - Reason player.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4948`
