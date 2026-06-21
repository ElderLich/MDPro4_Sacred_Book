# Duel.Hint

## Signature

```lua
Duel.Hint(int hint_type, int player, int desc) -> void
```

## Description

Sends a hint message of hint_type to player using desc as the message id.
For HINT_SELECTMSG, desc is also stored as that player's last selection hint. HINT_OPSELECTED is displayed to the other player.

## Parameters

- `hint_type` `int`
- `player` `int`
- `desc` `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5019`
