# Duel.ClearTargetCard

## Signature

```lua
Duel.ClearTargetCard() -> void
```

## Description

Clears the target-card group recorded on the current Chain Link, if one exists.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5005`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **20** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.ClearTargetCard`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Tohushaddoll Grysta](/examples/cards/95072744) | `95072744` | [Scripts/c95072744.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95072744.lua) | 64 |
| Zebufera, Vaalmonican Hallow Heathen | `2815176` | [Scripts/c2815176.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2815176.lua) | 52 |
| Thunder Dragon Thunderstormech | `12081875` | [Scripts/c12081875.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12081875.lua) | 50 |
| Darklord Eveningstar | `10136446` | [Scripts/c10136446.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10136446.lua) | 50 |
| Chasma, Dragon Ruler of Auroras | `4965193` | [Scripts/c4965193.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4965193.lua) | 47 |
| Tellarknight Constellar Caduceus | `58858807` | [Scripts/c58858807.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58858807.lua) | 46 |
| Darklord Tezcatlipoca | `88234365` | [Scripts/c88234365.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88234365.lua) | 45 |
| Darklord Amdusc | `51728779` | [Scripts/c51728779.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c51728779.lua) | 45 |
| Bait Doll | `7165085` | [Scripts/c7165085.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7165085.lua) | 45 |
| Darklord Ixchel | `52840267` | [Scripts/c52840267.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52840267.lua) | 44 |
| Kewl Tune Playlist | `40847034` | [Scripts/c40847034.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40847034.lua) | 41 |
| Darklord Nasten | `25339070` | [Scripts/c25339070.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25339070.lua) | 40 |
| Double Spell | `24096228` | [Scripts/c24096228.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24096228.lua) | 40 |
| Kewl Tune Loudness War | `41069676` | [Scripts/c41069676.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41069676.lua) | 38 |
| Darklord Nergal | `18168997` | [Scripts/c18168997.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18168997.lua) | 38 |
| Spellbook of the Master | `56981417` | [Scripts/c56981417.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56981417.lua) | 37 |
| Fusion Duplication | `43331750` | [Scripts/c43331750.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43331750.lua) | 34 |
| Trap of Darkness | `79766336` | [Scripts/c79766336.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c79766336.lua) | 33 |
| Transaction Rollback | `6351147` | [Scripts/c6351147.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6351147.lua) | 32 |
| Fake Feather | `22628574` | [Scripts/c22628574.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22628574.lua) | 31 |

## Script Examples

### Tohushaddoll Grysta (`95072744`)

Source: [Scripts/c95072744.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95072744.lua)

```lua
	local g=Duel.SelectTarget(tp,s.efffilter,tp,LOCATION_GRAVE,0,1,1,nil,e,tp,eg,ep,ev,re,r,rp)
	local tc=g:GetFirst()
	Duel.ClearTargetCard()
	tc:CreateEffectRelation(e)
	e:SetLabelObject(tc)
```

### Zebufera, Vaalmonican Hallow Heathen (`2815176`)

Source: [Scripts/c2815176.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2815176.lua)

```lua
	local tc=Duel.SelectTarget(tp,s.filter,tp,LOCATION_GRAVE+LOCATION_REMOVED,0,1,1,nil):GetFirst()
	local te,ceg,cev,cre,cr,crp=tc:CheckActivateEffect(false,true,true)
	Duel.ClearTargetCard()
	tc:CreateEffectRelation(e)
	local tg=te:GetTarget()
```

### Thunder Dragon Thunderstormech (`12081875`)

Source: [Scripts/c12081875.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12081875.lua)

```lua
	Duel.SetOperationInfo(0,CATEGORY_TODECK,g,1,0,0)
	local tc=g:GetFirst()
	Duel.ClearTargetCard()
	tc:CreateEffectRelation(e)
	e:SetLabelObject(tc)
```
