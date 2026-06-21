# Duel.GetTributeCount

## Signature

```lua
Duel.GetTributeCount(Card c, [Group mg], [bool ex]) -> int
```

## Description

返回场上[或mg中]用于通常召唤c的祭品数量，ex=true则允许对方场上的怪兽（太阳神之翼神龙-球体形）
此数量不一定等于Duel.GetTributeGroup的返回值中的卡片数量
因为某些卡可以作为多个祭品来使用

## Parameters

- `c` `Card`
- `mg` `Group` optional
- `ex` `bool` optional - default: false

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4981`
