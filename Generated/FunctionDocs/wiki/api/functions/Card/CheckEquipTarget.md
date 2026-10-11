# Card.CheckEquipTarget

## Signature

```lua
Card.CheckEquipTarget(Card c1, Card c2) -> bool
```

## Description

Checks whether c2 is a valid Equip target for c1.
The core requires c1 to be affected by an EFFECT_EQUIP_LIMIT that accepts c2, and it also enforces old and modern Union count limits.
This is only a legality check for the equip relationship; it does not reserve a Spell & Trap Zone or perform Duel.Equip.

## How To Use It

Use this before moving an existing Equip Card to a new monster or before offering a card from another location as an Equip Card.

```lua
return c:IsFaceup() and eqc:CheckEquipTarget(c)
```

This checks the Equip Card's local equip-limit rules. It does not by itself reserve a Spell & Trap Zone or perform the equip.

## Related Functions

- [Duel.Equip](/api/functions/Duel/Equip)
- [Auxiliary.AddEquipSpellEffect](/api/functions/Auxiliary/AddEquipSpellEffect)
- [Card.GetEquipTarget](/api/functions/Card/GetEquipTarget)

## Parameters

- `c1` `Card`
- `c2` `Card`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3576`
