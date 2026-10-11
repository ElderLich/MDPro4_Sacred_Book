# Card.GetOriginalCodeRule

## Signature

```lua
Card.GetOriginalCodeRule(Card c) -> int,int|nil
```

## Description

Returns c's rule-original card code.
Double-code cards return two codes: the printed original code and the second rule code. Other cards return only the duel code used by the core.

## Parameters

- `c` `Card`

## Returns

- `int` - Primary rule-original code.
- `int|nil` - Second rule code, when present.

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3438`
