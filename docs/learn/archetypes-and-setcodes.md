# Archetypes and Set Codes

Scripts should identify card families by code and set code, not by displayed
card name. Names change across languages; IDs, set codes, and local helper
metadata are the stable scripting layer.

## Which Check To Use

Most archetype bugs come from using an exact-ID check where a family check was
needed, or using a family check where the text really names one card.

| Card text or procedure needs | Use |
| --- | --- |
| This exact card ID, including current code changes. | `Card.IsCode` |
| One archetype, theme, or subfamily. | `Card.IsSetCard` |
| A card's printed/original identity for material or release rules. | `Card.IsOriginalCodeRule` |
| A card that lists another card by ID. | `aux.IsCodeListed` |
| The named card itself or a card that lists it. | `aux.IsCodeOrListed` |
| A card that lists a monster set name registered in script metadata. | `aux.IsSetNameMonsterListed` |

When unsure, search local scripts for known card IDs from the same theme and
copy the identity check shape they use. The set code number is data, not a name
you should invent from memory.

## Exact Card IDs

Use `IsCode` when a script names a specific card.

```lua
function s.filter(c)
    return c:IsCode(12345678)
end
```

`Card.IsCode` can accept several IDs.

```lua
function s.matfilter(c)
    return c:IsCode(89631139,23995346)
end
```

Use this when the card text references one exact card, or a short list of exact
cards. Because the engine exposes current code and alternate-code behavior
through this API, it is safer than comparing a raw database field.

## Set Codes

Use `IsSetCard` when a script cares about an archetype or family.

```lua
function s.filter(c)
    return c:IsFaceup() and c:IsSetCard(0x123)
end
```

Set codes can represent a broad family or a smaller branch of that family. When
a script needs the smaller branch, use the more specific set code used by the
local scripts and card data.

`Card.IsSetCard` accepts more than one value and returns true if any of them
match.

```lua
function s.filter(c)
    return c:IsSetCard(0x9f,0x99)
end
```

Local `c12908094.lua` uses this style for an Extra Deck filter that accepts
several related Xyz themes in one check:

```lua
function s.xyzfiltr(c,g)
    return c:IsSetCard(0x8f,0x54,0x59,0x82,0x206f,0x6d,0x48,0x107e,0x207e)
        and c:IsXyzSummonable(nil,g,2,99)
end
```

The core binding checks the card's current code, alternate code behavior, and
added set-code effects. That is why scripts should call the API instead of
trying to compare raw database fields manually.

## Subarchetypes

Some families contain nested groups. A broad set code might match the whole
family, while a more specific set code matches only a branch. Do not guess from
the displayed name alone.

MDPro3/YGOPro stores set codes as 16-bit values. The low 12 bits identify the
base family, while the high bits can require a subtype. In practical script
terms:

| Example shape | Meaning |
| --- | --- |
| `0x034` | broad base family |
| `0x1034` | subtype `0x1000` inside base family `0x034` |
| `0x2034` | subtype `0x2000` inside base family `0x034` |

A broad check can match cards in the base family. A subtype check requires the
matching subtype bits too. This is why local scripts sometimes use a value such
as `0x1034` when the card text is narrower than the displayed family name.

Do not hand-roll bit math in filters. Use `IsSetCard` and the set-code values
already present in local scripts or data.

Safer process:

1. Search local scripts for the card family or known card IDs.
2. Check which `IsSetCard(0x...)` value existing cards use.
3. Check card data when a script must match newly added cards.
4. Use the narrowest set code that matches the card text.

## Listed Cards And Listed Sets

Some effects care whether a card lists another card by ID. Use helper/API
functions for that instead of searching text manually.

```lua
function s.filter(c)
    return c:IsType(TYPE_MONSTER) and aux.IsCodeListed(c,12345678)
end
```

`aux.IsCodeOrListed` is useful when a card can be the exact named card or a card
that lists it.

Local scripts register listed-card metadata in `initial_effect` with
`aux.AddCodeList`. Local `c10186633.lua` registers a listed card and a listed
monster set name before its filters use those facts:

```lua
aux.AddCodeList(c,89943723)
aux.AddSetNameMonsterList(c,0x3008)
```

Later in that script, the group check accepts either the exact listed card or a
group whose cards belong to one of the named sets:

```lua
return #g==1 and g:GetFirst():IsCode(89943723)
    or aux.gfcheck(g,Card.IsSetCard,0x3008,0x1f)
```

Treat listed-card helpers as metadata checks, not text searches. A card must
have the appropriate listed metadata registered or generated for these helpers
to see it.

## Original-Code Checks

Some procedures care about the original printed identity, not what a card is
currently treated as. Use `Card.IsOriginalCodeRule` for those rules.

Local `c10000040.lua` uses it to require three exact original cards in a release
group:

```lua
c10000040.spchecks=aux.CreateChecks(Card.IsOriginalCodeRule,{10000020,10000000,10000010})
```

This is different from `IsCode`. A name-copying effect can make a card currently
treated as an ID, but it should not satisfy every original-name material or
release procedure.

## Common Filter Patterns

| Pattern | Example |
| --- | --- |
| Exact named card. | `c:IsCode(89943723)` |
| Any member of one family. | `c:IsSetCard(0x3008)` |
| Any member of several accepted families. | `c:IsSetCard(0x8f,0x54,0x59)` |
| Face-up archetype monster. | `c:IsFaceup() and c:IsSetCard(0x123) and c:IsType(TYPE_MONSTER)` |
| A card that lists a named card. | `aux.IsCodeListed(c,89943723)` |
| The named card or a card that lists it. | `aux.IsCodeOrListed(c,89943723)` |
| A group containing required kinds. | `aux.gfcheck(g,Card.IsSetCard,0x3008,0x1f)` |

Keep filters narrow enough for the card text, but broad enough for legitimate
subarchetype members. The right answer is usually visible in nearby local
scripts.

Useful API pages:

- [`Card.IsCode`](/api/functions/Card/IsCode)
- [`Card.IsSetCard`](/api/functions/Card/IsSetCard)
- [`Card.IsOriginalCodeRule`](/api/functions/Card/IsOriginalCodeRule)
- [`Auxiliary.AddCodeList`](/api/functions/Auxiliary/AddCodeList)
- [`Auxiliary.AddSetNameMonsterList`](/api/functions/Auxiliary/AddSetNameMonsterList)
- [`Auxiliary.IsCodeListed`](/api/functions/Auxiliary/IsCodeListed)
- [`Auxiliary.IsCodeOrListed`](/api/functions/Auxiliary/IsCodeOrListed)
- [`Auxiliary.IsSetNameMonsterListed`](/api/functions/Auxiliary/IsSetNameMonsterListed)
- [`Auxiliary.gfcheck`](/api/functions/Auxiliary/gfcheck)
