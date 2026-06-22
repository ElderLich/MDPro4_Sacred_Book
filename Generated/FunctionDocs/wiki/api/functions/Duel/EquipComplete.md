# Duel.EquipComplete

## Signature

```lua
Duel.EquipComplete() -> void
```

## Description

Completes a batch of step equips created with Duel.Equip(..., true) by enabling the equipped cards and raising the equip events.

## How To Use It

Use this only after one or more `Duel.Equip(..., true)` step equips.

It enables the equipped cards and raises the equip events as one completed procedure:

```lua
if Duel.Equip(tp,ec,tc,true,true) then
    -- more step equips can be added here
    Duel.EquipComplete()
end
```

## Related Functions

- [Duel.Equip](/api/functions/Duel/Equip)

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4905`
