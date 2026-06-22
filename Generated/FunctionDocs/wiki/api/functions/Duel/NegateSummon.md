# Duel.NegateSummon

## Signature

```lua
Duel.NegateSummon(Card|Group targets) -> void
```

## Description

Negates a current Normal Summon, Flip Summon, or Special Summon for targets.
targets may be a Card or Group. Normal and Flip Summon negation require a single card; Special Summon negation can process a group and only negates cards whose Summon is negatable by the current reason effect. The core raises the matching *_SUMMON_NEGATED event and returns no Lua value.

## Parameters

- `targets` `Card|Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4932`
