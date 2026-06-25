# Duel.SelectTarget

## Signature

```lua
Duel.SelectTarget(int sel_player, [function|nil f], int player, int s, int o, int min, int max, [Card|Group|nil ex], ... any) -> Group
```

## Description

Lets sel_player choose min to max cards that satisfy filter f, are not excluded by ex, and can be targeted by the currently handled effect.
The selected cards are registered as the current Chain's target cards. For non-continuous effects, the core also creates Chain relations used by IsRelateToEffect and related helpers.
This requires a current Chain; use Duel.SelectMatchingCard or Group.Select for ordinary resolution choices.

## How To Use It

Use this in the Target callback of an activated effect that targets cards.

The selected cards are saved as the Chain's targets. This function needs a current Chain; use `Duel.SelectMatchingCard` or `Group.Select` for ordinary resolution choices.
For one target, read it with `Duel.GetFirstTarget` and check `tc:IsRelateToEffect(e)` before applying the effect.
For several targets, use `Duel.GetTargetsRelateToChain` to get the target group that is still related to the resolving Chain.

```lua
function s.target(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
    if chkc then return chkc:IsOnField() and s.filter(chkc) end
    if chk==0 then return Duel.IsExistingTarget(s.filter,tp,LOCATION_MZONE,0,1,nil) end
    Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_TARGET)
    Duel.SelectTarget(tp,s.filter,tp,LOCATION_MZONE,0,1,1,nil)
end

function s.operation(e,tp,eg,ep,ev,re,r,rp)
    local tc=Duel.GetFirstTarget()
    if tc and tc:IsRelateToEffect(e) then
        Duel.Destroy(tc,REASON_EFFECT)
    end
end
```

## Related Functions

- [Duel.IsExistingTarget](/api/functions/Duel/IsExistingTarget)
- [Duel.GetFirstTarget](/api/functions/Duel/GetFirstTarget)
- [Duel.GetTargetsRelateToChain](/api/functions/Duel/GetTargetsRelateToChain)

## Parameters

- `sel_player` `int` - Player who makes the selection.
- `f` `function|nil` optional - Filter called with each candidate card first, then any extra arguments after ex.
- `player` `int` - Viewpoint player for s and o.
- `s` `int` - Locations on player's side to search.
- `o` `int` - Locations on the opponent's side to search.
- `min` `int` - Minimum number of cards to select.
- `max` `int` - Maximum number of cards to select.
- `ex` `Card|Group|nil` optional - Card or Group excluded from the selection.
- `...` `any` - Extra values passed to f after the candidate card.

## Returns

- `Group` - Group of cards selected by sel_player and registered as current Chain targets. If there is no current Chain or sel_player is invalid, the core returns no value.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4986`
