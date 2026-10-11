# Card.CopyEffect

## Signature

```lua
Card.CopyEffect(Card c, int code, int reset, [int count]) -> int
```

## Description

Copies the initial_effect of card code onto c and returns the generated copy id, or -1 if code belongs to a Normal Monster.
reset defaults to RESETS_STANDARD when 0. count defaults to 1; phase resets without a turn side are normalized to both players' turns. If c is a non-Effect Monster, the core also adds TYPE_EFFECT for the same reset.

## Parameters

- `c` `Card`
- `code` `int`
- `reset` `int`
- `count` `int` optional - default: 1

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3621`
