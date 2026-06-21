# Card.IsLocation

## Signature

```lua
Card.IsLocation(Card c, int location) -> bool
```

## Description

检查c当前位置是否是location
注：当怪兽召唤，反转召唤，特殊召唤时召唤成功之前，
并且location=LOCATION_MZONE时，此函数返回false

## Parameters

- `c` `Card`
- `location` `int`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3610`
