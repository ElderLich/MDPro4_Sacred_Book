# Card.GetLinkedGroupCount

## Signature

```lua
Card.GetLinkedGroupCount(Card c) -> int
```

## Description

Returns the number of cards in zones linked by c.

## Parameters

- `c` `Card`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3471`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **12** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.GetLinkedGroupCount) with `Card.GetLinkedGroupCount`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Gergonne's End | `59490397` | [Scripts/c59490397.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59490397.lua) | 2 |
| Decode Talker Heatsoul | `61245672` | [Scripts/c61245672.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61245672.lua) | 1 |
| Mekk-Knight Spectrum Supreme | `38502358` | [Scripts/c38502358.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38502358.lua) | 1 |
| Decode Destruction | `33062423` | [Scripts/c33062423.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33062423.lua) | 2 |
| Elphase | `60292055` | [Scripts/c60292055.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60292055.lua) | 1 |
| Trickstar Bella Madonna | `41302052` | [Scripts/c41302052.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41302052.lua) | 2 |
| Decode Talker | `1861629` | [Scripts/c1861629.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1861629.lua) | 1 |
| Decode Talker Extended | `30822527` | [Scripts/c30822527.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30822527.lua) | 1 |
| Trickstar Black Catbat | `94626871` | [Scripts/c94626871.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c94626871.lua) | 1 |
| Gorgon of Zilofthonia | `12067160` | [Scripts/c12067160.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12067160.lua) | 1 |
| Gouki The Blade Ogre | `95515058` | [Scripts/c95515058.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95515058.lua) | 1 |
| Code Talker | `53413628` | [Scripts/c53413628.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53413628.lua) | 2 |

## Script Examples

### Gergonne's End (`59490397`)

Source: [Scripts/c59490397.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59490397.lua)

```lua
function c59490397.descon(e,tp,eg,ep,ev,re,r,rp)
	local tc=e:GetHandler():GetEquipTarget()
	return tc and tc:GetLinkedGroupCount()==tc:GetLink()
end
function c59490397.destg(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Decode Talker Heatsoul (`61245672`)

Source: [Scripts/c61245672.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61245672.lua)

```lua
end
function c61245672.atkval(e,c)
	return c:GetLinkedGroupCount()*500
end
function c61245672.drcost(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Mekk-Knight Spectrum Supreme (`38502358`)

Source: [Scripts/c38502358.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38502358.lua)

```lua
function c38502358.indcon(e)
	local c=e:GetHandler()
	return c:GetSequence()>4 and c:IsType(TYPE_LINK) and c:GetLinkedGroupCount()==0
end
function c38502358.spcfilter(c,g,tp)
```
