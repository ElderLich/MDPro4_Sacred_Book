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

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
