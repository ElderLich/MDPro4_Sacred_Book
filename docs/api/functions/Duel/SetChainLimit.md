# Duel.SetChainLimit

## Signature

```lua
Duel.SetChainLimit(function f) -> void
```

## Description

Registers a temporary chain-limit callback for the current Chain window.
The callback is stored with the current reason player and is later called as f(e, chain_player, activating_player). If it returns false, that effect cannot be chained.

## Parameters

- `f` `function`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4887`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **87** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.SetChainLimit`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Ultra Polymerization](/examples/cards/76647978) | `76647978` | [Scripts/c76647978.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76647978.lua) | 71 |
| [Enneacraft - Atil.SPIA](/examples/cards/71801447) | `71801447` | [Scripts/c71801447.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71801447.lua) | 62 |
| [W:P Fancy Ball](/examples/cards/4993187) | `4993187` | [Scripts/c4993187.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4993187.lua) | 61 |
| Super Duper Polymerization | `44886582` | [Scripts/c44886582.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44886582.lua) | 59 |
| Borrelshroud Dragon | `66452432` | [Scripts/c66452432.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66452432.lua) | 53 |
| Phara, the Goddess of the Beginning | `82344137` | [Scripts/c82344137.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82344137.lua) | 52 |
| Accesscode Talker | `86066372` | [Scripts/c86066372.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c86066372.lua) | 50 |
| Borreload Dragon | `31833038` | [Scripts/c31833038.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31833038.lua) | 50 |
| Sky Striker Mecha Modules - Multirole | `24010609` | [Scripts/c24010609.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24010609.lua) | 49 |
| Metaltronus | `64664373` | [Scripts/c64664373.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c64664373.lua) | 49 |
| King's Resonance | `17269895` | [Scripts/c17269895.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17269895.lua) | 48 |
| Infernoid Pirmais | `60551528` | [Scripts/c60551528.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60551528.lua) | 48 |
| Frozen Domain of the Ice Barrier | `35380371` | [Scripts/c35380371.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35380371.lua) | 47 |
| Borrelguard Dragon | `68987122` | [Scripts/c68987122.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c68987122.lua) | 47 |
| Super Polymerization | `48130397` | [Scripts/c48130397.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48130397.lua) | 46 |
| Number S38: Titanic Galaxy | `16110708` | [Scripts/c16110708.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16110708.lua) | 45 |
| Knight Armed Dragon, the Armored Knight Dragon | `98007437` | [Scripts/c98007437.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c98007437.lua) | 45 |
| Lovely Labrynth of the Silver Castle | `2347656` | [Scripts/c2347656.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2347656.lua) | 45 |
| Uria, Lord of Searing Flames | `6007213` | [Scripts/c6007213.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6007213.lua) | 45 |
| The Winged Dragon of Ra - Immortal Phoenix | `10000090` | [Scripts/c10000090.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10000090.lua) | 44 |
| Borreload Liberator Dragon | `27096833` | [Scripts/c27096833.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27096833.lua) | 44 |
| Megalith Notrah Plura | `44293356` | [Scripts/c44293356.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44293356.lua) | 43 |
| Hot Red Dragon Archfiend King Calamity | `62242678` | [Scripts/c62242678.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62242678.lua) | 43 |
| Gouki The Tyrant Ogre | `7782069` | [Scripts/c7782069.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7782069.lua) | 43 |
| ...and 63 more |  |  |  |

## Script Examples

### Ultra Polymerization (`76647978`)

Source: [Scripts/c76647978.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76647978.lua)

```lua
	Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,nil,1,tp,LOCATION_EXTRA)
	if e:IsHasType(EFFECT_TYPE_ACTIVATE) then
		Duel.SetChainLimit(aux.FALSE)
	end
end
```

### Enneacraft - Atil.SPIA (`71801447`)

Source: [Scripts/c71801447.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71801447.lua)

```lua
	local c=e:GetHandler()
	if ep==1-tp and c:GetFlagEffect(id)>0 then
		Duel.SetChainLimit(s.chainlm)
	end
end
```

### W:P Fancy Ball (`4993187`)

Source: [Scripts/c4993187.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4993187.lua)

```lua
	if chk==0 then return res end
	Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,nil,1,0,0)
	Duel.SetChainLimit(s.chainlm)
end
function s.chainlm(e,rp,tp)
```
