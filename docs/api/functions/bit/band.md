# bit.band

## Signature

```lua
bit.band(int a, int b) -> int
```

## Description

Returns the bitwise AND of a and b.

## Parameters

- `a` `int`
- `b` `int`

## Returns

- `int` - Bitwise AND of a and b.

## Source

- `Utilities/utility.lua:15`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **984** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=bit.band) with `bit.band`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Artmage Non-Finito](/examples/cards/74631897) | `74631897` | [Scripts/c74631897.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c74631897.lua) | 1 |
| [Azure Ocean Dragon Lord - Neo-Daedalus Rage](/examples/cards/41570943) | `41570943` | [Scripts/c41570943.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c41570943.lua) | 2 |
| [Yomagna the Fire Phantom](/examples/cards/17350692) | `17350692` | [Scripts/c17350692.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c17350692.lua) | 1 |
| [El Shaddoll Apkallone](/examples/cards/50907446) | `50907446` | [Scripts/c50907446.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c50907446.lua) | 1 |
| [Meteoroa Drytron](/examples/cards/24166324) | `24166324` | [Scripts/c24166324.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c24166324.lua) | 1 |
| [Pere-Zenet Em Heru](/examples/cards/46273941) | `46273941` | [Scripts/c46273941.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c46273941.lua) | 1 |
| [Am Duazenet](/examples/cards/45151304) | `45151304` | [Scripts/c45151304.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c45151304.lua) | 1 |
| [Odd-Eyes Revolution Dragon](/examples/cards/16306932) | `16306932` | [Scripts/c16306932.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c16306932.lua) | 1 |
| [Nekroz Kaleidoscope](/examples/cards/51124303) | `51124303` | [Scripts/c51124303.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c51124303.lua) | 2 |
| [Transonic Bird](/examples/cards/34072799) | `34072799` | [Scripts/c34072799.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c34072799.lua) | 2 |
| [Yummy★Snatchy](/examples/cards/30581601) | `30581601` | [Scripts/c30581601.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c30581601.lua) | 1 |
| [Sonic Tracker](/examples/cards/17888577) | `17888577` | [Scripts/c17888577.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c17888577.lua) | 2 |
| [Stars Align Above the Shrine](/examples/cards/15306543) | `15306543` | [Scripts/c15306543.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c15306543.lua) | 1 |
| D/D Extra Surveyor | `74387963` | [Scripts/c74387963.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c74387963.lua) | 1 |
| Starving Venom Wing Dragon | `5148778` | [Scripts/c5148778.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c5148778.lua) | 1 |
| Red-Eyes Slash Dragon | `21140872` | [Scripts/c21140872.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c21140872.lua) | 1 |
| Trickstar Light Stage | `35371948` | [Scripts/c35371948.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c35371948.lua) | 1 |
| Ostinato | `9113513` | [Scripts/c9113513.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c9113513.lua) | 1 |
| Supreme King Dragon Lightwurm | `41908872` | [Scripts/c41908872.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c41908872.lua) | 1 |
| Duel Link Dragon, the Duel Dragon | `60025883` | [Scripts/c60025883.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c60025883.lua) | 2 |
| Gishki Nekromirror | `36982581` | [Scripts/c36982581.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c36982581.lua) | 1 |
| Performapal Celestial Magician | `58092907` | [Scripts/c58092907.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c58092907.lua) | 1 |
| Mementotlan Shleepy | `50042011` | [Scripts/c50042011.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c50042011.lua) | 1 |
| Meteonis Drytron | `22398665` | [Scripts/c22398665.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c22398665.lua) | 1 |
| ...and 960 more |  |  |  |

## Script Examples

### Artmage Non-Finito (`74631897`)

Source: [Scripts/c74631897.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c74631897.lua)

```lua
end
function s.splimit(e,se,sp,st)
	return bit.band(st,SUMMON_TYPE_FUSION)==SUMMON_TYPE_FUSION and Duel.GetFlagEffect(sp,id)==0
end
function s.condition(e,tp,eg,ep,ev,re,r,rp)
```

### Azure Ocean Dragon Lord - Neo-Daedalus Rage (`41570943`)

Source: [Scripts/c41570943.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c41570943.lua)

```lua
end
function s.sptg(e,tp,eg,ep,ev,re,r,rp,chk)
	local zone=bit.band(e:GetHandler():GetLinkedZone(tp),0x1f)
	if chk==0 then return Duel.GetLocationCount(tp,LOCATION_MZONE)>0
		and Duel.IsExistingMatchingCard(s.spfilter1,tp,LOCATION_GRAVE,0,1,nil,e,tp,zone) end
```

### Yomagna the Fire Phantom (`17350692`)

Source: [Scripts/c17350692.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c17350692.lua)

```lua
	local c=e:GetHandler()
	local race=e:GetLabel()
	if c:IsRelateToChain() and c:IsFaceup() and bit.band(c:GetRace(),race)==0 then
		local e1=Effect.CreateEffect(c)
		e1:SetType(EFFECT_TYPE_SINGLE)
```
