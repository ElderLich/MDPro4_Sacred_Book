# Card.IsCanBeLinkMaterial

## Signature

```lua
Card.IsCanBeLinkMaterial(Card c, [Card scard]) -> bool
```

## Description

Checks whether c can be used as Link Material, optionally for Link Monster scard.
Standard Link procedures call this before applying their own material filters.

## Parameters

- `c` `Card`
- `scard` `Card` optional - Link Monster that would use c as material.

## Returns

- `bool` - true if c may currently be used as Link Material for scard or for a generic Link Material check.

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3646`
