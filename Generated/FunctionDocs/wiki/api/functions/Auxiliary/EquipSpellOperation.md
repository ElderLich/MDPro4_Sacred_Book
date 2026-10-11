# Auxiliary.EquipSpellOperation

## Signature

```lua
Auxiliary.EquipSpellOperation(any eqlimit) -> void
```

## Description

Returns the shared Equip Spell operation. It equips the handler to the first target if both cards are still related to the effect, the target is face-up, and eqlimit allows it.
This is the operation used by Auxiliary.AddEquipSpellEffect; unusual equip flows should usually write their own operation.

## How To Use It

This helper builds the resolution callback used by `Auxiliary.AddEquipSpellEffect`.

It reads the first target, checks that the Equip Card and target still relate to the effect, checks that the target is still face-up, rechecks `eqlimit`, then calls `Duel.Equip`.

Use the manual pattern when the equip target is created during resolution or when the Equip Card needs a temporary limit registered after `Duel.Equip` succeeds.

## Related Functions

- [Auxiliary.AddEquipSpellEffect](/api/functions/Auxiliary/AddEquipSpellEffect)
- [Duel.Equip](/api/functions/Duel/Equip)
- [Card.IsRelateToEffect](/api/functions/Card/IsRelateToEffect)

## Parameters

- `eqlimit` `any`

## Source

- `Utilities/utility.lua:1925`
