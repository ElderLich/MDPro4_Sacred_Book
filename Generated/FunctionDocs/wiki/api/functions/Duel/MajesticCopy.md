# Duel.MajesticCopy

## Signature

```lua
Duel.MajesticCopy(Card c1, Card c2) -> void
```

## Description

Copies monster initial effects from copy_target onto c until the End Phase.
It copies chain-link monster effects, skips Xyz Material effects, converts mandatory trigger/quick effects to optional versions, and does not copy Spell/Trap effects.

## Parameters

- `c1` `Card`
- `c2` `Card`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5073`
