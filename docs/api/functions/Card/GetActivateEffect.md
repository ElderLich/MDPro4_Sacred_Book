# Card.GetActivateEffect

## Signature

```lua
Card.GetActivateEffect(Card c) -> Effect|nil
```

## Description

Returns c's activation effect, the effect with type EFFECT_TYPE_ACTIVATE. This is mainly used for Spell/Trap Cards.
Returns nil when the card has no registered activation effect, so guard the result before calling Effect methods.
Use the returned Effect to check whether a Field Spell or other Spell/Trap can be activated before moving or resolving it through another effect.

## Parameters

- `c` `Card`

## Returns

- `Effect|nil` - The activation effect registered on c, or nil if none is registered.

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3599`

## Guided Examples

Learn how to use this function in context:

- [Field Spells](/learn/field-spells)
- [Spell Card Patterns](/learn/spell-card-patterns)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **30** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.GetActivateEffect) with `Card.GetActivateEffect`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Ghostrick Renovation](/examples/cards/61818176) | `61818176` | [Scripts/c61818176.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c61818176.lua) | 2 |
| [Ursarctic Polari](/examples/cards/27693363) | `27693363` | [Scripts/c27693363.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c27693363.lua) | 2 |
| Sea Stealth Attack | `19089195` | [Scripts/c19089195.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c19089195.lua) | 3 |
| Favorite Hero | `11881272` | [Scripts/c11881272.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c11881272.lua) | 2 |
| Triamid Dancer | `69529337` | [Scripts/c69529337.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c69529337.lua) | 2 |
| Numeron Wall | `42352091` | [Scripts/c42352091.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c42352091.lua) | 2 |
| The Sacred Waters in the Sky | `26684111` | [Scripts/c26684111.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c26684111.lua) | 2 |
| Triamid Master | `32912040` | [Scripts/c32912040.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c32912040.lua) | 2 |
| Performapal Sky Magician | `73734821` | [Scripts/c73734821.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c73734821.lua) | 2 |
| Super Quantal Alphan Spike | `72332074` | [Scripts/c72332074.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c72332074.lua) | 2 |
| Bait Doll | `7165085` | [Scripts/c7165085.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c7165085.lua) | 1 |
| Necrovalley Temple | `56773577` | [Scripts/c56773577.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c56773577.lua) | 3 |
| Springans Booty | `7496001` | [Scripts/c7496001.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c7496001.lua) | 3 |
| Triamid Hunter | `95923441` | [Scripts/c95923441.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c95923441.lua) | 2 |
| Labrynth Archfiend | `48745395` | [Scripts/c48745395.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c48745395.lua) | 1 |
| Double Spell | `24096228` | [Scripts/c24096228.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c24096228.lua) | 1 |
| F.A. Overheat | `32036866` | [Scripts/c32036866.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c32036866.lua) | 2 |
| Dream Mirror of Joy | `74665651` | [Scripts/c74665651.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c74665651.lua) | 3 |
| Vampire Takeover | `22900598` | [Scripts/c22900598.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c22900598.lua) | 2 |
| Dream Mirror of Terror | `1050355` | [Scripts/c1050355.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c1050355.lua) | 3 |
| Malefic Territory | `75223115` | [Scripts/c75223115.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c75223115.lua) | 2 |
| Ignis Heat, the True Dracowarrior | `22499034` | [Scripts/c22499034.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c22499034.lua) | 3 |
| Dinomight Knight, the True Dracofighter | `58984738` | [Scripts/c58984738.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c58984738.lua) | 3 |
| Metaverse | `89208725` | [Scripts/c89208725.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c89208725.lua) | 2 |
| ...and 6 more |  |  |  |

## Script Examples

### Ghostrick Renovation (`61818176`)

Source: [Scripts/c61818176.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c61818176.lua)

```lua
end
function c61818176.actfilter(c,tp)
	return c:IsType(TYPE_FIELD) and c:GetActivateEffect():IsActivatable(tp,true,true)
end
function c61818176.activate(e,tp,eg,ep,ev,re,r,rp)
```

### Ursarctic Polari (`27693363`)

Source: [Scripts/c27693363.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c27693363.lua)

```lua
end
function c27693363.actfilter(c,tp)
	return c:IsCode(89264428) and c:GetActivateEffect():IsActivatable(tp,true,true)
end
function c27693363.acttg(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Sea Stealth Attack (`19089195`)

Source: [Scripts/c19089195.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c19089195.lua)

```lua
function c19089195.filter(c,tp)
	return c:IsCode(22702055) and (c:IsType(TYPE_FIELD) or Duel.GetLocationCount(tp,LOCATION_SZONE)>0)
		and c:GetActivateEffect() and c:GetActivateEffect():IsActivatable(tp,true,true)
end
function c19089195.activate(e,tp,eg,ep,ev,re,r,rp)
```
