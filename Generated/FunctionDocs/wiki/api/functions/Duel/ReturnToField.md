# Duel.ReturnToField

## Signature

```lua
Duel.ReturnToField(Card c, [int pos], [int zone]) -> bool|nil
```

## Description

Returns a card temporarily removed from the field to its previous controller and previous location.
pos defaults to the previous position and zone defaults to 0xff. If c was not removed for REASON_TEMPORARY, the binding returns no Lua value; otherwise it yields and returns whether the move succeeded.

## Parameters

- `c` `Card`
- `pos` `int` optional - default: previous position
- `zone` `int` optional - default: 0xff

## Returns

- `bool|nil` - Success flag, or nil if c was not temporarily removed from the field.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4883`
