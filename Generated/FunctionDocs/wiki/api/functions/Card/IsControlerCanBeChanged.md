# Card.IsControlerCanBeChanged

## Signature

```lua
Card.IsControlerCanBeChanged(Card c, [bool ignore_mzone], [int zone]) -> bool
```

## Description

Checks whether control of c can currently move to the other player.
The card must be in the Monster Zone and must not be affected by EFFECT_CANNOT_CHANGE_CONTROL. Unless ignore_mzone is true, the opponent must also have an available Monster Zone in zone.

## Parameters

- `c` `Card`
- `ignore_mzone` `bool` optional - default: false
- `zone` `int` optional - default: 0xff

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3682`
