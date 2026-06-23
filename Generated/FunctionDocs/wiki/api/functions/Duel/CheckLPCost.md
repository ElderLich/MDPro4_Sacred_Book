# Duel.CheckLPCost

## Signature

```lua
Duel.CheckLPCost(int player, int cost, [bool must_pay]) -> bool|nil
```

## Description

Checks whether player can pay the specified LP cost without paying it.
Use this in a Cost callback's chk==0 branch. The core returns false for nonpositive costs, and the optional must_pay flag is passed to the LP-cost check.

## Parameters

- `player` `int` - Player checked for payment ability.
- `cost` `int` - LP amount to check; values of 0 or less return false.
- `must_pay` `bool` optional - Passed through to the core LP-cost check; scripts use true when the player must be able to pay that exact amount.

## Returns

- `bool|nil` - True if the LP cost can be paid; false if it cannot or cost is nonpositive; nil if player is invalid.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4908`
