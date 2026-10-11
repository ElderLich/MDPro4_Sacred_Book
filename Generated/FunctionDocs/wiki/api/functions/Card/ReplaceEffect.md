# Card.ReplaceEffect

## Signature

```lua
Card.ReplaceEffect(Card c, int code, int reset, [int count]) -> int
```

## Description

Replaces c's effects with the effects of card code under the given reset flags and returns the replacement id.
count defaults to 1; phase resets automatically include both players' turns when no turn side is specified.

## Parameters

- `c` `Card`
- `code` `int`
- `reset` `int`
- `count` `int` optional - default: 1

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3622`
