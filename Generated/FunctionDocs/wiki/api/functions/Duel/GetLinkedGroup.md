# Duel.GetLinkedGroup

## Signature

```lua
Duel.GetLinkedGroup(int player, int s, int o) -> Group|nil
```

## Description

Returns a Group of cards in player-relative locations s and o that are linked.
Use the Card.GetLinkedGroup method when checking one Link Monster; use this Duel helper for field-wide location-mask checks.

## Parameters

- `player` `int` - Perspective player.
- `s` `int` - Location mask on player's side.
- `o` `int` - Location mask on the opponent's side from player's perspective.

## Returns

- `Group|nil` - Linked cards, or nil if player is invalid.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4940`
