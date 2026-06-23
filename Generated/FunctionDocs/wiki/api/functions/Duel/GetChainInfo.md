# Duel.GetChainInfo

## Signature

```lua
Duel.GetChainInfo(int chainc, ... any) -> ...
```

## Description

Returns information fields from chainc in the same order as the requested CHAININFO_* constants.
Use chainc=0 for the currently resolving Chain. Unknown requested fields return nil, and no values are returned if the Chain does not exist.

## Parameters

- `chainc` `int` - Chain index/count to inspect; scripts commonly use 0 for the current Chain Link.
- `...` `any` - One or more CHAININFO_* constants. Each requested field produces one return value.

## Returns

- `...` - Values corresponding to the requested CHAININFO_* constants. CHAININFO_TARGET_CARDS returns the Chain's target Group.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4947`
