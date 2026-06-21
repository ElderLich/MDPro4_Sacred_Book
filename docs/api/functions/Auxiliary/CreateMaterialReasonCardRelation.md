# Auxiliary.CreateMaterialReasonCardRelation

## Signature

```lua
Auxiliary.CreateMaterialReasonCardRelation(Card c, Effect te) -> void
```

## Description

Registers an EVENT_BE_MATERIAL continuous effect on c so that, when c is used as material, the Summoned monster creates an effect relation with te.

## Parameters

- `c` `Card`
- `te` `Effect`

## Source

- `Utilities/utility.lua:859`
