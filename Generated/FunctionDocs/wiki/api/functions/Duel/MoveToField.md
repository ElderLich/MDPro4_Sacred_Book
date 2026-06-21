# Duel.MoveToField

## Signature

```lua
Duel.MoveToField(Card c, int move_player, int target_player, int dest, int pos, bool enable, [int zone]) -> bool
```

## Description

Let the player move_player to move the c target_player field, the return value that is successful
Dest can only be LOCATION_MZONE or LOCATION_SZONE, pos represents an optional representation, and enable indicates whether or not the effect of c is applied immediately

## Parameters

- `c` `Card`
- `move_player` `int`
- `target_player` `int`
- `dest` `int`
- `pos` `int`
- `enable` `bool`
- `zone` `int` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4882`
