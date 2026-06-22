# Auxiliary.EnableArcanaCoin

## Signature

```lua
Auxiliary.EnableArcanaCoin(Card c, int event1, [... int]) -> void
```

## Description

Registers Arcana Force-style mandatory coin-toss trigger effects on c for event1 and any extra events.
The shared operation records the coin result as FLAG_ID_ARCANA_COIN; Reversal of Fate replaces the toss with a player choice.

## Parameters

- `c` `Card`
- `event1` `int`
- `...` `int` optional

## Source

- `Utilities/utility.lua:266`
