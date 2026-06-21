# Duel.GetReleaseGroupCount

## Signature

```lua
Duel.GetReleaseGroupCount(int player, [bool use_hand], [int reason]) -> int
```

## Description

Returns the number of cards player can Tribute/Release for effect purposes. If use_hand is true, valid cards in the hand are included.

## Parameters

- `player` `int`
- `use_hand` `bool` optional - default: false
- `reason` `int` optional - default: REASON_COST

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4975`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
