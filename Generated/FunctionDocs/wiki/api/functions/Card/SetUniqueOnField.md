# Card.SetUniqueOnField

## Signature

```lua
Card.SetUniqueOnField(Card c, int s, int o, function|int unique_code, [int unique_location]) -> void
```

## Description

设置c以unique_code只能在场上[或怪兽区域或魔陷区域，由unique_location决定]只能存在1张,function 的返回值类型必须是int
s不为0会检查自己场上的唯一性，o不为0则检查对方场上的唯一性

## Parameters

- `c` `Card`
- `s` `int`
- `o` `int`
- `unique_code` `function|int`
- `unique_location` `int` optional - default: LOCATIOIN_ONFIELD

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3657`
