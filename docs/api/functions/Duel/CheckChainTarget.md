# Duel.CheckChainTarget

## Signature

```lua
Duel.CheckChainTarget(int chainc, Card c) -> bool
```

## Description

Checks whether c is a valid card related to chainc.

## Parameters

- `chainc` `int`
- `c` `Card`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5064`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **10** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.CheckChainTarget) with `Duel.CheckChainTarget`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Dyna Tank | `75780818` | [Scripts/c75780818.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75780818.lua) | 1 |
| Mermail Abysstrite | `59170782` | [Scripts/c59170782.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59170782.lua) | 2 |
| Subterror Nemesis Defender | `68823957` | [Scripts/c68823957.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c68823957.lua) | 1 |
| Blackwing Tamer - Obsidian Hawk Joe | `81983656` | [Scripts/c81983656.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81983656.lua) | 1 |
| Cairngorgon, Antiluminescent Knight | `21501505` | [Scripts/c21501505.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21501505.lua) | 1 |
| Shift | `59560625` | [Scripts/c59560625.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59560625.lua) | 1 |
| Kagemusha of the Six Samurai | `1498130` | [Scripts/c1498130.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1498130.lua) | 1 |
| Remote Revenge | `61656650` | [Scripts/c61656650.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61656650.lua) | 2 |
| Fiend's Hand Mirror | `58607704` | [Scripts/c58607704.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58607704.lua) | 1 |
| Fairy's Hand Mirror | `17653779` | [Scripts/c17653779.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17653779.lua) | 1 |

## Script Examples

### Dyna Tank (`75780818`)

Source: [Scripts/c75780818.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75780818.lua)

```lua
end
function s.cefilter(c,ct)
	return Duel.CheckChainTarget(ct,c)
end
function s.cetg(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
```

### Mermail Abysstrite (`59170782`)

Source: [Scripts/c59170782.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59170782.lua)

```lua
	local c=e:GetHandler()
	if tc==c or tc:IsControler(1-tp) or tc:IsFacedown() or not tc:IsLocation(LOCATION_MZONE) or not tc:IsSetCard(0x74) then return false end
	return Duel.CheckChainTarget(ev,c)
end
function c59170782.tgop1(e,tp,eg,ep,ev,re,r,rp)
```

### Subterror Nemesis Defender (`68823957`)

Source: [Scripts/c68823957.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c68823957.lua)

```lua
end
function c68823957.cefilter(c,ct,oc)
	return oc~=c and Duel.CheckChainTarget(ct,c)
end
function c68823957.cetg(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
```
