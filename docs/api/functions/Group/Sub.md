# Group.Sub

## Signature

```lua
Group.Sub(Group g1, Group g2) -> void
```

## Description

Removes every card in g2 from g1. g1 is mutated unless it is read-only; g2 is not changed.

## Parameters

- `g1` `Group`
- `g2` `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libgroup.cpp:930`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **89** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Group.Sub) with `Group.Sub`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Artmage Non-Finito](/examples/cards/74631897) | `74631897` | [Scripts/c74631897.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74631897.lua) | 1 |
| [Ashtraja Susanoo](/examples/cards/17020474) | `17020474` | [Scripts/c17020474.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17020474.lua) | 1 |
| [D/D/D Alfred the Divine Sage King](/examples/cards/11852093) | `11852093` | [Scripts/c11852093.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11852093.lua) | 1 |
| [El Shaddoll Apkallone](/examples/cards/50907446) | `50907446` | [Scripts/c50907446.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50907446.lua) | 1 |
| [Mementotlan Fusion](/examples/cards/66518509) | `66518509` | [Scripts/c66518509.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66518509.lua) | 1 |
| [Performage Cup Tricker](/examples/cards/6812770) | `6812770` | [Scripts/c6812770.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6812770.lua) | 1 |
| [D/D Count Surveyor](/examples/cards/5997110) | `5997110` | [Scripts/c5997110.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5997110.lua) | 2 |
| Aroma Blend | `25861589` | [Scripts/c25861589.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25861589.lua) | 1 |
| Invocation - "Sword" | `37432075` | [Scripts/c37432075.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37432075.lua) | 1 |
| Invocation | `74063034` | [Scripts/c74063034.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74063034.lua) | 1 |
| A-to-Z-Dragon Buster Cannon | `65172015` | [Scripts/c65172015.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65172015.lua) | 1 |
| Branded in White | `34995106` | [Scripts/c34995106.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34995106.lua) | 1 |
| S:P Little Knight | `29301450` | [Scripts/c29301450.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29301450.lua) | 1 |
| Alba System Dogmatikalamity | `93053159` | [Scripts/c93053159.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93053159.lua) | 2 |
| Lunalight Masquerade | `2344618` | [Scripts/c2344618.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2344618.lua) | 1 |
| Amazoness Secret Arts | `86758746` | [Scripts/c86758746.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c86758746.lua) | 1 |
| Berserkion the Electromagna Warrior | `42901635` | [Scripts/c42901635.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42901635.lua) | 1 |
| Nebulus, Dragon Ruler of Mishaps | `94655777` | [Scripts/c94655777.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c94655777.lua) | 1 |
| Heavy Interlock | `20071842` | [Scripts/c20071842.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20071842.lua) | 1 |
| Gem-Knight Master Diamond Dispersion | `25342956` | [Scripts/c25342956.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25342956.lua) | 2 |
| Number 4: Stealth Kragen | `67557908` | [Scripts/c67557908.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67557908.lua) | 1 |
| ABC-Dragon Buster | `1561110` | [Scripts/c1561110.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1561110.lua) | 1 |
| Magikey Maftea | `99426088` | [Scripts/c99426088.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c99426088.lua) | 1 |
| Metaltron XII, the True Dracombatant | `57761191` | [Scripts/c57761191.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57761191.lua) | 1 |
| ...and 65 more |  |  |  |

## Script Examples

### Artmage Non-Finito (`74631897`)

Source: [Scripts/c74631897.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74631897.lua)

```lua
	local g=e:GetLabelObject()
	local dg=g:Filter(s.disfilter,nil)
	g:Sub(dg)
	Duel.SendtoGrave(dg,REASON_SPSUMMON+REASON_DISCARD)
	Duel.Release(g,REASON_SPSUMMON)
```

### Ashtraja Susanoo (`17020474`)

Source: [Scripts/c17020474.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17020474.lua)

```lua
				end
				local tmg=tg:Clone()
				tmg:Sub(selg)
				local tc=tmg:SelectUnselect(selg,tp,finish,false,1,tg:GetCount())
				if not tc then
```

### D/D/D Alfred the Divine Sage King (`11852093`)

Source: [Scripts/c11852093.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11852093.lua)

```lua
		Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_TOFIELD)
		pg=g:Select(tp,ct,ct,nil)
		g:Sub(pg)
	else
		g=Group.CreateGroup()
```
