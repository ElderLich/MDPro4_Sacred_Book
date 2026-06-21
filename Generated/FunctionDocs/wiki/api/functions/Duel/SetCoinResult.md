# Duel.SetCoinResult

## Signature

```lua
Duel.SetCoinResult(int res, ... any) -> void
```

## Description

强行修改投硬币的结果为res ,最多5个参数，res只能是 0 或 1, ，其他全算作 0
此函数用于永续的EVENT_TOSS_COIN事件中

## Parameters

- `res` `int`
- `...` `any`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5041`
