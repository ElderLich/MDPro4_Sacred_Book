# Duel.ConfirmDecktop

## Signature

```lua
Duel.ConfirmDecktop(int player, int count) -> void
```

## Description

Confirm the player card group above count cards

## Parameters

- `player` `int`
- `count` `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4890`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **151** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.ConfirmDecktop`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [GMX 55th Experiment Report](/examples/cards/38984832) | `38984832` | [Scripts/c38984832.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38984832.lua) | 64 |
| GMX - VELOX | `82706696` | [Scripts/c82706696.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82706696.lua) | 56 |
| Purrely | `25550531` | [Scripts/c25550531.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25550531.lua) | 56 |
| Magellanica, the Deep Sea City | `26534688` | [Scripts/c26534688.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c26534688.lua) | 56 |
| Gunkan Sushipyard Seaside Supper Spot | `62200831` | [Scripts/c62200831.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62200831.lua) | 54 |
| Sylvan Dancepione | `21903613` | [Scripts/c21903613.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21903613.lua) | 54 |
| Rank-Up-Magic Zexal Force | `36224040` | [Scripts/c36224040.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36224040.lua) | 53 |
| Materiactor Meltthrough | `66059345` | [Scripts/c66059345.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66059345.lua) | 53 |
| Ma'at | `18631392` | [Scripts/c18631392.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18631392.lua) | 51 |
| Silk Bomb Moth | `18300894` | [Scripts/c18300894.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18300894.lua) | 50 |
| Shadowreaver Knight 21 | `95506252` | [Scripts/c95506252.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95506252.lua) | 50 |
| Oracle of Zefra | `32354768` | [Scripts/c32354768.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32354768.lua) | 49 |
| Materiactor Meltdown | `38669664` | [Scripts/c38669664.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38669664.lua) | 49 |
| GMX Applied Experiment #55 | `18795635` | [Scripts/c18795635.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18795635.lua) | 49 |
| Buerillabaisse de Nouvelles | `26223582` | [Scripts/c26223582.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c26223582.lua) | 48 |
| Super Koi Koi | `66171432` | [Scripts/c66171432.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66171432.lua) | 48 |
| Chaos Ruler, the Chaotic Magical Dragon | `3040496` | [Scripts/c3040496.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3040496.lua) | 48 |
| Valiant Shark Lancer | `23672629` | [Scripts/c23672629.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23672629.lua) | 48 |
| Adamancipator Risen - Leonite | `47674738` | [Scripts/c47674738.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c47674738.lua) | 48 |
| Akashic Magician | `28776350` | [Scripts/c28776350.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28776350.lua) | 47 |
| Uradora of Fate | `27753563` | [Scripts/c27753563.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27753563.lua) | 46 |
| Rafale, Champion Fur Hire | `38916526` | [Scripts/c38916526.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38916526.lua) | 46 |
| Shooting Star Dragon | `24696097` | [Scripts/c24696097.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24696097.lua) | 45 |
| Hollowrokket Dragon | `51548207` | [Scripts/c51548207.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c51548207.lua) | 45 |
| ...and 127 more |  |  |  |

## Script Examples

### GMX 55th Experiment Report (`38984832`)

Source: [Scripts/c38984832.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38984832.lua)

```lua
		Duel.ConfirmCards(1-tp,g)
	else
		Duel.ConfirmDecktop(tp,count)
	end
end
```

### GMX - VELOX (`82706696`)

Source: [Scripts/c82706696.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82706696.lua)

```lua
	end
	if seq>-1 then
		Duel.ConfirmDecktop(tp,dct-seq)
		if e:GetHandler():IsSetCard(0x1dd) then
			Duel.RaiseEvent(e:GetHandler(),EVENT_CUSTOM+1595137,e,0,tp,tp,0)
```

### Purrely (`25550531`)

Source: [Scripts/c25550531.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25550531.lua)

```lua
function s.tdop(e,tp,eg,ep,ev,re,r,rp)
	local p=Duel.GetChainInfo(0,CHAININFO_TARGET_PLAYER)
	Duel.ConfirmDecktop(p,3)
	local g=Duel.GetDecktopGroup(p,3)
	if not g or #g<1 then return end
```
