# Card.IsOriginalCodeRule

## Signature

```lua
Card.IsOriginalCodeRule(Card c, int code1, [int code2], [... int]) -> bool
```

## Description

Checks whether c's rule-original card code matches any supplied code.
Nil code arguments are skipped. For double-code cards, the core checks both rule-original codes; otherwise it checks the card's duel code.

## Parameters

- `c` `Card`
- `code1` `int`
- `code2` `int` optional
- `...` `int` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3482`
