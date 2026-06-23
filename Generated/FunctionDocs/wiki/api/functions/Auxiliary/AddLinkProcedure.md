# Auxiliary.AddLinkProcedure

## Signature

```lua
Auxiliary.AddLinkProcedure(Card c, function|nil f, int min, [int max], [function|nil gf]) -> Effect
```

## Description

Registers the standard Link Summon procedure for c and returns the created Effect.
f filters each Link Material, min/max constrain the number of selected material cards, and gf optionally checks the selected group as a whole.
The helper creates an Extra Deck EFFECT_SPSUMMON_PROC with SUMMON_TYPE_LINK, uses Auxiliary.GetLinkCount to match the Link Rating, records materials with Card.SetMaterial, and sends them to the GY with REASON_MATERIAL+REASON_LINK.

## Parameters

- `c` `Card` - Link Monster receiving the procedure.
- `f` `function|nil` - Optional per-material filter. nil means no extra filter beyond normal Link Material legality.
- `min` `int` - Minimum number of material cards that must be selected.
- `max` `int` optional - Maximum number of material cards. Defaults to c:GetLink() when omitted.
- `gf` `function|nil` optional - Optional whole-group validator called as gf(selected_group, link_monster, player).

## Returns

- `Effect` - The registered Special Summon procedure effect.

## Source

- `Utilities/procedure.lua:2128`
