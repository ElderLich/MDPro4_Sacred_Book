# Card.IsLinkSetCard

## Signature

```lua
Card.IsLinkSetCard(Card c, int setcode1, [int setcode2], [... int]) -> bool
```

## Description

Checks whether c can be treated as any supplied setcode while used as Link Material. Nil setcode arguments are skipped.

## Parameters

- `c` `Card`
- `setcode1` `int`
- `setcode2` `int` optional
- `...` `int` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3400`
