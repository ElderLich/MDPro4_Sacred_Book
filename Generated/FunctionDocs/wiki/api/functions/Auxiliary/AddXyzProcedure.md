# Auxiliary.AddXyzProcedure

## Signature

```lua
Auxiliary.AddXyzProcedure(Card c, function|nil f, int lv, int ct, [function|nil alterf], [int alterdesc], [int maxct], [function|nil alterop]) -> void
```

## Description

Registers the standard Xyz Summon procedure for c.
f filters materials, lv is the required material Xyz Level, ct is the minimum material count, and maxct optionally caps the maximum.
The helper creates an Extra Deck EFFECT_SPSUMMON_PROC with SUMMON_TYPE_XYZ, checks and selects materials with the core Xyz helpers, records them with Card.SetMaterial, and overlays them with Duel.Overlay.
alterf, alterdesc, and alterop define an optional one-card alternate Xyz Summon route.

## Parameters

- `c` `Card` - Xyz Monster receiving the procedure.
- `f` `function|nil` - Optional per-material filter. nil means no extra material restriction beyond the normal Xyz checks.
- `lv` `int` - Required material Xyz Level.
- `ct` `int` - Minimum material count.
- `alterf` `function|nil` optional - Optional filter for a one-card alternate Xyz Summon route.
- `alterdesc` `int` optional - Prompt text id used when the alternate route can be chosen.
- `maxct` `int` optional - Maximum material count. Defaults to ct when omitted.
- `alterop` `function|nil` optional - Optional check/apply callback for the alternate route. The local helper calls it with chk==0 for legality and chk==1 after selection.

## Source

- `Utilities/procedure.lua:485`
