# Card.GetCurrentScale

## Signature

```lua
Card.GetCurrentScale(Card c) -> int
```

## Description

Returns the Pendulum Scale c currently uses.
In a Pendulum Zone, this returns the left or right current scale according to c's zone sequence. Outside a Pendulum Zone, it returns c's printed left scale value.

## Parameters

- `c` `Card`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3468`
