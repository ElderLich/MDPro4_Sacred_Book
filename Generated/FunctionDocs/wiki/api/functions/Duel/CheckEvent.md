# Duel.CheckEvent

## Signature

```lua
Duel.CheckEvent(int event, [bool get_info]) -> bool,Group,int,int,Effect,int,int
```

## Description

Check whether the current event point
If get_info = true and is the correct time point also returns the trigger point information eg, ep, ev, re, r, rp

## Parameters

- `event` `int`
- `get_info` `bool` optional

## Returns

- `bool`
- `Group` - may be nil
- `int` - may be nil
- `int` - may be nil
- `Effect` - may be nil
- `int` - may be nil
- `int` - may be nil

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4894`
