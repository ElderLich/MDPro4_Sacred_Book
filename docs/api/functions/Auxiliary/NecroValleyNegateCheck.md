# Auxiliary.NecroValleyNegateCheck

## Signature

```lua
Auxiliary.NecroValleyNegateCheck(Card|Group v) -> bool
```

## Description

Checks whether v, a Card or Group, contains a card affected by Necrovalley. If the current Chain is disablable and a matching card is found, it negates the current effect and returns true.

## Parameters

- `v` `Card|Group`

## Returns

- `bool` - true if the current effect was negated by the Necrovalley check.

## Source

- `Utilities/utility.lua:929`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **50** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.NecroValleyNegateCheck) with `Auxiliary.NecroValleyNegateCheck`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Ashtraja Susanoo](/examples/cards/17020474) | `17020474` | [Scripts/c17020474.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c17020474.lua) | 1 |
| Vernusylph and the Changing Season | `37313338` | [Scripts/c37313338.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c37313338.lua) | 1 |
| Meklord Astro the Eradicator | `2992036` | [Scripts/c2992036.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c2992036.lua) | 1 |
| Red Hypernova Dragon | `30698243` | [Scripts/c30698243.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c30698243.lua) | 1 |
| Clown Crew Meteor | `93172951` | [Scripts/c93172951.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c93172951.lua) | 1 |
| The Glitter of Raise Moon | `9362643` | [Scripts/c9362643.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c9362643.lua) | 1 |
| Fiendsmith's Lacrima | `46640168` | [Scripts/c46640168.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c46640168.lua) | 1 |
| Clown Crew Flair | `42759961` | [Scripts/c42759961.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c42759961.lua) | 1 |
| R.B. Operation Test | `16066654` | [Scripts/c16066654.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c16066654.lua) | 1 |
| Deskbot Base | `12215894` | [Scripts/c12215894.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c12215894.lua) | 1 |
| Unchained Ogre Shara | `95136979` | [Scripts/c95136979.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c95136979.lua) | 1 |
| Clown Crew Diabolo | `31533473` | [Scripts/c31533473.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c31533473.lua) | 1 |
| Clown Crew Dristy | `30109445` | [Scripts/c30109445.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c30109445.lua) | 1 |
| Chaos End Ruler - Ruler of the Beginning and the End | `41424250` | [Scripts/c41424250.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c41424250.lua) | 1 |
| Number 1: Infection Buzzking | `10666000` | [Scripts/c10666000.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c10666000.lua) | 1 |
| Despian Proskenion | `18666161` | [Scripts/c18666161.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c18666161.lua) | 1 |
| Drill Warrior | `3429238` | [Scripts/c3429238.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c3429238.lua) | 1 |
| Madolche Chateau | `14001430` | [Scripts/c14001430.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c14001430.lua) | 1 |
| Water Leviathan @Ignister | `37061511` | [Scripts/c37061511.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c37061511.lua) | 1 |
| Samsara D Lotus | `62318994` | [Scripts/c62318994.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c62318994.lua) | 1 |
| Rainbow Bridge of Salvation | `5611760` | [Scripts/c5611760.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c5611760.lua) | 1 |
| Dyna Mondo | `73898890` | [Scripts/c73898890.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c73898890.lua) | 1 |
| Way Where There's a Will | `91880660` | [Scripts/c91880660.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c91880660.lua) | 1 |
| Tierra, Source of Destruction | `91588074` | [Scripts/c91588074.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c91588074.lua) | 1 |
| ...and 26 more |  |  |  |

## Script Examples

### Ashtraja Susanoo (`17020474`)

Source: [Scripts/c17020474.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c17020474.lua)

```lua
	local c=e:GetHandler()
	local g=Duel.GetTargetsRelateToChain()
	if aux.NecroValleyNegateCheck(g) then return end
	local sg=g:Filter(aux.NecroValleyFilter(),nil)
	if sg:GetCount()==1 then
```

### Vernusylph and the Changing Season (`37313338`)

Source: [Scripts/c37313338.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c37313338.lua)

```lua
	local tc=Duel.GetFirstTarget()
	if tc:IsRelateToEffect(e) then
		if aux.NecroValleyNegateCheck(tc) then return end
		if not aux.NecroValleyFilter()(tc) then return end
		if Duel.GetLocationCount(tp,LOCATION_MZONE)>0 and tc:IsCanBeSpecialSummoned(e,0,tp,false,false)
```

### Meklord Astro the Eradicator (`2992036`)

Source: [Scripts/c2992036.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c2992036.lua)

```lua
function c2992036.activate(e,tp,eg,ep,ev,re,r,rp)
	local tg=Duel.GetChainInfo(0,CHAININFO_TARGET_CARDS):Filter(Card.IsRelateToEffect,nil,e)
	if aux.NecroValleyNegateCheck(tg) then return end
	if tg:GetCount()>0 then
		local ft=Duel.GetLocationCount(tp,LOCATION_MZONE)
```
