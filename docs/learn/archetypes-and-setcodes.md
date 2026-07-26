# Archetypes and Set Codes

A set code is the engine's stable identifier for an archetype, series, or
subfamily. Use it when card text names a family. Do not compare translated card
names or search a card's text at runtime.

This page covers every general set-code check exposed by the local core, the
listed-set and material-list helpers in `utility.lua`, dynamic membership, and
the less common places where a set code appears.

## Pick The Right Check

Start by asking **which version of the card's identity the rule describes**.

| The rule needs | Use |
| --- | --- |
| The card's membership right now. | `Card.IsSetCard` |
| Its database/rule-original membership, ignoring later name and set changes. | `Card.IsOriginalSetCard` |
| Its membership before it moved or changed state. | `Card.IsPreviousSetCard` |
| Membership while it is being tested as Fusion Material. | `Card.IsFusionSetCard` |
| Membership while it is being tested as Link Material. | `Card.IsLinkSetCard` |
| The archetype of the card that Special Summoned it. | `Card.IsSpecialSummonSetCard` |
| A card that *lists a monster from* an archetype in registered metadata. | `aux.IsSetNameMonsterListed` |
| A monster whose written material metadata names an archetype. | `aux.IsMaterialListSetCard` |
| One exact named card. | `Card.IsCode` |
| A card that lists one exact named card. | `aux.IsCodeListed` |
| The named card itself or a card that lists it. | `aux.IsCodeOrListed` |

The final three are card-code checks, not set-code checks. They are included
because effects often say either “an `X` card” or “a card that mentions `X`,”
and those are different script questions.

## Beginner Pattern: One Archetype Filter

Most archetype filters only need `IsSetCard` plus the visible restrictions from
the card text:

```lua
function s.thfilter(c)
    return c:IsSetCard(0x14f)
        and c:IsType(TYPE_MONSTER)
        and c:IsAbleToHand()
end
```

Read this as: “an `0x14f` monster that can be added to the hand.” The hex value
comes from local card data and nearby scripts. It is not derived from the
displayed archetype name.

Keep each part of the text visible in the filter. Set membership alone does not
imply that a card is a Monster, face-up, in a particular location, or able to
perform the requested action.

## How Set-Code Matching Works

DataEditorX exposes four set-code boxes. In a normal `.cdb`, those values are
packed into `datas.setcode` as 16-bit entries. See
[Card Data and Script Wiring](card-data-and-script-wiring#set-codes-and-archetype-filters)
for the database side.

Within one 16-bit set code:

- the low 12 bits identify the base family;
- the high 4 bits are subtype requirements.

The queried base family must match exactly. Every high-bit flag requested by
the query must also exist on the stored value.

| Stored membership | Query | Result | Why |
| --- | --- | --- | --- |
| `0x1034` | `0x034` | true | Same base family; no subtype was required. |
| `0x1034` | `0x1034` | true | Same base and the requested high bit exists. |
| `0x1034` | `0x2034` | false | The requested `0x2000` bit is absent. |
| `0x3034` | `0x1034` | true | A stored value may satisfy one of several high-bit requirements. |
| `0x3034` | `0x2034` | true | The `0x2000` bit also exists. |
| `0x3034` | `0x4034` | false | The base matches, but the requested high bit does not. |

That is why a broad query such as `0x034` can include several subfamilies,
while `0x1034` is narrower. Use the narrowest value required by the card text.
Do not reproduce this bit math inside normal filters; the core and auxiliary
helpers already apply it consistently.

### Several Arguments Mean “Any”

All six core `Is...SetCard` methods accept multiple set codes. They return true
when **any one** matches, and skip `nil` arguments:

```lua
function s.filter(c)
    return c:IsSetCard(0x3008,0x1f)
end
```

This does not require both families. If one card from each family is required,
check the cards as a Group instead; see
[Requiring Different Families](#requiring-different-families).

## Current Membership: `Card.IsSetCard`

Use `IsSetCard` for ordinary searches, targets, costs, continuous-effect
targets, and non-Fusion/non-Link material filters.

```lua
function s.filter(c)
    return c:IsFaceup()
        and c:IsSetCard(0x103)
        and c:IsType(TYPE_EFFECT)
end
```

The local core checks:

- set data for the card's current code;
- its alternate code when one exists;
- active `EFFECT_ADD_SETCODE` effects.

Consequently, `IsSetCard` follows current name/code changes and current added
membership. Comparing `datas.setcode` by hand would miss those cases.

### Three Useful Call Shapes

The readable beginner form is a method call:

```lua
return c:IsSetCard(0x19e)
```

When a Duel or Group method supplies the candidate card as the first filter
argument, the unbound function can be passed directly. Local scripts use this
shape:

```lua
local g=Duel.GetMatchingGroup(
    Card.IsSetCard,
    tp,LOCATION_HAND+LOCATION_ONFIELD,0,
    nil,0x19e
)
```

Here `Card.IsSetCard` receives each candidate first, then the extra `0x19e`
argument.

When another helper needs a one-argument predicate, bind the set code with
`aux.FilterBoolFunction`:

```lua
local setfilter=aux.FilterBoolFunction(Card.IsSetCard,0x107a)
aux.AddXyzProcedure(c,setfilter,5,2)
```

These are three ways to call the same check; they do not have different
membership semantics.

## Original Membership: `Card.IsOriginalSetCard`

Use `IsOriginalSetCard` when the rule intentionally cares about original
identity rather than what an effect currently makes the card become.

Local `c16449363.lua` uses it in a destruction-replacement filter:

```lua
function s.repfilter(c,tp)
    return c:IsFaceup()
        and c:IsOriginalSetCard(0x66)
        and c:IsType(TYPE_SYNCHRO)
        and c:IsOnField()
        and c:IsControler(tp)
end
```

The local core reads the card's original set data and also accounts for its
second rule-original code when one exists. It does **not** use a temporary
`EFFECT_ADD_SETCODE` membership.

Use this only when the wording or procedure really calls for original
identity. Ordinary “`X` card” filters normally use current `IsSetCard`.

## Previous Membership: `Card.IsPreviousSetCard`

Event Groups often contain a card after it has left the state described by the
trigger. Use `IsPreviousSetCard` together with the other previous-state checks.

Dual Avatar Feet - Kokoku (`c11759079.lua`) checks a destroyed monster as it
existed on the field:

```lua
function s.spfilter(c,tp)
    return c:IsReason(REASON_BATTLE+REASON_EFFECT)
        and c:IsPreviousSetCard(0x14f)
        and c:IsPreviousControler(tp)
        and c:IsPreviousLocation(LOCATION_MZONE)
        and c:IsPreviousPosition(POS_FACEUP)
end
```

The core checks the recorded previous code, alternate code, and the snapshot of
added set-code effects from that previous state.

Do not mix time frames accidentally. This is usually wrong in a leave-field
trigger:

```lua
-- The event describes the card before it left, but this asks about it now.
return c:IsPreviousLocation(LOCATION_MZONE) and c:IsSetCard(0x14f)
```

If location, position, controller, type, code, and set membership all describe
the departed card, keep all of those tests in the previous state.

## Fusion-Material Membership: `Card.IsFusionSetCard`

Fusion Material can gain an additional name or archetype only while being
tested as Fusion Material. Use `IsFusionSetCard` in Fusion procedure filters:

```lua
local f=aux.FilterBoolFunction(Card.IsFusionSetCard,0xa9)
aux.AddFusionProcCodeFun(c,34688023,f,1,true,true)
```

This pattern comes from Frightfur Leo (`c10383554.lua`).

`IsFusionSetCard` first accepts normal current `IsSetCard` membership, then
also checks:

- names supplied by `EFFECT_ADD_FUSION_CODE`, using the named card's set data;
- membership supplied by `EFFECT_ADD_FUSION_SETCODE`.

Use the matching Fusion-aware identity helpers together:

```lua
function s.matfilter(c)
    return c:IsFusionSetCard(0x1b0)
        and c:IsFusionType(TYPE_FUSION)
end
```

Do not substitute ordinary `IsSetCard`, `IsCode`, `IsType`, or `IsAttribute`
when the material can be treated differently specifically for Fusion use. See
[Fusion Procedure](fusion-procedure#fusion-specific-material-checks).

## Link-Material Membership: `Card.IsLinkSetCard`

Use `IsLinkSetCard` in Link Material filters:

```lua
local f=aux.FilterBoolFunction(Card.IsLinkSetCard,0xfc)
aux.AddLinkProcedure(c,f,2,2)
```

This pattern comes from Gouki Heel Ogre (`c10552026.lua`).

The local core accepts current `IsSetCard` membership and names supplied by
`EFFECT_ADD_LINK_CODE`; the added name's card data can provide the matching set
membership.

The local constants also contain `EFFECT_ADD_LINK_SETCODE`, but mark it
**reserved**, and the local core's `IsLinkSetCard` implementation does not read
it. Do not build a script around that reserved constant.

## The Summoning Card's Membership: `Card.IsSpecialSummonSetCard`

Despite being called on the Summoned monster, this method answers a different
question:

> Did the card that caused this Special Summon belong to the requested set?

Adamancipator Crystal - Dragite (`c10286023.lua`) uses it after being Special
Summoned:

```lua
function s.drcon(e,tp,eg,ep,ev,re,r,rp)
    return e:GetHandler():IsSpecialSummonSetCard(0x140)
end
```

The core checks the summoning card identity and set-code additions captured for
the Special Summon. It does not ask whether Dragite itself currently belongs to
`0x140`.

Use `c:IsSetCard(...)` when the rule describes the Summoned monster. Use
`c:IsSpecialSummonSetCard(...)` only when it describes the card responsible for
the summon.

## Synchro, Xyz, And Ritual Materials

This local core has no `IsSynchroSetCard`, `IsXyzSetCard`, or
`IsRitualSetCard`. Local procedures use ordinary current membership:

```lua
aux.AddSynchroProcedure(
    c,
    aux.FilterBoolFunction(Card.IsSetCard,0x29),
    aux.NonTuner(nil),
    1
)
```

The same principle applies to Xyz and Ritual filters unless a separate local
effect or helper explicitly changes the relevant identity. Do not invent a
material-specific method that the binding does not expose.

## When The Text Names One Card

An exact card name is not an archetype. Use `IsCode` for one named card or a
short list of named cards:

```lua
function s.filter(c)
    return c:IsCode(89943723)
end
```

Like `IsSetCard`, `IsCode` follows the card's current code and alternate-code
behavior. Several arguments mean “any of these names.”

Use `IsOriginalCodeRule` when a material, release, or similar rule explicitly
requires rule-original identity. Holactie the Creator of Light
(`c10000040.lua`) builds three separate checks this way:

```lua
s.spchecks=aux.CreateChecks(
    Card.IsOriginalCodeRule,
    {10000020,10000000,10000010}
)
```

For “a card that lists this exact card,” first register the metadata on the
listing card:

```lua
aux.AddCodeList(c,89943723)
```

Then use `aux.IsCodeListed(candidate,89943723)`. If either the named card itself
or a card that lists it is valid, use:

```lua
return aux.IsCodeOrListed(candidate,89943723)
```

These helpers read registered metadata; they do not scan translated card text.

## Cards That List A Set Name

“Belongs to an archetype” and “lists a monster from an archetype” are different
facts.

Register listed-set metadata in `initial_effect`:

```lua
function s.initial_effect(c)
    aux.AddSetNameMonsterList(c,0x62)
    -- effects...
end
```

Then another script can query it:

```lua
function s.thfilter(c)
    return aux.IsSetNameMonsterListed(c,0x62)
        and c:IsType(TYPE_SPELL+TYPE_TRAP)
        and c:IsAbleToHand()
end
```

`aux.AddSetNameMonsterList` does not make the card a member of that set. It
only records what the card lists. `aux.IsSetNameMonsterListed` returns false
when that metadata was never registered.

Blue-Eyes Toon Ultimate Dragon (`c71808988.lua`) demonstrates three distinct
possibilities in one practical filter:

```lua
function s.thfilter(c)
    return (c:IsSetCard(0x62)
            or aux.IsSetNameMonsterListed(c,0x62)
            or aux.IsCodeListed(c,15259703))
        and c:IsAbleToHand()
end
```

The candidates may belong to the set, list a monster from the set, or list one
specific card. Parentheses matter because the `IsAbleToHand` requirement must
apply to all three branches.

## Material-List Set Metadata

`aux.IsMaterialListSetCard` checks a script's `material_setcode` metadata. It
does not check whether the card itself belongs to the archetype.

A script supplies the metadata:

```lua
s.material_setcode=0x1017
```

Another script can inspect it:

```lua
function s.matval(e,c)
    return c:IsType(TYPE_SYNCHRO)
        and aux.IsMaterialListSetCard(c,0x1017)
end
```

Scrap Synchron (`c16449363.lua`) uses this pattern when deciding which Synchro
Monster can use it as extra material.

The helper accepts either one `material_setcode` value or a table of values and
uses the same base/subtype matching rule. If the metadata is absent, it returns
false.

## Adding Set Membership With Effects

### Current Membership

`EFFECT_ADD_SETCODE` makes affected cards count as a set for current
`IsSetCard` checks. Vernusylph Corolla (`c14108995.lua`) applies it to the
controller's EARTH monsters:

```lua
local e2=Effect.CreateEffect(c)
e2:SetType(EFFECT_TYPE_FIELD)
e2:SetRange(LOCATION_SZONE)
e2:SetTargetRange(LOCATION_MZONE,0)
e2:SetTarget(aux.TargetBoolFunction(Card.IsAttribute,ATTRIBUTE_EARTH))
e2:SetCode(EFFECT_ADD_SETCODE)
e2:SetValue(0x182)
c:RegisterEffect(e2)
```

For a temporary single-card addition, register a single effect and give it a
reset:

```lua
local e1=Effect.CreateEffect(e:GetHandler())
e1:SetType(EFFECT_TYPE_SINGLE)
e1:SetCode(EFFECT_ADD_SETCODE)
e1:SetValue(0x103)
e1:SetReset(RESET_EVENT+RESETS_STANDARD)
tc:RegisterEffect(e1)
```

Altergeist Adminia (`c61470213.lua`) uses that shape after taking control of a
monster.

### Fusion-Only Membership

Use `EFFECT_ADD_FUSION_SETCODE` when the card should gain the family only while
being considered as Fusion Material:

```lua
local e1=Effect.CreateEffect(e:GetHandler())
e1:SetType(EFFECT_TYPE_SINGLE)
e1:SetCode(EFFECT_ADD_FUSION_SETCODE)
e1:SetValue(0x1cd)
e1:SetReset(RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
tc:RegisterEffect(e1)
```

An ordinary `tc:IsSetCard(0x1cd)` does not consume this Fusion-only addition;
the material filter must use `tc:IsFusionSetCard(0x1cd)`.

Always copy the effect type, range/target range, and reset shape from a local
card with the same duration. Adding the correct value with the wrong lifetime
creates membership that disappears too early or persists too long.

## Requiring Different Families

Multiple arguments to `IsSetCard` are OR. For “1 card from family A and 1 card
from family B,” validate the selected Group.

EN Shuffle (`c10186633.lua`) uses `aux.gfcheck`:

```lua
function s.gcheck(g)
    return #g==1 and g:GetFirst():IsCode(89943723)
        or aux.gfcheck(g,Card.IsSetCard,0x3008,0x1f)
end
```

For a 2-card Group, `aux.gfcheck` tries both orders: one card must match the
first set code and the other must match the second.

For other group sizes or more complex requirements, write the rule explicitly.
For example, test that the Group contains at least one card from each family:

```lua
function s.gcheck(g)
    return g:IsExists(Card.IsSetCard,1,nil,0x3008)
        and g:IsExists(Card.IsSetCard,1,nil,0x1f)
end
```

Whether the same card may satisfy both requirements depends on the real card
text. `aux.gfcheck` requires two cards; two independent `IsExists` calls do not.

## Advanced Set-Code Contexts

### Virtual Monster Legality

`Duel.IsPlayerCanSpecialSummonMonster` has a `setcode` argument. It describes
the virtual card data used for a legality check, commonly for a Token or a Trap
being treated as a monster:

```lua
Duel.IsPlayerCanSpecialSummonMonster(
    tp,1154611,0xd4,TYPES_NORMAL_TRAP_MONSTER,
    1200,0,2,RACE_AQUA,ATTRIBUTE_WATER
)
```

This does not inspect an existing `Card` object. Keep this set code consistent
with the attributes used when the card is actually Special Summoned.

### Filtering `Duel.AnnounceCard`

`OPCODE_ISSETCARD` is not a normal card predicate. It is an opcode for the
postfix filter expression accepted by `Duel.AnnounceCard`:

```lua
local code=Duel.AnnounceCard(tp,0x51,OPCODE_ISSETCARD)
```

More complex local examples combine it with `OPCODE_ISTYPE`, `OPCODE_ISCODE`,
`OPCODE_AND`, `OPCODE_OR`, and `OPCODE_NOT`.

This filter checks database data for the card being announced. There is no
live card on the field, so temporary `EFFECT_ADD_SETCODE` membership is not
part of this test.

## Common Pitfalls

| Pitfall | Correct approach |
| --- | --- |
| Comparing a displayed archetype name. | Use a verified numeric set code. |
| Comparing or unpacking `datas.setcode` in Lua. | Call the matching `Is...SetCard` method. |
| Guessing a set code from another simulator or memory. | Search local scripts and local card data. |
| Treating `c:IsSetCard(a,b)` as “A and B.” | It means “A or B”; validate a Group for separate requirements. |
| Using `IsSetCard` in a leave-field event while other checks use previous state. | Use `IsPreviousSetCard` with the other `IsPrevious...` methods. |
| Using current membership for an original-identity rule. | Use `IsOriginalSetCard`. |
| Using ordinary membership in a Fusion or Link material procedure. | Use `IsFusionSetCard` or `IsLinkSetCard`. |
| Asking whether the Summoned monster belongs to the summoning card's set with `IsSpecialSummonSetCard`. | Remember that this method checks the card that caused the summon. |
| Treating `AddSetNameMonsterList` as archetype membership. | It registers “lists a monster from this set” metadata only. |
| Treating `material_setcode` as the card's own set. | It describes material-list metadata only. |
| Using reserved `EFFECT_ADD_LINK_SETCODE`. | The local core does not consume it; follow `IsLinkSetCard`/`EFFECT_ADD_LINK_CODE` patterns. |
| Confusing `Card.SetCardTarget` or `Duel.ShuffleSetCard` with set codes. | In those names, “Set” is a different verb; neither checks archetypes. |
| Omitting parentheses around mixed `and`/`or` family rules. | Group alternatives, then apply shared restrictions. |

## A Safe Research Workflow

1. Search local scripts for a known card ID from the same family.
2. Confirm the set value in several nearby scripts or in local card data.
3. Decide whether the rule needs current, original, previous, material-only, or
   summon-source identity.
4. Decide whether the text says “belongs to,” “lists,” or “lists as material.”
5. Add the visible type, location, face-up, and action-legality restrictions.
6. Test a broad member, a subfamily member, a non-member, a temporarily renamed
   card, and any previous-state/material edge case the effect can encounter.

Useful API pages:

- [`Card.IsSetCard`](/api/functions/Card/IsSetCard)
- [`Card.IsOriginalSetCard`](/api/functions/Card/IsOriginalSetCard)
- [`Card.IsPreviousSetCard`](/api/functions/Card/IsPreviousSetCard)
- [`Card.IsFusionSetCard`](/api/functions/Card/IsFusionSetCard)
- [`Card.IsLinkSetCard`](/api/functions/Card/IsLinkSetCard)
- [`Card.IsSpecialSummonSetCard`](/api/functions/Card/IsSpecialSummonSetCard)
- [`Card.IsCode`](/api/functions/Card/IsCode)
- [`Card.IsOriginalCodeRule`](/api/functions/Card/IsOriginalCodeRule)
- [`Auxiliary.AddCodeList`](/api/functions/Auxiliary/AddCodeList)
- [`Auxiliary.AddSetNameMonsterList`](/api/functions/Auxiliary/AddSetNameMonsterList)
- [`Auxiliary.IsCodeListed`](/api/functions/Auxiliary/IsCodeListed)
- [`Auxiliary.IsCodeOrListed`](/api/functions/Auxiliary/IsCodeOrListed)
- [`Auxiliary.IsSetNameMonsterListed`](/api/functions/Auxiliary/IsSetNameMonsterListed)
- [`Auxiliary.IsMaterialListSetCard`](/api/functions/Auxiliary/IsMaterialListSetCard)
- [`Auxiliary.gfcheck`](/api/functions/Auxiliary/gfcheck)
- [`Duel.IsPlayerCanSpecialSummonMonster`](/api/functions/Duel/IsPlayerCanSpecialSummonMonster)
- [`Duel.AnnounceCard`](/api/functions/Duel/AnnounceCard)
