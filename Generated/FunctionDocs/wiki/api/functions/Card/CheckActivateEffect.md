# Card.CheckActivateEffect

## Signature

```lua
Card.CheckActivateEffect(Card c, bool neglect_con, bool neglect_cost, bool copy_info) -> Effect,Group|nil,int|nil,int|nil,Effect|nil,int|nil,int|nil
```

## Description

Checks whether c has an activation effect that can currently be activated.
If neglect_con is true, condition checks are skipped. If neglect_cost is true, cost checks are skipped.
When copy_info is true, the returned values include the triggering event information: eg, ep, ev, re, r, and rp.

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
