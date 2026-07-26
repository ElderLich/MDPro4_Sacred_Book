# Card.CheckActivateEffect

## Signature

```lua
Card.CheckActivateEffect(Card c, bool neglect_con, bool neglect_cost, bool copy_info) -> Effect|nil,Group|nil,int|nil,int|nil,Effect|nil,int|nil,int|nil
```

## Description

Checks whether c has an activation effect that can currently be activated.
If neglect_con is true, condition checks are skipped. If neglect_cost is true, cost checks are skipped.
When copy_info is true and the matching activation is not a free-chain activation, the returned values include the triggering event information: eg, ep, ev, re, r, and rp.
Returns no Lua values when no activation effect is currently usable, so local scripts usually compare the first result with nil.

## Parameters

- `c` `Card`
- `neglect_con` `bool` - true to skip the activation effect's condition check.
- `neglect_cost` `bool` - true to skip the activation effect's cost check.
- `copy_info` `bool` - true to copy triggering-event information for non-free-chain activations.

## Returns

- `Effect|nil` - The usable activation effect, or nil/no value if none is currently usable.
- `Group|nil` - eg when copy_info returns event data.
- `int|nil` - ep when copy_info returns event data.
- `int|nil` - ev when copy_info returns event data.
- `Effect|nil` - re when copy_info returns event data.
- `int|nil` - r when copy_info returns event data.
- `int|nil` - rp when copy_info returns event data.

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3548`
