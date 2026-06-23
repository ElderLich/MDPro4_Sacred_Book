# Card.CompleteProcedure

## Signature

```lua
Card.CompleteProcedure(Card c) -> void
```

## Description

Marks c as having completed its proper Summon procedure.
Use this after a resolving effect successfully performs a proper Summon for a revive-limit monster, such as an effect-driven Ritual, Fusion, Synchro, Xyz, Link, or Special Summon-only procedure.
Do not call this for ordinary revive effects. Normal rule procedures registered with EFFECT_SPSUMMON_PROC are completed by the core after the procedure succeeds.

## Parameters

- `c` `Card` - Card whose proper Summon status is being completed.

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3569`
