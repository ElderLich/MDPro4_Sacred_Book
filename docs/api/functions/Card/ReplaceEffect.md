# Card.ReplaceEffect

## Signature

```lua
Card.ReplaceEffect(Card c, int code, int reset_flag, [int reset_count]) -> int
```

## Description

Replace the effect of c with the effect of the card whose card number is code, and add additional reset conditions
The return value is the code id representing the replacement effect

## Parameters

- `c` `Card`
- `code` `int`
- `reset_flag` `int`
- `reset_count` `int` optional - default: 1

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3567`
