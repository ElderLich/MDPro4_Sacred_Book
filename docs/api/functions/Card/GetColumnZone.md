# Card.GetColumnZone

## Signature

```lua
Card.GetColumnZone(Card c, int loc, [int player]) -> int
```

## Description

Returns the zone bitmask for columns overlapping c within loc.
When player is supplied as the opposing perspective, the core swaps the player/opponent halves of the mask.

## Parameters

- `c` `Card`
- `loc` `int`
- `player` `int` optional

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3432`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **13** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.GetColumnZone`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Mekk-Knight Purple Nightfall | `28692962` | [Scripts/c28692962.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28692962.lua) | 2 |
| Mekk-Knight Red Moon | `56809158` | [Scripts/c56809158.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56809158.lua) | 2 |
| Mekk-Knight Blue Sky | `20537097` | [Scripts/c20537097.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20537097.lua) | 2 |
| Mekk-Knight Green Horizon | `66022706` | [Scripts/c66022706.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66022706.lua) | 2 |
| Mekk-Knight Yellow Star | `29415459` | [Scripts/c29415459.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29415459.lua) | 2 |
| S-Force Specimen | `82977464` | [Scripts/c82977464.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82977464.lua) | 2 |
| Mekk-Knight Orange Sunset | `93020401` | [Scripts/c93020401.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93020401.lua) | 3 |
| Disablaster the Negation Fortress | `58707981` | [Scripts/c58707981.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58707981.lua) | 1 |
| Red Hared Hasty Horse | `19636995` | [Scripts/c19636995.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c19636995.lua) | 1 |
| Mekk-Knight Indigo Eclipse | `92204263` | [Scripts/c92204263.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92204263.lua) | 2 |
| Staring Contest | `97729135` | [Scripts/c97729135.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97729135.lua) | 4 |
| Iron Dragon Tiamaton | `46247282` | [Scripts/c46247282.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46247282.lua) | 1 |
| Sour Scheduling - Red Vinegar Vamoose | `65107325` | [Scripts/c65107325.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65107325.lua) | 1 |

## Script Examples

### Mekk-Knight Purple Nightfall (`28692962`)

Source: [Scripts/c28692962.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28692962.lua)

```lua
	local lg=Duel.GetMatchingGroup(c28692962.cfilter,tp,LOCATION_ONFIELD,LOCATION_ONFIELD,nil)
	for tc in aux.Next(lg) do
		zone=bit.bor(zone,tc:GetColumnZone(LOCATION_MZONE,tp))
	end
	return Duel.GetLocationCount(tp,LOCATION_MZONE,tp,LOCATION_REASON_TOFIELD,zone)>0
```

### Mekk-Knight Red Moon (`56809158`)

Source: [Scripts/c56809158.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56809158.lua)

```lua
	local lg=Duel.GetMatchingGroup(c56809158.cfilter,tp,LOCATION_ONFIELD,LOCATION_ONFIELD,nil)
	for tc in aux.Next(lg) do
		zone=bit.bor(zone,tc:GetColumnZone(LOCATION_MZONE,tp))
	end
	return Duel.GetLocationCount(tp,LOCATION_MZONE,tp,LOCATION_REASON_TOFIELD,zone)>0
```

### Mekk-Knight Blue Sky (`20537097`)

Source: [Scripts/c20537097.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20537097.lua)

```lua
	local lg=Duel.GetMatchingGroup(c20537097.cfilter,tp,LOCATION_ONFIELD,LOCATION_ONFIELD,nil)
	for tc in aux.Next(lg) do
		zone=bit.bor(zone,tc:GetColumnZone(LOCATION_MZONE,tp))
	end
	return Duel.GetLocationCount(tp,LOCATION_MZONE,tp,LOCATION_REASON_TOFIELD,zone)>0
```
