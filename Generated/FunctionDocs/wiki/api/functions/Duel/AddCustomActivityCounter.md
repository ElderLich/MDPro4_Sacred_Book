# Duel.AddCustomActivityCounter

## Signature

```lua
Duel.AddCustomActivityCounter(int counter_id, int activity_type, function f) -> void
```

## Description

设置操作类型为activity_type、代号为counter_id的计数器，放在initial_effect函数内
f为过滤函数，以Card类型为参数，返回值为false的卡片进行以下类型的操作，计数器增加1（目前最多为1）

## Parameters

- `counter_id` `int`
- `activity_type` `int`
- `f` `function`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5068`
