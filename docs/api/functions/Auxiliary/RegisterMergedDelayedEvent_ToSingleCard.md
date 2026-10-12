# Auxiliary.RegisterMergedDelayedEvent_ToSingleCard

## Signature

```lua
Auxiliary.RegisterMergedDelayedEvent_ToSingleCard(Card c, int code, int|table events) -> int
```

## Description

Registers single-card merged delayed event listeners for one event or a table of events, returning the generated custom event code. The helper clears stored cards when the owner moves to a public state and installs the shared Chain End raiser when needed.

## Parameters

- `c` `Card`
- `code` `int`
- `events` `int|table`

## Returns

- `int` - The generated custom event code.

## Source

- `Utilities/utility.lua:1687`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **39** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.RegisterMergedDelayedEvent_ToSingleCard) with `Auxiliary.RegisterMergedDelayedEvent_ToSingleCard`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Astrograph Sorcerer, the Starfrost Magician](/examples/cards/48171151) | `48171151` | [Scripts/c48171151.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c48171151.lua) | 1 |
| Starving Venom Wing Dragon | `5148778` | [Scripts/c5148778.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c5148778.lua) | 1 |
| Trirealm Rift Judgment | `65195679` | [Scripts/c65195679.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c65195679.lua) | 1 |
| Number 38: Hope Harbinger Dragon Titanic Galaxy | `63767246` | [Scripts/c63767246.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c63767246.lua) | 1 |
| Unchained Soul Rage Abominator | `21419436` | [Scripts/c21419436.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c21419436.lua) | 1 |
| Weaver of Fairy Tails | `78021082` | [Scripts/c78021082.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c78021082.lua) | 1 |
| Sudden Thunder Swamp | `23611122` | [Scripts/c23611122.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c23611122.lua) | 1 |
| Shadow Severing Strike | `57232301` | [Scripts/c57232301.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c57232301.lua) | 1 |
| Pendulum Witch | `43502497` | [Scripts/c43502497.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c43502497.lua) | 1 |
| Tragic Twin Twined Jewels | `81143465` | [Scripts/c81143465.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c81143465.lua) | 1 |
| Deep-Eyes White Dragon, the Blue Abyss | `67886895` | [Scripts/c67886895.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c67886895.lua) | 1 |
| CXyz Gimmick Puppet Fanatix Machinix | `3685372` | [Scripts/c3685372.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c3685372.lua) | 1 |
| Nouvelles Recipe Book "Recettes de Nouvellez" | `61944066` | [Scripts/c61944066.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c61944066.lua) | 1 |
| Tachyon Cloudragon | `72705654` | [Scripts/c72705654.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c72705654.lua) | 1 |
| Enneapolis | `17621695` | [Scripts/c17621695.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c17621695.lua) | 1 |
| Union Hangar | `66399653` | [Scripts/c66399653.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c66399653.lua) | 1 |
| Exosister Betrayal | `52335937` | [Scripts/c52335937.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c52335937.lua) | 1 |
| Clown Crew New Face | `6547248` | [Scripts/c6547248.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c6547248.lua) | 1 |
| Traptrix Pinguicula | `1688285` | [Scripts/c1688285.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c1688285.lua) | 1 |
| The Iris Swordsoul | `62849088` | [Scripts/c62849088.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c62849088.lua) | 1 |
| Zenet Per Akh | `72278590` | [Scripts/c72278590.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c72278590.lua) | 1 |
| Draco Awakening | `66092596` | [Scripts/c66092596.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c66092596.lua) | 1 |
| Bystial Baldrake | `72656408` | [Scripts/c72656408.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c72656408.lua) | 1 |
| Thundercrash Snarecrow | `53754391` | [Scripts/c53754391.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c53754391.lua) | 1 |
| ...and 15 more |  |  |  |

## Script Examples

### Astrograph Sorcerer, the Starfrost Magician (`48171151`)

Source: [Scripts/c48171151.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c48171151.lua)

```lua
	c:RegisterEffect(e1)
	--special summon
	local custom_code=aux.RegisterMergedDelayedEvent_ToSingleCard(c,id,EVENT_DESTROYED)
	local e2=Effect.CreateEffect(c)
	e2:SetDescription(aux.Stringid(id,1))
```

### Starving Venom Wing Dragon (`5148778`)

Source: [Scripts/c5148778.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c5148778.lua)

```lua
	c:RegisterEffect(e1)
	--gain atk
	local custom_code=aux.RegisterMergedDelayedEvent_ToSingleCard(c,id,EVENT_SPSUMMON_SUCCESS)
	local e2=Effect.CreateEffect(c)
	e2:SetDescription(aux.Stringid(id,1))
```

### Trirealm Rift Judgment (`65195679`)

Source: [Scripts/c65195679.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c65195679.lua)

```lua
	c:RegisterEffect(e1)
	--recycle
	local custom_code=aux.RegisterMergedDelayedEvent_ToSingleCard(c,id,{EVENT_SUMMON_SUCCESS,EVENT_SPSUMMON_SUCCESS})
	local e2=Effect.CreateEffect(c)
	e2:SetDescription(aux.Stringid(id,0))
```
