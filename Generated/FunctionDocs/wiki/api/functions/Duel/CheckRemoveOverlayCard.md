# Duel.CheckRemoveOverlayCard

## Signature

```lua
Duel.CheckRemoveOverlayCard(int player, int s, int o, int count, int reason) -> bool
```

## Description

检查player能否以原因reason移除以player来看的指定位置至少count张卡
s代表以player来看的自己的位置，o代表以player来看的对方的位置

## Parameters

- `player` `int`
- `s` `int`
- `o` `int`
- `count` `int`
- `reason` `int`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5017`
