# Min/Max Stat Card Selection

Some effects do not ask the player to choose from every valid card. They first
find the card or cards with the lowest or highest value, then either affect that
tied group or ask the player to choose from the tie.

Use this pattern for text such as "the monster with the highest DEF", "the
monster with the lowest ATK", "the highest Level", or any other numeric score
that can be calculated from a Card.

## The Core Shape

Start with a candidate Group, then extract the tied extreme group.

```lua
local g=Duel.GetMatchingGroup(s.filter,tp,0,LOCATION_MZONE,nil)
if #g>0 then
    local tg,value=g:GetMaxGroup(Card.GetDefense)
    -- tg contains every candidate tied for highest DEF
    -- value is that highest DEF value
end
```

`Group.GetMinGroup` and `Group.GetMaxGroup` return two values:

| Return | Meaning |
| --- | --- |
| First return | A Group containing every card tied for the minimum or maximum score. |
| Second return | The numeric minimum or maximum score. |

If the input Group is empty, the binding returns no values. Check that the
candidate Group is non-empty before using either return.

Useful scoring functions include `Card.GetAttack`, `Card.GetDefense`,
`Card.GetBaseAttack`, `Card.GetLevel`, `Card.GetRank`, and custom functions
that return an integer.

## Non-Targeting Resolution Pattern

For a non-targeting effect, activation only proves that at least one valid
candidate exists. Resolution rebuilds the candidate Group from the current game
state and then computes the min or max again.

Local `c97169186.lua` uses this pattern for a highest-DEF destroy effect:

```lua
function s.filter(c)
    return c:IsFaceup() and c:IsDefenseAbove(0)
end

function s.target(e,tp,eg,ep,ev,re,r,rp,chk)
    if chk==0 then
        return Duel.IsExistingMatchingCard(s.filter,tp,0,LOCATION_MZONE,1,nil)
    end
    local g=Duel.GetMatchingGroup(s.filter,tp,0,LOCATION_MZONE,nil)
    local tg=g:GetMaxGroup(Card.GetDefense)
    Duel.SetOperationInfo(0,CATEGORY_DESTROY,tg,1,0,0)
end

function s.activate(e,tp,eg,ep,ev,re,r,rp)
    local g=Duel.GetMatchingGroup(s.filter,tp,0,LOCATION_MZONE,nil)
    if #g>0 then
        local tg=g:GetMaxGroup(Card.GetDefense)
        if #tg>1 then
            Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_DESTROY)
            local sg=tg:Select(tp,1,1,nil)
            Duel.HintSelection(sg)
            Duel.Destroy(sg,REASON_EFFECT)
        else
            Duel.Destroy(tg,REASON_EFFECT)
        end
    end
end
```

Notice the DEF filter. Local scripts commonly use `Card.IsDefenseAbove(0)` when
an effect cares about DEF, so monsters without a usable DEF value are not placed
in the candidate pool.

## Tie Handling

`GetMinGroup` and `GetMaxGroup` do not break ties. They return all tied cards.

| Card text / rule shape | Script action |
| --- | --- |
| "your choice, if tied" | If `#tg>1`, prompt with `Duel.Hint`, choose one with `Group.Select`, then usually show it with `Duel.HintSelection`. |
| "all monsters with the lowest/highest..." | Act on the returned tied Group directly. |
| The effect must choose a single deterministic card | Build a scoring function or filter that makes ties impossible, or copy the local script/ruling pattern for that exact card. |

Local `c96470883.lua` shows the "choose if tied" min-ATK pattern:

```lua
local tg=g:GetMinGroup(Card.GetAttack)
if tg:GetCount()>1 then
    Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_DESTROY)
    local sg=tg:Select(tp,1,1,nil)
    Duel.Destroy(sg,REASON_EFFECT)
else
    Duel.Destroy(tg,REASON_EFFECT)
end
```

When the chosen card is not an official Chain target, this selection happens at
resolution and creates a normal selected Group, not a Chain target list.

## Using The Numeric Value

Sometimes the script needs the extreme value, not the card selected by that
value.

Local `c10796448.lua` uses the opponent's highest base ATK as a continuous
value:

```lua
function s.val(e,c)
    local g=Duel.GetMatchingGroup(Card.IsFaceup,e:GetOwnerPlayer(),0,LOCATION_MZONE,nil)
    if #g==0 then
        return 0
    end
    local _,val=g:GetMaxGroup(Card.GetBaseAttack)
    return val
end
```

Local `c99075257.lua` uses the highest Level from the event group, stores that
number with `SetLabel`, then uses it during resolution:

```lua
local g=eg:Filter(s.cfilter,nil,tp)
local _,lv=g:GetMaxGroup(Card.GetLevel)
if chk==0 then
    return lv>0 and Duel.IsExistingMatchingCard(s.filter,tp,LOCATION_DECK,0,1,nil,lv)
end
e:SetLabel(lv)
```

Do not store the tied Group from activation unless the card text really needs
that exact set later and you preserve it correctly. Most effects should rebuild
the Group at resolution.

## Custom Scoring Functions

The scoring function receives the card as its first argument and must return an
integer.

```lua
function s.counter_score(c)
    return c:GetCounter(0x1)
end

local tg,ct=g:GetMaxGroup(s.counter_score)
```

The generated API signature also supports extra arguments:

```lua
function s.counter_score(c,counter_type)
    return c:GetCounter(counter_type)
end

local tg,ct=g:GetMaxGroup(s.counter_score,0x1)
```

Use a custom score when the value is not a single built-in Card getter: counters,
materials, combined ATK and DEF, or a value that depends on one argument chosen
earlier in the script.

## Targeting Variant

If the card text targets the highest or lowest candidate, the target must be
chosen at activation time. There are two local-friendly ways to do that.

| Approach | When to use |
| --- | --- |
| Build the Group manually, call `GetMinGroup`/`GetMaxGroup`, choose with `Group.Select`, then record with `Duel.SetTargetCard`. | Useful when the extreme Group is easier to compute explicitly. |
| Put the extreme check inside the target filter, then use `Duel.IsExistingTarget` and `Duel.SelectTarget`. | Useful when you want standard target APIs and a simpler `chkc` branch. |

Local `c45950291.lua` uses the filter-based targeting approach. Its candidate
filter rejects any Xyz Monster if another candidate has a higher Rank:

```lua
function s.cfilter(c,rk)
    return c:IsFaceup() and c:GetRank()>rk
end

function s.filter1(c,e,tp)
    local rk=c:GetRank()
    return c:IsFaceup() and c:IsType(TYPE_XYZ)
        and not Duel.IsExistingMatchingCard(s.cfilter,tp,LOCATION_MZONE,0,1,nil,rk)
        and Duel.IsExistingMatchingCard(s.filter2,tp,LOCATION_EXTRA,0,1,nil,e,tp,c,rk+2,c:GetRace(),c:GetAttribute(),c:GetCode())
        and aux.MustMaterialCheck(c,tp,EFFECT_MUST_BE_XMATERIAL)
end
```

Because the extreme test is inside `s.filter1`, the target function can use the
ordinary target APIs:

```lua
if chk==0 then
    return Duel.IsExistingTarget(s.filter1,tp,LOCATION_MZONE,0,1,nil,e,tp)
end
Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_TARGET)
Duel.SelectTarget(tp,s.filter1,tp,LOCATION_MZONE,0,1,1,nil,e,tp)
```

This shape can be less direct than `GetMaxGroup`, but it integrates cleanly
with `Duel.SelectTarget` and target redirection checks because every candidate
is tested by one target filter.

## Activation vs Resolution

| Moment | What to do |
| --- | --- |
| `chk==0` for non-targeting effects | Prove that at least one valid candidate exists. |
| Target callback after `chk==0` | Optionally compute the current extreme Group for `Duel.SetOperationInfo`. |
| Operation for non-targeting effects | Rebuild the candidate Group, compute the extreme Group again, handle ties, then act. |
| Target callback for targeting effects | Choose or record the official Chain target from the current extreme candidates. |
| Operation for targeting effects | Read the target back and recheck relation plus current state. |

Do not require a unique highest or lowest card in `chk==0` unless the exact card
text or local script pattern requires uniqueness. A tie is still a valid extreme
group.

## Common Mistakes

| Mistake | Safer pattern |
| --- | --- |
| Calling `GetMaxGroup` on an empty Group and using the returns immediately. | Check `#g>0` first. |
| Assuming the returned Group has one card. | Treat it as a tied Group; select from it only when the card text allows or requires a choice. |
| Computing the extreme card at activation for a non-targeting effect and acting on that old card later. | Rebuild the candidate Group during resolution. |
| Forgetting `Duel.HintSelection` after a tie choice that the opponent should see. | Prompt with `Duel.Hint`, choose with `Group.Select`, then highlight the chosen Group when local scripts do. |
| Using DEF scoring without excluding invalid DEF candidates. | Use filters such as `Card.IsDefenseAbove(0)` when the local pattern does. |
| Using `Duel.SelectTarget` directly on a manually built extreme Group. | Use `Group.Select` plus `Duel.SetTargetCard`, or move the extreme check into the target filter. |

Useful API pages:

- [`Group.GetMinGroup`](/api/functions/Group/GetMinGroup)
- [`Group.GetMaxGroup`](/api/functions/Group/GetMaxGroup)
- [`Group.Select`](/api/functions/Group/Select)
- [`Duel.GetMatchingGroup`](/api/functions/Duel/GetMatchingGroup)
- [`Duel.IsExistingMatchingCard`](/api/functions/Duel/IsExistingMatchingCard)
- [`Duel.SelectTarget`](/api/functions/Duel/SelectTarget)
- [`Duel.SetTargetCard`](/api/functions/Duel/SetTargetCard)
- [`Duel.SetOperationInfo`](/api/functions/Duel/SetOperationInfo)
- [`Duel.HintSelection`](/api/functions/Duel/HintSelection)
- [`Card.GetAttack`](/api/functions/Card/GetAttack)
- [`Card.GetDefense`](/api/functions/Card/GetDefense)
- [`Card.GetBaseAttack`](/api/functions/Card/GetBaseAttack)
- [`Card.GetLevel`](/api/functions/Card/GetLevel)
- [`Card.GetRank`](/api/functions/Card/GetRank)
