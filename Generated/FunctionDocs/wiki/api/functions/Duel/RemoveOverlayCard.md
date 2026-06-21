# Duel.RemoveOverlayCard

## Signature

```lua
Duel.RemoveOverlayCard(int player, int s, int o, int min, int max, int reason) -> int
```

## Description

让player以reason原因移除以player来看的指定位置的min-max张叠放卡，返回值表示是否成功
s代表以player来看的自己的位置，o代表以player来看的对方的位置

## Parameters

- `player` `int`
- `s` `int`
- `o` `int`
- `min` `int`
- `max` `int`
- `reason` `int`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5018`
