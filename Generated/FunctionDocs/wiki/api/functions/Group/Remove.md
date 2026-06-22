# Group.Remove

## Signature

```lua
Group.Remove(Group g, function f, Card|nil ex, [... any]) -> void
```

## Description

Removes cards from mutable group g that satisfy f and are not ex, passing any extra arguments to f.

## Parameters

- `g` `Group`
- `f` `function`
- `ex` `Card|nil`
- `...` `any` optional

## Source

- `D:\Programs\GitHub\ygopro-core\libgroup.cpp:928`
