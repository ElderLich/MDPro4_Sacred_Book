# Duel.IsChainDisablable

## Signature

```lua
Duel.IsChainDisablable(int chainc) -> bool
```

## Description

Checks whether chainc's effect can be negated.
While a Chain is resolving, this asks the core whether that Chain link can currently be disabled; outside Chain resolution it returns true.

## Related Functions

- [Duel.NegateEffect](/api/functions/Duel/NegateEffect)
- [Duel.IsChainDisabled](/api/functions/Duel/IsChainDisabled)
- [Duel.GetChainInfo](/api/functions/Duel/GetChainInfo)

## Parameters

- `chainc` `int`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5062`
