# Duel.GetTargetsRelateToChain

## Signature

```lua
Duel.GetTargetsRelateToChain() -> Group
```

## Description

Returns all target cards currently related to the resolving Chain.
This is the relation-aware helper for multi-target operations; targets that left their expected place are omitted from the returned Group.
The returned Group can be empty, so check its count before applying a follow-up action.

## How To Use It

Use this during resolution when a targeting effect selected more than one card and only the targets still related to the Chain should be affected.

```lua
local g=Duel.GetTargetsRelateToChain()
if #g>0 then
    Duel.Destroy(g,REASON_EFFECT)
end
```

The returned Group can be empty. It is built from the current Chain's target cards and relation state, so it is usually clearer than manually filtering `CHAININFO_TARGET_CARDS`.

## Related Functions

- [Duel.SelectTarget](/api/functions/Duel/SelectTarget)
- [Duel.GetFirstTarget](/api/functions/Duel/GetFirstTarget)
- [Card.IsRelateToEffect](/api/functions/Card/IsRelateToEffect)

## Returns

- `Group` - New Group containing the current Chain targets whose Chain relation is still valid; empty when none qualify.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4950`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **177** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.GetTargetsRelateToChain) with `Duel.GetTargetsRelateToChain`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Astrograph Sorcerer, the Starfrost Magician](/examples/cards/48171151) | `48171151` | [Scripts/c48171151.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48171151.lua) | 1 |
| [Ashtraja Susanoo](/examples/cards/17020474) | `17020474` | [Scripts/c17020474.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17020474.lua) | 1 |
| [D/D/D Alfred the Divine Sage King](/examples/cards/11852093) | `11852093` | [Scripts/c11852093.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11852093.lua) | 1 |
| [Artmage Masterwork -Succession-](/examples/cards/37517035) | `37517035` | [Scripts/c37517035.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37517035.lua) | 1 |
| [GMX Associate Noma](/examples/cards/83528184) | `83528184` | [Scripts/c83528184.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c83528184.lua) | 1 |
| [Dracotail Shaulas](/examples/cards/42125140) | `42125140` | [Scripts/c42125140.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42125140.lua) | 1 |
| Ecclesia and the Dark Dragon | `78397661` | [Scripts/c78397661.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78397661.lua) | 1 |
| S:P Little Knight | `29301450` | [Scripts/c29301450.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29301450.lua) | 1 |
| Divine Serpent Apophis | `97800311` | [Scripts/c97800311.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97800311.lua) | 1 |
| Arms of Genex Return Zero | `61775475` | [Scripts/c61775475.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61775475.lua) | 1 |
| Ghoti Fury | `65898344` | [Scripts/c65898344.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65898344.lua) | 1 |
| Astrazma Urania | `18738846` | [Scripts/c18738846.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18738846.lua) | 1 |
| Purrelyeap!? | `82983267` | [Scripts/c82983267.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82983267.lua) | 1 |
| Yummy☆Surprise | `29369059` | [Scripts/c29369059.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29369059.lua) | 1 |
| Traptrix Atypus | `48183890` | [Scripts/c48183890.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48183890.lua) | 1 |
| R.B. Shepherd's Crook | `80071619` | [Scripts/c80071619.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80071619.lua) | 1 |
| Radiant Typhoon Mandate | `53813120` | [Scripts/c53813120.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53813120.lua) | 1 |
| Ryu-Ge Rivalry | `81549048` | [Scripts/c81549048.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81549048.lua) | 1 |
| Lunalight Perfume Dancer | `81196066` | [Scripts/c81196066.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81196066.lua) | 1 |
| Heraldic Beast Stad Whale | `97662494` | [Scripts/c97662494.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97662494.lua) | 1 |
| Possessed Destiny - Wynn | `60516416` | [Scripts/c60516416.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60516416.lua) | 1 |
| White Circle Reef | `21579049` | [Scripts/c21579049.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21579049.lua) | 1 |
| Unchained Firelord of Yama | `94014327` | [Scripts/c94014327.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c94014327.lua) | 1 |
| Zefra Metaltron | `85216896` | [Scripts/c85216896.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85216896.lua) | 1 |
| ...and 153 more |  |  |  |

## Script Examples

### Astrograph Sorcerer, the Starfrost Magician (`48171151`)

Source: [Scripts/c48171151.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48171151.lua)

```lua
	if not c:IsRelateToChain() then return end
	if Duel.SpecialSummon(c,0,tp,tp,false,false,POS_FACEUP)==0 then return end
	local desg=Duel.GetTargetsRelateToChain():Filter(s.spfilter1,nil,e,tp)
	if #desg>0 and Duel.SelectYesNo(tp,aux.Stringid(id,3)) then
		Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SPSUMMON)
```

### Ashtraja Susanoo (`17020474`)

Source: [Scripts/c17020474.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17020474.lua)

```lua
function s.setop(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	local g=Duel.GetTargetsRelateToChain()
	if aux.NecroValleyNegateCheck(g) then return end
	local sg=g:Filter(aux.NecroValleyFilter(),nil)
```

### D/D/D Alfred the Divine Sage King (`11852093`)

Source: [Scripts/c11852093.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11852093.lua)

```lua
end
function s.tfop(e,tp,eg,ep,ev,re,r,rp)
	local g=Duel.GetTargetsRelateToChain()
	local sct=Duel.GetLocationCount(tp,LOCATION_SZONE)
	local ct=math.min(g:GetCount(),sct)
```
