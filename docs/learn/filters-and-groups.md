# Filters, Card Objects, and Group Objects

Most card scripts spend a lot of time answering one question: "which cards
count?" Filters, `Card` objects, and `Group` objects are the normal tools for
that job.

## Filter Shape

A filter is a Lua function that receives a candidate `Card` first and returns
`true` or `false`.

```lua
function s.filter(c)
    return c:IsFaceup() and c:IsSetCard(0x123)
end
```

Keep a filter focused. It should describe one rule clearly: face-up monsters,
cards that can be sent to the GY, cards in a Set, monsters that can be Special
Summoned, and so on.

## Predefined Functions As Filters

Many `Card.*` functions can be passed directly when they already answer the
question you need.

```lua
Duel.IsExistingMatchingCard(Card.IsFaceup,tp,LOCATION_MZONE,0,1,nil)
```

Extra arguments work the same way as custom filters.

```lua
local p=Duel.GetTurnPlayer()
Duel.IsExistingMatchingCard(Card.IsControler,tp,LOCATION_ONFIELD,LOCATION_ONFIELD,1,nil,p)
```

Each candidate card becomes the first argument to `Card.IsControler`, and `p`
is passed after it.

## Passing Extra Arguments

Many Duel and Group functions pass extra arguments to the filter after the
candidate card.

```lua
function s.spfilter(c,e,tp)
    return c:IsLevelBelow(4)
        and c:IsCanBeSpecialSummoned(e,0,tp,false,false)
end

local g=Duel.GetMatchingGroup(s.spfilter,tp,LOCATION_GRAVE,0,nil,e,tp)
```

Here each filter call receives `c,e,tp`. The `nil` before `e,tp` is the
excluded card or group.

## Signature Map

Most filter APIs have the same mental shape:

```lua
API(filter, player, location1, location2, min_or_count, excluded, extra...)
```

The API chooses each candidate card and calls:

```lua
filter(candidate, extra...)
```

That means the first argument in your filter is always the candidate card, not
the activating effect or the player. Pass `e`, `tp`, archetype codes, levels,
or other comparison data after the excluded argument.

```lua
function s.thfilter(c,setcode)
    return c:IsSetCard(setcode) and c:IsAbleToHand()
end

Duel.IsExistingMatchingCard(s.thfilter,tp,LOCATION_GRAVE,0,1,nil,0x123)
```

This is also why direct `Card.*` functions work as filters when their argument
order already matches the question.

## The Excluded Card Or Group

Matching APIs commonly include an `ex` argument. It can be `nil`, a `Card`, or
in some APIs a `Group`. Matching candidates equal to the excluded card/group
are skipped.

```lua
local g=Duel.GetMatchingGroup(s.filter,tp,LOCATION_MZONE,0,e:GetHandler())
```

Use this when the handler should not select itself, or when a later selection
must exclude cards already chosen.

## Finding vs Selecting

Checking whether cards exist and selecting cards are separate actions.

| Need | Common API |
| --- | --- |
| Check non-targeting cards. | `Duel.IsExistingMatchingCard` |
| Select non-targeting cards. | `Duel.SelectMatchingCard` |
| Check official effect targets. | `Duel.IsExistingTarget` |
| Select official effect targets. | `Duel.SelectTarget` |
| Collect every matching card into a Group. | `Duel.GetMatchingGroup` |

The difference matters. If the card text targets, use target functions. If it
does not target, selection often happens during resolution with matching-card
functions.

## Which Selector Should I Reach For?

Use this quick rule before writing the callback:

| Text or script need | Check with | Select with |
| --- | --- | --- |
| The card text says "target". | `Duel.IsExistingTarget` | `Duel.SelectTarget` |
| The effect chooses cards during resolution. | `Duel.IsExistingMatchingCard` | `Duel.SelectMatchingCard` |
| You already collected a candidate Group. | `Group.IsExists` or `#g` | `Group.Select` or `Group.FilterSelect` |
| You need all matching cards, not player choice. | `Duel.GetMatchingGroupCount` | `Duel.GetMatchingGroup` |

Do not use `Duel.SelectTarget` just because a player chooses a card. In script
terms, targeting is a specific activation-time promise stored on the Chain
Link.

## Targeting Flow

Targeting callbacks usually include both a `chkc` branch and a `chk==0` branch.

```lua
function s.target(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
    if chkc then
        return chkc:IsControler(tp) and chkc:IsLocation(LOCATION_MZONE)
            and s.filter(chkc)
    end
    if chk==0 then
        return Duel.IsExistingTarget(s.filter,tp,LOCATION_MZONE,0,1,nil)
    end
    Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_TARGET)
    Duel.SelectTarget(tp,s.filter,tp,LOCATION_MZONE,0,1,1,nil)
end
```

`chkc` tells the client whether a manually chosen card is legal. The `chk==0`
branch only proves that at least one legal target exists. The real activation
branch selects the target.

## Groups Are Containers

A `Group` is a collection of cards. It is not a single card.

```lua
local g=Duel.GetMatchingGroup(s.filter,tp,LOCATION_MZONE,0,nil)
if #g>0 then
    Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_TOGRAVE)
    local sg=g:Select(tp,1,1,nil)
    Duel.SendtoGrave(sg,REASON_EFFECT)
end
```

Use `#g` or `g:GetCount()` when you only need the number of cards.

Do not call `Card` methods on a Group.

```lua
local g=Duel.SelectMatchingCard(tp,s.filter,tp,LOCATION_MZONE,0,1,1,nil)
-- Wrong: g:IsAttribute(ATTRIBUTE_DARK)
local tc=g:GetFirst()
if tc and tc:IsAttribute(ATTRIBUTE_DARK) then
    -- work with the card
end
```

If a script reports an error like "attempt to call a nil value" on a card
method, check whether the variable is actually a Group.

## Getting Cards From A Group

When the group is known to contain one selected card, `GetFirst` is common.

```lua
local tc=g:GetFirst()
if tc then
    Duel.SendtoHand(tc,nil,REASON_EFFECT)
end
```

When you need to process every card, use `aux.Next(g)` in modern scripts.

```lua
for tc in aux.Next(g) do
    tc:RegisterFlagEffect(id,RESET_EVENT+RESETS_STANDARD,0,1)
end
```

Older local scripts often use `GetFirst` and `GetNext`.

```lua
local tc=g:GetFirst()
while tc do
    -- work with tc
    tc=g:GetNext()
end
```

Both patterns read cards from a Group; they do not create new selections by
themselves.

For a Group that contains exactly two cards, `GetFirst` and `GetNext` can split
them into two variables.

```lua
local c1=g:GetFirst()
local c2=g:GetNext()
if c1 and c1:IsControler(1-tp) then
    c1,c2=c2,c1
end
```

That swap pattern is useful when the two cards need stable roles, such as "my
card" and "opponent's card."

Local scripts also use two-card Groups for stricter paired checks. In
`c99742859.lua`, the script first tests whether a candidate group has two cards
with different race, attribute, and Level values, then splits the selected
group:

```lua
function s.spcheck(g)
    return #g==2
        and g:GetClassCount(Card.GetRace)==2
        and g:GetClassCount(Card.GetAttribute)==2
        and g:GetClassCount(Card.GetLevel)==2
end

local sg=g:SelectSubGroup(tp,s.spcheck,false,2,2)
if sg then
    local tc1=sg:GetFirst()
    local tc2=sg:GetNext()
    Duel.SpecialSummonStep(tc1,0,tp,tp,false,false,POS_FACEUP)
    Duel.SpecialSummonStep(tc2,0,tp,tp,false,false,POS_FACEDOWN_DEFENSE)
    Duel.SpecialSummonComplete()
end
```

That is a good pattern when "choose two cards that satisfy a relationship"
cannot be expressed by a one-card filter alone.

## Filtering A Group

If you already have a Group, filter it instead of scanning the field again.

```lua
local tg=Duel.GetChainInfo(0,CHAININFO_TARGET_CARDS)
local rg=tg:Filter(Card.IsRelateToEffect,nil,e)
```

This is a common resolution pattern: keep only targets still related to the
resolving effect, then apply the operation to that smaller Group.

`Group.FilterSelect` combines filtering and player selection.

```lua
local sg=g:FilterSelect(tp,Card.IsAbleToGrave,1,1,nil)
```

Use it when the candidate pool is already in a Group.

`Group.Filter` returns a new Group. `Group.FilterSelect` asks the player to
choose from the filtered result.

```lua
local faceup=g:Filter(Card.IsFaceup,nil)
local sendable=faceup:Filter(Card.IsAbleToGrave,nil)
```

```lua
local sg=g:FilterSelect(tp,Card.IsAbleToGrave,1,1,nil)
```

If the effect moves every card that still qualifies, filter. If the player
chooses some of them, filter-select or select from the filtered Group.

## Other Ways To Create Groups

`Duel.GetMatchingGroup` uses a filter while collecting the cards.

```lua
local g=Duel.GetMatchingGroup(Card.IsFaceup,tp,LOCATION_MZONE,0,nil)
```

`Duel.GetFieldGroup` collects all cards in locations without a filter.

```lua
local g=Duel.GetFieldGroup(tp,LOCATION_ONFIELD,0)
local faceup=g:Filter(Card.IsFaceup,nil)
```

Use `GetFieldGroup` when the starting pool is "everything in these locations."
Use `GetMatchingGroup` when the filter is part of the collection itself.

## Checking A Group

`Group.IsExists` asks whether at least a number of cards in the Group match a
filter.

```lua
if g:IsExists(Card.IsRace,1,nil,RACE_DRAGON) then
    -- at least one Dragon is in the Group
end
```

`Group.IsContains` asks whether a specific card is in the Group.

```lua
if c:GetEquipGroup():IsContains(e:GetHandler()) then
    -- this card is among the equipped cards
end
```

Use `IsExists` for a rule and `IsContains` for membership of a known card.

## Checking Or Selecting Subgroups

Some effects need a valid set, not just valid individual cards: two monsters
with different names, monsters whose Levels add up, or multiple cards with
different races. Use subgroup helpers for those.

```lua
function s.diffcheck(g)
    return #g==2 and g:GetClassCount(Card.GetCode)==2
end

if g:CheckSubGroup(s.diffcheck,2,2) then
    local sg=g:SelectSubGroup(tp,s.diffcheck,false,2,2)
end
```

`CheckSubGroup` belongs in activation legality. `SelectSubGroup` belongs where
the player actually chooses. If the chosen Group must survive until a delayed
operation, call `KeepAlive` and later `DeleteGroup`; see
[Creation, building, and registration of an effect object](effect-object).

## Counting

Use the count helper that matches the data you have.

| Data you have | Count pattern |
| --- | --- |
| A Group | `#g` or `g:GetCount()` |
| A filtered Group | `g:Filter(...):GetCount()` |
| Cards in field locations | `Duel.GetMatchingGroupCount(...)` |
| Cards in a simple location | `Duel.GetFieldGroupCount(player,loc1,loc2)` |

Other count helpers, such as `Group.FilterCount` and class-count helpers, are
useful when the Group already exists and the count depends on a filter or on
distinct values. Prefer the most direct API for the question you are asking.

Do not build a Group just to count cards if a count API already answers the
question.

## A Practical Selection Pattern

This complete flow checks for a card in the GY, selects it, then sends it to
the hand.

```lua
function s.thfilter(c)
    return c:IsSetCard(0x123) and c:IsAbleToHand()
end

function s.thtg(e,tp,eg,ep,ev,re,r,rp,chk)
    if chk==0 then
        return Duel.IsExistingMatchingCard(s.thfilter,tp,LOCATION_GRAVE,0,1,nil)
    end
    Duel.SetOperationInfo(0,CATEGORY_TOHAND,nil,1,tp,LOCATION_GRAVE)
end

function s.thop(e,tp,eg,ep,ev,re,r,rp)
    Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_ATOHAND)
    local g=Duel.SelectMatchingCard(tp,s.thfilter,tp,LOCATION_GRAVE,0,1,1,nil)
    if #g>0 then
        Duel.SendtoHand(g,nil,REASON_EFFECT)
        Duel.ConfirmCards(1-tp,g)
    end
end
```

Because this example does not target, the selected card is chosen during
resolution.

Useful API pages:

- [`Duel.GetMatchingGroup`](/api/functions/Duel/GetMatchingGroup)
- [`Duel.IsExistingMatchingCard`](/api/functions/Duel/IsExistingMatchingCard)
- [`Duel.SelectMatchingCard`](/api/functions/Duel/SelectMatchingCard)
- [`Duel.IsExistingTarget`](/api/functions/Duel/IsExistingTarget)
- [`Duel.SelectTarget`](/api/functions/Duel/SelectTarget)
- [`Group.Filter`](/api/functions/Group/Filter)
- [`Group.FilterSelect`](/api/functions/Group/FilterSelect)
- [`Group.FilterCount`](/api/functions/Group/FilterCount)
- [`Group.GetClassCount`](/api/functions/Group/GetClassCount)
- [`Group.CheckSubGroup`](/api/functions/Group/CheckSubGroup)
- [`Group.SelectSubGroup`](/api/functions/Group/SelectSubGroup)
- [`Group.Select`](/api/functions/Group/Select)
- [`Group.IsExists`](/api/functions/Group/IsExists)
- [`Group.IsContains`](/api/functions/Group/IsContains)
- [`Group.GetFirst`](/api/functions/Group/GetFirst)
- [`Group.GetNext`](/api/functions/Group/GetNext)
