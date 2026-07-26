# Card.IsXyzSummonable

## Signature

```lua
Card.IsXyzSummonable(Card c, [Group|nil materials], [int minc], [int maxc]) -> bool
```

## Description

Checks whether Xyz Monster c can be Xyz Summoned by the current reason player with an optional material group and min/max constraints.
Use this in effect target and operation branches before calling Duel.XyzSummon. minc and maxc default to 0 when omitted, leaving the registered procedure's own count rules in control.
The core rejects this check during the Damage Step.

## Parameters

- `c` `Card` - Xyz Monster being tested.
- `materials` `Group|nil` optional - Optional material pool or exact material group supplied by the effect.
- `minc` `int` optional - Optional minimum material count override. Defaults to 0.
- `maxc` `int` optional - Optional maximum material count override. Defaults to 0.

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3580`
