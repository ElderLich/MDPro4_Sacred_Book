# Auxiliary.AddXyzProcedureLevelFree

## Signature

```lua
Auxiliary.AddXyzProcedureLevelFree(Card c, [function|nil f], [function|nil gf], int minc, int maxc, [function alterf], [string alterdesc], [function alterop]) -> void
```

## Description

Add an Xyz Summon procedure for c
Use minc [to maxc] monsters satisfying condition f, and within the group satisfying condition gf, for overlay; f is a required condition, gf is an additional condition
Or overlay on a single monster (typically an Xyz Monster)
alterf is the condition this monster must satisfy, desc is the description, op is the operation required during overlay (e.g., Number F0: Utopic Future)

## Parameters

- `c` `Card`
- `f` `function|nil` optional
- `gf` `function|nil` optional
- `minc` `int`
- `maxc` `int`
- `alterf` `function` optional
- `alterdesc` `string` optional
- `alterop` `function` optional

## Source

- `Utilities/procedure.lua:700`
