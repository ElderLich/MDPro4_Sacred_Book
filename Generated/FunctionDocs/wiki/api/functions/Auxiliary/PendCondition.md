# Auxiliary.PendCondition

## Signature

```lua
Auxiliary.PendCondition(Effect e, Card|nil c, Group|nil og) -> bool
```

## Description

Condition function for the shared Pendulum Summon procedure.
It checks the two Pendulum Zones, current scales, hand and face-up Extra Deck candidate pools, available Monster Zones, once-per-turn state, extra Pendulum Summon effects, and whether at least one candidate can be Pendulum Summoned.

## Parameters

- `e` `Effect`
- `c` `Card|nil` - Procedure handler. When nil, the helper returns true for the core's availability probe.
- `og` `Group|nil` - Optional candidate group supplied by the core or another helper; nil uses the player's hand/Extra Deck candidates.

## Returns

- `bool` - true if a Pendulum Summon is available.

## Source

- `Utilities/procedure.lua:2004`
