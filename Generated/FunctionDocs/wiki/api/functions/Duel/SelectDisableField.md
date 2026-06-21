# Duel.SelectDisableField

## Signature

```lua
Duel.SelectDisableField(int player, int count, int s, int o, int filter) -> int
```

## Description

让玩家player选择指定位置满足标记条件filter的count个可用的空格，并返回选择位置的标记
常用于选择区域不能使用或移动怪兽格子
##位置标记的定义如下
##flag = 0;
##seq为在玩家p，位置l中选择的格子序号
##for(int32 i = 0; i < count; ++i) {
##	flag |= 1 << (seq[i] + (p[i] == player ? 0 : 16) + (l[i] == LOCATION_MZONE ? 0 : 8));
##}

## Parameters

- `player` `int`
- `count` `int`
- `s` `int`
- `o` `int`
- `filter` `int`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5028`
