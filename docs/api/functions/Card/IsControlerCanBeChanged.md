# Card.IsControlerCanBeChanged

## Signature

```lua
Card.IsControlerCanBeChanged(Card c, [bool ignore_mzone], [int zone]) -> bool
```

## Description

Check whether the control of c can be changed
Note: This function appends the space on the field to the Card.IsAbleToChangeControler

## Parameters

- `c` `Card`
- `ignore_mzone` `bool` optional - default: false
- `zone` `int` optional - default: 0xff

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3627`
