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

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.HasMentionedCounter) with `Auxiliary.HasMentionedCounter`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Spell Power Attainment | `39123673` | [Scripts/c39123673.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39123673.lua) | 2 |

## Script Examples

### Spell Power Attainment (`39123673`)

Source: [Scripts/c39123673.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39123673.lua)

```lua
	[0x1]=true,
}
function Auxiliary.HasMentionedCounter(c,counter)
	return c.mentioned_counter and c.mentioned_counter[counter] or false
end
```
