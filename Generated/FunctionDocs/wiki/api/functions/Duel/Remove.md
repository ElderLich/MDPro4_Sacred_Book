# Duel.Remove

## Signature

```lua
Duel.Remove(Card|Group targets, int pos, int reason, [int reason_player]) -> int
```

## Description

In the case of reason, except for the pos form, the return value is the actual number being manipulated
If the reason contains REASON_TEMPORARY, then the exception is considered temporary, you can return to the field by Duel.ReturnToField

## Parameters

- `targets` `Card|Group`
- `pos` `int`
- `reason` `int`
- `reason_player` `int` optional

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4859`
