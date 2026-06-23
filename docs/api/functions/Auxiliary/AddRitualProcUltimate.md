# Auxiliary.AddRitualProcUltimate

## Signature

```lua
Auxiliary.AddRitualProcUltimate(Card c, function filter, function level_function, string greater_or_equal, [int summon_location], [function|nil grave_filter], [function|nil mat_filter], [bool pause], [function|nil extra_operation], [function|nil extra_target]) -> Effect
```

## Description

Creates the configurable Ritual Summon activation effect for c and returns it.
The generated effect checks for a Ritual Monster, gathers Ritual Materials, validates an equal or greater-or-equal material total, releases Ritual Materials, Special Summons with SUMMON_TYPE_RITUAL, and completes the procedure.
Use wrapper helpers for ordinary Ritual Spells, and call this directly when a script needs Graveyard material, a material filter, delayed registration, or extra target/operation callbacks.

## Parameters

- `c` `Card`
- `filter` `function` - Ritual Monster filter. It receives the candidate Ritual Monster plus the helper's extra arguments and should return true for monsters this effect can Summon.
- `level_function` `function` - Function used to get the required value from the Ritual Monster, commonly Card.GetOriginalLevel or Card.GetLevel.
- `greater_or_equal` `string` - Use "Greater" for equal-or-higher material totals or "Equal" for exact totals.
- `summon_location` `int` optional - Location to search for the Ritual Monster. Defaults to LOCATION_HAND.
- `grave_filter` `function|nil` optional - Optional filter for extra Graveyard materials that the helper may merge into the material pool.
- `mat_filter` `function|nil` optional - Optional filter applied to candidate Ritual Materials before the material subgroup is selected.
- `pause` `bool` optional - If true, returns the effect without registering it to c.
- `extra_operation` `function|nil` optional - Optional callback run after the Ritual Summon operation. Local wrappers pass the Summoned monster and selected material group to this callback.
- `extra_target` `function|nil` optional - Optional callback run during the target branch for extra operation info or activation checks.

## Returns

- `Effect` - The created Ritual Summon activation effect. If pause is false or nil, the helper also registers it to c.

## Source

- `Utilities/procedure.lua:1750`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
