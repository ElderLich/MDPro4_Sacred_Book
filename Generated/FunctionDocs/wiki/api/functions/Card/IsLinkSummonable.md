# Card.IsLinkSummonable

## Signature

```lua
Card.IsLinkSummonable(Card c, Group|nil materials, [Card|nil lcard], [int minc], [int maxc]) -> bool
```

## Description

Checks whether Link Monster c can be Link Summoned by the current reason player.
Optional materials, lcard, minc, and maxc restrict the Link Material pool and material count used by the core check.
Use this in effect target and operation branches before calling Duel.LinkSummon. minc and maxc default to 0 when omitted, leaving the registered procedure's own count rules in control.
The core rejects this check during the Damage Step.

## Parameters

- `c` `Card` - Link Monster being tested.
- `materials` `Group|nil` - Optional temporary material pool. nil lets the registered procedure collect its normal pool.
- `lcard` `Card|nil` optional - Optional fixed material that the final selected group must include.
- `minc` `int` optional - Runtime minimum material-card count. default: 0
- `maxc` `int` optional - Runtime maximum material-card count. default: 0

## Returns

- `bool` - true if c has a legal Link Summon under the supplied temporary limits.

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3578`
