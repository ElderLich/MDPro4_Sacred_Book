# Duel.GetLinkedGroup

## Signature

```lua
Duel.GetLinkedGroup(int player, int s_range, int o_range) -> Group
```

## Description

返回以玩家player来看的 s_range 和 o_range 区域的处于连接状态的卡片组[其实只要后面2个参数不为0就行，只要不为0，都会变成LOCATION_MZONE]（？）

## Parameters

- `player` `int`
- `s_range` `int`
- `o_range` `int`

## Returns

- `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4940`
