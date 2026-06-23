# Count Limits And Once Per Turn

`Effect.SetCountLimit` is the normal tool for "once per turn", "twice per
turn", and "once per Duel" effect-use limits. The core checks this during
activation legality and spends the count when the effect is used.

Use flag effects only when the script needs custom memory that is not just a
standard use count. Dragon Master Magia's separate Monster, Spell, and Trap
negation markers are a good flag-effect pattern; a normal "you can only use
this effect once per turn" should usually be a count limit.

## Basic Shared Count

Most effects use the card id as the count code:

```lua
local e1=Effect.CreateEffect(c)
e1:SetDescription(aux.Stringid(id,0))
e1:SetType(EFFECT_TYPE_IGNITION)
e1:SetRange(LOCATION_HAND)
e1:SetCountLimit(1,id)
e1:SetTarget(s.sptg)
e1:SetOperation(s.spop)
c:RegisterEffect(e1)
```

The first argument is the maximum number of uses. The optional second argument
is the shared count code. Effects with the same nonzero code share the same
count for that player. If the code is omitted, the effect spends its own local
count instead of a shared code.

The core treats `SetCountLimit(0, code)` as `SetCountLimit(1, code)`.

## Separate Effects On One Card

When one card has several effects that should each be usable once, give each
effect a different code. Scripts often use the offset returned by `GetID()`:

```lua
local s,id,o=GetID()

e1:SetCountLimit(1,id)
e2:SetCountLimit(1,id+o)
e3:SetCountLimit(1,id+o*2)
```

This pattern appears in `c10266279.lua`: three different effects use `id`,
`id+o`, and `id+o*2`, so spending one does not spend the others.

If two effects intentionally share "you can only use 1 of these effects per
turn", give them the same count code.

## Special Count Codes

The source define file names three common modifiers:

| Code | Use |
| --- | --- |
| `EFFECT_COUNT_CODE_OATH` | Oath-style use count, such as `id+EFFECT_COUNT_CODE_OATH`. In this core, negated activations and failed procedure attempts roll the spent count back through `dec_effect_code`. |
| `EFFECT_COUNT_CODE_DUEL` | Stores the count in the duel-long count map instead of the turn-reset map. |
| `EFFECT_COUNT_CODE_SINGLE` | Shares a count between effects on the same card object without sharing it with every copy of the same card name. |

`EFFECT_COUNT_CODE_CHAIN` uses the chain count map. When it is passed as the
exact code, `SetCountLimit` stores it together with `EFFECT_COUNT_CODE_SINGLE`;
the chain count map is cleared as chain state resets.

For example, `c1157683.lua` gives two Quick Effects on the same Continuous Trap
the same per-card count:

```lua
e1:SetCountLimit(1,EFFECT_COUNT_CODE_SINGLE)
e2:SetCountLimit(1,EFFECT_COUNT_CODE_SINGLE)
```

And `c10131855.lua` uses a chain-scoped limit on a replacement effect:

```lua
e2:SetCode(EVENT_CHAINING)
e2:SetRange(LOCATION_SZONE)
e2:SetCountLimit(1,EFFECT_COUNT_CODE_CHAIN)
```

## Manually Spending Another Effect's Count

Most scripts do not call `UseCountLimit`; the core spends the count for a
normal activation. Use `Effect.UseCountLimit` when a script manually uses or
borrows another `Effect` object and must spend that other effect's count.

`c10266279.lua` checks for another effect on a card in the GY, uses that effect
as a replacement, and manually spends its count before banishing the card:

```lua
local te=tc:IsHasEffect(99311889,tp)
if te then
    te:UseCountLimit(tp)
    Duel.Remove(tc,POS_FACEUP,REASON_COST+REASON_REPLACE)
end
```

`Effect.CheckCountLimit(e,p)` is the matching read-side helper. It returns
whether the count is still available for player `p`; normal activation checks
already call the core count check.

## Custom Activity Counters

Use `Duel.AddCustomActivityCounter` and `Duel.GetCustomActivityCount` when the
restriction depends on actions that happened earlier this turn, not on how many
times one effect was used.

`c12500059.lua` registers a Special Summon activity counter during
`initial_effect`, then checks that the player has not performed a disallowed
Special Summon before paying the cost:

```lua
Duel.AddCustomActivityCounter(id,ACTIVITY_SPSUMMON,s.counterfilter)

function s.counterfilter(c)
    return c:IsRace(RACE_FAIRY) and c:IsFaceup()
end

function s.spcost(e,tp,eg,ep,ev,re,r,rp,chk)
    e:SetLabel(100)
    if chk==0 then return Duel.GetCustomActivityCount(id,tp,ACTIVITY_SPSUMMON)==0 end
    -- register the matching Special Summon restriction for the rest of the turn
end
```

The filter returns `true` for allowed activity. The counter increments when the
registered filter returns `false`, so the script checks whether the disallowed
activity count is still `0`.

## Choosing The Tool

| Need | Use |
| --- | --- |
| One effect can be used once per turn | `e:SetCountLimit(1,id)` |
| Several effects share one use | Give them the same count code |
| Several effects each get their own use | Use different codes such as `id`, `id+o`, `id+o*2` |
| Multiple effects on the same card share a count, but other copies do not | `EFFECT_COUNT_CODE_SINGLE` |
| Count should last for the whole Duel | `EFFECT_COUNT_CODE_DUEL` |
| Script manually spends another effect object's use | `Effect.UseCountLimit` |
| Restrict based on actions already performed this turn | Custom activity counters |
| Store custom state such as which option was chosen | [Flag effects](/learn/flag-effects) |

Relevant API pages:

- [`Effect.SetCountLimit`](/api/functions/Effect/SetCountLimit)
- [`Effect.CheckCountLimit`](/api/functions/Effect/CheckCountLimit)
- [`Effect.UseCountLimit`](/api/functions/Effect/UseCountLimit)
- [`Duel.AddCustomActivityCounter`](/api/functions/Duel/AddCustomActivityCounter)
- [`Duel.GetCustomActivityCount`](/api/functions/Duel/GetCustomActivityCount)
