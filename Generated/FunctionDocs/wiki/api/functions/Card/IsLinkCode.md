# Card.IsLinkCode

## Signature

```lua
Card.IsLinkCode(Card c, int code1, [int code2], [... int]) -> bool
```

## Description

Checks whether c matches any supplied code while used as Link Material.
This includes c's current code, second code, and EFFECT_ADD_LINK_CODE values. If no link-code additions apply, the binding falls back to Card.IsCode.

## Parameters

- `c` `Card`
- `code1` `int`
- `code2` `int` optional
- `...` `int` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3442`
