# Auxiliary.AddXyzProcedureLevelFree

## Signature

```lua
Auxiliary.AddXyzProcedureLevelFree(Card c, function|nil f, function|nil gf, int minc, int maxc, [function|nil alterf], [int alterdesc], [function|nil alterop]) -> void
```

## Description

Registers a Level-free Xyz Summon procedure on c.
This helper uses f, gf, minc, maxc, and optional alternate-summon settings, and returns no explicit value.

## Parameters

- `c` `Card`
- `f` `function|nil`
- `gf` `function|nil`
- `minc` `int`
- `maxc` `int`
- `alterf` `function|nil` optional
- `alterdesc` `int` optional
- `alterop` `function|nil` optional

## Source

- `Utilities/procedure.lua:700`
