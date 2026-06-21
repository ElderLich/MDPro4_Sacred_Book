# Card.CopyEffect

## Signature

```lua
Card.CopyEffect(Card c, int code, int reset_flag, [int reset_count]) -> int
```

## Description

Adding a card number for c is the replicable effect of the card's code, and adding an additional reset condition
The return value is the code id representing the copy effect

## Parameters

- `c` `Card`
- `code` `int`
- `reset_flag` `int`
- `reset_count` `int` optional - default: 1

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3566`
