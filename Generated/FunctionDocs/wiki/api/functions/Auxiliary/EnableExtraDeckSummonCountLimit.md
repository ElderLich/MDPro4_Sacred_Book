# Auxiliary.EnableExtraDeckSummonCountLimit

## Signature

```lua
Auxiliary.EnableExtraDeckSummonCountLimit() -> void
```

## Description

Initializes the shared Extra Deck Summon count table with one count for each player and registers a global Draw Phase Start reset. The helper only manages the counter; individual card scripts still check and decrement it.

## Source

- `Utilities/utility.lua:482`
