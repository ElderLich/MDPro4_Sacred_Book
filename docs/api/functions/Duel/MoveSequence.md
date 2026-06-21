# Duel.MoveSequence

## Signature

```lua
Duel.MoveSequence(Card c, int seq) -> void
```

## Description

Move the serial number of c, usually used to change the grid in the field or in the card group to move to the top or bottom

## Parameters

- `c` `Card`
- `seq` `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4884`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **140** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.MoveSequence`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Flower Cardian Peony with Butterfly](/examples/cards/57261568) | `57261568` | [Scripts/c57261568.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57261568.lua) | 62 |
| Vaylantz Genesis Grand Duke | `76075139` | [Scripts/c76075139.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76075139.lua) | 60 |
| Arktos XII - Chronochasm Vaylantz | `50687050` | [Scripts/c50687050.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50687050.lua) | 56 |
| Purrely | `25550531` | [Scripts/c25550531.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25550531.lua) | 56 |
| Magellanica, the Deep Sea City | `26534688` | [Scripts/c26534688.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c26534688.lua) | 56 |
| Gunkan Sushipyard Seaside Supper Spot | `62200831` | [Scripts/c62200831.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62200831.lua) | 54 |
| Mamonaka the Vaylantz United | `40680521` | [Scripts/c40680521.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40680521.lua) | 53 |
| Rank-Up-Magic Zexal Force | `36224040` | [Scripts/c36224040.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36224040.lua) | 53 |
| S-Force Justify | `35334193` | [Scripts/c35334193.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35334193.lua) | 51 |
| Loris, Lady of Lament | `50699850` | [Scripts/c50699850.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50699850.lua) | 51 |
| Shadowreaver Knight 21 | `95506252` | [Scripts/c95506252.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95506252.lua) | 50 |
| Oracle of Zefra | `32354768` | [Scripts/c32354768.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32354768.lua) | 49 |
| Magikey Mechmusket - Batosbuster | `19489718` | [Scripts/c19489718.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c19489718.lua) | 48 |
| Sprind the Irondash Dragon | `1906812` | [Scripts/c1906812.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1906812.lua) | 48 |
| Valiant Shark Lancer | `23672629` | [Scripts/c23672629.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23672629.lua) | 48 |
| Adamancipator Risen - Leonite | `47674738` | [Scripts/c47674738.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c47674738.lua) | 48 |
| Raiza the Mega Monarch | `69327790` | [Scripts/c69327790.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c69327790.lua) | 48 |
| Galaxy Satellite Dragon | `92362073` | [Scripts/c92362073.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92362073.lua) | 47 |
| Theorealize | `48739627` | [Scripts/c48739627.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48739627.lua) | 47 |
| Uradora of Fate | `27753563` | [Scripts/c27753563.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27753563.lua) | 46 |
| Parallel Panzer | `93394164` | [Scripts/c93394164.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93394164.lua) | 46 |
| Seventh Ascension | `23153227` | [Scripts/c23153227.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23153227.lua) | 45 |
| Destiny HERO - Dark Angel | `26964762` | [Scripts/c26964762.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c26964762.lua) | 45 |
| R.B. VALCan Booster | `6821579` | [Scripts/c6821579.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6821579.lua) | 45 |
| ...and 116 more |  |  |  |

## Script Examples

### Flower Cardian Peony with Butterfly (`57261568`)

Source: [Scripts/c57261568.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57261568.lua)

```lua
				for i=1,ct do
					local mg=Duel.GetDecktopGroup(1-tp,1)
					Duel.MoveSequence(mg:GetFirst(),SEQ_DECKBOTTOM)
				end
			end
```

### Vaylantz Genesis Grand Duke (`76075139`)

Source: [Scripts/c76075139.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76075139.lua)

```lua
			local s=Duel.SelectDisableField(tp,1,LOCATION_MZONE,0,~flag)
			local nseq=math.log(s,2)
			Duel.MoveSequence(sc,nseq)
		end
	end
```

### Arktos XII - Chronochasm Vaylantz (`50687050`)

Source: [Scripts/c50687050.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50687050.lua)

```lua
			local nseq=math.log(s,2)
			Duel.HintSelection(sg)
			Duel.MoveSequence(sc,nseq)
		end
	end
```
