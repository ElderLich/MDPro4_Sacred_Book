# Card.CheckActivateEffect

## Signature

```lua
Card.CheckActivateEffect(Card c, bool neglect_con, bool neglect_cost, bool copy_info) -> Effect,Group|nil,int|nil,int|nil,Effect|nil,int|nil,int|nil
```

## Description

Return to the timing of the launch of the correct c "card launch" effect, ignored_con = true ignoring the launch conditions, ignored_cost = true ignoring the launch cost
Copy_info = false or the free-time effect only returns the effect
Otherwise return the effect of the time point for the code when the trigger point information eg, ep, ev, re, r, rp

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
