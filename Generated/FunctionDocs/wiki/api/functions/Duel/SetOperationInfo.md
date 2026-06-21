# Duel.SetOperationInfo

## Signature

```lua
Duel.SetOperationInfo(int chainc, int category, [Card|Group|nil|0 targets], int count, int target_player, int target_param) -> void
```

## Description

Sets the operation information of the currently processed chain This operation information contains the effect classification determined in the effect processing to be processed
For example, stealth snipers need to set CATEGORY_DICE, but can not set CATEGORY_DESTROY, because not sure
For destructive effects, targets need to be set to launch the object may become the impact of chain card,
And sets count to the number of cards to be processed as determined at launch
For example, when the black hole launched, targets need to be set to all the monsters on the field, count to set the number of strange field
For CATEGORY_SPECIAL_SUMMON, CATEGORY_TOHAND, CATEGORY_TODECK, etc., which need to move the card position,
If the card to be processed is deterministic (such as fetching objects), set targets for these cards, count for the number,
If the card to be processed is uncertain (the effect can be determined when processing, is generally not take the effect of the object)
Set the targets to nil, count is expected to deal with the number of cards,
Target_player is expected to be handled by the holder of the card (not sure to 0)
Target_param is the location of the card expected to be processed
For example: SetOperationInfo (0, CATEGORY_TOHAND, nil, 1, tp, LOCATION_DECK)
Operational information is used to initiate detection of many effects, such as Stardust Dragon, Royal Valley

## Parameters

- `chainc` `int`
- `category` `int`
- `targets` `Card|Group|nil|0` optional
- `count` `int`
- `target_player` `int`
- `target_param` `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5008`
