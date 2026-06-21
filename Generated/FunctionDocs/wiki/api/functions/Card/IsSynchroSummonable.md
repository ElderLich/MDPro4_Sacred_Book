# Card.IsSynchroSummonable

## Signature

```lua
Card.IsSynchroSummonable(Card c, [Card|nil tuner], [Group mg]) -> bool
```

## Description

检查是否可以以tuner作为调整，场上的卡[或mg]为同调素材对c进行同调召唤手续
如果tuner是nil，此函数与Card.IsSpecialSummonable作用相同

## Parameters

- `c` `Card`
- `tuner` `Card|nil` optional
- `mg` `Group` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3576`
