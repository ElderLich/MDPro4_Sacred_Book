# Auxiliary.EnablePendulumAttribute

## Signature

```lua
Auxiliary.EnablePendulumAttribute(Card c, [bool|nil reg]) -> void
```

## Description

Registers the standard Pendulum Summon procedure for Pendulum Monster c.
The procedure is a LOCATION_PZONE EFFECT_SPSUMMON_PROC_G with SUMMON_TYPE_PENDULUM, using Auxiliary.PendCondition and Auxiliary.PendOperation.
Unless reg is false, the helper also registers the simple Pendulum Card activation effect from the hand.

## Parameters

- `c` `Card` - Pendulum Monster receiving the shared Pendulum Summon procedure.
- `reg` `bool|nil` optional - When false, skip the default hand activation effect. nil or true registers it.

## Source

- `Utilities/procedure.lua:1948`
