# Duel.GetFieldCard

## Signature

```lua
Duel.GetFieldCard(int player, int location, int sequence) -> Card|nil
```

## Description

Returns the card at player, location, and sequence, or nil if that slot is empty or invalid.
The binding also returns nil while the card at that slot is in Summoning or Special Summon step status. Field Zone sequence 0 maps to the Field Zone, and Pendulum Zone sequences 0 and 1 only return cards currently marked as Pendulum Zone cards.

## Parameters

- `player` `int`
- `location` `int`
- `sequence` `int`

## Returns

- `Card|nil`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4943`
