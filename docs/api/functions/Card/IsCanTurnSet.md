# Card.IsCanTurnSet

## Signature

```lua
Card.IsCanTurnSet(Card c) -> bool
```

## Description

Check whether c can turn into the inside of that

## Parameters

- `c` `Card`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3634`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **174** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.IsCanTurnSet`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Salamandra with Chain](/examples/cards/62091148) | `62091148` | [Scripts/c62091148.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62091148.lua) | 81 |
| Regenesis Birth | `27781371` | [Scripts/c27781371.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27781371.lua) | 60 |
| Chaos Hats | `2372506` | [Scripts/c2372506.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2372506.lua) | 59 |
| Magical Hats | `81210420` | [Scripts/c81210420.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81210420.lua) | 59 |
| Enneacraft - Atori.MAR | `54842941` | [Scripts/c54842941.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54842941.lua) | 57 |
| Scrap-Iron Sacred Statue | `85520170` | [Scripts/c85520170.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85520170.lua) | 52 |
| First Penguin | `12975671` | [Scripts/c12975671.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12975671.lua) | 50 |
| King's Resonance | `17269895` | [Scripts/c17269895.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17269895.lua) | 48 |
| Clown Crew Flair | `42759961` | [Scripts/c42759961.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42759961.lua) | 48 |
| Divine Abyss of the Sacred Beast | `86132414` | [Scripts/c86132414.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c86132414.lua) | 47 |
| Subterror Behemoth Burrowing | `28369508` | [Scripts/c28369508.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28369508.lua) | 47 |
| Subterror Final Battle | `74640994` | [Scripts/c74640994.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74640994.lua) | 46 |
| Ultimate Conductor Tyranno | `18940556` | [Scripts/c18940556.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18940556.lua) | 45 |
| Tri-Brigade Arms Mouser | `33781156` | [Scripts/c33781156.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33781156.lua) | 45 |
| Enneacraft Reset | `19504025` | [Scripts/c19504025.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c19504025.lua) | 45 |
| Dreaming Reality of Nemleria, Realized | `16893370` | [Scripts/c16893370.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16893370.lua) | 45 |
| Lavalval Salamander | `67797569` | [Scripts/c67797569.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67797569.lua) | 45 |
| The Executor of the Underworld - Pluto | `37706769` | [Scripts/c37706769.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37706769.lua) | 45 |
| Centaur Mina | `33129626` | [Scripts/c33129626.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33129626.lua) | 45 |
| Ghostrick or Treat | `27170599` | [Scripts/c27170599.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27170599.lua) | 45 |
| Amaze Attraction Horror House | `92650018` | [Scripts/c92650018.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92650018.lua) | 45 |
| Ninjitsu Art Notebook of Mystery | `95545183` | [Scripts/c95545183.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95545183.lua) | 45 |
| Ghostrick Fairy | `36239585` | [Scripts/c36239585.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36239585.lua) | 45 |
| Traptrix Cularia | `952523` | [Scripts/c952523.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c952523.lua) | 44 |
| ...and 150 more |  |  |  |

## Script Examples

### Salamandra with Chain (`62091148`)

Source: [Scripts/c62091148.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62091148.lua)

```lua
end
function s.posfilter(c)
	return c:IsType(TYPE_EFFECT) and c:IsFaceup() and c:IsCanTurnSet()
end
function s.operation(e,tp,eg,ep,ev,re,r,rp)
```

### Regenesis Birth (`27781371`)

Source: [Scripts/c27781371.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27781371.lua)

```lua
end
function s.posfilter(c)
	return c:IsFaceup() and c:IsCanTurnSet()
end
function s.postg(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
```

### Chaos Hats (`2372506`)

Source: [Scripts/c2372506.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2372506.lua)

```lua
end
function s.filter(c)
	return aux.IsCodeListed(c,33599853) and c:GetSequence()<5 and c:IsCanTurnSet()
end
function s.spfilter(c,e,tp)
```
