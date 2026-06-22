# Auxiliary.EnablePendulumAttribute

## Signature

```lua
Auxiliary.EnablePendulumAttribute(Card c, [bool|nil reg]) -> void
```

## Description

Registers the Pendulum Summon procedure for Pendulum Monster c.
Unless reg is false, it also registers the Pendulum Card activation effect from the hand.

## Parameters

- `c` `Card`
- `reg` `bool|nil` optional

## Source

- `Utilities/procedure.lua:1948`
