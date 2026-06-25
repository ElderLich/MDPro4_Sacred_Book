# Group.Select

## Signature

```lua
Group.Select(Group g, int player, int min, int max, [Card|Group|nil ex]) -> Group|nil
```

## Description

Lets player choose min to max cards from g, optionally excluding ex, and returns the selected Group.
This is a plain Group choice; it does not register Chain targets or create IsRelateToEffect relations.

## How To Use It

Use this when you already built the candidate Group and only need the player to choose from it.

```lua
local g=Duel.GetMatchingGroup(s.filter,tp,LOCATION_GRAVE,0,nil)
Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_ATOHAND)
local sg=g:Select(tp,1,1,nil)
Duel.SendtoHand(sg,nil,REASON_EFFECT)
```

If you still need to filter while selecting, use `Group.FilterSelect` or `Duel.SelectMatchingCard` instead.

## Related Functions

- [Group.FilterSelect](/api/functions/Group/FilterSelect)
- [Duel.SelectMatchingCard](/api/functions/Duel/SelectMatchingCard)
- [Duel.SelectTarget](/api/functions/Duel/SelectTarget)

## Parameters

- `g` `Group` - Selectable card pool.
- `player` `int` - Player who makes the selection; invalid players make the core return no values.
- `min` `int` - Minimum number of cards to select.
- `max` `int` - Maximum number of cards to select.
- `ex` `Card|Group|nil` optional - Card or Group excluded from selectable cards; nil excludes nothing.

## Returns

- `Group|nil` - New Group containing selected cards, or nil if player is invalid.

## Source

- `D:\Programs\GitHub\ygopro-core\libgroup.cpp:915`
