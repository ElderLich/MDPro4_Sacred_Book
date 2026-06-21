# Duel.IsExistingTarget

## Signature

```lua
Duel.IsExistingTarget([function|nil f], int player, int s, int o, int count, [Card|Group|nil ex], ... any) -> bool
```

## Description

基本同Duel.IsExistingMatchingCard ，不同之处在于需要追加判定卡片是否能成为当前正在处理的效果的对象

## Parameters

- `f` `function|nil` optional
- `player` `int`
- `s` `int`
- `o` `int`
- `count` `int`
- `ex` `Card|Group|nil` optional
- `...` `any`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4985`
