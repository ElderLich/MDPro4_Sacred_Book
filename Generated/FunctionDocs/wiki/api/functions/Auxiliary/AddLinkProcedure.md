# Auxiliary.AddLinkProcedure

## Signature

```lua
Auxiliary.AddLinkProcedure(Card c, [function|nil f], int min, [int max], [function gf]) -> Effect
```

## Description

Add a Link Summon procedure for c
Use minc-maxc monsters satisfying filter condition f [and within the group satisfying filter condition gf] as Link Materials

## Parameters

- `c` `Card`
- `f` `function|nil` optional
- `min` `int`
- `max` `int` optional
- `gf` `function` optional

## Returns

- `Effect`

## Source

- `Utilities/procedure.lua:2128`
