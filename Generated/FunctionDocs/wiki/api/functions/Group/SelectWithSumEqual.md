# Group.SelectWithSumEqual

## Signature

```lua
Group.SelectWithSumEqual(Group g, int player, function f, int acc, int min, int max, [... any]) -> Group|nil
```

## Description

Lets player select cards from g whose f-sum equals acc using between min and max cards.
Cards previously set with Duel.SetSelectedCard are forced into the sum, removed from the selectable pool, cleared afterward, and are not included in the returned Group.

## Parameters

- `g` `Group`
- `player` `int`
- `f` `function`
- `acc` `int`
- `min` `int`
- `max` `int`
- `...` `any` optional

## Returns

- `Group|nil` - Selected optional cards, or nil for invalid player.

## Source

- `D:\Programs\GitHub\ygopro-core\libgroup.cpp:921`
