# Auxiliary.RegisterMergedDelayedEvent_ToSingleCard

## Signature

```lua
Auxiliary.RegisterMergedDelayedEvent_ToSingleCard(Card c, int code, int|table events) -> int
```

## Description

Registers single-card merged delayed event listeners for one event or a table of events, returning the generated custom event code. The helper clears stored cards when the owner moves to a public state and installs the shared Chain End raiser when needed.

## Parameters

- `c` `Card`
- `code` `int`
- `events` `int|table`

## Returns

- `int` - The generated custom event code.

## Source

- `Utilities/utility.lua:1687`
