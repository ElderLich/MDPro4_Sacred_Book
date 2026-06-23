# Auxiliary.AddXyzProcedureLevelFree

## Signature

```lua
Auxiliary.AddXyzProcedureLevelFree(Card c, function|nil f, function|nil gf, int minc, int maxc, [function|nil alterf], [int alterdesc], [function|nil alterop]) -> void
```

## Description

Registers a Level-free Xyz Summon procedure on c.
f filters each candidate material, while gf can validate the selected group as a whole, such as requiring all materials to have the same Rank.
The local helper still checks Card.IsCanBeXyzMaterial, zone availability, and EFFECT_XYZ_MIN_COUNT, but procedure.lua notes that EFFECT_DOUBLE_XMATERIAL is not supported in this path.

## Parameters

- `c` `Card` - Xyz Monster receiving the Level-free procedure.
- `f` `function|nil` - Optional per-material filter.
- `gf` `function|nil` - Optional whole-group validator called on the selected material group.
- `minc` `int` - Minimum material count.
- `maxc` `int` - Maximum material count.
- `alterf` `function|nil` optional - Optional filter for a one-card alternate Xyz Summon route.
- `alterdesc` `int` optional - Prompt text id used when the alternate route can be chosen.
- `alterop` `function|nil` optional - Optional check/apply callback for the alternate route.

## Source

- `Utilities/procedure.lua:700`
