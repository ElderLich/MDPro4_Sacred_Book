# Auxiliary.HasMentionedCounter

## Signature

```lua
Auxiliary.HasMentionedCounter(Card c, int counter) -> bool
```

## Description

Checks c.mentioned_counter\[counter\], returning that entry when present and false otherwise. The card script must declare its mentioned_counter table; this checks mention metadata, not counters currently on the card.

## Parameters

- `c` `Card`
- `counter` `int` - Counter identifier.

## Returns

- `bool` - Scripts use true entries for mentioned counter identifiers.

## Source

- `Utilities/utility.lua:581`
