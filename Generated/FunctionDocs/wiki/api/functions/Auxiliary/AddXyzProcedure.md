# Auxiliary.AddXyzProcedure

## Signature

```lua
Auxiliary.AddXyzProcedure(Card c, [function|nil f], int lv, int ct, [function alterf], [string alterdesc], [int maxct], [function alterop]) -> void
```

## Description

Registers the standard Xyz Summon procedure for c.
f filters materials, lv is the required Level, ct is the minimum material count, and maxct optionally caps the maximum. alterf/alterdesc/alterop define an alternate one-card Xyz Summon route.

## Parameters

- `c` `Card`
- `f` `function|nil` optional
- `lv` `int`
- `ct` `int`
- `alterf` `function` optional
- `alterdesc` `string` optional
- `maxct` `int` optional
- `alterop` `function` optional

## Source

- `Utilities/procedure.lua:485`
