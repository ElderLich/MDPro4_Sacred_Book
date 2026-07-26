# Card.GetUnionCount

## Signature

```lua
Card.GetUnionCount(Card c) -> int,int
```

## Description

Returns two values for c: the number of modern Union cards equipped to it, then the number of old Union cards equipped to it.
The local core counts equipped cards with TYPE_UNION plus EFFECT_UNION_STATUS or EFFECT_OLDUNION_STATUS.

## Parameters

- `c` `Card` - Monster whose equipped Union cards should be counted.

## Returns

- `int` - Number of equipped modern Union cards.
- `int` - Number of equipped old Union cards.

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3526`
