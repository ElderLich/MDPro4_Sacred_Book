# Auxiliary.BecomeOriginalCode

## Signature

```lua
Auxiliary.BecomeOriginalCode(Card c, Card tc, [int reset]) -> Effect
```

## Description

Registers an EFFECT_CHANGE_CODE effect on c so its code becomes tc's original rule code until reset; reset defaults to standard event reset through the End Phase.

## Parameters

- `c` `Card`
- `tc` `Card`
- `reset` `int` optional - defult: RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END

## Returns

- `Effect`

## Source

- `Utilities/utility.lua:2010`
