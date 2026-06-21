# Duel.GetTargetsRelateToChain

## Signature

```lua
Duel.GetTargetsRelateToChain() -> Group
```

## Description

Returns all target cards currently related to the Chain.

## Returns

- `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4950`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **143** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.GetTargetsRelateToChain`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Astrograph Sorcerer, the Star Magician](/examples/cards/48171151) | `48171151` | [Scripts/c48171151.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48171151.lua) | 80 |
| [D/D/D Alfred the Divine Sage King](/examples/cards/11852093) | `11852093` | [Scripts/c11852093.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11852093.lua) | 68 |
| [Artmage Masterwork -Succession-](/examples/cards/37517035) | `37517035` | [Scripts/c37517035.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37517035.lua) | 63 |
| [GMX Associate Noma](/examples/cards/83528184) | `83528184` | [Scripts/c83528184.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c83528184.lua) | 62 |
| S:P Little Knight | `29301450` | [Scripts/c29301450.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29301450.lua) | 58 |
| Arms of Genex Return Zero | `61775475` | [Scripts/c61775475.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61775475.lua) | 56 |
| Ghoti Fury | `65898344` | [Scripts/c65898344.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65898344.lua) | 56 |
| Astrolasma Urania | `18738846` | [Scripts/c18738846.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18738846.lua) | 55 |
| Purrelyeap!? | `82983267` | [Scripts/c82983267.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82983267.lua) | 55 |
| Yummy☆Surprise | `29369059` | [Scripts/c29369059.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29369059.lua) | 55 |
| Traptrix Atypus | `48183890` | [Scripts/c48183890.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48183890.lua) | 54 |
| Radiant Typhoon Mandate | `53813120` | [Scripts/c53813120.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53813120.lua) | 54 |
| Ryu-Ge Rivalry | `81549048` | [Scripts/c81549048.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81549048.lua) | 54 |
| Lunalight Perfume Dancer | `81196066` | [Scripts/c81196066.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81196066.lua) | 53 |
| Possessed Resonance - Wynn | `60516416` | [Scripts/c60516416.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60516416.lua) | 52 |
| White Circle Reef | `21579049` | [Scripts/c21579049.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21579049.lua) | 52 |
| Zefra Metaltron | `85216896` | [Scripts/c85216896.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85216896.lua) | 52 |
| Heart of the Blue-Eyes | `54475145` | [Scripts/c54475145.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54475145.lua) | 51 |
| Argostars - Giantslaying | `30964246` | [Scripts/c30964246.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30964246.lua) | 51 |
| Excited Melffys | `79561872` | [Scripts/c79561872.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c79561872.lua) | 51 |
| Yummyusment★Acroquey | `93360904` | [Scripts/c93360904.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93360904.lua) | 51 |
| Soul Union | `69389481` | [Scripts/c69389481.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c69389481.lua) | 51 |
| Goblin Biker Grand Crisis | `15094540` | [Scripts/c15094540.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15094540.lua) | 51 |
| Dark Rebellion Xyz Dragon of the Four Heavenly Dragons | `90091224` | [Scripts/c90091224.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90091224.lua) | 50 |
| ...and 119 more |  |  |  |

## Script Examples

### Astrograph Sorcerer, the Star Magician (`48171151`)

Source: [Scripts/c48171151.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48171151.lua)

```lua
	if not c:IsRelateToChain() then return end
	if Duel.SpecialSummon(c,0,tp,tp,false,false,POS_FACEUP)==0 then return end
	local desg=Duel.GetTargetsRelateToChain():Filter(s.spfilter1,nil,e,tp)
	if #desg>0 and Duel.SelectYesNo(tp,aux.Stringid(id,3)) then
		Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SPSUMMON)
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

### Artmage Masterwork -Succession- (`37517035`)

Source: [Scripts/c37517035.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37517035.lua)

```lua
end
function s.tdop(e,tp,eg,ep,ev,re,r,rp)
	local g=Duel.GetTargetsRelateToChain():Filter(aux.NecroValleyFilter(),nil)
	if g:GetCount()>0 then
		Duel.SendtoDeck(g,nil,SEQ_DECKSHUFFLE,REASON_EFFECT)
```
