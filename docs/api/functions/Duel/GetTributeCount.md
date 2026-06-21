# Duel.GetTributeCount

## Signature

```lua
Duel.GetTributeCount(Card c, [Group mg], [bool ex]) -> int
```

## Description

Returns the number of sacrifices that are normally used to invoke c, where ex = true allows monsters on the other side of the field (the wing of the Sun God-Sphere)
This number does not necessarily equal the number of cards in the return value of Duel.GetTributeGroup
Because some cards can be used as two sacrifices

## Parameters

- `c` `Card`
- `mg` `Group` optional
- `ex` `bool` optional - default: false

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4981`
