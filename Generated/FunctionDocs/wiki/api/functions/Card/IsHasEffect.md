# Card.IsHasEffect

## Signature

```lua
Card.IsHasEffect(Card c, int code, [int player]) -> Effect,...?
```

## Description

检查c是否受到效果种类是code的效果的影响
没有则返回nil
有则返回那些效果

## Parameters

- `c` `Card`
- `code` `int`
- `player` `int` optional

## Returns

- `Effect`
- `...?` - Effect

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3549`
