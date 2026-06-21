# Card.EnableCounterPermit

## Signature

```lua
Card.EnableCounterPermit(Card c, int countertype, [int location], [function condition]) -> void
```

## Description

允许c[在位置location，满足条件condition]放置那个需要“可以放置”才能放置的指示物countertype
（location的默认值与c的种类有关，灵摆怪兽需要指定能否在怪兽区域或灵摆区域放置指示物）

## Parameters

- `c` `Card`
- `countertype` `int`
- `location` `int` optional
- `condition` `function` optional

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3631`
