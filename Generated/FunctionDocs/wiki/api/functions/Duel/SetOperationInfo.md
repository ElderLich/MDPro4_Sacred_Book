# Duel.SetOperationInfo

## Signature

```lua
Duel.SetOperationInfo(int chainc, int category, Card|Group|nil targets, int count, int player, int param) -> void
```

## Description

Records operation information for category on chainc.
Use concrete targets and count when the affected cards are known. For unresolved non-targeting movement effects, pass nil targets with the expected count, target player, and target location.
This information is used by response checks such as Stardust Dragon-style effects.

## Parameters

- `chainc` `int` - Chain index/count passed to the core chain lookup; scripts commonly use 0 for the current Chain Link.
- `category` `int` - CATEGORY_* operation category to record.
- `targets` `Card|Group|nil` - Known affected cards. Card or Group values are cloned into a read-only Group; nil records only count, player, and param.
- `count` `int` - Expected number of affected cards.
- `player` `int` - Target player stored in the operation info.
- `param` `int` - Category-specific value, commonly a destination location, amount, or other operation parameter.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5008`
