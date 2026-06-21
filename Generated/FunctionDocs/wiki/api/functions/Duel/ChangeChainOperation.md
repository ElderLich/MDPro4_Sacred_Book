# Duel.ChangeChainOperation

## Signature

```lua
Duel.ChangeChainOperation(int chainc, function f) -> void
```

## Description

把连锁chainc的效果的处理函数换成f，用于实现“把效果变成”等的效果
f(e,tp,eg,ep,ev,re,r,rp)

## Parameters

- `chainc` `int`
- `f` `function`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4928`
