# Duel.SetDiceResult

## Signature

```lua
Duel.SetDiceResult(int res, ... any) -> void
```

## Description

强行修改投骰子的结果为res ,最多5个参数，res只能是 1~255, ，其他数字全算作 1
此函数用于永续的EVENT_TOSS_DICE事件中

## Parameters

- `res` `int`
- `...` `any`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5042`
