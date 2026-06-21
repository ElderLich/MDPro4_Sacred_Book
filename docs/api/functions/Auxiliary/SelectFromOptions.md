# Auxiliary.SelectFromOptions

## Signature

```lua
Auxiliary.SelectFromOptions(int tp, ... table) -> int
```

## Description

Duel.SelectOption with option condition
Return value starts from 1, different from Duel.SelectOption

## Parameters

- `tp` `int`
- `...` `table` - {condition, option\[, value\]}

## Returns

- `int`

## Source

- `Utilities/utility.lua:152`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **135** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.SelectFromOptions`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Gem-Knight Dispersion](/examples/cards/24220368) | `24220368` | [Scripts/c24220368.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24220368.lua) | 66 |
| [Magnet Bonding](/examples/cards/65514302) | `65514302` | [Scripts/c65514302.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65514302.lua) | 65 |
| [Hecahands Tartaros](/examples/cards/57809669) | `57809669` | [Scripts/c57809669.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57809669.lua) | 65 |
| [Chimera Fusion](/examples/cards/63136489) | `63136489` | [Scripts/c63136489.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63136489.lua) | 62 |
| [Vidolium the Unstable Power Patron of Unity](/examples/cards/70488851) | `70488851` | [Scripts/c70488851.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70488851.lua) | 61 |
| [A Bao A Qu, the Lightless Shadow](/examples/cards/4731783) | `4731783` | [Scripts/c4731783.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4731783.lua) | 61 |
| [Camelot, Realm of Noble Knights and Noble Arms](/examples/cards/15635751) | `15635751` | [Scripts/c15635751.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15635751.lua) | 61 |
| [Earthbound Servant Geo Gremlin](/examples/cards/8690387) | `8690387` | [Scripts/c8690387.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8690387.lua) | 61 |
| Super Duper Polymerization | `44886582` | [Scripts/c44886582.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44886582.lua) | 59 |
| Double Interlock | `38129297` | [Scripts/c38129297.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38129297.lua) | 59 |
| Dark Contact | `77124096` | [Scripts/c77124096.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77124096.lua) | 58 |
| Clown Crew Soiree Operations | `70058649` | [Scripts/c70058649.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70058649.lua) | 57 |
| Sinful Spoils of the White Forest | `3496543` | [Scripts/c3496543.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3496543.lua) | 56 |
| Yummy☆Surprise | `29369059` | [Scripts/c29369059.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29369059.lua) | 55 |
| Spirit Poacher | `85150300` | [Scripts/c85150300.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85150300.lua) | 54 |
| Megalith Anastasis | `29876299` | [Scripts/c29876299.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29876299.lua) | 54 |
| Fabled Realm's Revival | `57775790` | [Scripts/c57775790.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57775790.lua) | 54 |
| Psychic Omnibuster | `70659412` | [Scripts/c70659412.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70659412.lua) | 52 |
| Enneacraft Reverth | `80015408` | [Scripts/c80015408.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80015408.lua) | 52 |
| Clown Crew Biancaviso | `82159583` | [Scripts/c82159583.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82159583.lua) | 52 |
| Shadow Severing Strike | `57232301` | [Scripts/c57232301.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57232301.lua) | 52 |
| Kewl Tune B2B | `65961304` | [Scripts/c65961304.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65961304.lua) | 52 |
| Clown Crew Meteor | `93172951` | [Scripts/c93172951.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93172951.lua) | 52 |
| Stellarnova Binding | `69678646` | [Scripts/c69678646.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c69678646.lua) | 50 |
| ...and 111 more |  |  |  |

## Script Examples

### Gem-Knight Dispersion (`24220368`)

Source: [Scripts/c24220368.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24220368.lua)

```lua
	end
	if b1 and b2 then
		op=aux.SelectFromOptions(tp,
			{b1,aux.Stringid(id,1)},
			{b2,aux.Stringid(id,2)})
```

### Magnet Bonding (`65514302`)

Source: [Scripts/c65514302.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65514302.lua)

```lua
	local op=0
	if b1 or b2 or b3 then
		op=aux.SelectFromOptions(tp,
			{b1,aux.Stringid(id,1),1},
			{b2,aux.Stringid(id,2),2},
```

### Hecahands Tartaros (`57809669`)

Source: [Scripts/c57809669.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57809669.lua)

```lua
	local op=0
	if b1 or b2 then
		op=aux.SelectFromOptions(tp,
			{b1,aux.Stringid(id,1),1},
			{b2,aux.Stringid(id,2),2})
```
