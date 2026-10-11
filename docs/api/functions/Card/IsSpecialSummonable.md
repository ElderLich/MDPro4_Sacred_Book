# Card.IsSpecialSummonable

## Signature

```lua
Card.IsSpecialSummonable(Card c, [int sum_type]) -> bool
```

## Description

Checks whether c can currently be Special Summoned by the current reason player under sum_type, defaulting to 0.
This is a broad core check. For effect resolution and activation filters, prefer Card.IsCanBeSpecialSummoned so the effect, target player, position, nocheck, nolimit, and zone match the later Duel.SpecialSummon call.

## Parameters

- `c` `Card` - Card being checked.
- `sum_type` `int` optional - Summon type value to test; default: 0.

## Returns

- `bool` - True if the core currently considers c Special Summonable under that summon type.

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3630`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
