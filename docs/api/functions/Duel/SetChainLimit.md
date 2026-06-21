# Duel.SetChainLimit

## Signature

```lua
Duel.SetChainLimit(function f) -> void
```

## Description

Set the chain conditions, f function prototype for bool f (e, ep, tp)
E said to limit the effect of chain, ep said to limit the chain of players, tp that launched the effect of the players
Calling this function in cost or target processing can limit the kinds of effects that can be chained (such as superfusion)
If f returns false, it means that the chain can not be chained. Once the chain condition has been set, the new chain will be canceled.

## Parameters

- `f` `function`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4887`
