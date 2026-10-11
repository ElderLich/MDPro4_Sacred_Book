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

- Detected in **89** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.SetChainLimit) with `Duel.SetChainLimit`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Levia-Dragoon - Daedalus](/examples/cards/78579058) | `78579058` | [Scripts/c78579058.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78579058.lua) | 1 |
| [Ultra Polymerization](/examples/cards/76647978) | `76647978` | [Scripts/c76647978.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76647978.lua) | 1 |
| [Enneacraft - Atil.SPIA](/examples/cards/71801447) | `71801447` | [Scripts/c71801447.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71801447.lua) | 1 |
| [W:P Fancy Ball](/examples/cards/4993187) | `4993187` | [Scripts/c4993187.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4993187.lua) | 1 |
| Super Duper Polymerization | `44886582` | [Scripts/c44886582.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44886582.lua) | 1 |
| Phara the Primordial Goddess | `82344137` | [Scripts/c82344137.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82344137.lua) | 1 |
| Borrelshroud Dragon | `66452432` | [Scripts/c66452432.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66452432.lua) | 1 |
| Accesscode Talker | `86066372` | [Scripts/c86066372.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c86066372.lua) | 2 |
| Borreload Dragon | `31833038` | [Scripts/c31833038.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31833038.lua) | 1 |
| Sky Striker Mecha Modules - Multirole | `24010609` | [Scripts/c24010609.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24010609.lua) | 1 |
| Metaltronus | `64664373` | [Scripts/c64664373.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c64664373.lua) | 1 |
| King's Resonance | `17269895` | [Scripts/c17269895.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17269895.lua) | 1 |
| Infernoid Pirmais | `60551528` | [Scripts/c60551528.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60551528.lua) | 1 |
| Frozen Domain of the Ice Barrier | `35380371` | [Scripts/c35380371.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35380371.lua) | 1 |
| Borrelguard Dragon | `68987122` | [Scripts/c68987122.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c68987122.lua) | 1 |
| Super Polymerization | `48130397` | [Scripts/c48130397.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48130397.lua) | 1 |
| Number S38: Titanic Galaxy | `16110708` | [Scripts/c16110708.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16110708.lua) | 1 |
| Knight Armed Dragon, the Armored Knight Dragon | `98007437` | [Scripts/c98007437.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c98007437.lua) | 1 |
| Lovely Labrynth of the Silver Castle | `2347656` | [Scripts/c2347656.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2347656.lua) | 1 |
| Uria, Lord of Searing Flames | `6007213` | [Scripts/c6007213.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6007213.lua) | 1 |
| The Winged Dragon of Ra - Immortal Phoenix | `10000090` | [Scripts/c10000090.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10000090.lua) | 1 |
| Borreload Liberator Dragon | `27096833` | [Scripts/c27096833.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27096833.lua) | 1 |
| Megalith Notrah Plura | `44293356` | [Scripts/c44293356.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44293356.lua) | 1 |
| Hot Red Dragon Archfiend King Calamity | `62242678` | [Scripts/c62242678.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62242678.lua) | 1 |
| ...and 65 more |  |  |  |

## Script Examples

### Levia-Dragoon - Daedalus (`78579058`)

Source: [Scripts/c78579058.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78579058.lua)

```lua
	Duel.SetOperationInfo(0,CATEGORY_HANDES_OPPO,nil,0,1-tp,1)
	Duel.SetOperationInfo(0,CATEGORY_DRAW,nil,0,1-tp,1)
	Duel.SetChainLimit(aux.FALSE)
end
function s.drop(e,tp,eg,ep,ev,re,r,rp)
```

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
