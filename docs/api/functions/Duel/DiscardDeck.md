# Duel.DiscardDeck

## Signature

```lua
Duel.DiscardDeck(int player, int count, int reason) -> int
```

## Description

Sends count cards from the top of player's Deck to the Graveyard for reason, and returns the number actually moved.

## Parameters

- `player` `int`
- `count` `int`
- `reason` `int`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4910`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **136** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.DiscardDeck`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Enlightenment Dragon](/examples/cards/46186135) | `46186135` | [Scripts/c46186135.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46186135.lua) | 1 |
| Tearlaments Scheiren | `572850` | [Scripts/c572850.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c572850.lua) | 1 |
| Tearlaments Havnis | `37961969` | [Scripts/c37961969.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37961969.lua) | 1 |
| Deep Sea Minstrel | `71978434` | [Scripts/c71978434.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71978434.lua) | 1 |
| Tearlaments Merrli | `74078255` | [Scripts/c74078255.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74078255.lua) | 1 |
| Cyberse Clock Dragon | `42717221` | [Scripts/c42717221.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42717221.lua) | 1 |
| Naturia Mole Cricket | `93454062` | [Scripts/c93454062.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93454062.lua) | 1 |
| Tearlaments Kitkallos | `92731385` | [Scripts/c92731385.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92731385.lua) | 1 |
| Deep Sea Sentry | `45483489` | [Scripts/c45483489.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45483489.lua) | 1 |
| Speedroid Gum Prize | `70939418` | [Scripts/c70939418.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70939418.lua) | 1 |
| Laundry Trap | `79371769` | [Scripts/c79371769.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c79371769.lua) | 1 |
| The Zombie Vampire | `73082255` | [Scripts/c73082255.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c73082255.lua) | 2 |
| Curious, the Lightsworn Dominion | `98095162` | [Scripts/c98095162.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c98095162.lua) | 1 |
| Agido the Ancient Sentinel | `62320425` | [Scripts/c62320425.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62320425.lua) | 1 |
| Minerva, the Athenian Lightsworn | `18843291` | [Scripts/c18843291.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18843291.lua) | 1 |
| Deep Sea Artisan | `8495780` | [Scripts/c8495780.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8495780.lua) | 1 |
| Virtual World City - Kauwloon | `14886190` | [Scripts/c14886190.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c14886190.lua) | 1 |
| Clear Phantom | `70717628` | [Scripts/c70717628.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70717628.lua) | 1 |
| Wrecker Panda | `28139785` | [Scripts/c28139785.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28139785.lua) | 1 |
| Michael, the Arch-Lightsworn | `4779823` | [Scripts/c4779823.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4779823.lua) | 1 |
| Minerva, the Exalted Lightsworn | `30100551` | [Scripts/c30100551.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30100551.lua) | 2 |
| Jain, Twilightsworn General | `84673417` | [Scripts/c84673417.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84673417.lua) | 1 |
| Naturia Ladybug | `19605133` | [Scripts/c19605133.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c19605133.lua) | 1 |
| Slash Draw | `71344451` | [Scripts/c71344451.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71344451.lua) | 1 |
| ...and 112 more |  |  |  |

## Script Examples

### Enlightenment Dragon (`46186135`)

Source: [Scripts/c46186135.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46186135.lua)

```lua
end
function s.tgop(e,tp,eg,ep,ev,re,r,rp)
	Duel.DiscardDeck(tp,4,REASON_EFFECT)
end
function s.thcon(e,tp,eg,ep,ev,re,r,rp)
```

### Tearlaments Scheiren (`572850`)

Source: [Scripts/c572850.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c572850.lua)

```lua
			and Duel.IsPlayerCanDiscardDeck(tp,1) then
			Duel.BreakEffect()
			Duel.DiscardDeck(tp,3,REASON_EFFECT)
		end
	end
```

### Tearlaments Havnis (`37961969`)

Source: [Scripts/c37961969.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37961969.lua)

```lua
function c37961969.tgop(e,tp,eg,ep,ev,re,r,rp)
	if e:GetHandler():IsRelateToEffect(e) and Duel.SpecialSummon(e:GetHandler(),0,tp,tp,false,false,POS_FACEUP)>0 then
		Duel.DiscardDeck(tp,3,REASON_EFFECT)
	end
end
```
