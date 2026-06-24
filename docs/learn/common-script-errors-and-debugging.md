# Common Script Errors And Debugging

Most script bugs come from one of two places: the effect was not legal when the
engine checked it, or the cards you remembered at activation are no longer valid
when the Chain resolves. Debugging is easier when you first decide which
callback is failing.

Use this loop before changing code:

1. Find the `Effect.CreateEffect(c)` block that owns the behavior.
2. Check `SetType`, `SetCode`, `SetRange`, properties, and count limits.
3. Follow `SetCondition`, `SetCost`, `SetTarget`, and `SetOperation` in order.
4. Split the `chk==0` legality branch from the real activation branch.
5. At resolution, recheck every card or Group that came from an earlier step.

## Fast Triage

| Symptom | First place to look |
| --- | --- |
| The client never offers the effect. | Type, code, range, condition, cost `chk==0`, target `chk==0`, and count limit. |
| Activation is offered but errors immediately. | Nil `Card`, `Group`, or `Effect` values, often from `GetFirst`, `GetFirstTarget`, or chain data. |
| The effect activates but does nothing. | Resolution relation checks, location changes, and operation legality rechecks. |
| The wrong cards are affected. | `SelectTarget` versus `SelectMatchingCard`, location masks, `SetTargetRange`, and filters. |
| A temporary effect lasts too long or disappears early. | `SetReset`, reset count, and whether the effect was registered on the card or the Duel. |
| A once-per-turn limit is too strict or too loose. | `SetCountLimit` code, oath flags, and whether cloned effects share the same code. |

## Nil Values

Lua will error if you call a Card method on `nil`. Any function that returns a
Card from a Group, target list, or chain lookup can produce `nil` when no card
exists in that context.

```lua
local tc=Duel.GetFirstTarget()
if tc and tc:IsRelateToEffect(e) then
    Duel.SendtoHand(tc,nil,REASON_EFFECT)
end
```

Use the guard when the card might not exist. Local scripts such as Sphere Mode
guard the result of `g:GetFirst()` before using it after a selection. Book of
Moon can assume a selected target exists because its target function selected
exactly one official target, but the resolution still checks relation, location,
and face-up state.

`Effect` values can be nil too. In Chain callbacks, `re` is the effect that
created the Chain Link. Outside those callbacks, do not assume that `re` exists.

Relevant API:
[Duel.GetFirstTarget](/api/functions/Duel/GetFirstTarget),
[Group.GetFirst](/api/functions/Group/GetFirst),
[Card.IsRelateToEffect](/api/functions/Card/IsRelateToEffect)

## Missing `chk==0`

Cost and target callbacks are called once to ask "can this be activated?" and
again to perform the real cost or target selection. The `chk==0` branch must not
move cards, pay LP, discard, release, register restrictions, or make selections.

Book of Moon shows the target shape:

```lua
if chk==0 then
    return Duel.IsExistingTarget(c14087893.filter,tp,LOCATION_MZONE,LOCATION_MZONE,1,nil)
end
Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_FACEUP)
local g=Duel.SelectTarget(tp,c14087893.filter,tp,LOCATION_MZONE,LOCATION_MZONE,1,1,nil)
Duel.SetOperationInfo(0,CATEGORY_POSITION,g,1,0,0)
```

Chow Chow Chan shows the same split for a cost:

```lua
if chk==0 then return e:GetHandler():IsDiscardable() end
Duel.SendtoGrave(e:GetHandler(),REASON_COST+REASON_DISCARD)
```

Relevant API:
[Duel.IsExistingTarget](/api/functions/Duel/IsExistingTarget),
[Duel.SelectTarget](/api/functions/Duel/SelectTarget),
[Duel.SetOperationInfo](/api/functions/Duel/SetOperationInfo)

## Cost, Target, And Operation Desync

The legality branch proves that an activation can start. It does not guarantee
that the operation will still be legal later. Recheck the board at resolution
instead of trusting old assumptions.

Rescue Hedgehog checks the Deck, Monster Zone space, and Special Summon lock in
`target`, then checks those facts again in `operation` before selecting and
Summoning. That is the pattern to copy when a target branch depends on changing
state:

```lua
local g=Duel.GetMatchingGroup(s.filter,tp,LOCATION_DECK,0,nil,e,tp)
if Duel.IsPlayerAffectedByEffect(tp,59822133)
    or Duel.GetLocationCount(tp,LOCATION_MZONE)<2
    or not g:CheckSubGroup(s.chk,2,2) then return end
```

If the target branch gives the player a choice, record only the information that
is still valid later: official targets, labels, label objects, or kept Groups.
Then validate it again in the operation.

Relevant API:
[Effect.SetLabel](/api/functions/Effect/SetLabel),
[Effect.SetLabelObject](/api/functions/Effect/SetLabelObject),
[Duel.GetLocationCount](/api/functions/Duel/GetLocationCount)

## Targeting Versus Selecting

Use `Duel.SelectTarget` only when the effect targets. It records official Chain
targets and lets the engine create target relation. Use `Duel.SelectMatchingCard`
when the effect merely chooses a card during resolution or as a cost.

| Text shape | Check branch | Real branch | Resolution |
| --- | --- | --- | --- |
| Targets a card | `Duel.IsExistingTarget` | `Duel.SelectTarget` | `Duel.GetFirstTarget()` and `tc:IsRelateToEffect(e)` |
| Chooses during resolution | `Duel.IsExistingMatchingCard` | no target selection | `Duel.SelectMatchingCard` in operation |
| Chooses as cost | cost `chk==0` checks availability | `Duel.SelectMatchingCard` and pay cost | no target relation |

Book of Moon targets, so it uses `SelectTarget`. Neo-Daedalus sends "Umi" as a
cost, so it uses `SelectMatchingCard` in the cost callback.

Relevant API:
[Duel.SelectTarget](/api/functions/Duel/SelectTarget),
[Duel.SelectMatchingCard](/api/functions/Duel/SelectMatchingCard),
[Duel.GetChainInfo](/api/functions/Duel/GetChainInfo)

## Relation Checks

After a Chain starts, targets and handlers can move, flip face-down, leave the
field, or stop being related to the effect. Check relation before applying the
operation.

```lua
local tc=Duel.GetFirstTarget()
if tc and tc:IsRelateToEffect(e) and tc:IsLocation(LOCATION_MZONE) then
    Duel.ChangePosition(tc,POS_FACEDOWN_DEFENSE)
end
```

Use `Card.IsRelateToEffect(e)` for cards tied to that effect's target relation
or handler relation. Use `Card.IsRelateToChain()` when a card was recorded as a
Chain target through `Duel.SetTargetCard` or similar Chain data rather than a
normal `SelectTarget` call; X-Saber Perina uses this when granting an effect to
the Synchro Monster it targeted during material handling.

For negation effects that destroy the Chain Link's handler, check the triggering
effect's handler after negating:

```lua
if Duel.NegateActivation(ev) and re:GetHandler():IsRelateToEffect(re) then
    Duel.Destroy(eg,REASON_EFFECT)
end
```

Relevant API:
[Card.IsRelateToEffect](/api/functions/Card/IsRelateToEffect),
[Card.IsRelateToChain](/api/functions/Card/IsRelateToChain),
[Duel.SetTargetCard](/api/functions/Duel/SetTargetCard)

## Wrong Location Masks

Location masks answer "where can this card be found?" A broad mask can make an
effect legal for the wrong cards; a narrow mask can hide valid cards from the
client.

| Need | Prefer |
| --- | --- |
| Monster Zone only | `LOCATION_MZONE` |
| Spell and Trap Zone only | `LOCATION_SZONE` |
| Either Monster Zone or Spell and Trap Zone | `LOCATION_ONFIELD` |
| Graveyard only | `LOCATION_GRAVE` |
| hand or Deck | `LOCATION_HAND+LOCATION_DECK` |
| both players' monster zones | `LOCATION_MZONE,LOCATION_MZONE` in the self/opponent parameters |

Avoid unexplained numeric masks in learner code. Local older scripts sometimes
use compact masks like `0xe`; documentation examples should use named constants
so the affected zones are obvious.

Relevant API:
[Duel.GetLocationCount](/api/functions/Duel/GetLocationCount),
[Duel.GetMZoneCount](/api/functions/Duel/GetMZoneCount),
[Constants](/api/constants)

## `IsFaceup` Versus `IsFaceupEx`

Use `Card.IsFaceup` for cards whose battle position exists on the field. Use
`Card.IsFaceupEx` when a script wants "public enough to be treated as face-up"
across public locations or face-up Extra Deck style checks.

Local procedure helpers use `IsFaceupEx` for material checks that can involve
public non-field locations. The generated examples for `Card.IsFaceupEx` include
filters such as:

```lua
return c:IsFaceupEx() and c:IsType(TYPE_MONSTER) and c:IsCanBeFusionMaterial()
```

Do not add `IsFaceup()` to a Graveyard or hand filter just because the card must
be visible to players. In those locations it is usually either public by
location rules or should use `IsFaceupEx` when the local helper expects that
meaning.

Relevant API:
[Card.IsFaceup](/api/functions/Card/IsFaceup),
[Card.IsFaceupEx](/api/functions/Card/IsFaceupEx)

## Count-Limit Mistakes

`SetCountLimit(1)` limits that Effect object. `SetCountLimit(1,id)` shares a
named once-per-turn limit across effects that use the same code. Use separate
codes, often `id+o`, when two effects on the same card should each be usable
once.

X-Saber Perina uses one limit for its Summon trigger and a different one for its
material trigger:

```lua
e1:SetCountLimit(1,id)
e3:SetCountLimit(1,id+o)
```

Cyber Dragon Infinity uses `SetCountLimit(1)` on the once-per-copy absorb effect
and negate effect. That is correct because those effects do not need a shared
named limit across multiple cards.

Relevant API:
[Effect.SetCountLimit](/api/functions/Effect/SetCountLimit),
[Effect.UseCountLimit](/api/functions/Effect/UseCountLimit),
[Count limits and once per turn](/learn/count-limits)

## Reset Flag Mistakes

Temporary effects need a reset. Card-bound effects usually use
`RESET_EVENT+RESETS_STANDARD`; phase effects usually add `RESET_PHASE+PHASE_END`
and, when needed, a reset count.

Rescue Hedgehog disables the Summoned monsters with:

```lua
e1:SetReset(RESET_EVENT+RESETS_STANDARD)
```

Sphere Mode registers a delayed return watcher with:

```lua
e1:SetReset(RESET_PHASE+PHASE_END,2)
```

If an effect vanishes too early, check whether the card moved through a reset
event. If it never expires, check whether you forgot `SetReset`, registered the
effect globally, or used a reset count that never reaches zero.

Relevant API:
[Effect.SetReset](/api/functions/Effect/SetReset),
[Card.RegisterFlagEffect](/api/functions/Card/RegisterFlagEffect),
[Reset Flags And Effect Duration](/learn/reset-flags-and-duration)

## Missing `SetRange` Or `SetTargetRange`

For a continuous field effect, `SetRange` says where the source card must be for
the effect to apply. `SetTargetRange` says which side and location the effect
affects.

Banner of Courage has both:

```lua
e2:SetType(EFFECT_TYPE_FIELD)
e2:SetRange(LOCATION_SZONE)
e2:SetTargetRange(LOCATION_MZONE,0)
e2:SetCode(EFFECT_UPDATE_ATTACK)
```

If you omit `SetRange`, a card-bound continuous effect may not be tied to the
zone you intended. If you omit `SetTargetRange`, the effect has no clear affected
side/location. When `EFFECT_FLAG_PLAYER_TARGET` is present, `SetTargetRange`
uses player flags instead of location masks.

Relevant API:
[Effect.SetRange](/api/functions/Effect/SetRange),
[Effect.SetTargetRange](/api/functions/Effect/SetTargetRange),
[Player Restrictions](/learn/player-restrictions)

## Negation Confusion

Negating an activation, negating a resolving effect, disabling a card, and
negating a Summon are different jobs.

| Goal | Typical tool | Local example |
| --- | --- | --- |
| Negate a Chain Link's activation | `Duel.NegateActivation(ev)` | Cyber Dragon Infinity, Chow Chow Chan |
| Negate a Chain Link while it is resolving | `Duel.NegateEffect(ev)` or `EFFECT_DISABLE_CHAIN` | Dark-Imprisoning Mirror, Rescue Hedgehog |
| Leave a card's effects disabled | register `EFFECT_DISABLE` or `EFFECT_DISABLE_EFFECT` | Rescue Hedgehog |
| Negate a Summon | `Duel.NegateSummon(eg)` in a Summon-negation window | Solemn-style scripts and `aux.NegateSummonCondition` examples |
| Prevent a Summon from being negated | `EFFECT_CANNOT_DISABLE_SPSUMMON` | Holactie |

Do not use `Duel.NegateActivation` for a continuous watcher such as
Dark-Imprisoning Mirror. It watches `EVENT_CHAIN_SOLVING` and calls
`Duel.NegateEffect(ev)` because the Chain Link is already resolving.

Relevant API:
[Duel.NegateActivation](/api/functions/Duel/NegateActivation),
[Duel.NegateEffect](/api/functions/Duel/NegateEffect),
[Duel.NegateSummon](/api/functions/Duel/NegateSummon),
[Auxiliary.NegateSummonCondition](/api/functions/Auxiliary/NegateSummonCondition)

## Group Lifetime Mistakes

Most Groups are temporary. Use them immediately, or keep them alive when a later
callback must read the same Group.

Holactie stores selected Tributes for its Summon procedure:

```lua
sg:KeepAlive()
e:SetLabelObject(sg)
```

and deletes the Group after releasing it:

```lua
local g=e:GetLabelObject()
Duel.Release(g,REASON_SPSUMMON)
g:DeleteGroup()
```

Rescue Hedgehog keeps a Group until the End Phase watcher either destroys the
marked monsters or finds that none remain, then calls `DeleteGroup()` and resets
the watcher.

Relevant API:
[Group.KeepAlive](/api/functions/Group/KeepAlive),
[Group.DeleteGroup](/api/functions/Group/DeleteGroup),
[Effect.SetLabelObject](/api/functions/Effect/SetLabelObject)

## `IsCode` Versus `IsOriginalCodeRule`

Use `Card.IsCode` when the current card code or alternate code should count.
Use `Card.IsOriginalCodeRule` when the rule-original identity matters even if
the card's current name or code has changed.

Holactie checks the original Egyptian God identities for its release group:

```lua
c10000040.spchecks=aux.CreateChecks(Card.IsOriginalCodeRule,{10000020,10000000,10000010})
```

That would be too strict or too loose if replaced blindly with `IsCode`,
depending on copied names and alternate-code effects. For ordinary "search this
named card" filters, `IsCode` is usually the right choice.

Relevant API:
[Card.IsCode](/api/functions/Card/IsCode),
[Card.IsOriginalCodeRule](/api/functions/Card/IsOriginalCodeRule),
[Archetypes and set codes](/learn/archetypes-and-setcodes)

## A Practical Debugging Pass

When a script still feels wrong, write a short checklist beside the effect:

1. What callback is running when the problem happens?
2. Does `chk==0` only answer true or false?
3. Does the real branch select or pay exactly once?
4. Does operation recheck relation, location, immunity, and available zones?
5. Is every stored Group either used immediately or paired with `KeepAlive` and `DeleteGroup`?
6. Are count codes and reset flags shared only where the card text says they should be?

Then compare the shape against a small local script. Book of Moon is the clean
targeting baseline, Cyber Dragon Infinity is the clean activation-negation
baseline, Banner of Courage is the clean continuous field-effect baseline, and
Rescue Hedgehog is the clean "store a Group for later" baseline.
