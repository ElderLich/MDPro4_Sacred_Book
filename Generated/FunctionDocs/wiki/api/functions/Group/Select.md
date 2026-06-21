# Group.Select

## Signature

```lua
Group.Select(Group g, int player, int min, int max, [Card|Group|nil ex]) -> Group
```

## Description

Lets player choose min to max cards from g, optionally excluding ex, and returns the selected Group.

## How To Use It

Use this when you already built the candidate Group and only need the player to choose from it.

```lua
local g=Duel.GetMatchingGroup(s.filter,tp,LOCATION_GRAVE,0,nil)
Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_ATOHAND)
local sg=g:Select(tp,1,1,nil)
Duel.SendtoHand(sg,nil,REASON_EFFECT)
```

If you still need to filter while selecting, use `Group.FilterSelect` or `Duel.SelectMatchingCard` instead.

## Parameters

- `g` `Group`
- `player` `int`
- `min` `int`
- `max` `int`
- `ex` `Card|Group|nil` optional

## Returns

- `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libgroup.cpp:915`
