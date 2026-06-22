# Duel.GetMatchingGroup

## Signature

```lua
Duel.GetMatchingGroup([function|nil f], int player, int s, int o, [Card|Group|nil ex], ... any) -> Group
```

## Description

Returns a Group containing cards from the specified locations that satisfy filter f and are not excluded by ex.
s is player's own location mask and o is the opponent's location mask from that player's viewpoint. Extra arguments after ex are passed to f.

## How To Use It

Use this when you need to keep or further process all matching cards rather than only checking if they exist.

`s` and `o` are location masks from `player`'s point of view. For example, `LOCATION_MZONE,0` means that player's Monster Zone, while `0,LOCATION_MZONE` means the opponent's Monster Zone.

```lua
local g=Duel.GetMatchingGroup(s.filter,tp,LOCATION_MZONE,LOCATION_MZONE,nil)
if #g>0 then
    Duel.HintSelection(g)
end
```

## Parameters

- `f` `function|nil` optional - Filter callback; nil accepts cards that pass location and exclusion checks.
- `player` `int` - Reference player for the s and o location masks.
- `s` `int` - Location mask on player's side.
- `o` `int` - Location mask on the opponent's side from player's viewpoint.
- `ex` `Card|Group|nil` optional - Card or Group excluded from the result; nil excludes nothing.
- `...` `any` - Extra values forwarded to f after the candidate Card.

## Returns

- `Group` - New Group containing every matching card.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4969`
