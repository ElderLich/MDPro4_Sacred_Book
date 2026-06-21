# Card.IsLinkSummonable

## Signature

```lua
Card.IsLinkSummonable(Card c, [Group|nil mg], [int min], [int max]) -> bool
```

## Description

Check if card c can be Link Summoned using [min-max Link Materials] from cards on the field [or mg]
If mg is nil, this function is equivalent to c:IsSpecialSummonable(SUMMON_TYPE_LINK)

## Parameters

- `c` `Card`
- `mg` `Group|nil` optional
- `min` `int` optional - default: 0
- `max` `int` optional - default: 0

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3578`
