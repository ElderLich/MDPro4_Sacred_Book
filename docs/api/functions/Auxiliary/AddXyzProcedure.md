# Auxiliary.AddXyzProcedure

## Signature

```lua
Auxiliary.AddXyzProcedure(Card c, [function|nil f], int lv, int ct, [function alterf], [string alterdesc], [int maxct], [function alterop]) -> void
```

## Description

Add an excess summon for c
With the conditions to meet the conditions for the f-level cv-maxct lv monster to be stacked
The rest of the parameters are used to stack on a single monster (usually an excess of monsters)
Alterf for this monster to meet the conditions, desc for the description, op for the stacked operation (hope Huanglong)

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
