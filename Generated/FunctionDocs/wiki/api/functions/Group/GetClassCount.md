# Group.GetClassCount

## Signature

```lua
Group.GetClassCount(Group g, function f, ... any) -> int
```

## Description

Counts distinct classes among cards in g according to f. Cards with the same return value from f count as the same class; extra arguments are passed to f.

## Parameters

- `g` `Group`
- `f` `function`
- `...` `any`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libgroup.cpp:927`
