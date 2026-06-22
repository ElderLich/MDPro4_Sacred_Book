# Duel.CreateToken

## Signature

```lua
Duel.CreateToken(int player, int code) -> Card|false
```

## Description

Creates a Token card with card code code for player and returns it.
The returned Token is not placed on the field automatically; scripts normally pass it to Duel.SpecialSummon or another operation afterwards.

## Parameters

- `player` `int`
- `code` `int`

## Returns

- `Card|false`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4872`
