# Card.ResetEffect

## Signature

```lua
Card.ResetEffect(Card c, int reset_code, int reset_type) -> void
```

## Description

以重置类型为reset_type、重置种类为reset_code手动重置c受到的效果的影响
reset_type只能是以下类型，对应的重置种类为
RESET_EVENT       发生事件重置        reset_code为事件
RESET_PHASE       阶段结束重置        reset_code为阶段
RESET_CODE        重置指定code的效果  reset_code为效果的种类code，只能重置EFFECT_TYPE_SINGLE的永续型效果
RESET_COPY        重置复制的效果      reset_code为copy_id
RESET_CARD        重置卡片的效果      reset_code为效果owner的卡号

## Parameters

- `c` `Card`
- `reset_code` `int`
- `reset_type` `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3550`
