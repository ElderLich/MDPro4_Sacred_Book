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

## Filter Shape

A filter should answer one question clearly: "does this card count?"

```lua
function s.spfilter(c,e,tp)
    return c:IsLevelBelow(4)
        and c:IsCanBeSpecialSummoned(e,0,tp,false,false)
end
```

The first argument is always the candidate card. Extra arguments after the
excluded card/group are passed to the filter after that card.

```lua
local g=Duel.GetMatchingGroup(s.spfilter,tp,LOCATION_GRAVE,0,nil,e,tp)
```

Here each filter call receives `c,e,tp`.

## The Excluded Card or Group

Many APIs include an `ex` argument. It can be `nil`, one `Card`, or sometimes a
`Group`. Matching cards equal to `ex` are skipped.

```lua
local g=Duel.GetMatchingGroup(s.filter,tp,LOCATION_MZONE,0,e:GetHandler())
```

Use this when a card should not select itself, or when an already selected group
should be excluded from a later selection.

## Matching vs Targeting

Targeting is not only "selecting a card". It registers the selected cards as
the Chain's official targets.

| Need | Use |
| --- | --- |
| Check whether matching cards exist. | `Duel.IsExistingMatchingCard` |
| Select non-targeting cards. | `Duel.SelectMatchingCard` |
| Check whether targetable cards exist. | `Duel.IsExistingTarget` |
| Select official targets. | `Duel.SelectTarget` |

If the card text targets, use target functions and check relation during
resolution.

## Groups

A `Group` is a set of cards. Many scripts collect a group, filter it, select
from it, then move or apply effects to the chosen cards.

```lua
local g=Duel.GetMatchingGroup(s.filter,tp,LOCATION_MZONE,0,nil)
if #g>0 then
    Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_TOGRAVE)
    local sg=g:Select(tp,1,1,nil)
    Duel.SendtoGrave(sg,REASON_EFFECT)
end
```

Use `#g` or `g:GetCount()` when you only need the count.

## Filtering a Group

When you already have a group, use `Group.Filter` to make a smaller one.

```lua
local tg=Duel.GetChainInfo(0,CHAININFO_TARGET_CARDS)
local rg=tg:Filter(Card.IsRelateToEffect,nil,e)
```

This pattern is common when a multi-target operation needs only the targets
still related to the resolving effect.

## Iterating a Group

Use `aux.Next(g)` when you need to process each card.

```lua
for tc in aux.Next(g) do
    tc:RegisterFlagEffect(id,RESET_EVENT+RESETS_STANDARD,0,1)
end
```

For older-style iteration, use `GetFirst` and `GetNext`.

```lua
local tc=g:GetFirst()
while tc do
    -- work with tc
    tc=g:GetNext()
end
```

Useful API pages:

- [`Duel.GetMatchingGroup`](/api/functions/Duel/GetMatchingGroup)
- [`Duel.IsExistingMatchingCard`](/api/functions/Duel/IsExistingMatchingCard)
- [`Duel.SelectMatchingCard`](/api/functions/Duel/SelectMatchingCard)
- [`Duel.IsExistingTarget`](/api/functions/Duel/IsExistingTarget)
- [`Duel.SelectTarget`](/api/functions/Duel/SelectTarget)
- [`Group.Filter`](/api/functions/Group/Filter)
- [`Group.Select`](/api/functions/Group/Select)
- [`Group.GetFirst`](/api/functions/Group/GetFirst)
