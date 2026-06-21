# Duel.GetLocationCount

## Signature

```lua
Duel.GetLocationCount(int player, int location, [int use_player], [int reason], [int zone]) -> int
```

## Description

返回玩家player的场上location可用的[区域 zone 里的]空格数
location只能是LOCATION_MZONE或者LOCATION_SZONE
reason为LOCATION_REASON_TOFIELD或LOCATION_REASON_CONTROL
##第三个第四个额外参数与凯撒斗技场等限制格子的效果有关

## Parameters

- `player` `int`
- `location` `int`
- `use_player` `int` optional
- `reason` `int` optional
- `zone` `int` optional - default: 0xff

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4935`
