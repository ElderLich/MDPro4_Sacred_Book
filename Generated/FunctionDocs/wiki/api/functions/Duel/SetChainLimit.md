# Duel.SetChainLimit

## Signature

```lua
Duel.SetChainLimit(function f) -> void
```

## Description

设定连锁条件，f的函数原型为 bool f(e,ep,tp)
e表示要限制连锁的效果，ep表示要限制连锁的玩家，tp表示发动该效果的玩家
在cost或者target处理中调用此函数可以限制可以连锁的效果的种类（如超融合）
如果f返回false表示不能连锁，一旦设置连锁条件后发生了新的连锁那么连锁条件将会解除

## Parameters

- `f` `function`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4887`
