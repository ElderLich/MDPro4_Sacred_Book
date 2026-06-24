# Counter Traps

Counter Traps are Trap Card activations whose card type gives them Spell Speed
3. In script they still use `EFFECT_TYPE_ACTIVATE`; the local core reads
`TYPE_COUNTER` from the handler and assigns the faster response speed.

The main beginner skill is choosing the correct negation family. A Counter Trap
that negates a Summon is not resolving a Chain Link. A Counter Trap that
responds to a Spell, Trap, or monster effect is answering `EVENT_CHAINING`.

## Counter Trap Activation Shape

Solemn Judgment (`c41420027.lua`) shows both families on one card:

```lua
local e1=Effect.CreateEffect(c)
e1:SetCategory(CATEGORY_DISABLE_SUMMON+CATEGORY_DESTROY)
e1:SetType(EFFECT_TYPE_ACTIVATE)
e1:SetCode(EVENT_SUMMON)
e1:SetCondition(aux.NegateSummonCondition)
e1:SetCost(c41420027.cost1)
e1:SetTarget(c41420027.target1)
e1:SetOperation(c41420027.activate1)
c:RegisterEffect(e1)

local e4=Effect.CreateEffect(c)
e4:SetCategory(CATEGORY_NEGATE+CATEGORY_DESTROY)
e4:SetType(EFFECT_TYPE_ACTIVATE)
e4:SetCode(EVENT_CHAINING)
e4:SetCondition(c41420027.condition2)
e4:SetCost(c41420027.cost2)
e4:SetTarget(c41420027.target2)
e4:SetOperation(c41420027.activate2)
c:RegisterEffect(e4)
```

Both effects are `EFFECT_TYPE_ACTIVATE`. The event code decides which timing
family each activation belongs to.

## Summon Negation

Summon-negating Counter Traps listen to Summon events, usually cloning the same
effect across Normal, Flip, and Special Summon windows:

```lua
local e2=e1:Clone()
e2:SetCode(EVENT_FLIP_SUMMON)
c:RegisterEffect(e2)
local e3=e1:Clone()
e3:SetCode(EVENT_SPSUMMON)
c:RegisterEffect(e3)
```

The condition is commonly `aux.NegateSummonCondition`, sometimes with an extra
card-specific filter. Chaos Trap Hole (`c11593137.lua`) adds an Attribute
check:

```lua
function c11593137.condition(e,tp,eg,ep,ev,re,r,rp)
    return aux.NegateSummonCondition() and eg:IsExists(c11593137.filter,1,nil)
end
```

The operation uses `Duel.NegateSummon`, then applies the card's follow-up:

```lua
function c11593137.activate(e,tp,eg,ep,ev,re,r,rp)
    local g=eg:Filter(c11593137.filter,nil)
    Duel.NegateSummon(g)
    Duel.Remove(g,POS_FACEUP,REASON_EFFECT)
end
```

Do not use `Duel.NegateActivation` here. There is no Chain Link activation to
negate in this timing family.

## Activation Negation

Counter Traps that answer activated Spells, Traps, or monster effects usually
listen to `EVENT_CHAINING`, check the triggering effect, and call
`Duel.NegateActivation(ev)`.

Dark Bribe (`c77538567.lua`) answers the opponent's Spell/Trap activation:

```lua
function c77538567.condition(e,tp,eg,ep,ev,re,r,rp)
    return re:IsHasType(EFFECT_TYPE_ACTIVATE) and rp==1-tp and Duel.IsChainNegatable(ev)
end
```

Its operation negates that activation, destroys the activating card if it is
still related, then draws for the opponent:

```lua
function c77538567.activate(e,tp,eg,ep,ev,re,r,rp)
    if Duel.NegateActivation(ev) and re:GetHandler():IsRelateToEffect(re) then
        Duel.Destroy(eg,REASON_EFFECT)
    end
    Duel.Draw(1-tp,1,REASON_EFFECT)
end
```

That `IsRelateToEffect(re)` check matters because the handler being answered is
the Chain Link's handler, not the Counter Trap itself.

## Monster Effect Responses

Solemn Strike (`c40605147.lua`) and Divine Wrath (`c49010598.lua`) both answer
monster effects with `EVENT_CHAINING`:

```lua
function c40605147.condition(e,tp,eg,ep,ev,re,r,rp)
    return re:IsActiveType(TYPE_MONSTER) and Duel.IsChainNegatable(ev)
end
```

They still call `Duel.NegateActivation(ev)` because they are negating the
activation of the monster effect Chain Link. That is different from applying a
lingering disabled state to a monster.

Use `Duel.NegateEffect(ev)` when the script is negating a resolving effect
without negating its activation. Local examples such as Infinite Impermanence
and Mind Scan use `Duel.NegateEffect` from watcher effects after their own
Trap activation has already resolved.

## Spell Activation Filters

Some Counter Traps care about the kind of activation being answered. Spell
Shield Type-8 (`c38275183.lua`) checks that the Chain Link is a Spell Card
activation:

```lua
return re:IsActiveType(TYPE_SPELL)
    and re:IsHasType(EFFECT_TYPE_ACTIVATE)
    and Duel.IsChainNegatable(ev)
```

That pair is useful:

- `re:IsActiveType(TYPE_SPELL)` checks the active card/effect family.
- `re:IsHasType(EFFECT_TYPE_ACTIVATE)` checks that the Chain Link is a card
  activation effect, not some other effect shape.

## Announce The Right Operation

The target branch should announce what the Counter Trap is about to do.

```lua
function c41420027.target2(e,tp,eg,ep,ev,re,r,rp,chk)
    if chk==0 then return true end
    Duel.SetOperationInfo(0,CATEGORY_NEGATE,eg,1,0,0)
    if re:GetHandler():IsDestructable() and re:GetHandler():IsRelateToEffect(re) then
        Duel.SetOperationInfo(0,CATEGORY_DESTROY,eg,1,0,0)
    end
end
```

For Summon negation, announce `CATEGORY_DISABLE_SUMMON`. For activation
negation, announce `CATEGORY_NEGATE`. For follow-up destruction, banishing,
drawing, or sending, announce those categories too.

## Negation Families

| Script family | Event | Common check | Operation |
| --- | --- | --- | --- |
| Summon negation | `EVENT_SUMMON`, `EVENT_FLIP_SUMMON`, `EVENT_SPSUMMON` | `aux.NegateSummonCondition()` | `Duel.NegateSummon(eg)` |
| Card/effect activation negation | `EVENT_CHAINING` | `Duel.IsChainNegatable(ev)` plus type/player checks | `Duel.NegateActivation(ev)` |
| Effect negation during resolution | usually watcher or resolving effect logic | Chain info or watched handler checks | `Duel.NegateEffect(ev)` |
| Lingering monster disable | normal Trap/Effect operation | targeted monster still legal | register `EFFECT_DISABLE` / `EFFECT_DISABLE_EFFECT` |

Counter Traps most often use the first two rows. The last two rows are included
because confusing them is a common source of broken scripts.

## Common Pitfalls

| Mistake | Better pattern |
| --- | --- |
| Writing a Counter Trap as `EFFECT_TYPE_QUICK_O`. | Use `EFFECT_TYPE_ACTIVATE`; `TYPE_COUNTER` supplies Spell Speed 3. |
| Calling `Duel.NegateActivation` in a Summon event. | Use `Duel.NegateSummon` with the Summoned group. |
| Calling `Duel.NegateSummon` while answering `EVENT_CHAINING`. | Use Chain APIs such as `Duel.NegateActivation(ev)`. |
| Forgetting `Duel.IsChainNegatable(ev)` on response effects. | Keep it with the card-specific Chain checks. |
| Destroying the Chain handler without checking relation. | Check `re:GetHandler():IsRelateToEffect(re)`. |
| Announcing only destruction. | Announce `CATEGORY_NEGATE` or `CATEGORY_DISABLE_SUMMON` as well. |

## Useful API Pages

- [`Effect.SetType`](/api/functions/Effect/SetType)
- [`Effect.SetCode`](/api/functions/Effect/SetCode)
- [`Effect.SetCondition`](/api/functions/Effect/SetCondition)
- [`Effect.SetCost`](/api/functions/Effect/SetCost)
- [`Effect.SetTarget`](/api/functions/Effect/SetTarget)
- [`Effect.SetOperation`](/api/functions/Effect/SetOperation)
- [`Effect.Clone`](/api/functions/Effect/Clone)
- [`Effect.IsActiveType`](/api/functions/Effect/IsActiveType)
- [`Effect.IsHasType`](/api/functions/Effect/IsHasType)
- [`Duel.IsChainNegatable`](/api/functions/Duel/IsChainNegatable)
- [`Duel.NegateActivation`](/api/functions/Duel/NegateActivation)
- [`Duel.NegateEffect`](/api/functions/Duel/NegateEffect)
- [`Duel.NegateSummon`](/api/functions/Duel/NegateSummon)
- [`Duel.SetOperationInfo`](/api/functions/Duel/SetOperationInfo)
- [`Card.IsRelateToEffect`](/api/functions/Card/IsRelateToEffect)

Related lessons:

- [Trap Card Patterns](trap-card-patterns)
- [Chain Timing And Activation Windows](chain-timing-and-activation-windows)
- [Negation and Immunity](negation-and-immunity)
- [Common Script Errors And Debugging](common-script-errors-and-debugging)
