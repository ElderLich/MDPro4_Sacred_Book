# Duel.SetChainLimit

## Signature

```lua
Duel.SetChainLimit(function f) -> void
```

## Description

Registers a temporary chain-limit callback for the current Chain window.
The callback is stored with the current reason player and is later called as f(e, chain_player, activating_player). If it returns false, that effect cannot be chained.

## Parameters

- `f` `function`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4887`
