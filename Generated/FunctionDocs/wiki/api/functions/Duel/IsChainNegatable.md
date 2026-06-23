# Duel.IsChainNegatable

## Signature

```lua
Duel.IsChainNegatable(int chainc) -> bool
```

## Description

Compatibility check for whether chainc's activation can be negated.
In this MDPro3 core binding, the function currently returns true for any chain count.
Local scripts still call it in negation conditions so the script expresses the intended activation-legality check.

## Parameters

- `chainc` `int` - Chain Link number to test, commonly the ev argument in an EVENT_CHAINING condition.

## Returns

- `bool` - true when this binding considers that Chain Link's activation negatable.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5061`
