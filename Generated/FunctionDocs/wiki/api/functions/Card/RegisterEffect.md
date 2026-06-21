# Card.RegisterEffect

## Signature

```lua
Card.RegisterEffect(Card c, Effect e, [bool forced]) -> int
```

## Description

把效果e注册给c，返回效果的全局id，并设置e的Handler为c
默认情况下注册时如果c带有免疫e的效果那么注册会失败
如果forced为true则不会检查c对e的免疫效果

## Parameters

- `c` `Card`
- `e` `Effect`
- `forced` `bool` optional - default: false

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3548`
