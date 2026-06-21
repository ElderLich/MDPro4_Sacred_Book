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

## Listed Cards

Some effects care whether a card lists another card by ID. Use helper/API
functions for that instead of searching text manually.

```lua
function s.filter(c)
  return c:IsType(TYPE_MONSTER) and aux.IsCodeListed(c,12345678)
end
```

Useful API pages:

- [`Card.IsCode`](/api/functions/Card/IsCode)
- [`Card.IsSetCard`](/api/functions/Card/IsSetCard)
- [`Auxiliary.IsCodeListed`](/api/functions/Auxiliary/IsCodeListed)
- [`Auxiliary.IsCodeOrListed`](/api/functions/Auxiliary/IsCodeOrListed)
