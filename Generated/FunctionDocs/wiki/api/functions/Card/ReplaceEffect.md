# Card.ReplaceEffect

## Signature

```lua
Card.ReplaceEffect(Card c, int code, int reset_flag, [int reset_count]) -> int
```

## Description

把c的效果替换为卡号是code的卡的效果，并且添加额外的reset条件
返回值是表示替换效果的代号id

## Parameters

- `c` `Card`
- `code` `int`
- `reset_flag` `int`
- `reset_count` `int` optional - default: 1

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3567`
