# Auxiliary.EnableMulcharmyGlobalCheck

## Signature

```lua
Auxiliary.EnableMulcharmyGlobalCheck() -> void
```

## Description

Installs the shared Mulcharmy activation-count watcher once per Duel process.
The watcher listens to EVENT_CHAINING and registers player flag 84192580 through the End Phase whenever that player activates a monster effect from set 0x1b2.
Mulcharmy monster scripts call this from initial_effect, then check Duel.GetFlagEffect(tp,84192580)&lt;=1 as part of their hand-activation condition.

## Source

- `Utilities/utility.lua:2053`
