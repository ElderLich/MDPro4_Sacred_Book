# Link Procedure Guide

Link scripts are built around Link Rating, Link Materials, and zones pointed to
by Link Markers. A normal Link Monster registers a rule Summon procedure in the
Extra Deck. During that procedure, the player selects a legal material group,
the selected cards are recorded as materials, and the helper sends them to the
GY with `REASON_MATERIAL+REASON_LINK`.

Effects can also make a player Link Summon during resolution. Those effects
should still ask the chosen Link Monster whether the current material group is
legal before calling the core Summon function.

## The Three Jobs

| Job | Where it usually lives | What it does |
| --- | --- | --- |
| Link Monster procedure | The Link Monster script in `initial_effect` | Registers an `EFFECT_SPSUMMON_PROC` in the Extra Deck with `SUMMON_TYPE_LINK`. |
| Effect that performs a Link Summon | A Spell, Trap, or monster effect | Checks [`Card.IsLinkSummonable`](/api/functions/Card/IsLinkSummonable), then calls [`Duel.LinkSummon`](/api/functions/Duel/LinkSummon). |
| Link Marker and linked-zone effects | Usually on a Link Monster after it is on the field | Reads linked groups, linked zones, mutual links, columns, or Link Material properties. |

For a normal Link Monster, start with the first job. The procedure is what
teaches the engine how that monster can be Link Summoned.

## Standard Link Procedure

Beat Cop from the Underworld (`c99011763.lua`) has the simplest "2 monsters"
shape:

```lua
function c99011763.initial_effect(c)
    c:EnableReviveLimit()
    aux.AddLinkProcedure(c,nil,2,2)
end
```

Read that as:

| Piece | Meaning |
| --- | --- |
| `aux.AddLinkProcedure` | Registers the Link Summon procedure on the Extra Deck monster. |
| `nil` | No extra material filter; any legal Link Material can be used. |
| `2` | Minimum number of material cards selected. |
| `2` | Maximum number of material cards selected. |
| `c:EnableReviveLimit()` | Marks the Link Monster as needing a proper Summon before it can be revived by ordinary revive effects. |

Cyberse Witch (`c11674673.lua`) shows the same pattern with a per-material
filter:

```lua
aux.AddLinkProcedure(c,aux.FilterBoolFunction(Card.IsLinkRace,RACE_CYBERSE),2,2)
c:EnableReviveLimit()
```

The filter is checked on each candidate material. Here, each material must be a
Cyberse Link Material according to [`Card.IsLinkRace`](/api/functions/Card/IsLinkRace).

## Helper Arguments

The standard helper is:

```lua
aux.AddLinkProcedure(c,f,min,max,gf)
```

| Argument | Meaning |
| --- | --- |
| `c` | The Link Monster receiving the procedure. |
| `f` | Optional per-material filter. `nil` means no extra Type, Race, Attribute, Set, or name restriction. |
| `min` | Minimum number of material cards the player must select. |
| `max` | Optional maximum number of material cards. When omitted, local `procedure.lua` uses `c:GetLink()`. |
| `gf` | Optional whole-group check. Use this for text that depends on the selected group as a whole. |

Exceed the Pendulum (`c92812851.lua`) uses a group check:

```lua
aux.AddLinkProcedure(c,aux.FilterBoolFunction(Card.IsType,TYPE_EFFECT),2,99,s.gchk)

function s.gchk(g)
    return g:IsExists(Card.IsType,1,nil,TYPE_PENDULUM)
end
```

The per-card filter requires every material to be an Effect Monster. The group
check then requires at least one selected material to be a Pendulum Monster.
This is a common split: use `f` for "each material must be..." and `gf` for
"among those materials, the full group must also..."

## What The Helper Builds

Local `procedure.lua` creates and registers this procedure:

```lua
local e1=Effect.CreateEffect(c)
e1:SetDescription(1166)
e1:SetType(EFFECT_TYPE_FIELD)
e1:SetCode(EFFECT_SPSUMMON_PROC)
e1:SetProperty(EFFECT_FLAG_CANNOT_DISABLE+EFFECT_FLAG_UNCOPYABLE)
e1:SetRange(LOCATION_EXTRA)
e1:SetCondition(Auxiliary.LinkCondition(f,min,max,gf))
e1:SetTarget(Auxiliary.LinkTarget(f,min,max,gf))
e1:SetOperation(Auxiliary.LinkOperation(f,min,max,gf))
e1:SetValue(SUMMON_TYPE_LINK)
c:RegisterEffect(e1)
```

This is a rule procedure, not an activated effect. It does not make a Chain
Link. The core asks the condition whether a legal Link Summon exists, the
target branch lets the player choose Link Materials, and the operation branch
moves those materials.

The helper refuses its procedure for a face-up Pendulum Link Monster in the
Extra Deck. That check is directly in `Auxiliary.LinkCondition`.

## Link Rating And Material Count

`min` and `max` limit the number of cards selected. They are not the total Link
Rating. The total Link Rating check happens separately:

```lua
sg:CheckWithSumEqual(Auxiliary.GetLinkCount,lc:GetLink(),#sg,#sg)
```

That line means: the selected group must be able to sum to the Link Monster's
Link Rating, using one count value per selected card.

Local [`Auxiliary.GetLinkCount`](/api/functions/Auxiliary/GetLinkCount) gives
ordinary materials a value of `1`. A Link Monster with Link Rating greater than
1 can count as either `1` or its own Link Rating. The helper encodes that
choice for `Group.CheckWithSumEqual`.

That is why a Link-4 with `min=2,max=4` can usually accept:

| Selected materials | Why the sum can work |
| --- | --- |
| Four non-Link monsters | `1+1+1+1=4` |
| One Link-2 and two non-Link monsters | `2+1+1=4` |
| One Link-3 and one non-Link monster | `3+1=4` |
| Two Link-2 monsters | `2+2=4` |

The selected card count must still stay inside `min` and `max`. A Link-4 helper
with `min=3,max=4` would not accept only two Link-2 monsters, even though their
Link Rating sum can equal 4.

## Material Pool

The ordinary material pool comes from your Monster Zone:

```lua
local mg=Duel.GetMatchingGroup(Auxiliary.LConditionFilter,tp,LOCATION_MZONE,0,nil,f,lc,e)
```

`Auxiliary.LConditionFilter` checks that the card:

- is face-up if it is on the field, unless the procedure effect has
  `EFFECT_FLAG_SET_AVAILABLE`
- can be used as Link Material for the Link Monster through
  [`Card.IsCanBeLinkMaterial`](/api/functions/Card/IsCanBeLinkMaterial)
- passes the optional per-material filter `f`

If an effect calls `Duel.LinkSummon` with a material group, the helper filters
that group instead of starting from the whole Monster Zone.

Local Link procedures also account for:

- mandatory Link Materials through `EFFECT_MUST_BE_LMATERIAL`
- Extra Monster Zone and Main Monster Zone availability through
  [`Duel.GetLocationCountFromEx`](/api/functions/Duel/GetLocationCountFromEx)
- optional whole-group checks through `gf(sg,lc,tp)`
- fixed required material through the `lmat` argument used by effect-driven
  Link Summons
- extra Link Material effects through `EFFECT_EXTRA_LINK_MATERIAL`

`Auxiliary.GetLinkMaterials` can include extra candidates from the hand, Spell &
Trap Zone, or opponent's field only when a related `EFFECT_EXTRA_LINK_MATERIAL`
effect says that candidate is usable. The procedure then checks compatibility
again after the group is selected and consumes the extra-material effect's count
limit with `te:UseCountLimit(tp)`.

## Operation Order

The ordinary operation is short and important:

```lua
local g=e:GetLabelObject()
c:SetMaterial(g)
Auxiliary.LExtraMaterialCount(g,c,tp)
Duel.SendtoGrave(g,REASON_MATERIAL+REASON_LINK)
g:DeleteGroup()
```

The selected group was kept alive by the target branch, then stored on the
procedure effect. During operation:

1. [`Card.SetMaterial`](/api/functions/Card/SetMaterial) records the group as
   the Link Monster's materials.
2. `Auxiliary.LExtraMaterialCount` consumes compatible extra-material count
   limits.
3. [`Duel.SendtoGrave`](/api/functions/Duel/SendtoGrave) sends the selected
   cards to the GY with `REASON_MATERIAL+REASON_LINK`.
4. The kept-alive group is deleted.

Unlike Xyz Summons, Link Materials do not become overlay materials under the
new monster. A normal Link procedure sends them to the GY.

## Effects That Link Summon

World Legacy Awakens (`c12989604.lua`) is a clean Spell example. It asks the
Extra Deck for any Link Monster that is currently Link Summonable:

```lua
function c12989604.filter(c)
    return c:IsLinkSummonable(nil)
end

function c12989604.target(e,tp,eg,ep,ev,re,r,rp,chk)
    if chk==0 then
        return Duel.IsExistingMatchingCard(c12989604.filter,tp,LOCATION_EXTRA,0,1,nil)
    end
    Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,nil,1,0,0)
end

function c12989604.activate(e,tp,eg,ep,ev,re,r,rp)
    Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SPSUMMON)
    local g=Duel.SelectMatchingCard(tp,c12989604.filter,tp,LOCATION_EXTRA,0,1,1,nil)
    local tc=g:GetFirst()
    if tc then
        Duel.LinkSummon(tp,tc,nil)
    end
end
```

The `nil` material group means "use that Link Monster's normal material pool."
The selected Link Monster's registered procedure still performs final material
selection and movement.

Prank-Kids Plan (`c15447747.lua`) uses a restricted material group:

```lua
function c15447747.matfilter(c)
    return c:IsFaceup() and c:IsSetCard(0x120)
end

function c15447747.lkfilter(c,mg)
    return c:IsSetCard(0x120) and c:IsLinkSummonable(mg)
end

function c15447747.lkop(e,tp,eg,ep,ev,re,r,rp)
    local mg=Duel.GetMatchingGroup(c15447747.matfilter,tp,LOCATION_MZONE,0,nil)
    Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SPSUMMON)
    local tg=Duel.SelectMatchingCard(tp,c15447747.lkfilter,tp,LOCATION_EXTRA,0,1,1,nil,mg)
    local tc=tg:GetFirst()
    if tc then
        Duel.LinkSummon(tp,tc,mg)
    end
end
```

Here, the effect only permits face-up Prank-Kids monsters you control as the
material group. The Extra Deck filter receives that group and asks each
Prank-Kids Link Monster whether it can be Link Summoned with it.

The core bindings for [`Card.IsLinkSummonable`](/api/functions/Card/IsLinkSummonable)
and [`Duel.LinkSummon`](/api/functions/Duel/LinkSummon) both reject use during
the Damage Step. `Duel.LinkSummon` yields to the core and returns no Lua value.

## Fixed Required Material

Some effects require a specific card to be used as Link Material. Outburst
Dragon (`c87263576.lua`) does that with the `lcard` argument:

```lua
function c87263576.lkfilter(c,lc)
    return c:IsRace(RACE_DRAGON) and c:IsLinkSummonable(nil,lc)
end

function c87263576.lkop(e,tp,eg,ep,ev,re,r,rp)
    local c=e:GetHandler()
    if c:IsControler(1-tp) or not c:IsRelateToEffect(e) or c:IsFacedown() then return end
    local g=Duel.GetMatchingGroup(c87263576.lkfilter,tp,LOCATION_EXTRA,0,nil,c)
    if g:GetCount()>0 then
        Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SPSUMMON)
        local sg=g:Select(tp,1,1,nil)
        Duel.LinkSummon(tp,sg:GetFirst(),nil,c)
    end
end
```

The fourth argument to `Duel.LinkSummon` is the required material. In
`Auxiliary.LinkCondition`, that card is added to the material pool only if it
passes the Link Material filter, and `Auxiliary.LCheckGoal` requires the final
selected group to contain it.

Use this shape when the effect text says to immediately Link Summon using that
specific monster.

## Using An Opponent's Monster

Unchained Soul of Disaster (`c89019964.lua`) shows a controlled way to use an
opponent's monster as part of the temporary material group:

```lua
function c89019964.tgfilter(c,tp,ec)
    local mg=Group.FromCards(ec,c)
    return c:IsFaceup() and Duel.IsExistingMatchingCard(c89019964.lfilter,tp,LOCATION_EXTRA,0,1,nil,mg)
end

function c89019964.lfilter(c,mg)
    return c:IsAttribute(ATTRIBUTE_DARK) and c:IsLinkSummonable(mg,nil,2,2)
end

function c89019964.operation(e,tp,eg,ep,ev,re,r,rp)
    local c=e:GetHandler()
    local tc=Duel.GetFirstTarget()
    if c:IsFaceup() and c:IsRelateToEffect(e) and c:IsControler(tp)
        and tc:IsFaceup() and tc:IsRelateToEffect(e) and tc:IsControler(1-tp)
        and not tc:IsImmuneToEffect(e) then
        local mg=Group.FromCards(c,tc)
        Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SPSUMMON)
        local g=Duel.SelectMatchingCard(tp,c89019964.lfilter,tp,LOCATION_EXTRA,0,1,1,nil,mg)
        local lc=g:GetFirst()
        if lc then
            Duel.LinkSummon(tp,lc,mg,nil,2,2)
        end
    end
end
```

The operation rebuilds the exact two-card group at resolution and checks that
both monsters are still face-up, related, controlled by the expected players,
and not immune to the effect. That is the habit to copy: do not trust a target
chosen earlier if the field can change before resolution.

## Reading Linked Zones

Link Monsters often need to know which zones their Link Markers point to.
Gorgon of Zilofthonia (`c12067160.lua`) uses several linked-zone APIs:

```lua
function s.zonelimit(e)
    return 0x7f007f & ~e:GetHandler():GetLinkedZone()
end

function s.antg(e,c)
    return e:GetHandler():GetLinkedGroup():IsContains(c)
end

function s.discon(e,tp,eg,ep,ev,re,r,rp)
    local rc=re:GetHandler()
    return rc and re:IsActiveType(TYPE_MONSTER) and rc:IsRelateToChain()
        and e:GetHandler():GetLinkedGroup():IsContains(rc)
        and rc:IsCanBeDisabledByEffect(e) and Duel.IsChainDisablable(ev)
end
```

Use [`Card.GetLinkedGroup`](/api/functions/Card/GetLinkedGroup) when you need
the actual cards in linked zones. Use
[`Card.GetLinkedZone`](/api/functions/Card/GetLinkedZone) when you need the zone
mask itself.

Cyberse Witch also shows why the optional `player` argument matters:

```lua
function c11674673.thcfilter(c,ec)
    if c:IsLocation(LOCATION_MZONE) then
        return ec:GetLinkedGroup():IsContains(c)
    else
        return bit.extract(ec:GetLinkedZone(c:GetPreviousControler()),c:GetPreviousSequence())~=0
    end
end
```

The card was Special Summoned and may no longer be in the same place by the
time the trigger checks the event group. Passing `c:GetPreviousControler()`
asks for the linked-zone mask from the relevant player's perspective, then
`bit.extract` checks the previous sequence.

For field-wide checks, use [`Duel.GetLinkedZone`](/api/functions/Duel/GetLinkedZone)
or [`Duel.GetLinkedGroup`](/api/functions/Duel/GetLinkedGroup). For mutual-link
effects, use the mutual versions:
[`Card.GetMutualLinkedGroup`](/api/functions/Card/GetMutualLinkedGroup),
[`Card.GetMutualLinkedZone`](/api/functions/Card/GetMutualLinkedZone), and
their count helpers.

## Material Memory

After a successful Link Summon, the new Link Monster can inspect its materials
with [`Card.GetMaterial`](/api/functions/Card/GetMaterial). Beat Cop from the
Underworld uses `EFFECT_MATERIAL_CHECK` to remember whether its materials had
different names and included at least two DARK materials:

```lua
function c99011763.valcheck(e,c)
    local g=c:GetMaterial()
    if g:GetClassCount(Card.GetLinkCode)==g:GetCount()
        and g:IsExists(Card.IsLinkAttribute,2,nil,ATTRIBUTE_DARK) then
        e:GetLabelObject():SetLabel(1)
    else
        e:GetLabelObject():SetLabel(0)
    end
end
```

Use Link-specific identity helpers when material text cares about Link Material
properties:

| Helper | Use |
| --- | --- |
| [`Card.GetLinkCode`](/api/functions/Card/GetLinkCode) | Material name/code while used for a Link Summon. |
| [`Card.IsLinkCode`](/api/functions/Card/IsLinkCode) | Code check using Link Material identity. |
| [`Card.IsLinkRace`](/api/functions/Card/IsLinkRace) | Race check using Link Material identity. |
| [`Card.IsLinkAttribute`](/api/functions/Card/IsLinkAttribute) | Attribute check using Link Material identity. |
| [`Card.IsLinkType`](/api/functions/Card/IsLinkType) | Type check using Link Material identity. |

## Common Pitfalls

| Mistake | Better habit |
| --- | --- |
| Forgetting `EnableReviveLimit` on a Link Monster. | Put it near `aux.AddLinkProcedure` in `initial_effect`. |
| Treating `min` and `max` as Link Rating limits. | Read them as the number of selected material cards. Link Rating is checked with `Auxiliary.GetLinkCount`. |
| Assuming every Link Monster material always contributes its Link Rating. | A Link Monster with Link Rating greater than 1 may count as 1 or its Link Rating. |
| Sending materials manually in an effect before calling `Duel.LinkSummon`. | Let the selected Link Monster's procedure choose, record, and send materials. |
| Calling `Duel.LinkSummon` without a matching `Card.IsLinkSummonable` check. | Check the Extra Deck candidates first, then recheck or rebuild the group in the operation if the field may have changed. |
| Forgetting that `Duel.LinkSummon` has no Lua return value. | Put follow-up logic in later events or structure the effect around the Summon itself. |
| Using a target-branch material group after resolution changes. | Rebuild the group in the operation and verify cards are still face-up, related, and controlled correctly. |
| Checking linked zones with the wrong player perspective. | Pass the player argument to `GetLinkedZone` when previous controller or opponent perspective matters. |
| Confusing linked cards with linked zone masks. | Use `GetLinkedGroup` for cards and `GetLinkedZone` for bitmasks. |
| Trying to Link Summon during the Damage Step. | Local core rejects `Card.IsLinkSummonable` and `Duel.LinkSummon` during the Damage Step. |

## Useful API Pages

- [`Auxiliary.AddLinkProcedure`](/api/functions/Auxiliary/AddLinkProcedure)
- [`Auxiliary.GetLinkCount`](/api/functions/Auxiliary/GetLinkCount)
- [`Auxiliary.GetLinkMaterials`](/api/functions/Auxiliary/GetLinkMaterials)
- [`Auxiliary.LinkCondition`](/api/functions/Auxiliary/LinkCondition)
- [`Auxiliary.LinkTarget`](/api/functions/Auxiliary/LinkTarget)
- [`Auxiliary.LinkOperation`](/api/functions/Auxiliary/LinkOperation)
- [`Card.IsLinkSummonable`](/api/functions/Card/IsLinkSummonable)
- [`Card.IsCanBeLinkMaterial`](/api/functions/Card/IsCanBeLinkMaterial)
- [`Duel.LinkSummon`](/api/functions/Duel/LinkSummon)
- [`Duel.GetLocationCountFromEx`](/api/functions/Duel/GetLocationCountFromEx)
- [`Card.GetLinkedGroup`](/api/functions/Card/GetLinkedGroup)
- [`Card.GetLinkedGroupCount`](/api/functions/Card/GetLinkedGroupCount)
- [`Card.GetLinkedZone`](/api/functions/Card/GetLinkedZone)
- [`Card.GetMutualLinkedGroup`](/api/functions/Card/GetMutualLinkedGroup)
- [`Card.GetMutualLinkedGroupCount`](/api/functions/Card/GetMutualLinkedGroupCount)
- [`Card.GetMutualLinkedZone`](/api/functions/Card/GetMutualLinkedZone)
- [`Duel.GetLinkedGroup`](/api/functions/Duel/GetLinkedGroup)
- [`Duel.GetLinkedGroupCount`](/api/functions/Duel/GetLinkedGroupCount)
- [`Duel.GetLinkedZone`](/api/functions/Duel/GetLinkedZone)
- [`Card.GetLinkCode`](/api/functions/Card/GetLinkCode)
- [`Card.IsLinkCode`](/api/functions/Card/IsLinkCode)
- [`Card.GetLink`](/api/functions/Card/GetLink)
- [`Card.IsLinkRace`](/api/functions/Card/IsLinkRace)
- [`Card.IsLinkAttribute`](/api/functions/Card/IsLinkAttribute)
- [`Card.IsLinkType`](/api/functions/Card/IsLinkType)
- [`Card.GetMaterial`](/api/functions/Card/GetMaterial)
- [`Card.SetMaterial`](/api/functions/Card/SetMaterial)
- [`Duel.SendtoGrave`](/api/functions/Duel/SendtoGrave)
- [`Group.CheckWithSumEqual`](/api/functions/Group/CheckWithSumEqual)
- [`Group.SelectSubGroup`](/api/functions/Group/SelectSubGroup)
- [`Group.GetClassCount`](/api/functions/Group/GetClassCount)
