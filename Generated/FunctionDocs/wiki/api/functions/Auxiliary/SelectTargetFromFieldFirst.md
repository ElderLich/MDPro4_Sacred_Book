# Auxiliary.SelectTargetFromFieldFirst

## Signature

```lua
Auxiliary.SelectTargetFromFieldFirst(int tp, function f, int player, int s, int o, int min, int max, any ex, ... any) -> Group
```

## Description

Target-selection helper that first offers matching on-field effect targets with HINTMSG_FIELD_FIRST. If accepted, it sets those cards as targets; otherwise it restores the previous hint and falls back to Duel.SelectTarget.

## Parameters

- `tp` `int`
- `f` `function`
- `player` `int`
- `s` `int`
- `o` `int`
- `min` `int`
- `max` `int`
- `ex` `any`
- `...` `any`

## Returns

- `Group` - The selected target cards.

## Source

- `Utilities/utility.lua:1395`
