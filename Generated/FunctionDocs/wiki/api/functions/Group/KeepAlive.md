# Group.KeepAlive

## Signature

```lua
Group.KeepAlive(Group g) -> void
```

## Description

Prevents g from being automatically released by Lua until Group.DeleteGroup is called.
Use this when a selected Group is stored on an Effect with SetLabelObject or otherwise needs to survive into a later callback. Pair it with Group.DeleteGroup when the delayed effect is done.

## Parameters

- `g` `Group` - Group to preserve until DeleteGroup is called.

## Source

- `D:\Programs\GitHub\ygopro-core\libgroup.cpp:901`
