# Card.IsControlerCanBeChanged

## Signature

```lua
Card.IsControlerCanBeChanged(Card c, [bool ignore_mzone], [int zone]) -> bool
```

## Description

检查c的控制权是否可以改变。
ignore_mzone=true 会忽视转移控制权后的玩家场上是否有空格位， zone 表示必须要使用的位置

## Parameters

- `c` `Card`
- `ignore_mzone` `bool` optional - default: false
- `zone` `int` optional - default: 0xff

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3627`
