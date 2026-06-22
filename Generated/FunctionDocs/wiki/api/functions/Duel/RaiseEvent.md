# Duel.RaiseEvent

## Signature

```lua
Duel.RaiseEvent(Card|Group eg, int code, Effect|nil re, int r, int rp, int ep, int ev) -> void
```

## Description

Raises event code for a Card or Group with the supplied effect, reason, reason player, event player, and event value.
The core processes instant events after raising the event and yields without returning Lua values.

## Parameters

- `eg` `Card|Group`
- `code` `int`
- `re` `Effect|nil`
- `r` `int`
- `rp` `int`
- `ep` `int`
- `ev` `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4895`
