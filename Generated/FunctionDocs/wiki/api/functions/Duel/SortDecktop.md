# Duel.SortDecktop

## Signature

```lua
Duel.SortDecktop(int sort_player, int target_player, int count) -> void
```

## Description

Lets sort_player reorder the top count cards of target_player's Main Deck.
Both players must be valid and count must be at least 1. If count is larger than the remaining Deck size, the processor only sorts the available top cards.

## Parameters

- `sort_player` `int`
- `target_player` `int`
- `count` `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4893`
