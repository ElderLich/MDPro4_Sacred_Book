# Auxiliary.SelectFromOptions

## Signature

```lua
Auxiliary.SelectFromOptions(int tp, ... table) -> any|nil
```

## Description

Filters option tables by their condition, calls Duel.SelectOption with the available option labels, and returns the selected table's custom value or original index.
Each option is {condition, option\[, value\]}. If no condition is true, the helper returns nil. Its default index return is 1-based, unlike Duel.SelectOption's 0-based return.

## Parameters

- `tp` `int`
- `...` `table`

## Returns

- `any|nil` - Selected option value or 1-based option index; nil if no option is available.

## Source

- `Utilities/utility.lua:152`

## Guided Examples

Learn how to use this function in context:

- [Ritual Summon Choices](/learn/ritual-summon-choices)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **162** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.SelectFromOptions) with `Auxiliary.SelectFromOptions`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Gem-Knight Dispersion](/examples/cards/24220368) | `24220368` | [Scripts/c24220368.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c24220368.lua) | 1 |
| [Magnet Bonding](/examples/cards/65514302) | `65514302` | [Scripts/c65514302.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c65514302.lua) | 1 |
| [Hecahands Tartaros](/examples/cards/57809669) | `57809669` | [Scripts/c57809669.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c57809669.lua) | 1 |
| [Chimera Fusion](/examples/cards/63136489) | `63136489` | [Scripts/c63136489.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c63136489.lua) | 1 |
| [Vidolium the Unstable Power Patron of Unity](/examples/cards/70488851) | `70488851` | [Scripts/c70488851.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c70488851.lua) | 1 |
| [A Bao A Qu, the Lightless Shadow](/examples/cards/4731783) | `4731783` | [Scripts/c4731783.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c4731783.lua) | 1 |
| [Camelot, Realm of Noble Knights and Noble Arms](/examples/cards/15635751) | `15635751` | [Scripts/c15635751.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c15635751.lua) | 1 |
| [Earthbound Servant Geo Gremlin](/examples/cards/8690387) | `8690387` | [Scripts/c8690387.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c8690387.lua) | 1 |
| [Stars Align Above the Shrine](/examples/cards/15306543) | `15306543` | [Scripts/c15306543.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c15306543.lua) | 1 |
| [Mitsurugi Magatama](/examples/cards/76725398) | `76725398` | [Scripts/c76725398.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c76725398.lua) | 1 |
| Witchcrafter Celebration | `6958567` | [Scripts/c6958567.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c6958567.lua) | 1 |
| Super Duper Polymerization | `44886582` | [Scripts/c44886582.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c44886582.lua) | 1 |
| Double Interlock | `38129297` | [Scripts/c38129297.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c38129297.lua) | 1 |
| Number 101: Silent Honor ARK - Soul Asylum | `2419596` | [Scripts/c2419596.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c2419596.lua) | 1 |
| Dark Contact | `77124096` | [Scripts/c77124096.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c77124096.lua) | 1 |
| Clown Crew Soiree Operations | `70058649` | [Scripts/c70058649.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c70058649.lua) | 1 |
| Sinful Spoils of the White Forest | `3496543` | [Scripts/c3496543.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c3496543.lua) | 1 |
| Yummy☆Surprise | `29369059` | [Scripts/c29369059.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c29369059.lua) | 1 |
| Spirit Poacher | `85150300` | [Scripts/c85150300.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c85150300.lua) | 1 |
| Shimmering Shatterer of the Sacred Beasts | `3441553` | [Scripts/c3441553.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c3441553.lua) | 2 |
| Megalith Anastasis | `29876299` | [Scripts/c29876299.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c29876299.lua) | 1 |
| Fabled Realm's Revival | `57775790` | [Scripts/c57775790.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c57775790.lua) | 1 |
| Psychic Omnibuster | `70659412` | [Scripts/c70659412.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c70659412.lua) | 1 |
| Enneacraft Reverth | `80015408` | [Scripts/c80015408.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c80015408.lua) | 1 |
| ...and 138 more |  |  |  |

## Script Examples

### Gem-Knight Dispersion (`24220368`)

Source: [Scripts/c24220368.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c24220368.lua)

```lua
	end
	if b1 and b2 then
		op=aux.SelectFromOptions(tp,
			{b1,aux.Stringid(id,1)},
			{b2,aux.Stringid(id,2)})
```

### Magnet Bonding (`65514302`)

Source: [Scripts/c65514302.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c65514302.lua)

```lua
	local op=0
	if b1 or b2 or b3 then
		op=aux.SelectFromOptions(tp,
			{b1,aux.Stringid(id,1),1},
			{b2,aux.Stringid(id,2),2},
```

### Hecahands Tartaros (`57809669`)

Source: [Scripts/c57809669.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c57809669.lua)

```lua
	local op=0
	if b1 or b2 then
		op=aux.SelectFromOptions(tp,
			{b1,aux.Stringid(id,1),1},
			{b2,aux.Stringid(id,2),2})
```
