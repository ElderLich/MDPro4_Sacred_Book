# Card.GetHandSynchro

## Signature

```lua
Card.GetHandSynchro(Card c) -> nil|Effect,function|nil,int|nil,int|nil
```

## Description

如果卡片 c 受到手卡同调效果 EFFECT_HAND_SYNCHRO 影响，则返回 Effect e,function target,int min,int max ;否则返回nil

## Parameters

- `c` `Card`

## Returns

- `nil|Effect`
- `function|nil`
- `int|nil`
- `int|nil`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3547`
