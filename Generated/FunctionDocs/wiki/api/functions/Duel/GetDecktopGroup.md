# Duel.GetDecktopGroup

## Signature

```lua
Duel.GetDecktopGroup(int player, int count) -> Group
```

## Description

Returns a Group containing up to count cards from the top of player's Deck.
If count is larger than the remaining Deck size, only the available cards are included. This accessor does not confirm or reveal those cards by itself.

## Parameters

- `player` `int` - Player whose Deck is read.
- `count` `int` - Maximum number of cards to include from the top of the Deck.

## Returns

- `Group` - New Group containing the top Deck cards, or an empty Group if no cards are available.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4967`
