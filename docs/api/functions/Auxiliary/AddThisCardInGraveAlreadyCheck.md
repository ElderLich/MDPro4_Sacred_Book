# Auxiliary.AddThisCardInGraveAlreadyCheck

## Signature

```lua
Auxiliary.AddThisCardInGraveAlreadyCheck(Card c) -> void
```

## Description

Registers a continuous effect on c that records the effect that sent c to the Graveyard.
This lets later Graveyard-condition checks distinguish a card that was already in the Graveyard from one sent there by the currently resolving effect.

## Parameters

- `c` `Card`

## Source

- `Utilities/utility.lua:1551`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **40** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.AddThisCardInGraveAlreadyCheck) with `Auxiliary.AddThisCardInGraveAlreadyCheck`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Predaplant Bal Teah](/examples/cards/66787942) | `66787942` | [Scripts/c66787942.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c66787942.lua) | 1 |
| Abyss-steam | `63941169` | [Scripts/c63941169.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c63941169.lua) | 1 |
| Masked HERO Furnace | `58288218` | [Scripts/c58288218.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c58288218.lua) | 1 |
| Unchained Soul Lord of Yama | `24269961` | [Scripts/c24269961.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c24269961.lua) | 1 |
| Armed Rebeellion | `21056275` | [Scripts/c21056275.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c21056275.lua) | 1 |
| Maiden of Blue Tears | `99176254` | [Scripts/c99176254.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c99176254.lua) | 1 |
| Tachyon Cloudragon | `72705654` | [Scripts/c72705654.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c72705654.lua) | 1 |
| Mirage Swordsman | `73936388` | [Scripts/c73936388.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c73936388.lua) | 1 |
| Naturia Mole Cricket | `93454062` | [Scripts/c93454062.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c93454062.lua) | 1 |
| Thousand Umbral Horror | `2932235` | [Scripts/c2932235.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c2932235.lua) | 1 |
| Cross Keeper | `40740224` | [Scripts/c40740224.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c40740224.lua) | 1 |
| Amphibious Swarmship Amblowhale | `20665527` | [Scripts/c20665527.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c20665527.lua) | 1 |
| Sacred Fire King Garunix | `66431519` | [Scripts/c66431519.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c66431519.lua) | 1 |
| Predaprimitive | `89176044` | [Scripts/c89176044.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c89176044.lua) | 1 |
| Unchained Ogre Shara | `95136979` | [Scripts/c95136979.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c95136979.lua) | 1 |
| The Abyss Dragon Swordsoul | `5141117` | [Scripts/c5141117.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c5141117.lua) | 1 |
| Geistgrinder Golem | `26913989` | [Scripts/c26913989.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c26913989.lua) | 1 |
| Blackwing - Shamal the Sandstorm | `8571567` | [Scripts/c8571567.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c8571567.lua) | 1 |
| Maiden of White | `17947697` | [Scripts/c17947697.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c17947697.lua) | 1 |
| Dillingerous Dragon | `23732205` | [Scripts/c23732205.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c23732205.lua) | 1 |
| Assault Lion | `67676619` | [Scripts/c67676619.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c67676619.lua) | 1 |
| Galaxy War Drake | `19316241` | [Scripts/c19316241.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c19316241.lua) | 1 |
| Promethean Princess, Bestower of Flames | `2772337` | [Scripts/c2772337.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c2772337.lua) | 1 |
| Assault Synchron | `77202120` | [Scripts/c77202120.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c77202120.lua) | 1 |
| ...and 16 more |  |  |  |

## Script Examples

### Predaplant Bal Teah (`66787942`)

Source: [Scripts/c66787942.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c66787942.lua)

```lua
	aux.AddCodeList(c,24094653)
	--same effect send this card to grave and summon another card check
	local e0=aux.AddThisCardInGraveAlreadyCheck(c)
	--Synchro summon
	aux.AddSynchroProcedure(c,nil,aux.NonTuner(nil),1)
```

### Abyss-steam (`63941169`)

Source: [Scripts/c63941169.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c63941169.lua)

```lua
function s.initial_effect(c)
	--same effect send this card to grave and spsummon another card check
	local e0=aux.AddThisCardInGraveAlreadyCheck(c)
	--draw
	local e1=Effect.CreateEffect(c)
```

### Masked HERO Furnace (`58288218`)

Source: [Scripts/c58288218.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c58288218.lua)

```lua
function s.initial_effect(c)
	aux.AddCodeList(c,21143940,24094653)
	local e0=aux.AddThisCardInGraveAlreadyCheck(c)
	--search
	local e1=Effect.CreateEffect(c)
```
