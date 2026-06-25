# Duel.NegateEffect

## Signature

```lua
Duel.NegateEffect(int chainc, [bool forced]) -> bool
```

## Description

Attempts to negate the effect of a Chain Link without necessarily negating its activation, and returns true if the effect was successfully negated.
Use this for text such as "negate that effect". The optional forced argument requests a forced disable.
Use Duel.NegateActivation for activation negation and Duel.NegateSummon for Summon negation; those are different game events.

## How To Use It

Use this during resolution for effects that negate the effect of a Chain Link without treating the activation as negated.

```lua
if Duel.NegateEffect(ev) then
    -- follow-up that requires the effect to be negated
end
```

The optional `forced` argument is passed to the core disable-chain check. Activation-negation cards should usually use `Duel.NegateActivation` instead.

## Related Functions

- [Duel.IsChainDisablable](/api/functions/Duel/IsChainDisablable)
- [Duel.NegateActivation](/api/functions/Duel/NegateActivation)
- [Duel.GetChainInfo](/api/functions/Duel/GetChainInfo)

## Parameters

- `chainc` `int` - Chain Link number whose effect should be negated.
- `forced` `bool` optional - Optional forced-disable request.

## Returns

- `bool` - true if the Chain Link's effect was negated; false if it cannot be negated or the negation fails.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4930`
