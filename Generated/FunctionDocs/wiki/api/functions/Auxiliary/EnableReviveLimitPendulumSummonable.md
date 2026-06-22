# Auxiliary.EnableReviveLimitPendulumSummonable

## Signature

```lua
Auxiliary.EnableReviveLimitPendulumSummonable(Card c, [int loc]) -> void
```

## Description

Enables revive-limit handling for c while also allowing it to be Pendulum Summoned from loc.
The helper stores loc on c's metatable and completes c's procedure when it is successfully Pendulum Summoned.

## Parameters

- `c` `Card`
- `loc` `int` optional - default: 0xff

## Source

- `Utilities/procedure.lua:2097`
