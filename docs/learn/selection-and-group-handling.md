# Selection And Group Handling

Selection code is where many beginner scripts start to feel slippery. The same
line can mean "choose one card now," "register official Chain targets," "pick a
valid material set," or "keep this Group alive for a later effect."

This page focuses on the practical question: what state does this selection
create?

| Need | Use |
| --- | --- |
| Check whether non-targeting cards exist. | [`Duel.IsExistingMatchingCard`](/api/functions/Duel/IsExistingMatchingCard) |
| Select non-targeting cards. | [`Duel.SelectMatchingCard`](/api/functions/Duel/SelectMatchingCard) |
| Check whether official targets exist. | [`Duel.IsExistingTarget`](/api/functions/Duel/IsExistingTarget) |
| Select official Chain targets. | [`Duel.SelectTarget`](/api/functions/Duel/SelectTarget) |
| Choose from a Group you already built. | [`Group.Select`](/api/functions/Group/Select) or [`Group.FilterSelect`](/api/functions/Group/FilterSelect) |
| Choose a set that must satisfy a relationship. | [`Group.CheckSubGroup`](/api/functions/Group/CheckSubGroup) and [`Group.SelectSubGroup`](/api/functions/Group/SelectSubGroup) |
| Preserve a Group past the current callback. | [`Group.KeepAlive`](/api/functions/Group/KeepAlive), store it, then [`Group.DeleteGroup`](/api/functions/Group/DeleteGroup) |

## The Selection Decision

Start by reading the card text.

If the effect says "target", the target callback should use
`Duel.IsExistingTarget` and `Duel.SelectTarget`. The selected cards become the
current Chain's targets, and local core creates relations used by
`Card.IsRelateToEffect`.

If the text does not target, do not use `SelectTarget` just because the player
will choose a card. Check with `Duel.IsExistingMatchingCard`, then choose with
`Duel.SelectMatchingCard` at the moment the card is really chosen.

## Official Target Pattern

Book of Moon (`c14087893.lua`) is the compact target pattern:

```lua
function s.target(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
    if chkc then
        return chkc:IsLocation(LOCATION_MZONE) and s.filter(chkc)
    end
    if chk==0 then
        return Duel.IsExistingTarget(s.filter,tp,LOCATION_MZONE,LOCATION_MZONE,1,nil)
    end
    Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_FACEUP)
    local g=Duel.SelectTarget(tp,s.filter,tp,LOCATION_MZONE,LOCATION_MZONE,1,1,nil)
    Duel.SetOperationInfo(0,CATEGORY_POSITION,g,1,0,0)
end
```

The operation then reads the target back and rechecks relation and state:

```lua
function s.activate(e,tp,eg,ep,ev,re,r,rp)
    local tc=Duel.GetFirstTarget()
    if tc:IsRelateToEffect(e) and tc:IsLocation(LOCATION_MZONE) and tc:IsFaceup() then
        Duel.ChangePosition(tc,POS_FACEDOWN_DEFENSE)
    end
end
```

The important part is not only the function names. It is the state they create:
`SelectTarget` registers Chain targets. `GetFirstTarget` and relation checks
are meaningful because that Chain target state exists.

## Resolution Selection Pattern

When an effect chooses during resolution, select from the current game state
instead.

```lua
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

This pattern creates a normal selected Group, not Chain targets. There is no
`Duel.GetFirstTarget` to read later because no target list was made.

## Selecting From A Group

If you already collected a Group, keep working with it. Do not scan the field
again unless the candidate pool really changed.

```lua
local g=Duel.GetMatchingGroup(Card.IsFaceup,tp,LOCATION_MZONE,0,nil)
Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_TOGRAVE)
local sg=g:FilterSelect(tp,Card.IsAbleToGrave,1,1,nil)
if #sg>0 then
    Duel.SendtoGrave(sg,REASON_EFFECT)
end
```

Use `Group.Filter` when every remaining card should be affected. Use
`Group.FilterSelect` or `Group.Select` when the player chooses from the Group.

```lua
local related=tg:Filter(Card.IsRelateToEffect,nil,e)
Duel.Destroy(related,REASON_EFFECT)
```

That style is common after reading `CHAININFO_TARGET_CARDS` or another stored
Group.

## Choosing A Valid Set

Some effects need "two cards that work together," not "one card that passes a
filter." A one-card filter cannot express relationships like same Attribute,
different names, exact Level sum, or one Normal Monster plus one Effect
Monster.

Rescue Hedgehog (`c99742859.lua`) checks for a pair of Level 3 or lower
monsters in the Deck with the same race, same Attribute, same Level, and one
Normal Monster plus one Effect Monster:

```lua
function s.chk(g)
    if g:GetClassCount(Card.GetRace)>1
        or g:GetClassCount(Card.GetAttribute)>1
        or g:GetClassCount(Card.GetLevel)>1 then
        return false
    end
    local fc=g:GetFirst()
    local sc=g:GetNext()
    return fc:IsType(TYPE_NORMAL) and sc:IsType(TYPE_EFFECT)
        or sc:IsType(TYPE_NORMAL) and fc:IsType(TYPE_EFFECT)
end
```

The target checks whether such a subgroup exists:

```lua
local g=Duel.GetMatchingGroup(s.filter,tp,LOCATION_DECK,0,nil,e,tp)
if chk==0 then
    return Duel.GetMZoneCount(tp,e:GetHandler())>1
        and g:CheckSubGroup(s.chk,2,2)
end
```

The operation checks again, then lets the player choose the actual pair:

```lua
local sg=g:SelectSubGroup(tp,s.chk,false,2,2)
if not sg then return end
for tc in aux.Next(sg) do
    Duel.SpecialSummonStep(tc,0,tp,tp,false,false,POS_FACEUP)
end
Duel.SpecialSummonComplete()
```

Use this shape whenever the chosen cards must satisfy a group-level rule.

## Min/Max Stat Selection

Some effects do not ask the player to choose freely. They select the card with
the lowest or highest value among the current candidates. Local scripts use
`Group.GetMinGroup` and `Group.GetMaxGroup` for this.

Queen of Roses (`c96470883.lua`) destroys the face-up monster with the lowest
ATK during the controller's Standby Phase:

```lua
local g=Duel.GetMatchingGroup(s.filter,tp,LOCATION_MZONE,LOCATION_MZONE,nil)
if #g>0 then
    local tg=g:GetMinGroup(Card.GetAttack)
    if #tg>1 then
        Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_DESTROY)
        local sg=tg:Select(tp,1,1,nil)
        Duel.Destroy(sg,REASON_EFFECT)
    else
        Duel.Destroy(tg,REASON_EFFECT)
    end
end
```

Fissure (`c97169186.lua`) uses the same shape with the highest DEF among the
opponent's face-up monsters:

```lua
local g=Duel.GetMatchingGroup(s.filter,tp,0,LOCATION_MZONE,nil)
local tg=g:GetMaxGroup(Card.GetDefense)
```

`GetMinGroup` and `GetMaxGroup` return the tied group, not necessarily one
card. If more than one card shares the same value, choose from that tied group
with `Group.Select`. If the effect should simply affect all tied cards, act on
the returned Group directly.

A continuous modifier can use the returned value without selecting any cards.
`c10796448.lua` reads the opponent's highest base ATK and returns it as this
card's ATK boost:

```lua
local tg,val=g:GetMaxGroup(Card.GetBaseAttack)
return val
```

Use this pattern for "highest ATK", "lowest DEF", "highest Level", and similar
effects. Build the candidate Group from the current game state at resolution
when the effect does not target.

For the full pattern, including tie choices, returned numeric values, custom
scoring functions, and targeting variants, see
[Min/Max Stat Card Selection](min-max-stat-selection).

## SelectUnselect

`Group.SelectUnselect` is a lower-level interactive helper. It lets the player
either add one card from a candidate Group or remove one card from an already
selected Group, then returns the card chosen for that click. Many local
procedure helpers use it to build material groups step by step.

A simple local use appears in Neo-Daedalus (`c10485110.lua`), where the script
asks for one releasable card and allows cancellation:

```lua
local g=Duel.GetReleaseGroup(tp,false,REASON_SPSUMMON):Filter(s.spfilter,nil,tp)
Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_RELEASE)
local tc=g:SelectUnselect(nil,tp,false,true,1,1)
if tc then
    e:SetLabelObject(tc)
    return true
end
return false
```

For ordinary "choose 1 to 3 cards" effects, `Group.Select` or
`Duel.SelectMatchingCard` is usually clearer. Reach for `SelectUnselect` when
the player is building a set and may need to toggle cards in or out before the
selection is complete.

## Keeping A Group For Later

Groups returned by selection helpers are temporary Lua objects. If a script
stores a Group on an effect and uses it after the current callback, preserve it
with `KeepAlive`.

Rescue Hedgehog keeps the two summoned monsters so an End Phase effect can find
and destroy the surviving ones:

```lua
sg:KeepAlive()
local e3=Effect.CreateEffect(c)
e3:SetType(EFFECT_TYPE_FIELD+EFFECT_TYPE_CONTINUOUS)
e3:SetCode(EVENT_PHASE+PHASE_END)
e3:SetLabel(fid)
e3:SetLabelObject(sg)
Duel.RegisterEffect(e3,tp)
```

When the delayed effect no longer needs the Group, release it:

```lua
local g=e:GetLabelObject()
if not g:IsExists(s.desfilter,1,nil,e:GetLabel()) then
    g:DeleteGroup()
    e:Reset()
    return false
end
```

Do not call `KeepAlive` for every selected Group. Use it when the Group must
survive into a later callback, and pair it with `DeleteGroup` when the delayed
effect is done.

## Iterating Groups

Use `aux.Next(g)` for ordinary iteration:

```lua
for tc in aux.Next(g) do
    tc:RegisterFlagEffect(id,RESET_EVENT+RESETS_STANDARD,0,1)
end
```

Use `GetFirst` when the Group is known to contain one card:

```lua
local tc=g:GetFirst()
if tc and tc:IsAbleToHand() then
    Duel.SendtoHand(tc,nil,REASON_EFFECT)
end
```

Use `GetFirst` and `GetNext` when you intentionally split a two-card Group into
stable roles:

```lua
local c1=g:GetFirst()
local c2=g:GetNext()
```

A Group is still a Group even when it contains one card. If you need to call a
`Card.*` method, get the card first.

## Recheck Before Acting

Activation checks prove the effect was legal when activated. Resolution still
needs to look at the current game state.

| Situation | Recheck |
| --- | --- |
| Official target | `tc:IsRelateToEffect(e)` plus current location/state |
| Non-targeting resolution selection | Run the selection filter at resolution |
| Stored delayed Group | Filter for flags, relation, location, or other current requirements |
| Material or subgroup choice | Re-run `CheckSubGroup` before `SelectSubGroup` |
| Zone-sensitive Special Summon | Recheck `Duel.GetLocationCount` or `Duel.GetMZoneCount` |

That habit prevents stale Groups, moved targets, and outdated field counts from
turning into illegal operations.

## Common Mistakes

| Mistake | Better pattern |
| --- | --- |
| Using `Duel.SelectTarget` for a non-targeting effect. | Use `Duel.SelectMatchingCard` when the text does not target. |
| Calling `Duel.GetFirstTarget` after `SelectMatchingCard`. | Store/read the Group returned by the selection, or select at resolution. |
| Calling `Card` methods on a Group. | Use `g:GetFirst()` or iterate with `aux.Next(g)`. |
| Checking `CheckSubGroup` only in the target callback. | Check again in the operation before `SelectSubGroup`. |
| Storing a Group on an effect without `KeepAlive`. | Call `sg:KeepAlive()`, store it, and later call `sg:DeleteGroup()`. |
| Keeping every Group alive by habit. | Keep only Groups needed after the current callback. |
| Moving cards from an old Group without filtering. | Filter for current relation, location, and action legality first. |

Useful API pages:

- [`Duel.IsExistingMatchingCard`](/api/functions/Duel/IsExistingMatchingCard)
- [`Duel.SelectMatchingCard`](/api/functions/Duel/SelectMatchingCard)
- [`Duel.IsExistingTarget`](/api/functions/Duel/IsExistingTarget)
- [`Duel.SelectTarget`](/api/functions/Duel/SelectTarget)
- [`Duel.GetFirstTarget`](/api/functions/Duel/GetFirstTarget)
- [`Duel.GetTargetsRelateToChain`](/api/functions/Duel/GetTargetsRelateToChain)
- [`Group.Select`](/api/functions/Group/Select)
- [`Group.Filter`](/api/functions/Group/Filter)
- [`Group.FilterSelect`](/api/functions/Group/FilterSelect)
- [`Group.GetMinGroup`](/api/functions/Group/GetMinGroup)
- [`Group.GetMaxGroup`](/api/functions/Group/GetMaxGroup)
- [`Group.CheckSubGroup`](/api/functions/Group/CheckSubGroup)
- [`Group.SelectSubGroup`](/api/functions/Group/SelectSubGroup)
- [`Group.SelectUnselect`](/api/functions/Group/SelectUnselect)
- [`Group.KeepAlive`](/api/functions/Group/KeepAlive)
- [`Group.DeleteGroup`](/api/functions/Group/DeleteGroup)
- [`Group.GetFirst`](/api/functions/Group/GetFirst)
- [`Group.GetNext`](/api/functions/Group/GetNext)
- [`Card.IsRelateToEffect`](/api/functions/Card/IsRelateToEffect)
