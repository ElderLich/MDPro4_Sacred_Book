# Duel.NegateActivation

## Signature

```lua
Duel.NegateActivation(int chainc) -> bool
```

## Description

Attempts to negate the activation of a Chain Link and returns true only if the activation was successfully negated.
Use it in a resolving negation operation after checking activation legality, commonly with Duel.IsChainNegatable. Gate follow-up actions such as destroy, banish, or send to the GY behind the boolean return.
Use Duel.NegateEffect for "negate that effect" text where the activation itself is not negated.

## How To Use It

Use this during resolution for effects that negate the activation of a Chain Link.

```lua
if Duel.NegateActivation(ev) then
    Duel.Destroy(rc,REASON_EFFECT)
end
```

Gate follow-up actions behind the boolean return. Use `Duel.NegateEffect` when the effect is negated but the activation itself is not.

## Related Functions

- [Duel.IsChainNegatable](/api/functions/Duel/IsChainNegatable)
- [Duel.NegateEffect](/api/functions/Duel/NegateEffect)
- [Duel.GetChainInfo](/api/functions/Duel/GetChainInfo)

## Parameters

- `chainc` `int` - Chain Link number to negate, commonly ev in an EVENT_CHAINING operation.

## Returns

- `bool` - true if the activation was negated; false if the Chain Link cannot be negated or the negation fails.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4929`
