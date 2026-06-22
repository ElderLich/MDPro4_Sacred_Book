# Duel.ChainAttack

## Signature

```lua
Duel.ChainAttack([Card c]) -> void
```

## Description

Marks the current attacker so it can make another attack, optionally against card c.
The binding only sets chain-attack state. It returns no Lua value and does nothing if there is no current attacker or the attacker is not affected by the resolving effect.

## Parameters

- `c` `Card` optional

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4961`
