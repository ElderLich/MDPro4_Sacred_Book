# Duel.ReleaseRitualMaterial

## Signature

```lua
Duel.ReleaseRitualMaterial(Group g) -> void
```

## Description

Moves the selected Ritual Materials in g using Ritual-material rules.
Standard hand or field materials are Tributed, while materials such as suitable Graveyard Ritual Materials are banished instead.
Call Card.SetMaterial before this function, then Special Summon with SUMMON_TYPE_RITUAL and call Card.CompleteProcedure after the Summon succeeds. The function does not return a count.

## Parameters

- `g` `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4999`
