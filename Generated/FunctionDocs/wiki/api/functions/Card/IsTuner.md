# Card.IsTuner

## Signature

```lua
Card.IsTuner(Card c, Card scard) -> bool
```

## Description

检查c是否为scard的调整怪兽。
除了检查TYPE_TUNER以外，还会检查其身上所有能让其变为调整怪兽的效果。

## Parameters

- `c` `Card`
- `scard` `Card`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3506`
