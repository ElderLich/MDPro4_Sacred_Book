# Duel.ChangeAttacker

## Signature

```lua
Duel.ChangeAttacker(Card c, [bool ignore_count]) -> void
```

## Description

Changes the current attacking monster to attacker.
Unless ignore_count is true, the new attacker gains an attack announcement count, and during the Damage Phase also gains attacked-count and attacked-card records.

## Parameters

- `c` `Card`
- `ignore_count` `bool` optional - default: false

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4919`
