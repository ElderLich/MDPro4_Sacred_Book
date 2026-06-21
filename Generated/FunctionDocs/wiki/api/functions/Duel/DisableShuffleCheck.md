# Duel.DisableShuffleCheck

## Signature

```lua
Duel.DisableShuffleCheck([bool disable]) -> void
```

## Description

使下一个操作不检查是否需要洗切卡组或手卡
注：如果不调用此函数，
除了调用Duel.DiscardDeck和Duel.Draw之外从卡组中取出卡或者把卡加入手卡
或者把卡加入卡组（非最上端或最底端）时，系统会自动在效果处理结束时洗切卡组或手卡
如果不希望如此，比如从卡组顶端除外一张卡等操作，那么需要调用此函数
此函数仅保证紧接着的一次操作不会进行洗卡检测

## Parameters

- `disable` `bool` optional - default: true

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4912`
