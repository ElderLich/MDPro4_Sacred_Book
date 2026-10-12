# Field Zones And Sequences

Field-zone scripts usually combine three different ideas:

- a location constant, such as `LOCATION_MZONE` or `LOCATION_SZONE`
- a sequence number, such as `c:GetSequence()`
- a zone mask, such as the mask returned by `Duel.GetLocationCount`

Keep those ideas separate. Locations say where a card is. Sequences say which
slot inside that location. Masks say which slots are usable, selected, linked,
or unavailable.

## Count Available Zones

Use `Duel.GetLocationCount` when a card needs an open Monster Zone or Spell &
Trap Zone right now:

```lua
if Duel.GetLocationCount(tp,LOCATION_MZONE)<=0 then return end
```

The MDPro4/YGOPro core returns two values: the count and the usable zone mask.
Most scripts only store the first value:

```lua
local ft=Duel.GetLocationCount(tp,LOCATION_MZONE)
```

The core comment for `GetLocationCount` says the count can be negative. That
matters when a cost or effect will free a zone. In `c1003840.lua`, the cost can
Tribute a monster from the player's Main Monster Zone, so activation accepts
`ft>-1`; the operation still rechecks for an open zone before Special
Summoning:

```lua
function c1003840.spcost(e,tp,eg,ep,ev,re,r,rp,chk)
    local ft=Duel.GetLocationCount(tp,LOCATION_MZONE)
    if chk==0 then return ft>-1 and Duel.CheckReleaseGroup(tp,c1003840.cfilter,1,nil,e,tp,ft) end
    local g=Duel.SelectReleaseGroup(tp,c1003840.cfilter,1,1,nil,e,tp,ft)
    e:SetLabel(g:GetFirst():GetLevel())
    Duel.Release(g,REASON_COST)
end

function c1003840.spop(e,tp,eg,ep,ev,re,r,rp)
    if not e:GetHandler():IsRelateToEffect(e) or Duel.GetLocationCount(tp,LOCATION_MZONE)<=0 then return end
    -- select and Special Summon
end
```

Recheck zone availability in the operation whenever another Chain response
could change the field before the effect resolves.

## Count A Zone That Will Be Freed

Use `Duel.GetMZoneCount` or `Duel.GetSZoneCount` when a chosen card or group is
expected to leave the field before the new card is placed. The core temporarily
counts `targets` as gone, then returns the count and usable mask.

`c10186633.lua` checks whether returning a monster to the Deck will free enough
Monster Zone space for the later Special Summon:

```lua
function c10186633.tdfilter(c,e,tp)
    return c:IsFaceup() and c:IsType(TYPE_MONSTER)
        and c:IsAbleToDeck() and Duel.GetMZoneCount(tp,c)>0
        and Duel.IsExistingMatchingCard(c10186633.spfilter,tp,LOCATION_DECK,0,1,nil,e,tp,c:GetCode())
end
```

`c10024317.lua` does the same kind of check for the Spell & Trap Zone before a
Spell/Trap is Set from the Deck:

```lua
function c10024317.desfilter(c,tp)
    if c:IsFacedown() then return false end
    return Duel.GetSZoneCount(tp,c)>0
        and Duel.IsExistingMatchingCard(c10024317.filter,tp,LOCATION_DECK,0,1,nil,true)
end
```

If the card is not guaranteed to leave by the time the placement happens, do
not use it as the `targets` argument.

## Sequence Numbers

`Card.GetSequence` returns the card's raw sequence inside its current location.
For ordinary Main Monster Zones and Spell & Trap Zones, scripts treat sequences
`0` through `4` as the five normal slots. This is why many scripts guard zone
math with `seq<5` or `seq>4`.

`c10852583.lua` only moves itself between ordinary Main Monster Zones:

```lua
function c10852583.seqcon(e,tp,eg,ep,ev,re,r,rp)
    local seq=e:GetHandler():GetSequence()
    if seq>4 then return false end
    return (seq>0 and Duel.CheckLocation(tp,LOCATION_MZONE,seq-1))
        or (seq<4 and Duel.CheckLocation(tp,LOCATION_MZONE,seq+1))
end
```

Extra Monster Zones can appear as Monster Zone sequences `5` and `6` in zone
logic. The local `utility.lua` maps them to columns 1 and 3 for column-based
effects. The source define file also documents the Field Zone sequence as `5`
when reading `Card.GetSequence` on a Field Spell.

## Zone Masks

Zone masks are player-relative bitmasks. The `SelectDisableField` define
comment and core binding use this layout:

| Zone from `player` viewpoint | Bit for `seq` |
| --- | --- |
| player's Monster Zone | `0x1 << seq` |
| player's Spell & Trap Zone | `0x1 << (seq+8)` |
| opponent's Monster Zone | `0x1 << (seq+16)` |
| opponent's Spell & Trap Zone | `0x1 << (seq+24)` |

For normal Main Monster Zones and Spell & Trap Zones, `seq` is usually `0`
through `4`. Monster Zone masks may also include `5` and `6` for Extra Monster
Zones when the selection allows them.

`Duel.SelectDisableField(player,count,location1,location2,filter)` lets the
player select available zones and returns the selected mask. Its `filter`
argument marks zones that cannot be selected. In `c10852583.lua`, the script
builds a mask of adjacent usable zones, flips it into an unavailable-zone mask,
then asks the player to choose one:

```lua
local flag=0
if seq>0 and Duel.CheckLocation(tp,LOCATION_MZONE,seq-1) then flag=bit.replace(flag,0x1,seq-1) end
if seq<4 and Duel.CheckLocation(tp,LOCATION_MZONE,seq+1) then flag=bit.replace(flag,0x1,seq+1) end
flag=bit.bxor(flag,0xff)
Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_TOZONE)
local s=Duel.SelectDisableField(tp,1,LOCATION_MZONE,0,flag)
```

When an effect highlights a zone without selecting it, use the same mask layout
with `HINT_ZONE`. `c10045474.lua` points at its own Spell & Trap Zone:

```lua
Duel.Hint(HINT_ZONE,tp,0x1<<(c:GetSequence()+8))
```

## Linked Zones And Columns

Link-related APIs return zone masks that can be passed into summon legality
checks and summon operations.

`c98978921.lua` gets the handler's linked zones from the activating player's
viewpoint, uses the same `zone` mask in the filter, then passes it to
`Duel.SpecialSummon`:

```lua
function c98978921.filter(c,e,tp,zone)
    return c:IsLevelBelow(4) and c:IsType(TYPE_NORMAL)
        and c:IsCanBeSpecialSummoned(e,0,tp,false,false,POS_FACEUP,tp,zone)
end

function c98978921.operation(e,tp,eg,ep,ev,re,r,rp)
    local zone=e:GetHandler():GetLinkedZone(tp)
    if zone==0 then return end
    Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SPSUMMON)
    local g=Duel.SelectMatchingCard(tp,c98978921.filter,tp,LOCATION_HAND,0,1,1,nil,e,tp,zone)
    if g:GetCount()>0 then
        Duel.SpecialSummon(g,0,tp,tp,false,false,POS_FACEUP,zone)
    end
end
```

Use `Duel.GetLinkedZone(tp)` when the effect cares about any currently linked
zone from the player's viewpoint, not only the zones pointed to by one Link
Monster. If a script only wants the player's Monster Zone bits from a broader
mask, local scripts commonly mask with `0x7f`.

For column effects, prefer the built-in column APIs and local helpers instead
of hand-mirroring sequence numbers:

- `Card.GetColumnGroup()` returns cards in the same column.
- `Card.GetColumnZone(location, ...)` returns a column zone mask.
- `aux.GetColumn(c,tp)` returns the column number from player `tp`'s viewpoint.
- `aux.SequenceToGlobal(p,loc,seq)` converts a local sequence to the global
  mask layout used by field-zone selection.

## Choosing The Tool

| Need | Use |
| --- | --- |
| Check whether a zone is currently open | `Duel.GetLocationCount` |
| Check after a specific card or group leaves | `Duel.GetMZoneCount`, `Duel.GetSZoneCount` |
| Check one exact slot | `Duel.CheckLocation` |
| Read a card's slot | `Card.GetSequence` |
| Let the player choose a zone mask | `Duel.SelectDisableField` |
| Restrict a Special Summon to Link arrows | `Card.GetLinkedZone`, `Duel.GetLinkedZone` |
| Work with columns | `Card.GetColumnGroup`, `Card.GetColumnZone`, `aux.GetColumn` |

Relevant API pages:

- [`Duel.GetLocationCount`](/api/functions/Duel/GetLocationCount)
- [`Duel.GetMZoneCount`](/api/functions/Duel/GetMZoneCount)
- [`Duel.GetSZoneCount`](/api/functions/Duel/GetSZoneCount)
- [`Duel.SelectDisableField`](/api/functions/Duel/SelectDisableField)
- [`Duel.GetLinkedZone`](/api/functions/Duel/GetLinkedZone)
- [`Card.GetSequence`](/api/functions/Card/GetSequence)
- [`Card.GetLinkedZone`](/api/functions/Card/GetLinkedZone)
- [`Card.GetColumnZone`](/api/functions/Card/GetColumnZone)
- [`Auxiliary.GetColumn`](/api/functions/Auxiliary/GetColumn)
- [`Auxiliary.SequenceToGlobal`](/api/functions/Auxiliary/SequenceToGlobal)
