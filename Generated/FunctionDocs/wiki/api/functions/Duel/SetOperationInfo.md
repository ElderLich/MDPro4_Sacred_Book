# Duel.SetOperationInfo

## Signature

```lua
Duel.SetOperationInfo(int chainc, int category, Card|Group|nil targets, int count, int player, int param) -> void
```

## Description

Records operation information for category on chainc.
Use concrete targets and count when the affected cards are known. For unresolved non-targeting movement effects, pass nil targets with the expected count, target player, and target location.
For LP effects, target_player is the affected player and target_param is the amount. This information announces intent; it does not perform the operation or create official card targets.

## How To Use It

Call this in the Target callback when the Chain Link can announce a category, affected cards or players, count, amount, or source location.

Known targets can be passed directly:

```lua
local g=Duel.SelectTarget(tp,s.filter,tp,0,LOCATION_ONFIELD,1,1,nil)
Duel.SetOperationInfo(0,CATEGORY_DESTROY,g,1,0,0)
```

For unresolved movement from a location, pass `nil` for targets and use `target_player` plus `target_param` as the location or amount:

```lua
Duel.SetOperationInfo(0,CATEGORY_TOHAND,nil,1,tp,LOCATION_DECK)
Duel.SetOperationInfo(0,CATEGORY_DAMAGE,nil,0,1-tp,800)
```

This announces intent; the operation still has to recheck legality and perform the actual action.

## Related Functions

- [Effect.SetCategory](/api/functions/Effect/SetCategory)
- [Duel.GetOperationInfo](/api/functions/Duel/GetOperationInfo)
- [Duel.SetTargetPlayer](/api/functions/Duel/SetTargetPlayer)
- [Duel.SetTargetParam](/api/functions/Duel/SetTargetParam)

## Parameters

- `chainc` `int` - Chain index/count passed to the core chain lookup; scripts commonly use 0 for the current Chain Link.
- `category` `int` - CATEGORY_* operation category to record.
- `targets` `Card|Group|nil` - Known affected cards. Card or Group values are cloned into a read-only Group; nil records only count, player, and param.
- `count` `int` - Expected number of affected cards.
- `player` `int` - Target player stored in the operation info.
- `param` `int` - Category-specific value, commonly a destination location, amount, or other operation parameter.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5008`
