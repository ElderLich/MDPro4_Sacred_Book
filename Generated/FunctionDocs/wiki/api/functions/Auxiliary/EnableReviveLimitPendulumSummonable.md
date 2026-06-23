# Auxiliary.EnableReviveLimitPendulumSummonable

## Signature

```lua
Auxiliary.EnableReviveLimitPendulumSummonable(Card c, [int loc]) -> void
```

## Description

Enables revive-limit handling for c while also allowing it to be Pendulum Summoned from loc.
The helper calls Card.EnableReviveLimit, stores loc on c's metatable as psummonable_location, and completes c's procedure when it is successfully Pendulum Summoned.

## Parameters

- `c` `Card` - Special Summon Monster that should be allowed to complete its procedure by Pendulum Summon.
- `loc` `int` optional - Location mask from which the card is allowed to be Pendulum Summoned. Defaults to 0xff.

## Source

- `Utilities/procedure.lua:2097`
