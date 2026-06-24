# Targeting Flow

Targeting is more than choosing a card. A targeting effect records official
Chain targets during activation, then resolution reads those targets and checks
whether they are still related to the effect.

Use matching-card functions when the card text does not target. Use target
functions when the selected cards must become the effect's targets.

## Basic Target Pattern

A normal targeted effect has four pieces:

1. `EFFECT_FLAG_CARD_TARGET` on the effect.
2. `Duel.IsExistingTarget` in the `chk==0` legality branch.
3. `Duel.SelectTarget` in the real activation branch.
4. `Duel.GetFirstTarget` plus `tc:IsRelateToEffect(e)` during resolution.

The Winged Dragon of Ra (`10000010`) uses the standard one-target destroy
shape:

```lua
function c10000010.destg(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
    if chkc then return chkc:IsLocation(LOCATION_MZONE) end
    if chk==0 then return Duel.IsExistingTarget(aux.TRUE,tp,LOCATION_MZONE,LOCATION_MZONE,1,nil) end
    Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_DESTROY)
    local g=Duel.SelectTarget(tp,aux.TRUE,tp,LOCATION_MZONE,LOCATION_MZONE,1,1,nil)
    Duel.SetOperationInfo(0,CATEGORY_DESTROY,g,g:GetCount(),0,0)
end

function c10000010.desop(e,tp,eg,ep,ev,re,r,rp)
    local tc=Duel.GetFirstTarget()
    if tc:IsRelateToEffect(e) then
        Duel.Destroy(tc,REASON_EFFECT)
    end
end
```

`IsExistingTarget` is the legality check. `SelectTarget` records the selected
card as the Chain target. `SetOperationInfo` announces the expected operation;
it does not destroy the card.

## The `chkc` Branch

The optional `chkc` argument is used when the client checks whether a manually
chosen card is a legal target. Keep this branch consistent with the later
`SelectTarget` call.

```lua
function s.target(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
    if chkc then
        return chkc:IsControler(tp) and chkc:IsLocation(LOCATION_MZONE)
            and s.filter(chkc)
    end
    if chk==0 then
        return Duel.IsExistingTarget(s.filter,tp,LOCATION_MZONE,0,1,nil)
    end
    Duel.SelectTarget(tp,s.filter,tp,LOCATION_MZONE,0,1,1,nil)
end
```

If the target rules depend on extra values, pass the same extra arguments to
both `IsExistingTarget` and `SelectTarget`.

The `chkc` branch usually answers three questions:

| Check | Common local pattern |
| --- | --- |
| Is the card in the right place? | `chkc:IsLocation(...)` or `chkc:IsOnField()` |
| Is the controller restricted? | `chkc:IsControler(tp)` or `chkc:IsControler(1-tp)` |
| Does the card satisfy the filter? | `s.filter(chkc, extra...)` |

Some effects must also exclude the handler. Mystical Space Typhoon
(`c5318639.lua`) can target any Spell/Trap on the field except itself while it
is being activated:

```lua
if chkc then
    return chkc:IsOnField() and s.filter(chkc) and chkc~=e:GetHandler()
end
```

Target-redirection effects make this branch important. Cairngorgon,
Antiluminescent Knight (`c21501505.lua`) uses `Duel.CheckChainTarget` in its
filter, then the `chkc` branch asks whether the manually chosen card is a valid
replacement target for the checked Chain Link:

```lua
function s.filter(c,ct)
    return Duel.CheckChainTarget(ct,c)
end

if chkc then
    return chkc:IsOnField() and s.filter(chkc,ct)
end
```

## Multiple Targets

When an effect selects multiple targets, read the target group during
resolution and filter it for relation. Branded Loss (`10065487`) selects one
Fusion Monster and one opponent's monster, merges the selected groups, and
records both as the operation targets:

```lua
function c10065487.target(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
    if chkc then return false end
    if chk==0 then return Duel.IsExistingTarget(c10065487.filter1,tp,LOCATION_MZONE,0,1,nil)
        and Duel.IsExistingTarget(c10065487.filter2,tp,0,LOCATION_MZONE,1,nil) end
    Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_TODECK)
    local g=Duel.SelectTarget(tp,c10065487.filter1,tp,LOCATION_MZONE,0,1,1,nil)
    Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_TODECK)
    local g2=Duel.SelectTarget(tp,c10065487.filter2,tp,0,LOCATION_MZONE,1,1,nil)
    g:Merge(g2)
    Duel.SetOperationInfo(0,CATEGORY_TODECK,g,2,0,0)
end

function c10065487.activate(e,tp,eg,ep,ev,re,r,rp)
    local g=Duel.GetChainInfo(0,CHAININFO_TARGET_CARDS):Filter(Card.IsRelateToEffect,nil,e)
    if Duel.SendtoDeck(g,nil,SEQ_DECKSHUFFLE,REASON_EFFECT)>0 then
        -- continue resolving the rest of the effect
    end
end
```

`Duel.GetTargetsRelateToChain()` is the shorter helper when all you need is
the group of current targets still related to the resolving Chain.

The local generated API includes `Duel.GetTargetsRelateToChain`. If an external
tutorial mentions `Duel.GetTargetCards(e)`, do not copy that name unless it is
defined in your local environment. In this project, use the local helper above
or the explicit Chain-info form:

```lua
local tg=Duel.GetChainInfo(0,CHAININFO_TARGET_CARDS)
if tg then
    tg=tg:Filter(Card.IsRelateToEffect,nil,e)
end
```

## Target Count And The `min,max` Pair

`Duel.SelectTarget` uses `min,max` to decide how many cards the player may
select. The legality branch should prove that the minimum can be satisfied.

| Text shape | Check | Select |
| --- | --- | --- |
| "Target 1 card" | `Duel.IsExistingTarget(...,1,...)` | `Duel.SelectTarget(...,1,1,...)` |
| "Target up to 2 cards" | usually at least `1` if activation requires a target | `Duel.SelectTarget(...,1,2,...)` |
| "Target exactly 2 cards" | prove two legal targets or split the two requirements | `Duel.SelectTarget(...,2,2,...)` or two one-card selections |

When the targets have different requirements, two separate selections are often
clearer than one broad filter. The selected Groups can be merged before
`SetOperationInfo`.

## How Resolution Wording Changes Rechecks

After the semicolon, card text often refers back to the target in different
ways. Local scripts do not parse that wording for you; the operation function
must make the right current-state checks.

| Wording idea | Resolution habit |
| --- | --- |
| "destroy it" / "destroy that card" | Check relation first. Add location/state checks if the action only makes sense for the current card state. |
| "destroy that target" | Check relation and recheck the target requirements that still matter. |
| "destroy those cards" | Filter the target group for relation, then apply the action to the surviving related cards. |
| "destroy both/all those targets" | Filter for relation and required current state; if the effect requires all of them to remain valid, bail out when the filtered group is too small. |

Book of Moon rechecks relation, Monster Zone location, and face-up state because
its operation only changes a face-up monster to face-down Defense Position:

```lua
local tc=Duel.GetFirstTarget()
if tc:IsRelateToEffect(e) and tc:IsLocation(LOCATION_MZONE) and tc:IsFaceup() then
    Duel.ChangePosition(tc,POS_FACEDOWN_DEFENSE)
end
```

The exact card text decides how strict the operation should be. The safe habit
is to read the target back, filter for relation, then recheck whatever current
state the operation still requires.

## Recording Targets Without Selecting

`Duel.SetTargetCard` records cards as the current Chain's target cards without
running a target selection prompt. Use it only after the script has already
identified the cards by another legal route.

The script `c30964246.lua` first builds a group with matching APIs and
`Card.IsCanBeEffectTarget`, then registers the chosen subgroup:

```lua
function s.filter(c,e)
    return c:IsAbleToHand() and c:IsCanBeEffectTarget(e)
end

function s.thtg1(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
    local g=Duel.GetMatchingGroup(s.filter,tp,LOCATION_ONFIELD,LOCATION_ONFIELD,nil,e)
    if chkc then return false end
    if chk==0 then return g:CheckSubGroup(s.sgselect,2,2,tp) end
    Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_RTOHAND)
    local sg=g:SelectSubGroup(tp,s.sgselect,false,2,2,tp)
    Duel.SetTargetCard(sg)
    Duel.SetOperationInfo(0,CATEGORY_TOHAND,sg,#sg,0,0)
end
```

Because `SetTargetCard` does not perform the same selection and targetability
check by itself, the script checks `Card.IsCanBeEffectTarget(e)` before
selecting the subgroup.

## Targeting vs Non-Targeting

| Text / behavior | Check | Select or record | Resolve |
| --- | --- | --- | --- |
| Targets one card | `Duel.IsExistingTarget` | `Duel.SelectTarget` | `Duel.GetFirstTarget()` and `tc:IsRelateToEffect(e)` |
| Targets several cards | `Duel.IsExistingTarget` for each requirement | `Duel.SelectTarget`, `Duel.SetTargetCard` when already selected legally | `Duel.GetTargetsRelateToChain()` or `CHAININFO_TARGET_CARDS` filtered by relation |
| Does not target and chooses at resolution | `Duel.IsExistingMatchingCard` if needed | usually none in target callback | `Duel.SelectMatchingCard` during operation |
| Announces an expected action | legality checks for that action | `Duel.SetOperationInfo` | perform the action in operation |

Relevant API pages:

- [`Effect.SetTarget`](/api/functions/Effect/SetTarget)
- [`Duel.IsExistingTarget`](/api/functions/Duel/IsExistingTarget)
- [`Duel.SelectTarget`](/api/functions/Duel/SelectTarget)
- [`Duel.SetTargetCard`](/api/functions/Duel/SetTargetCard)
- [`Duel.GetFirstTarget`](/api/functions/Duel/GetFirstTarget)
- [`Duel.GetTargetsRelateToChain`](/api/functions/Duel/GetTargetsRelateToChain)
- [`Duel.GetChainInfo`](/api/functions/Duel/GetChainInfo)
- [`Duel.CheckChainTarget`](/api/functions/Duel/CheckChainTarget)
- [`Card.IsRelateToEffect`](/api/functions/Card/IsRelateToEffect)
- [`Card.IsRelateToChain`](/api/functions/Card/IsRelateToChain)
- [`Duel.SetOperationInfo`](/api/functions/Duel/SetOperationInfo)
