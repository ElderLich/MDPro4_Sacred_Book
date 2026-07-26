# Card.IsLinkBelow

## Signature

```lua
Card.IsLinkBelow(Card c, int link) -> bool
```

## Description

Checks whether c has a nonzero Link Rating that is less than or equal to link.

## Parameters

- `c` `Card`
- `link` `int`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3619`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **14** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.IsLinkBelow`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [W:P Fancy Ball](/examples/cards/4993187) | `4993187` | [Scripts/c4993187.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4993187.lua) | 61 |
| Borrelshroud Dragon | `66452432` | [Scripts/c66452432.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66452432.lua) | 53 |
| Marincess Wonder Heart | `94207108` | [Scripts/c94207108.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c94207108.lua) | 49 |
| Quadborrel Dragon | `29296344` | [Scripts/c29296344.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29296344.lua) | 48 |
| V-LAN Hydra | `13536606` | [Scripts/c13536606.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13536606.lua) | 48 |
| Amphibious Swarmship Amblowhale | `20665527` | [Scripts/c20665527.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20665527.lua) | 48 |
| Decode Talker Heatsoul | `61245672` | [Scripts/c61245672.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61245672.lua) | 48 |
| Triple Burst Dragon | `49725936` | [Scripts/c49725936.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49725936.lua) | 47 |
| Transcode Talker | `46947713` | [Scripts/c46947713.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46947713.lua) | 46 |
| Sunseed Shadow | `30013902` | [Scripts/c30013902.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30013902.lua) | 46 |
| Protectcode Talker | `58036229` | [Scripts/c58036229.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58036229.lua) | 43 |
| Primite Dragon Nether Berzelius | `26462013` | [Scripts/c26462013.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c26462013.lua) | 40 |
| Miniborrel Dragon | `73341839` | [Scripts/c73341839.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c73341839.lua) | 36 |
| Trickstar Foxglove Witch | `86750474` | [Scripts/c86750474.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c86750474.lua) | 35 |

## Script Examples

### W:P Fancy Ball (`4993187`)

Source: [Scripts/c4993187.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4993187.lua)

```lua
end
function s.mattg(e,c)
	return c:IsFaceup() and c:IsLinkBelow(2)
end
function s.lktg(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Borrelshroud Dragon (`66452432`)

Source: [Scripts/c66452432.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66452432.lua)

```lua
end
function s.spfilter(c,e,tp)
	return c:IsSetCard(0x10f) and c:IsType(TYPE_LINK) and c:IsLinkBelow(4)
		and c:IsCanBeSpecialSummoned(e,0,tp,false,false) and Duel.GetLocationCountFromEx(tp,tp,nil,c)>0
end
```

### Marincess Wonder Heart (`94207108`)

Source: [Scripts/c94207108.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c94207108.lua)

```lua
end
function c94207108.spfilter2(c,e,tp)
	return c:IsSetCard(0x12b) and c:IsLinkBelow(3) and c:IsType(TYPE_LINK) and c:IsCanBeSpecialSummoned(e,0,tp,false,false)
end
function c94207108.sptg2(e,tp,eg,ep,ev,re,r,rp,chk)
```
