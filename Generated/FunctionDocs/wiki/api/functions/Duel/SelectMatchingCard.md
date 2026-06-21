# Duel.SelectMatchingCard

## Signature

```lua
Duel.SelectMatchingCard(int sel_player, [function|nil f], int player, int s, int o, int min, int max, [Card|Group|nil ex], ... any) -> Group
```

## Description

Lets sel_player choose min to max cards from the specified locations that satisfy filter f and are not excluded by ex.
s is player's own location mask and o is the opponent's location mask from that player's viewpoint. Extra arguments after ex are passed to f.

## How To Use It

Use this when the selected cards do not need to become official effect targets.

A common pattern is to check with `Duel.IsExistingMatchingCard`, select with `Duel.SelectMatchingCard`, then move or modify the selected group during the operation:

```lua
local g=Duel.SelectMatchingCard(tp,s.filter,tp,LOCATION_GRAVE,0,1,1,nil,e,tp)
if #g>0 then
    Duel.SpecialSummon(g,0,tp,tp,false,false,POS_FACEUP)
end
```

Use `Duel.SelectTarget` in a Target callback when later resolution must re-check `tc:IsRelateToEffect(e)`.

## Parameters

- `sel_player` `int`
- `f` `function|nil` optional
- `player` `int`
- `s` `int`
- `o` `int`
- `min` `int`
- `max` `int`
- `ex` `Card|Group|nil` optional
- `...` `any`

## Returns

- `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4973`
