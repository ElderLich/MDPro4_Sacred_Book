# Auxiliary.nbcon

## Signature

```lua
Auxiliary.nbcon(int tp, Effect re) -> bool
```

## Description

Condition helper for effects that negate an activation and banish the activating card. It requires tp to be able to banish, and the activating card must either no longer be related to its effect or be able to be banished.

## Parameters

- `tp` `int`
- `re` `Effect`

## Returns

- `bool` - true if the activation can be negated and the card can be banished if needed.

## Source

- `Utilities/utility.lua:1467`
