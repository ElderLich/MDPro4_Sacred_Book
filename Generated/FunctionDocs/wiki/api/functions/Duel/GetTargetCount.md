# Duel.GetTargetCount

## Signature

```lua
Duel.GetTargetCount([function|nil f], int player, int s, int o, [Card|Group|nil ex], ... any) -> int
```

## Description

基本同Duel.GetMatchingGroupCount ，不同之处在于需要追加判定卡片是否能成为当前正在处理的效果的对象

## Parameters

- `f` `function|nil` optional
- `player` `int`
- `s` `int`
- `o` `int`
- `ex` `Card|Group|nil` optional
- `...` `any`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4984`
