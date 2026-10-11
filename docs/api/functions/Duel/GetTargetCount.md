# Duel.GetTargetCount

## Signature

```lua
Duel.GetTargetCount(function|nil filter, int player, int location1, int location2, Card|Group|nil exception, [... any]) -> int
```

## Description

Counts cards matching filter in the given field locations that can be used as effect targets, excluding exception when supplied.

## Parameters

- `filter` `function|nil`
- `player` `int`
- `location1` `int`
- `location2` `int`
- `exception` `Card|Group|nil`
- `...` `any` optional

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4984`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **26** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.GetTargetCount) with `Duel.GetTargetCount`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [D/D/D Alfred the Divine Sage King](/examples/cards/11852093) | `11852093` | [Scripts/c11852093.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11852093.lua) | 1 |
| Amazement Administrator Arlekino | `94821366` | [Scripts/c94821366.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c94821366.lua) | 1 |
| Astrazma Urania | `18738846` | [Scripts/c18738846.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18738846.lua) | 1 |
| Tauzenet Wadjet | `73490148` | [Scripts/c73490148.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c73490148.lua) | 1 |
| Gouki The Master Ogre | `30286474` | [Scripts/c30286474.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30286474.lua) | 1 |
| Exstellarknight Constellar Ptolemy Ω7 | `6195332` | [Scripts/c6195332.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6195332.lua) | 1 |
| Sacred Noble Knight of King Custennin | `78876707` | [Scripts/c78876707.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78876707.lua) | 1 |
| Legendary Lord Six Samurai - Enishi | `70634245` | [Scripts/c70634245.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70634245.lua) | 1 |
| Red Dragon Archfiend's Chains | `92936364` | [Scripts/c92936364.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92936364.lua) | 1 |
| Clown Crew Finale | `84031736` | [Scripts/c84031736.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84031736.lua) | 1 |
| Infinitrack Earth Slicer | `97584719` | [Scripts/c97584719.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97584719.lua) | 1 |
| Ragnaraika Selene Snapper | `75352507` | [Scripts/c75352507.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75352507.lua) | 1 |
| Jade Dragon Mech | `69191257` | [Scripts/c69191257.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c69191257.lua) | 1 |
| Barrage Blast | `51369889` | [Scripts/c51369889.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c51369889.lua) | 1 |
| Dark Armed Dragon Punisher | `39030883` | [Scripts/c39030883.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39030883.lua) | 1 |
| Gungnir, Dragon of the Ice Barrier | `65749035` | [Scripts/c65749035.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65749035.lua) | 1 |
| Brionac, Dragon of the Ice Barrier | `50321796` | [Scripts/c50321796.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50321796.lua) | 1 |
| Superdreadnought Rail Cannon Flying Launcher | `38354018` | [Scripts/c38354018.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38354018.lua) | 1 |
| Superheavy Samurai Steam Train King | `17775525` | [Scripts/c17775525.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17775525.lua) | 1 |
| XYZ Hyper Cannon | `21723081` | [Scripts/c21723081.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21723081.lua) | 1 |
| Predaplast | `72129804` | [Scripts/c72129804.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c72129804.lua) | 1 |
| Dance Princess of the Ice Barrier | `59546528` | [Scripts/c59546528.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59546528.lua) | 1 |
| Linkslayer | `35595518` | [Scripts/c35595518.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35595518.lua) | 1 |
| Red Ogre | `68722455` | [Scripts/c68722455.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c68722455.lua) | 1 |
| ...and 2 more |  |  |  |

## Script Examples

### D/D/D Alfred the Divine Sage King (`11852093`)

Source: [Scripts/c11852093.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11852093.lua)

```lua
function s.tftg(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
	if chkc then return chkc:IsLocation(LOCATION_GRAVE+LOCATION_REMOVED) and chkc:IsControler(tp) and s.tffilter(chkc,tp) end
	local count1=Duel.GetTargetCount(s.tffilter,tp,LOCATION_GRAVE+LOCATION_REMOVED,0,nil,tp)
	local count2=Duel.GetMatchingGroupCount(s.mfilter,tp,LOCATION_MZONE,0,nil)
	if chk==0 then return Duel.GetLocationCount(tp,LOCATION_SZONE)>0 and count1>0 and count2>0 end
```

### Amazement Administrator Arlekino (`94821366`)

Source: [Scripts/c94821366.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c94821366.lua)

```lua
function c94821366.descost(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsExistingMatchingCard(c94821366.costfilter,tp,LOCATION_GRAVE,0,1,nil) end
	local rt=Duel.GetTargetCount(nil,tp,0,LOCATION_ONFIELD,nil)
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_REMOVE)
	local g=Duel.SelectMatchingCard(tp,c94821366.costfilter,tp,LOCATION_GRAVE,0,1,rt,nil)
```

### Astrazma Urania (`18738846`)

Source: [Scripts/c18738846.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18738846.lua)

```lua
end
function s.discost(e,tp,eg,ep,ev,re,r,rp,chk)
	local ct=Duel.GetTargetCount(aux.NegateAnyFilter,tp,0,LOCATION_ONFIELD,nil)
	if chk==0 then return Duel.IsExistingMatchingCard(s.cfilter,tp,LOCATION_HAND,0,1,nil) end
	local g=Duel.GetMatchingGroup(s.cfilter,tp,LOCATION_HAND,0,nil)
```
