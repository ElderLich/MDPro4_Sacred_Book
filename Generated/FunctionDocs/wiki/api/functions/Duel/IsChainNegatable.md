# Duel.IsChainNegatable

## Signature

```lua
Duel.IsChainNegatable(int chainc) -> bool
```

## Description

Compatibility check for whether chainc's activation can be negated.
In this MDPro4 core binding, the function currently returns true for any chain count.
Local scripts still call it in negation conditions so the script expresses the intended activation-legality check.
Use it with Duel.NegateActivation, not as a substitute for effect-negation checks such as Duel.IsChainDisablable.

## How To Use It

Use this in activation-negation conditions to express that the responding effect only works on a Chain Link whose activation can be negated.

```lua
return Duel.IsChainNegatable(ev)
```

In the current MDPro4 core binding this function returns true for any chain count, but local scripts still use it as the activation-negation legality marker. Use `Duel.IsChainDisablable` when the operation is effect negation rather than activation negation.

## Related Functions

- [Duel.NegateActivation](/api/functions/Duel/NegateActivation)
- [Duel.GetCurrentChain](/api/functions/Duel/GetCurrentChain)
- [Duel.IsChainDisablable](/api/functions/Duel/IsChainDisablable)

## Parameters

- `chainc` `int` - Chain Link number to test, commonly the ev argument in an EVENT_CHAINING condition.

## Returns

- `bool` - true when this binding considers that Chain Link's activation negatable.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5061`
