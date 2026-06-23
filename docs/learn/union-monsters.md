# Union Monsters

Union Monsters are monsters that can become Equip Cards and later return to the
Monster Zone. In local MDPro3/YGOPro scripts, modern Union behavior is centered
on [`aux.EnableUnionAttribute`](/api/functions/Auxiliary/EnableUnionAttribute)
and [`aux.SetUnionState`](/api/functions/Auxiliary/SetUnionState).

The important thing to remember is that equipping a monster with
[`Duel.Equip`](/api/functions/Duel/Equip) is not enough by itself. A Union card
also needs the Union status and equip-limit effects that make the core treat it
as a Union Equip Card.

## The Standard Modern Union Package

Most modern Union Monsters start like this:

```lua
function s.initial_effect(c)
    aux.EnableUnionAttribute(c,s.eqfilter)
end

function s.eqfilter(c)
    return c:IsRace(RACE_MACHINE) and c:IsAttribute(ATTRIBUTE_LIGHT)
end
```

The filter receives the monster that the Union card may equip to. Union Pilot
(`c89357740.lua`) uses a broad filter:

```lua
function s.eqfilter(c)
    return c:IsType(TYPE_EFFECT)
end
```

`aux.EnableUnionAttribute` registers four pieces:

| Piece | Why it matters |
| --- | --- |
| Equipped destroy substitute | Lets the equipped Union card be destroyed instead of the equipped monster. |
| `EFFECT_UNION_LIMIT` | Stores the legal equip-target filter for the Union card. |
| Monster Zone ignition effect | Equips the Union Monster to a legal face-up monster you control. |
| Spell & Trap Zone ignition effect | Special Summons the equipped Union Monster back to the Monster Zone. |

The helper also uses the shared Union flag (`FLAG_ID_UNION`) to stop the same
Union card from equipping and unequipping repeatedly in the same turn through
the shared ignition package.

## Manual Union Equips

Some effects equip a Union Monster from the Deck, GY, banishment, or another
location. Those effects must do the Union legality checks themselves, then call
`aux.SetUnionState` after the equip succeeds.

Union Hangar (`c66399653.lua`) is the key local example:

```lua
function s.union_filter(c,ec,tp)
    return c:IsRace(RACE_MACHINE)
        and c:IsAttribute(ATTRIBUTE_LIGHT)
        and c:IsType(TYPE_UNION)
        and not c:IsCode(ec:GetCode())
        and c:CheckUniqueOnField(tp)
        and not c:IsForbidden()
        and c:CheckUnionTarget(ec)
        and aux.CheckUnionEquip(c,ec)
end
```

The operation equips the selected Union and then applies Union state:

```lua
local ec=sg:GetFirst()
if ec and Duel.Equip(tp,ec,tc) then
    aux.SetUnionState(ec)
end
```

That final line is the difference between "a card equipped by an effect" and "a
Union card equipped as a Union card."

## What `SetUnionState` Adds

[`aux.SetUnionState`](/api/functions/Auxiliary/SetUnionState) reads the card's
registered `EFFECT_UNION_LIMIT`. If the card has one, it registers:

| Effect | Purpose |
| --- | --- |
| `EFFECT_EQUIP_LIMIT` | Keeps the Union card equipped only to legal targets. |
| `EFFECT_UNION_STATUS` | Marks the equipped card as a modern Union card for core Union counts. |
| `EFFECT_OLDUNION_STATUS` | Added only for old Union scripts that set `old_union`. |

If the card does not have `EFFECT_UNION_LIMIT`, `SetUnionState` has nothing to
copy and returns without making a Union state. That is why most manual equip
filters also call [`Card.CheckUnionTarget`](/api/functions/Card/CheckUnionTarget):

```lua
return c:IsType(TYPE_UNION)
    and c:CheckUnionTarget(target)
    and aux.CheckUnionEquip(c,target)
```

## Union Counts

The local core tracks two Union counts on the equipped monster:

```lua
local modern_count,old_count=tc:GetUnionCount()
```

[`Card.GetUnionCount`](/api/functions/Card/GetUnionCount) returns the modern
Union count first and the old Union count second. Local
[`aux.CheckUnionEquip`](/api/functions/Auxiliary/CheckUnionEquip) wraps those
counts and applies the modern-vs-old compatibility rule used by Union scripts.

Union Driver (`c99249638.lua`) shows why the optional third argument exists:

```lua
local exct=aux.IsUnionState(e) and 1 or 0
return Duel.IsExistingMatchingCard(s.refilter,tp,LOCATION_DECK,0,1,nil,
    c:GetEquipTarget(),tp,exct)
```

When a currently equipped Union card replaces itself with another Union, the
script can ignore the current modern Union count during the check. That lets it
test the state after the replacement, not the crowded state before the
replacement.

## Checking Equipped Union State

Use [`aux.IsUnionState`](/api/functions/Auxiliary/IsUnionState) when an effect
should work only while the handler is equipped as a Union card:

```lua
function s.condition(e,tp,eg,ep,ev,re,r,rp)
    return aux.IsUnionState(e)
end
```

The helper checks both `EFFECT_UNION_STATUS` and whether the handler has an
equip target. That is safer than checking only `LOCATION_SZONE`.

## Unequipping To The Monster Zone

The shared helper registers the usual unequip ignition effect automatically.
If a card scripts its own unequip, copy the same resolution discipline:

```lua
function s.sptg(e,tp,eg,ep,ev,re,r,rp,chk)
    local c=e:GetHandler()
    if chk==0 then
        return Duel.GetLocationCount(tp,LOCATION_MZONE)>0
            and c:GetEquipTarget()
            and c:IsCanBeSpecialSummoned(e,0,tp,true,false)
    end
    Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,c,1,0,0)
end

function s.spop(e,tp,eg,ep,ev,re,r,rp)
    local c=e:GetHandler()
    if c:IsRelateToEffect(e) then
        Duel.SpecialSummon(c,0,tp,tp,true,false,POS_FACEUP)
    end
end
```

Check Monster Zone space in the target branch and recheck that the card is
still related to the effect at resolution.

## Support Searches

Use `TYPE_UNION` for actual Union Monsters:

```lua
function s.filter(c)
    return c:IsType(TYPE_UNION) and c:IsAbleToHand()
end
```

Support Spell/Trap Cards that mention Union can be marked with:

```lua
s.has_text_type=TYPE_UNION
```

Then another script can search Union-related Spell/Trap Cards with
[`aux.IsTypeInText`](/api/functions/Auxiliary/IsTypeInText), as Union
Controller (`c2133971.lua`) does.

## Common Mistakes

| Mistake | Better pattern |
| --- | --- |
| Calling `Duel.Equip` and stopping there. | Call `aux.SetUnionState(equipped_union)` after a successful manual Union equip. |
| Ignoring equip-target legality. | Check `c:CheckUnionTarget(target)` and `aux.CheckUnionEquip(c,target)` before selecting. |
| Forgetting Spell & Trap Zone space. | Check `Duel.GetLocationCount(tp,LOCATION_SZONE)>0` before equipping from another location. |
| Treating every equipped monster as a Union card. | Use `aux.IsUnionState(e)` or `EFFECT_UNION_STATUS`-aware helpers. |
| Mixing old and modern Union counts by hand. | Prefer `aux.CheckUnionEquip` unless you are deliberately maintaining legacy Union behavior. |

The Union rule of thumb is blunt but useful: any effect that equips a Union
Monster by hand must also recreate the Union state, or the card is merely
equipped.
