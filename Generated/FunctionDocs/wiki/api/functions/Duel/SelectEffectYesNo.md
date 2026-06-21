# Duel.SelectEffectYesNo

## Signature

```lua
Duel.SelectEffectYesNo(int player, Card c, [int desc]) -> bool
```

## Description

让玩家player选择是否发动卡片c的效果[提示文字可以自行用desc替换，desc 用 aux.Stringid 获取]

## Parameters

- `player` `int`
- `c` `Card`
- `desc` `int` optional - default: 95

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5022`
