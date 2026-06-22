# Duel.ConfirmCards

## Signature

```lua
Duel.ConfirmCards(int player, Card|Group targets, [bool skip_panel]) -> void
```

## Description

Reveals a Card or Group to player and waits for the client confirmation.
If skip_panel is true, the client skips the extra confirmation panel when possible.

## Parameters

- `player` `int`
- `targets` `Card|Group`
- `skip_panel` `bool` optional - default: false

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4892`
