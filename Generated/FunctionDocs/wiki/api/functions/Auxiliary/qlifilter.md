# Auxiliary.qlifilter

## Signature

```lua
Auxiliary.qlifilter(Effect e, Effect te) -> bool
```

## Description

Qli immunity value helper.
It accepts activated monster effects from monsters whose original Level or Rank is lower than the handler's current Level, and rejects Link Monsters.

## Parameters

- `e` `Effect`
- `te` `Effect`

## Returns

- `bool`

## Source

- `Utilities/utility.lua:895`
