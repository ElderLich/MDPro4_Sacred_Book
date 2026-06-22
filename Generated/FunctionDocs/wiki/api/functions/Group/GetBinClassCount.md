# Group.GetBinClassCount

## Signature

```lua
Group.GetBinClassCount(Group g, function f, ... any) -> int
```

## Description

Calls f for each card in g, ORs the returned integer values together, and returns the number of set bits in the result.

## Parameters

- `g` `Group`
- `f` `function`
- `...` `any`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libgroup.cpp:934`
