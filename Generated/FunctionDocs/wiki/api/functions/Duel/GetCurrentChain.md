# Duel.GetCurrentChain

## Signature

```lua
Duel.GetCurrentChain() -> int
```

## Description

Returns the number of Chain Links currently stored in the active Chain.
Use Duel.GetChainInfo to inspect a specific Chain Link; this function only returns the current Chain size.

## How To Use It

Use this when a condition or operation needs the current Chain length.

```lua
if Duel.GetCurrentChain()>0 then
    -- a Chain is currently being built or resolved
end
```

For data about a specific Chain Link, use `Duel.GetChainInfo` instead of treating the count as the data itself.

## Related Functions

- [Duel.GetChainInfo](/api/functions/Duel/GetChainInfo)
- [Duel.CheckTiming](/api/functions/Duel/CheckTiming)
- [Duel.IsChainSolving](/api/functions/Duel/IsChainSolving)

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4945`
