# Duel.GetChainInfo

## Signature

```lua
Duel.GetChainInfo(int chainc, ... any) -> ...
```

## Description

Returns the chainc information, if chainc = 0, returns the chain of information currently being processed
This function returns the corresponding number of return values ​​in sequence according to the number of arguments passed in. The arguments can be:
CHAININFO_CHAIN_COUNT The serial number of the chain
CHAININFO_TRIGGERING_EFFECT The effect of the chain
CHAININFO_TRIGGERING_PLAYER
CHAININFO_TRIGGERING_CONTROLER The player to which the chained position belongs
CHAININFO_TRIGGERING_LOCATION The location where the chain occurred
CHAININFO_TRIGGERING_SEQUENCE The number of the position where the chain occurred
CHAININFO_TARGET_CARDS Chain of object cards
CHAININFO_TARGET_PLAYER The target player for the chain
CHAININFO_TARGET_PARAM The object parameters of the chain
CHAININFO_DISABLE_REASON The chain is invalid for the effect of the effect
CHAININFO_DISABLE_PLAYER The chain is invalid for the reason the player
CHAININFO_CHAIN_ID The unique identifier for the chain
CHAININFO_TYPE Type of Chain Card (Monster, Magic, Trap)
CHAININFO_EXTTYPE The specific type of chain card (for example, monster, continuous magic, counterattack trap)
For example:
Duel.GetChainInfo(0, CHAININFO_TRIGGERING_LOCATION, CHAININFO_TARGET_CARDS)
This will return the location and object card where the current chain occurred

## Parameters

- `chainc` `int`
- `...` `any`

## Returns

- `...`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4947`
