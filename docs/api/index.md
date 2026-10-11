# API

Choose the reference for the scripting layer you need. These pages follow this project's MDPro3/YGOPro core and helper sources; available functions can differ between simulators.

## Choose a Reference

| Reference | What you will find |
| --- | --- |
| [Core and standard helper functions](functions/) | `Card`, `Effect`, `Group`, `Duel`, and standard Lua helpers. |
| [Standard constants](constants) | Locations, events, effect codes, and standard-format flags. |
| [Rush Duel helpers](/rush/api/functions/) | The `RushDuel` namespace and its `RD` alias. |
| [Rush Duel constants](/rush/api/constants) | Constants defined by the Rush rules and helper library. |

## Using the Rush API

Rush scripts use `Card`, `Effect`, `Group`, and `Duel` alongside the Rush helpers, so you will use both references. The matching Rush bootstrap must load the helper library and rules before your card script runs; the database's Rush label alone does not enable them.

Start with the [Rush API overview](/rush/api/), or follow the [Rush Duel learning path](/learn/rush-duel) for complete examples. Keep Rush-specific constants separate from the standard definitions.

## Sources

- `ygopro-core/lib*.cpp`
- `Define/def.lua`
- `Utilities/utility.lua`
- `Utilities/procedure.lua`
- `Rush/Utilities/RD*.lua` and `Rush/Utilities/special.lua`
