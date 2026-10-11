# Card.RemoveCounter

## Signature

```lua
Card.RemoveCounter(Card c, int player, int countertype, int count, int reason) -> bool|nil
```

## Description

Removes count counters of countertype from c for reason, using player as the removing player.
When countertype is 0, the core clears every counter on c and returns no Lua value. Otherwise it yields and returns whether the requested counters were removed.

## Parameters

- `c` `Card`
- `player` `int`
- `countertype` `int`
- `count` `int`
- `reason` `int`

## Returns

- `bool|nil`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3684`

## Guided Examples

Learn how to use this function in context:

- [Counters](/learn/counters)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **28** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.RemoveCounter) with `Card.RemoveCounter`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [El Shaddoll Apkallone](/examples/cards/50907446) | `50907446` | [Scripts/c50907446.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50907446.lua) | 1 |
| El Shaddoll Meshachrer | `32467459` | [Scripts/c32467459.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32467459.lua) | 1 |
| Zebufera, Vaalmonican Hallow Heathen | `2815176` | [Scripts/c2815176.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2815176.lua) | 1 |
| Limit Code | `86607583` | [Scripts/c86607583.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c86607583.lua) | 1 |
| Enneapolis | `17621695` | [Scripts/c17621695.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17621695.lua) | 1 |
| Summer Schoolwork Successful! | `77751766` | [Scripts/c77751766.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77751766.lua) | 1 |
| Link Turret | `55034079` | [Scripts/c55034079.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55034079.lua) | 1 |
| Full Moon Mirror | `44857722` | [Scripts/c44857722.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44857722.lua) | 1 |
| Ursarctic Radiation | `32692693` | [Scripts/c32692693.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32692693.lua) | 1 |
| Duralume, Vaalmonican Heathen Hallow | `76821171` | [Scripts/c76821171.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76821171.lua) | 1 |
| Gouki Cage Match | `85638822` | [Scripts/c85638822.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85638822.lua) | 1 |
| Tempest Magician | `63101919` | [Scripts/c63101919.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63101919.lua) | 1 |
| Thelematech Clatis | `98986900` | [Scripts/c98986900.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c98986900.lua) | 1 |
| F.A. Shining Star GT | `37414347` | [Scripts/c37414347.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37414347.lua) | 1 |
| Blackwing Armor Master | `69031175` | [Scripts/c69031175.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c69031175.lua) | 1 |
| Brainwashing Beam | `59258334` | [Scripts/c59258334.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59258334.lua) | 1 |
| War Rock Ordeal | `71331215` | [Scripts/c71331215.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71331215.lua) | 1 |
| Linkbelt Wall Dragon | `63092423` | [Scripts/c63092423.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63092423.lua) | 1 |
| Pitch-Black Power Stone | `34029630` | [Scripts/c34029630.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34029630.lua) | 1 |
| Hinezumi Hanabi | `71459017` | [Scripts/c71459017.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71459017.lua) | 1 |
| Fire Cracker | `81109178` | [Scripts/c81109178.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81109178.lua) | 1 |
| Shien's Daredevil | `98162021` | [Scripts/c98162021.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c98162021.lua) | 1 |
| Summon Shock | `42719764` | [Scripts/c42719764.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42719764.lua) | 1 |
| Updraft | `90557975` | [Scripts/c90557975.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90557975.lua) | 1 |
| ...and 4 more |  |  |  |

## Script Examples

### El Shaddoll Apkallone (`50907446`)

Source: [Scripts/c50907446.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50907446.lua)

```lua
	if exg and exg:IsExists(c50907446.FShaddollSpFilter2,1,nil,c,tp,g:GetFirst(),chkf)
		and (mg:GetCount()==0 or (exg:GetCount()>0 and Duel.SelectYesNo(tp,aux.Stringid(81788994,0)))) then
		fc:RemoveCounter(tp,0x16,3,REASON_EFFECT)
		Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_FMATERIAL)
		local sg=exg:FilterSelect(tp,c50907446.FShaddollSpFilter2,1,1,nil,c,tp,g:GetFirst(),chkf)
```

### El Shaddoll Meshachrer (`32467459`)

Source: [Scripts/c32467459.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32467459.lua)

```lua
	local g=mg:SelectSubGroup(tp,s.FShaddollCheck,false,3,3,gc,c,tp,c,chkf,exg)
	if exg and g:IsExists(aux.IsInGroup,1,nil,exg) then
		fc:RemoveCounter(tp,0x16,3,REASON_EFFECT)
	end
	Duel.SetFusionMaterial(g)
```

### Zebufera, Vaalmonican Hallow Heathen (`2815176`)

Source: [Scripts/c2815176.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2815176.lua)

```lua
		Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_FACEUP)
		local tc=g:FilterSelect(tp,Card.IsCanRemoveCounter,1,1,nil,tp,0x6a,1,REASON_COST):GetFirst()
		tc:RemoveCounter(tp,0x6a,1,REASON_COST)
		ct=ct+1
	end
```
