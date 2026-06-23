# Duel.GetLinkedZone

## Signature

```lua
Duel.GetLinkedZone(int player) -> int
```

## Description

Returns the zone bitmask currently pointed to by Link Markers from player's perspective.
Use bit operations to test individual zones. For one Link Monster's markers, use Card.GetLinkedZone.

## Parameters

- `player` `int` - Perspective player for the returned zone mask.

## Returns

- `int` - Linked-zone bitmask from player's perspective.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4942`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **22** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.GetLinkedZone`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Rescue Ferret | `56343672` | [Scripts/c56343672.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56343672.lua) | 49 |
| Topologic Blaster Dragon | `30064423` | [Scripts/c30064423.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30064423.lua) | 47 |
| Sunvine Thrasher | `91557476` | [Scripts/c91557476.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c91557476.lua) | 47 |
| Topologic Zeroboros | `66403530` | [Scripts/c66403530.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66403530.lua) | 43 |
| Topologic Bomber Dragon | `5821478` | [Scripts/c5821478.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5821478.lua) | 43 |
| Salamangreat Mole | `89484053` | [Scripts/c89484053.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c89484053.lua) | 43 |
| Codebreaker Virus Berserker | `48736598` | [Scripts/c48736598.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48736598.lua) | 42 |
| Pasto-Ral Theorealize | `36709484` | [Scripts/c36709484.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36709484.lua) | 41 |
| Codebreaker Virus Swordsman | `84121193` | [Scripts/c84121193.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84121193.lua) | 38 |
| Crusadia Maximus | `81524756` | [Scripts/c81524756.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81524756.lua) | 38 |
| World Legacy - "World Crown" | `27918365` | [Scripts/c27918365.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27918365.lua) | 36 |
| World Chalice Guardragon | `84899094` | [Scripts/c84899094.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84899094.lua) | 36 |
| Crusadia Draco | `54525057` | [Scripts/c54525057.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54525057.lua) | 36 |
| Crusadia Reclusia | `55241609` | [Scripts/c55241609.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55241609.lua) | 34 |
| Sea Archiver | `53309998` | [Scripts/c53309998.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53309998.lua) | 34 |
| Topologic Gumblar Dragon | `22593417` | [Scripts/c22593417.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22593417.lua) | 33 |
| Crusadia Leonis | `28031913` | [Scripts/c28031913.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28031913.lua) | 31 |
| Crusadia Arboria | `91646304` | [Scripts/c91646304.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c91646304.lua) | 27 |
| Lane Restriction | `47914440` | [Scripts/c47914440.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c47914440.lua) | 25 |
| Packet Link | `78859567` | [Scripts/c78859567.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78859567.lua) | 24 |
| World Legacy Succession | `99674361` | [Scripts/c99674361.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c99674361.lua) | 21 |
| Link Infra-Flier | `65100616` | [Scripts/c65100616.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65100616.lua) | 12 |

## Script Examples

### Rescue Ferret (`56343672`)

Source: [Scripts/c56343672.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56343672.lua)

```lua
function c56343672.sptg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then
		local zone=Duel.GetLinkedZone(tp)
		local ct=Duel.GetLocationCount(tp,LOCATION_MZONE,tp,LOCATION_REASON_TOFIELD,zone)
		local seq=e:GetHandler():GetSequence()
```

### Topologic Blaster Dragon (`30064423`)

Source: [Scripts/c30064423.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30064423.lua)

```lua
end
function s.econ(e,tp,eg,ep,ev,re,r,rp)
	local zone=Duel.GetLinkedZone(0)+(Duel.GetLinkedZone(1)<<0x10)
	return not eg:IsContains(e:GetHandler()) and eg:IsExists(s.cfilter,1,nil,zone) and e:GetHandler():GetSequence()>4
end
```

### Sunvine Thrasher (`91557476`)

Source: [Scripts/c91557476.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c91557476.lua)

```lua
function c91557476.sptg(e,tp,eg,ep,ev,re,r,rp,chk)
	local bc=e:GetHandler():GetBattleTarget()
	local zone=Duel.GetLinkedZone(tp)&0x1f
	if chk==0 then return Duel.GetLocationCount(tp,LOCATION_MZONE,tp,LOCATION_REASON_TOFIELD,zone)>0
		and bc:IsCanBeSpecialSummoned(e,0,tp,false,false) end
```
