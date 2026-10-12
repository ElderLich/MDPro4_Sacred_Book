# Auxiliary.EnableArcanaCoin

## Signature

```lua
Auxiliary.EnableArcanaCoin(Card c, int event1, [... int]) -> void
```

## Description

Registers Arcana Force-style mandatory coin-toss trigger effects on c for event1 and any extra events.
The shared operation records the coin result as FLAG_ID_ARCANA_COIN; Reversal of Fate replaces the toss with a player choice.

## Parameters

- `c` `Card`
- `event1` `int`
- `...` `int` optional

## Source

- `Utilities/utility.lua:266`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **11** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.EnableArcanaCoin) with `Auxiliary.EnableArcanaCoin`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Arcana Force EX - The Light Ruler | `5861892` | [Scripts/c5861892.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c5861892.lua) | 1 |
| Arcana Force XV - The Fiend | `59712426` | [Scripts/c59712426.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c59712426.lua) | 1 |
| Arcana Force EX - The Dark Ruler | `69831560` | [Scripts/c69831560.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c69831560.lua) | 1 |
| Arcana Force XXI - The World | `23846921` | [Scripts/c23846921.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c23846921.lua) | 1 |
| Arcana Force XVIII - The Moon | `97452817` | [Scripts/c97452817.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c97452817.lua) | 1 |
| Arcana Force III - The Empress | `35781051` | [Scripts/c35781051.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c35781051.lua) | 1 |
| Arcana Force 0 - The Fool | `62892347` | [Scripts/c62892347.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c62892347.lua) | 1 |
| Arcana Force XIV - Temperance | `60953118` | [Scripts/c60953118.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c60953118.lua) | 1 |
| Arcana Force VI - The Lovers | `97574404` | [Scripts/c97574404.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c97574404.lua) | 1 |
| Arcana Force I - The Magician | `8396952` | [Scripts/c8396952.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c8396952.lua) | 1 |
| Arcana Force IV - The Emperor | `61175706` | [Scripts/c61175706.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c61175706.lua) | 1 |

## Script Examples

### Arcana Force EX - The Light Ruler (`5861892`)

Source: [Scripts/c5861892.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c5861892.lua)

```lua
	c:RegisterEffect(e2)
	--coin
	aux.EnableArcanaCoin(c,EVENT_SPSUMMON_SUCCESS)
	--
	local e3=Effect.CreateEffect(c)
```

### Arcana Force XV - The Fiend (`59712426`)

Source: [Scripts/c59712426.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c59712426.lua)

```lua
	c:RegisterEffect(e1)
	--coin
	aux.EnableArcanaCoin(c,EVENT_SUMMON_SUCCESS,EVENT_FLIP_SUMMON_SUCCESS,EVENT_SPSUMMON_SUCCESS)
	--heads: optional destroy
	local e2=Effect.CreateEffect(c)
```

### Arcana Force EX - The Dark Ruler (`69831560`)

Source: [Scripts/c69831560.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c69831560.lua)

```lua
	c:RegisterEffect(e2)
	--coin
	aux.EnableArcanaCoin(c,EVENT_SPSUMMON_SUCCESS)
	--coin effect
	local e3=Effect.CreateEffect(c)
```
