# Auxiliary.PendCondition

## Signature

```lua
Auxiliary.PendCondition(Effect e, Card|nil c, Group|nil og) -> bool
```

## Description

Condition function for the shared Pendulum Summon procedure. It checks the two Pendulum Zones, available locations and zones, once-per-turn state, and valid summonable monsters.

## Parameters

- `e` `Effect`
- `c` `Card|nil`
- `og` `Group|nil`

## Returns

- `bool` - true if a Pendulum Summon is available.

## Source

- `Utilities/procedure.lua:2004`
