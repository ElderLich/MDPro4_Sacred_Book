# Duel.Release

## Signature

```lua
Duel.Release(Card|Group targets, int reason, [int reason_player]) -> int
```

## Description

Tributes/Releases targets for reason and returns the number of cards actually released.
Use REASON_COST when paying a cost and REASON_EFFECT or REASON_SPSUMMON when the release is part of an effect or Summon procedure.
Match the reason to the filter that selected the cards, such as cost-specific releasable checks for costs.

## How To Use It

Use this to Tribute/Release cards as a cost, effect, or Summon procedure.

When selecting a release cost, select cards that are legal to release, then release them with the same reason used for the cost:

```lua
local g=Duel.SelectReleaseGroupEx(tp,nil,1,1,REASON_COST,false,nil)
if #g>0 then
    Duel.Release(g,REASON_COST)
end
```

The return value is the number of cards actually released.

## Related Functions

- [Card.IsReleasable](/api/functions/Card/IsReleasable)
- [Duel.GetReleaseGroup](/api/functions/Duel/GetReleaseGroup)
- [Duel.SelectReleaseGroupEx](/api/functions/Duel/SelectReleaseGroupEx)

## Parameters

- `targets` `Card|Group`
- `reason` `int`
- `reason_player` `int` optional

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4881`
