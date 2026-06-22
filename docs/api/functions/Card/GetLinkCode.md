# Card.GetLinkCode

## Signature

```lua
Card.GetLinkCode(Card c) -> int,...?
```

## Description

Returns c's Link Material codes: current code, second code when present, then EFFECT_ADD_LINK_CODE values.

## Parameters

- `c` `Card`

## Returns

- `int` - Current code.
- `...?` - Additional Link Material code values, if any.

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3390`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **19** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.GetLinkCode`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Saryuja Skull Dread | `74997493` | [Scripts/c74997493.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74997493.lua) | 51 |
| Knightmare Unicorn | `38342335` | [Scripts/c38342335.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38342335.lua) | 50 |
| Arcana Extra Joker | `64454614` | [Scripts/c64454614.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c64454614.lua) | 50 |
| Artifact Dagda | `7480763` | [Scripts/c7480763.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7480763.lua) | 47 |
| Knightmare Gryphon | `65330383` | [Scripts/c65330383.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65330383.lua) | 47 |
| Dark Templar @Ignister | `97383507` | [Scripts/c97383507.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97383507.lua) | 44 |
| Beat Cop from the Underworld | `99011763` | [Scripts/c99011763.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c99011763.lua) | 44 |
| Haggard Lizardose | `9763474` | [Scripts/c9763474.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9763474.lua) | 43 |
| Knightmare Cerberus | `75452921` | [Scripts/c75452921.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75452921.lua) | 43 |
| Knightmare Goblin | `39064822` | [Scripts/c39064822.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39064822.lua) | 42 |
| Black Luster Soldier - Soldier of Chaos | `49202162` | [Scripts/c49202162.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49202162.lua) | 42 |
| Knightmare Phoenix | `2857636` | [Scripts/c2857636.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2857636.lua) | 42 |
| Cross-Sheep | `50277355` | [Scripts/c50277355.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50277355.lua) | 41 |
| Ferocious Flame Swordsman | `98642179` | [Scripts/c98642179.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c98642179.lua) | 41 |
| Seraphim Papillion | `91140491` | [Scripts/c91140491.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c91140491.lua) | 39 |
| Shinobi Insect Hagakuremino | `70709488` | [Scripts/c70709488.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70709488.lua) | 39 |
| Barricadeborg Blocker | `13117073` | [Scripts/c13117073.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13117073.lua) | 38 |
| Apollousa, Bow of the Goddess | `4280258` | [Scripts/c4280258.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4280258.lua) | 37 |
| Formud Skipper | `50366775` | [Scripts/c50366775.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50366775.lua) | 34 |

## Script Examples

### Saryuja Skull Dread (`74997493`)

Source: [Scripts/c74997493.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74997493.lua)

```lua
end
function c74997493.lcheck(g,lc)
	return g:GetClassCount(Card.GetLinkCode)==g:GetCount()
end
function c74997493.regcon(e,tp,eg,ep,ev,re,r,rp)
```

### Knightmare Unicorn (`38342335`)

Source: [Scripts/c38342335.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38342335.lua)

```lua
end
function c38342335.lcheck(g,lc)
	return g:GetClassCount(Card.GetLinkCode)==g:GetCount()
end
function c38342335.tdcon(e,tp,eg,ep,ev,re,r,rp)
```

### Arcana Extra Joker (`64454614`)

Source: [Scripts/c64454614.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c64454614.lua)

```lua
end
function c64454614.lcheck(g,lc)
	return g:GetClassCount(Card.GetLinkCode)==g:GetCount()
end
function c64454614.negfilter(c,g)
```
