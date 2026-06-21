# Card.GetSequence

## Signature

```lua
Card.GetSequence(Card c) -> int
```

## Description

返回c在当前位置的序号
在场上时，序号代表所在的格子，从左往右分别是0-4，场地魔法格的序号为5
在其它地方时，序号表示的是第几张卡，最下面的卡的序号为0

## Parameters

- `c` `Card`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3468`
