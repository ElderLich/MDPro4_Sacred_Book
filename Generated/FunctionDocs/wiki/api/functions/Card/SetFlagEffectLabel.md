# Card.SetFlagEffectLabel

## Signature

```lua
Card.SetFlagEffectLabel(Card c, int code, int label) -> bool
```

## Description

Sets the first matching flag effect label for code on c to label and returns whether a flag effect was found.

## Parameters

- `c` `Card` - Card whose matching flag effect is updated.
- `code` `int` - Flag-effect code to find.
- `label` `int` - New integer label stored on the first matching flag effect.

## Returns

- `bool` - True if a matching flag effect was updated; false if none exists.

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3558`
