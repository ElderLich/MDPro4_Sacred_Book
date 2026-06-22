# Duel.SelectMatchingCard

## Signature

```lua
Duel.SelectMatchingCard(int sel_player, [function|nil f], int player, int s, int o, int min, int max, [Card|Group|nil ex], ... any) -> Group|nil
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

- `sel_player` `int` - Player who makes the selection; invalid players make the core return no values.
- `f` `function|nil` optional - Filter callback; nil accepts cards that pass location and exclusion checks.
- `player` `int` - Reference player for the s and o location masks.
- `s` `int` - Location mask on player's side.
- `o` `int` - Location mask on the opponent's side from player's viewpoint.
- `min` `int` - Minimum number of cards to select.
- `max` `int` - Maximum number of cards to select.
- `ex` `Card|Group|nil` optional - Card or Group excluded from selectable cards; nil excludes nothing.
- `...` `any` - Extra values forwarded to f after the candidate Card.

## Returns

- `Group|nil` - New Group containing the selected cards, or nil if sel_player is invalid.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4973`
