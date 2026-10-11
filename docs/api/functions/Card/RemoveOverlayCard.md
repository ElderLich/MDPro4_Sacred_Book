# Card.RemoveOverlayCard

## Signature

```lua
Card.RemoveOverlayCard(Card c, int player, int min, int max, int reason) -> int
```

## Description

Lets player remove between min and max Xyz Materials from c for reason and returns the number actually removed.
The core also offers applicable EFFECT_OVERLAY_REMOVE_REPLACE effects before selecting materials.

## Parameters

- `c` `Card`
- `player` `int`
- `min` `int`
- `max` `int`
- `reason` `int`

## Returns

- `int` - Number of Xyz Materials actually removed.

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3583`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **88** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.RemoveOverlayCard) with `Card.RemoveOverlayCard`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Performage Cup Tricker](/examples/cards/6812770) | `6812770` | [Scripts/c6812770.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6812770.lua) | 1 |
| Grandpa Demetto | `44190146` | [Scripts/c44190146.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44190146.lua) | 1 |
| Number 101: Silent Honor ARK - Soul Asylum | `2419596` | [Scripts/c2419596.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2419596.lua) | 2 |
| Number 99: Utopia Dragonar | `95134948` | [Scripts/c95134948.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95134948.lua) | 1 |
| D/D/D Deviser King Deus Machinex | `46593546` | [Scripts/c46593546.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46593546.lua) | 1 |
| Darktellarknight Batlamyus | `64414267` | [Scripts/c64414267.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c64414267.lua) | 1 |
| Heroic Champion - Magnum Excalibur | `14301396` | [Scripts/c14301396.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c14301396.lua) | 1 |
| Salamangreat Blaze Dragon | `9608555` | [Scripts/c9608555.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9608555.lua) | 1 |
| Squeeze, the Full Moon of Raise Moon - JACKPOT! | `9484285` | [Scripts/c9484285.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9484285.lua) | 1 |
| Number 93: Utopia Kaiser | `23187256` | [Scripts/c23187256.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23187256.lua) | 1 |
| Fairy Tail - Wiccat | `27632520` | [Scripts/c27632520.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27632520.lua) | 1 |
| Raidraptor - Rising Rebellion Falcon | `71222868` | [Scripts/c71222868.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71222868.lua) | 1 |
| Exstellarknight Constellar Ptolemy Ω7 | `6195332` | [Scripts/c6195332.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6195332.lua) | 1 |
| Sacred Noble Knight of King Custennin | `78876707` | [Scripts/c78876707.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78876707.lua) | 1 |
| Tellarknight Ptolemaeus | `18326736` | [Scripts/c18326736.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18326736.lua) | 2 |
| Magikey Deity - Ashtartu | `26988374` | [Scripts/c26988374.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c26988374.lua) | 2 |
| Infinitrack Earth Slicer | `97584719` | [Scripts/c97584719.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97584719.lua) | 1 |
| Grenosaurus Giga-Cannon | `34481518` | [Scripts/c34481518.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34481518.lua) | 1 |
| Number 6: Chronomaly Atlandis | `9161357` | [Scripts/c9161357.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9161357.lua) | 1 |
| Number 39: Utopia Double | `62517849` | [Scripts/c62517849.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62517849.lua) | 1 |
| Baby Spider | `60023855` | [Scripts/c60023855.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60023855.lua) | 1 |
| Chasma, Dragon Ruler of Auroras | `4965193` | [Scripts/c4965193.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4965193.lua) | 1 |
| Ebon High Magician | `85551711` | [Scripts/c85551711.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85551711.lua) | 2 |
| Madolche Puddingcess Chocolat-a-la-Mode | `44311445` | [Scripts/c44311445.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44311445.lua) | 1 |
| ...and 64 more |  |  |  |

## Script Examples

### Performage Cup Tricker (`6812770`)

Source: [Scripts/c6812770.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6812770.lua)

```lua
	local tc=Duel.GetFirstTarget()
	if not tc:IsRelateToEffect(e) then return end
	if tc:GetOverlayCount()>0 and tc:RemoveOverlayCard(tp,1,1,REASON_EFFECT)~=0
		and c:IsRelateToEffect(e) and Duel.SpecialSummon(c,0,tp,tp,false,false,POS_FACEUP)>0 then
		Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_FACEUP)
```

### Grandpa Demetto (`44190146`)

Source: [Scripts/c44190146.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44190146.lua)

```lua
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_DEATTACHFROM)
	local tc=Duel.SelectMatchingCard(tp,c44190146.costfilter,tp,LOCATION_MZONE,0,1,1,nil,tp):GetFirst()
	tc:RemoveOverlayCard(tp,1,1,REASON_COST)
end
function c44190146.filter(c,e,tp)
```

### Number 101: Silent Honor ARK - Soul Asylum (`2419596`)

Source: [Scripts/c2419596.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2419596.lua)

```lua
	local c=e:GetHandler()
	if chk==0 then return c:CheckRemoveOverlayCard(tp,1,REASON_COST) end
	c:RemoveOverlayCard(tp,1,1,REASON_COST)
	local ct=Duel.GetOperatedGroup():GetFirst()
	e:SetLabelObject(ct)
```
