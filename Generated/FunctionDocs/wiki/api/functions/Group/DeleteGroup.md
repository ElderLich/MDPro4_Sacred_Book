# Group.DeleteGroup

## Signature

```lua
Group.DeleteGroup(Group g) -> void
```

## Description

Releases a Group previously preserved with Group.KeepAlive so Lua can manage it normally again.
Calling this on an ordinary Group has no effect.

## Parameters

- `g` `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libgroup.cpp:902`
