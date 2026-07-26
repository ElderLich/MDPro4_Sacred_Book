# Card.IsLink

## Signature

```lua
Card.IsLink(Card c, int link1, [int link2], [... int]) -> bool
```

## Description

Checks whether c:GetLink() equals any supplied link value. Nil link arguments are skipped; non-Link cards compare as 0.

## Parameters

- `c` `Card`
- `link1` `int`
- `link2` `int` optional
- `...` `int` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3492`
