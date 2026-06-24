# Duel.NegateActivation

## Signature

```lua
Duel.NegateActivation(int chainc) -> bool
```

## Description

Attempts to negate the activation of a Chain Link and returns true only if the activation was successfully negated.
Use it in a resolving negation operation after checking activation legality, commonly with Duel.IsChainNegatable. Gate follow-up actions such as destroy, banish, or send to the GY behind the boolean return.

## Parameters

- `chainc` `int` - Chain Link number to negate, commonly ev in an EVENT_CHAINING operation.

## Returns

- `bool` - true if the activation was negated; false if the Chain Link cannot be negated or the negation fails.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4929`
