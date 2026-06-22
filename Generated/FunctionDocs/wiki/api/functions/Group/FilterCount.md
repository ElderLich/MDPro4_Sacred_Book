# Group.FilterCount

## Signature

```lua
Group.FilterCount(Group g, function f, [Card|Group|nil ex], ... any) -> int
```

## Description

Counts cards in g that satisfy f, excluding ex.
Extra arguments after ex are passed to f after the Card argument.

## Parameters

- `g` `Group`
- `f` `function`
- `ex` `Card|Group|nil` optional
- `...` `any`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libgroup.cpp:913`
