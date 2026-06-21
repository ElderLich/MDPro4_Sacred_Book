# Filters, Card Objects, and Group Objects

Filters are small functions that receive a `Card` first and return `true` or
`false`.

```lua
function s.filter(c)
  return c:IsFaceup() and c:IsSetCard(0x123)
end
```

They are used by Duel and Group functions to find cards.

```lua
local g=Duel.GetMatchingGroup(s.filter,tp,LOCATION_MZONE,0,nil)
```

## Extra Filter Arguments

Arguments after `nil` are passed to the filter after the card.

```lua
function s.atkfilter(c,atk)
  return c:IsFaceup() and c:GetAttack()>=atk
end

local g=Duel.GetMatchingGroup(s.atkfilter,tp,LOCATION_MZONE,0,nil,2000)
```

## Groups

A `Group` is a set of cards. Many scripts collect a group, filter it, select
from it, then move or apply effects to the chosen cards.

```lua
local g=Duel.GetMatchingGroup(s.filter,tp,LOCATION_MZONE,0,nil)
local sg=g:Select(tp,1,1,nil)
Duel.SendtoGrave(sg,REASON_EFFECT)
```

Useful API pages:

- [`Duel.GetMatchingGroup`](/api/functions/Duel/GetMatchingGroup)
- [`Group.Filter`](/api/functions/Group/Filter)
- [`Group.Select`](/api/functions/Group/Select)
- [`Group.GetFirst`](/api/functions/Group/GetFirst)
- [`Card.IsFaceup`](/api/functions/Card/IsFaceup)
- [`Card.IsSetCard`](/api/functions/Card/IsSetCard)
