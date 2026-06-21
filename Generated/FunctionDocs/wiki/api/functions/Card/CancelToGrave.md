# Card.CancelToGrave

## Signature

```lua
Card.CancelToGrave(Card c, [bool cancel]) -> void
```

## Description

取消送墓确定状态，cancel=false则重新设置送墓确定状态
注：送墓确定状态指的是在场上发动的不留场的魔法和陷阱后，这些卡片的状态
送墓确定状态中的卡无法返回手卡和卡组，并且连锁结束时送去墓地
此函数的作用是取消此状态使其留场，用于光之护封剑和废铁稻草人等卡

## Parameters

- `c` `Card`
- `cancel` `bool` optional - default: true

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3651`
