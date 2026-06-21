# Duel.RevealSelectDeckSequence

## Signature

```lua
Duel.RevealSelectDeckSequence([bool enabled]) -> void
```

## Description

Enables showing the real sequence when selecting cards from the Deck.

## Parameters

- `enabled` `bool` optional - default: true

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4914`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **5** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.RevealSelectDeckSequence`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Hollowrokket Dragon | `51548207` | [Scripts/c51548207.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c51548207.lua) | 45 |
| Kewl Tune Cue | `16387555` | [Scripts/c16387555.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16387555.lua) | 43 |
| Kashtira Ogre | `94392192` | [Scripts/c94392192.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c94392192.lua) | 36 |
| Puppet Shark | `53323475` | [Scripts/c53323475.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53323475.lua) | 30 |
| Hatsugai | `43618262` | [Scripts/c43618262.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43618262.lua) | 26 |

## Script Examples

### Hollowrokket Dragon (`51548207`)

Source: [Scripts/c51548207.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c51548207.lua)

```lua
		local g=Duel.GetDecktopGroup(1-tp,ct)
		Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_REMOVE)
		Duel.RevealSelectDeckSequence(true)
		local sg=g:FilterSelect(tp,Card.IsAbleToRemove,1,1,nil,tp)
		Duel.RevealSelectDeckSequence(false)
```

### Kewl Tune Cue (`16387555`)

Source: [Scripts/c16387555.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16387555.lua)

```lua
	local g=Duel.GetDecktopGroup(1-tp,2)
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_REMOVE)
	Duel.RevealSelectDeckSequence(true)
	local sg=g:FilterSelect(tp,Card.IsAbleToRemove,1,1,nil)
	Duel.RevealSelectDeckSequence(false)
```

### Kashtira Ogre (`94392192`)

Source: [Scripts/c94392192.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c94392192.lua)

```lua
	local g=Duel.GetDecktopGroup(1-tp,ct)
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_REMOVE)
	Duel.RevealSelectDeckSequence(true)
	local sg=g:FilterSelect(tp,c94392192.rmfilter,1,1,nil,tp)
	Duel.RevealSelectDeckSequence(false)
```
