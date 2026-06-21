# Card.CheckRemoveOverlayCard

## Signature

```lua
Card.CheckRemoveOverlayCard(Card c, int player, int count, int reason) -> bool
```

## Description

Check the player player can be reason for the reason, at least remove the c stacked count cards

## Parameters

- `c` `Card`
- `player` `int`
- `count` `int`
- `reason` `int`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3527`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **86** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.CheckRemoveOverlayCard`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Grandpa Demetto | `44190146` | [Scripts/c44190146.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44190146.lua) | 58 |
| Number 99: Utopia Dragonar | `95134948` | [Scripts/c95134948.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95134948.lua) | 57 |
| D/D/D Deviser King Deus Machinex | `46593546` | [Scripts/c46593546.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46593546.lua) | 56 |
| Darktellarknight Batlamyus | `64414267` | [Scripts/c64414267.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c64414267.lua) | 55 |
| Heroic Champion - Magnum Excalibur | `14301396` | [Scripts/c14301396.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c14301396.lua) | 55 |
| Salamangreat Blaze Dragon | `9608555` | [Scripts/c9608555.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9608555.lua) | 53 |
| Fairy Tail - Wiccat | `27632520` | [Scripts/c27632520.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27632520.lua) | 52 |
| Raidraptor - Rising Rebellion Falcon | `71222868` | [Scripts/c71222868.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71222868.lua) | 52 |
| Time Thief Redoer | `55285840` | [Scripts/c55285840.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55285840.lua) | 52 |
| Exstellarknight Constellar Ptolemy Ω7 | `6195332` | [Scripts/c6195332.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6195332.lua) | 50 |
| Sacred Noble Knight of King Custennin | `78876707` | [Scripts/c78876707.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78876707.lua) | 50 |
| Tellarknight Ptolemaeus | `18326736` | [Scripts/c18326736.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18326736.lua) | 49 |
| Infinitrack Earth Slicer | `97584719` | [Scripts/c97584719.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97584719.lua) | 49 |
| Grenosaurus Giga-Cannon | `34481518` | [Scripts/c34481518.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34481518.lua) | 49 |
| Number 6: Chronomaly Atlandis | `9161357` | [Scripts/c9161357.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9161357.lua) | 49 |
| Number 39: Utopia Double | `62517849` | [Scripts/c62517849.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62517849.lua) | 48 |
| Baby Spider | `60023855` | [Scripts/c60023855.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60023855.lua) | 48 |
| Chasma, Dragon Ruler of Auroras | `4965193` | [Scripts/c4965193.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4965193.lua) | 47 |
| Ebon High Magician | `85551711` | [Scripts/c85551711.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85551711.lua) | 47 |
| Barrage Blast | `51369889` | [Scripts/c51369889.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c51369889.lua) | 47 |
| Madolche Puddingcess Chocolat-a-la-Mode | `44311445` | [Scripts/c44311445.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44311445.lua) | 46 |
| Rubysapphirus, the Adamant Jewel | `6906306` | [Scripts/c6906306.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6906306.lua) | 46 |
| Tally-ho! Springans | `9175957` | [Scripts/c9175957.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9175957.lua) | 46 |
| The Undying Legion | `43355214` | [Scripts/c43355214.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43355214.lua) | 46 |
| ...and 62 more |  |  |  |

## Script Examples

### Grandpa Demetto (`44190146`)

Source: [Scripts/c44190146.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44190146.lua)

```lua
end
function c44190146.costfilter(c,tp)
	return c:IsCode(75574498) and c:IsFaceup() and c:CheckRemoveOverlayCard(tp,1,REASON_COST)
end
function c44190146.spcost(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Number 99: Utopia Dragonar (`95134948`)

Source: [Scripts/c95134948.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95134948.lua)

```lua
function c95134948.spcost(e,tp,eg,ep,ev,re,r,rp,chk)
	local c=e:GetHandler()
	if chk==0 then return c:CheckRemoveOverlayCard(tp,2,REASON_COST)
		and Duel.GetCustomActivityCount(95134948,tp,ACTIVITY_SPSUMMON)==0
		and Duel.GetFlagEffect(tp,95134949)==0
```

### D/D/D Deviser King Deus Machinex (`46593546`)

Source: [Scripts/c46593546.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46593546.lua)

```lua
	local rc=re:GetHandler()
	if chk==0 then return c:IsType(TYPE_XYZ)
		and (c:CheckRemoveOverlayCard(tp,2,REASON_EFFECT)
			or Duel.IsExistingMatchingCard(c46593546.ovltgfilter,tp,LOCATION_ONFIELD,0,1,nil))
		and rc:IsRelateToEffect(re) and rc:IsCanOverlay() end
```
