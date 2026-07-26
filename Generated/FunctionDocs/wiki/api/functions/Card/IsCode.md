# Card.IsCode

## Signature

```lua
Card.IsCode(Card c, int code1, [int code2], [... int]) -> bool
```

## Description

Checks whether c's current card code, or alternate code if it has one, matches any supplied code.

## How To Use It

Use this in filters when a card must specifically be one or more card IDs.

```lua
function s.matfilter(c)
    return c:IsCode(89631139,23995346)
end
```

This checks the card's current code and alternate code, so copied or changed-code effects can matter.

## Parameters

- `c` `Card`
- `code1` `int`
- `code2` `int` optional
- `...` `int` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3483`
