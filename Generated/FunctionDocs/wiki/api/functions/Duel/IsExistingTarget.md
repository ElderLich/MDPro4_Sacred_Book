# Duel.IsExistingTarget

## Signature

```lua
Duel.IsExistingTarget([function|nil f], int player, int s, int o, int count, [Card|Group|nil ex], ... any) -> bool
```

## Description

Checks whether the specified locations contain at least count cards that satisfy filter f, are not excluded by ex, and can be targeted by the currently handled effect.
Use this in Target callbacks when the card must become an official effect target.

## How To Use It

Use this in a Target callback when the effect text chooses target cards.

`Duel.IsExistingTarget` is like `Duel.IsExistingMatchingCard`, but it also checks whether each candidate can become a target of the current effect. That matters for cards unaffected by targeting, cards protected by effects, and target restrictions.

```lua
function s.target(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
    if chkc then return chkc:IsOnField() and s.filter(chkc) end
    if chk==0 then
        return Duel.IsExistingTarget(s.filter,tp,LOCATION_MZONE,LOCATION_MZONE,1,nil)
    end
    Duel.SelectTarget(tp,s.filter,tp,LOCATION_MZONE,LOCATION_MZONE,1,1,nil)
end
```

## Parameters

- `f` `function|nil` optional - Filter called with each candidate card first, then any extra arguments after ex.
- `player` `int` - Viewpoint player for s and o.
- `s` `int` - Locations on player's side to search.
- `o` `int` - Locations on the opponent's side to search.
- `count` `int` - Minimum number of legal targets required.
- `ex` `Card|Group|nil` optional - Card or Group excluded from the search.
- `...` `any` - Extra values passed to f after the candidate card.

## Returns

- `bool` - True if at least count matching cards can be targeted by the current effect.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4985`
