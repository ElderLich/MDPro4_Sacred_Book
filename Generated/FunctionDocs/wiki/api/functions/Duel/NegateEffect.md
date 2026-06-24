# Duel.NegateEffect

## Signature

```lua
Duel.NegateEffect(int chainc, [bool forced]) -> bool
```

## Description

Attempts to negate the effect of a Chain Link without necessarily negating its activation, and returns true if the effect was successfully negated.
Use this for text such as "negate that effect". The optional forced argument requests a forced disable.

## Parameters

- `chainc` `int` - Chain Link number whose effect should be negated.
- `forced` `bool` optional - Optional forced-disable request.

## Returns

- `bool` - true if the Chain Link's effect was negated; false if it cannot be negated or the negation fails.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4930`
