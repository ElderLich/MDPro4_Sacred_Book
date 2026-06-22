# Duel.CheckEvent

## Signature

```lua
Duel.CheckEvent(int event, [bool get_info]) -> bool,Group|nil,int|nil,int|nil,Effect|nil,int|nil,int|nil
```

## Description

Without get_info, returns whether event is present in the current event state.
With get_info true, returns true plus event cards, event player, event value, reason effect, reason, and reason player when found; otherwise returns false.

## Parameters

- `event` `int`
- `get_info` `bool` optional - default: false

## Returns

- `bool`
- `Group|nil` - Event cards when get_info succeeds.
- `int|nil` - Event player.
- `int|nil` - Event value.
- `Effect|nil` - Reason effect.
- `int|nil` - Reason.
- `int|nil` - Reason player.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4894`
