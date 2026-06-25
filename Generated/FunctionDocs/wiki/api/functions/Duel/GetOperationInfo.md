# Duel.GetOperationInfo

## Signature

```lua
Duel.GetOperationInfo(int chainc, int category) -> bool,Group|nil,int|nil,int|nil,int|nil
```

## Description

Returns operation information recorded for category on chainc.
The first return value is false when that category is not recorded. Otherwise, the remaining values correspond to Duel.SetOperationInfo: targets, count, target_player, and target_param.
Use this in response checks that need to inspect what a Chain Link announced, such as whether it is expected to destroy cards, move cards from a location, or change LP.

## How To Use It

Use this in response checks or follow-up operations that need to read what a Chain Link announced with `Duel.SetOperationInfo`.

```lua
local ex,g,ct,p,loc=Duel.GetOperationInfo(ev,CATEGORY_TOHAND)
if ex and bit.band(loc or 0,LOCATION_DECK)~=0 then
    -- the Chain Link announced adding from the Deck
end
```

The first return value is false when that category was not recorded. The remaining values mirror the `targets`, `count`, `target_player`, and `target_param` arguments.

## Related Functions

- [Duel.SetOperationInfo](/api/functions/Duel/SetOperationInfo)
- [Effect.SetCategory](/api/functions/Effect/SetCategory)
- [Duel.GetChainInfo](/api/functions/Duel/GetChainInfo)

## Parameters

- `chainc` `int` - Chain Link number to inspect. Use 0 for the current Chain Link.
- `category` `int` - CATEGORY_* flag whose operation info should be read.

## Returns

- `bool` - true if operation info for category exists; false if not.
- `Group|nil` - Recorded target cards, or nil when only count/player/param were recorded.
- `int|nil` - Recorded expected count.
- `int|nil` - Recorded target player.
- `int|nil` - Recorded category-specific parameter, often a location or amount.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5009`
