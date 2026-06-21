# Card.CheckActivateEffect

## Signature

```lua
Card.CheckActivateEffect(Card c, bool neglect_con, bool neglect_cost, bool copy_info) -> Effect,Group|nil,int|nil,int|nil,Effect|nil,int|nil,int|nil
```

## Description

返回c的可以发动时机正确的“卡的发动”的效果，neglect_con=true则无视发动条件，neglect_cost=true则无视发动cost
copy_info=false或者自由时点的效果则只返回这个效果 e
否则还返回这个效果的触发时点的信息 e,eg,ep,ev,re,r,rp

## Parameters

- `c` `Card`
- `neglect_con` `bool`
- `neglect_cost` `bool`
- `copy_info` `bool`

## Returns

- `Effect`
- `Group|nil`
- `int|nil`
- `int|nil`
- `Effect|nil`
- `int|nil`
- `int|nil`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3545`
