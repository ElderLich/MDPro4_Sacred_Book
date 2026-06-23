# Auxiliary.PendulumSummonableBool

## Signature

```lua
Auxiliary.PendulumSummonableBool(Card c) -> bool
```

## Description

Returns true if c has a psummonable_location flag that includes its current location.
The shared Pendulum candidate filter passes this result as the nocheck and nolimit values for Card.IsCanBeSpecialSummoned, allowing revive-limit Pendulum Summonable monsters only from configured locations.

## Parameters

- `c` `Card` - Card previously configured by Auxiliary.EnableReviveLimitPendulumSummonable.

## Returns

- `bool` - true if c's current location is Pendulum Summonable by its flag.

## Source

- `Utilities/procedure.lua:2111`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
