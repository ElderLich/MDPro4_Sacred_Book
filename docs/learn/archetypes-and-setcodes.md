# Archetypes and Set Codes

Scripts should identify card families by code and set code, not by displayed
card name. Names change across languages; IDs and set codes are stable scripting
data.

## Card ID

Use exact card IDs when a script names a specific card.

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
cards.

## Set Code

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

Safer process:

1. Search local scripts for the card family or known card IDs.
2. Check which `IsSetCard(0x...)` value existing cards use.
3. Check card data when a script must match newly added cards.
4. Use the narrowest set code that matches the card text.

## Listed Cards

Some effects care whether a card lists another card by ID. Use helper/API
functions for that instead of searching text manually.

```lua
function s.filter(c)
    return c:IsType(TYPE_MONSTER) and aux.IsCodeListed(c,12345678)
end
```

`aux.IsCodeOrListed` is useful when a card can be the exact named card or a card
that lists it.

## Name Changes and Alternate Codes

Some effects change a card's code. `Card.IsCode` checks the current code and
alternate code behavior exposed by the engine, so it is safer than comparing a
manual field.

```lua
if c:IsCode(id) then
    -- this card is currently treated as that ID
end
```

For families, prefer `IsSetCard` unless the card text demands exact IDs.

Useful API pages:

- [`Card.IsCode`](/api/functions/Card/IsCode)
- [`Card.IsSetCard`](/api/functions/Card/IsSetCard)
- [`Auxiliary.IsCodeListed`](/api/functions/Auxiliary/IsCodeListed)
- [`Auxiliary.IsCodeOrListed`](/api/functions/Auxiliary/IsCodeOrListed)
