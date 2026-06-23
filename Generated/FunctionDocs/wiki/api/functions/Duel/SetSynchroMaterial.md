# Duel.SetSynchroMaterial

## Signature

```lua
Duel.SetSynchroMaterial(Group g) -> void
```

## Description

Stores g as the Synchro Material group for the current Synchro Material custom procedure.
Local standard Synchro helpers usually keep their selected material group on the procedure effect instead; this function appears in custom material-provider scripts such as Flower Cardian Synchro helpers.
This records the selected group for the core. It does not move those cards and returns no value.

## Parameters

- `g` `Group` - Selected Synchro Material group to store for the custom procedure.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4991`
