# Card.GetMutualLinkedGroupCount

## Signature

```lua
Card.GetMutualLinkedGroupCount(Card c) -> int
```

## Description

Returns the number of cards mutually linked with c.

## Parameters

- `c` `Card`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3426`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **16** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.GetMutualLinkedGroupCount`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Worldsea Dragon Zealantis | `45112597` | [Scripts/c45112597.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45112597.lua) | 53 |
| Knightmare Unicorn | `38342335` | [Scripts/c38342335.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38342335.lua) | 50 |
| V-LAN Hydra | `13536606` | [Scripts/c13536606.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13536606.lua) | 48 |
| G Golem Invalid Dolmen | `24151924` | [Scripts/c24151924.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24151924.lua) | 46 |
| Firewall Dragon | `5043010` | [Scripts/c5043010.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5043010.lua) | 45 |
| Knightmare Cerberus | `75452921` | [Scripts/c75452921.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75452921.lua) | 43 |
| Knightmare Goblin | `39064822` | [Scripts/c39064822.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39064822.lua) | 42 |
| Knightmare Phoenix | `2857636` | [Scripts/c2857636.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2857636.lua) | 42 |
| Knightmare Mermaid | `3679218` | [Scripts/c3679218.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3679218.lua) | 41 |
| Tri-Gate Wizard | `32617464` | [Scripts/c32617464.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32617464.lua) | 37 |
| Appliancer Laundry Dragon | `77102944` | [Scripts/c77102944.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77102944.lua) | 33 |
| Binary Blader | `80088625` | [Scripts/c80088625.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80088625.lua) | 32 |
| Appliancer Propelion | `81769387` | [Scripts/c81769387.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81769387.lua) | 31 |
| World Legacy's Nightmare | `25163979` | [Scripts/c25163979.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25163979.lua) | 30 |
| World Legacy Struggle | `58374719` | [Scripts/c58374719.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58374719.lua) | 22 |
| World Legacy's Sorrow | `85763457` | [Scripts/c85763457.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85763457.lua) | 19 |

## Script Examples

### Worldsea Dragon Zealantis (`45112597`)

Source: [Scripts/c45112597.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45112597.lua)

```lua
end
function c45112597.filter(c)
	return c:GetMutualLinkedGroupCount()>0
end
function c45112597.destg(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Knightmare Unicorn (`38342335`)

Source: [Scripts/c38342335.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38342335.lua)

```lua
	local g=Duel.SelectTarget(tp,Card.IsAbleToDeck,tp,LOCATION_ONFIELD,LOCATION_ONFIELD,1,1,nil)
	Duel.SetOperationInfo(0,CATEGORY_TODECK,g,1,0,0)
	if e:GetHandler():GetMutualLinkedGroupCount()>0 then
		e:SetCategory(CATEGORY_TODECK+CATEGORY_DRAW)
		e:SetLabel(1)
```

### V-LAN Hydra (`13536606`)

Source: [Scripts/c13536606.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13536606.lua)

```lua
end
function c13536606.atkval(e,c)
	return c:GetMutualLinkedGroupCount()*300
end
function c13536606.rfilter(c,tp,g)
```
