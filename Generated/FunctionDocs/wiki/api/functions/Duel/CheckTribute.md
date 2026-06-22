# Duel.CheckTribute

## Signature

```lua
Duel.CheckTribute(Card c, int min, [int max], [Group|nil mg], [int toplayer], [int zone]) -> bool
```

## Description

Checks whether there is a valid Tribute set for Normal Summoning or Setting c.
max defaults to min, mg can restrict the candidate pool, toplayer defaults to c's current controller, and zone defaults to the current extra-summon zone limit when present or 0x1f otherwise.

## Parameters

- `c` `Card`
- `min` `int`
- `max` `int` optional - default: min
- `mg` `Group|nil` optional
- `toplayer` `int` optional - default: c's controller
- `zone` `int` optional - default: current extra-summon zone limit or 0x1f

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4982`
