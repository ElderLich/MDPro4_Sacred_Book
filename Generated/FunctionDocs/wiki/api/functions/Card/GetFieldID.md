# Card.GetFieldID

## Signature

```lua
Card.GetFieldID(Card c) -> int
```

## Description

返回c转移到当前位置的时间标识
此数值唯一，越小表示c是越早出现在那个位置
卡片从里侧翻开也会改变此数值

## Parameters

- `c` `Card`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3477`
