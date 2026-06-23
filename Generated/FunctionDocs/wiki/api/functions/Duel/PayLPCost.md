# Duel.PayLPCost

## Signature

```lua
Duel.PayLPCost(int player, int cost, [bool must_pay]) -> void
```

## Description

Makes player pay the specified LP cost.
Call this only in the real Cost branch after the chk==0 branch has used Duel.CheckLPCost or an equivalent legality check.

## Parameters

- `player` `int` - Player who pays the LP cost.
- `cost` `int` - LP amount to pay.
- `must_pay` `bool` optional - Passed through to the core LP-cost payment processor.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4909`
