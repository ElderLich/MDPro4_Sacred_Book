# Auxiliary.EnableNeosReturn

## Signature

```lua
Auxiliary.EnableNeosReturn(Card c, function operation, any set_category) -> void
```

## Description

Registers the shared Elemental HERO Neos Fusion End Phase return effects on c. It creates a mandatory return effect and an optional version used while c is affected by effect code 42015635, then returns both effects.

## Parameters

- `c` `Card`
- `operation` `function`
- `set_category` `any`

## Source

- `Utilities/utility.lua:222`
