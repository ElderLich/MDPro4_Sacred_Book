# Duel.GetChainInfo

## Signature

```lua
Duel.GetChainInfo(int chainc, ... any) -> ...
```

## Description

Returns information fields from chainc in the same order as the requested CHAININFO_* constants.
Use chainc=0 for the currently resolving Chain. Unknown requested fields return nil, and no values are returned if the Chain does not exist.

## Parameters

- `chainc` `int`
- `...` `any`

## Returns

- `...`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4947`
