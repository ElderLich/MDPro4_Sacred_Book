# Card.ReverseInDeck

## Signature

```lua
Card.ReverseInDeck(Card c) -> void
```

## Description

Marks c face-up while it is in the Deck.
If c is the current top card of the Main Deck, the core also sends the top-of-Deck update to the client.

## Parameters

- `c` `Card`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3659`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **3** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.ReverseInDeck`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Pharaoh's Treasure | `63571750` | [Scripts/c63571750.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63571750.lua) | 27 |
| Parasite Paracide | `27911549` | [Scripts/c27911549.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27911549.lua) | 24 |
| Grave Lure | `57270476` | [Scripts/c57270476.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57270476.lua) | 18 |

## Script Examples

### Pharaoh's Treasure (`63571750`)

Source: [Scripts/c63571750.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63571750.lua)

```lua
	if not c:IsLocation(LOCATION_DECK) then return end
	Duel.ShuffleDeck(tp)
	c:ReverseInDeck()
	local e1=Effect.CreateEffect(c)
	e1:SetDescription(aux.Stringid(63571750,0))
```

### Parasite Paracide (`27911549`)

Source: [Scripts/c27911549.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27911549.lua)

```lua
	if not c:IsLocation(LOCATION_DECK) then return end
	Duel.ShuffleDeck(1-tp)
	c:ReverseInDeck()
	local e1=Effect.CreateEffect(c)
	e1:SetDescription(aux.Stringid(27911549,1))
```

### Grave Lure (`57270476`)

Source: [Scripts/c57270476.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57270476.lua)

```lua
		local tc=g:GetFirst()
		Duel.ShuffleDeck(1-tp)
		tc:ReverseInDeck()
		local e1=Effect.CreateEffect(e:GetHandler())
		e1:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_CONTINUOUS)
```
