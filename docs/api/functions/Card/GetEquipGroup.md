# Card.GetEquipGroup

## Signature

```lua
Card.GetEquipGroup(Card c) -> Group
```

## Description

Returns the Equip Cards currently equipped to c as a Group.

## Parameters

- `c` `Card`

## Returns

- `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3517`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **63** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.GetEquipGroup`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Power Tool Braver Dragon | `63265554` | [Scripts/c63265554.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63265554.lua) | 58 |
| DoomZ XII Zero - Drastea | `92472273` | [Scripts/c92472273.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92472273.lua) | 57 |
| Dragunity Arma Leyvaten | `63487632` | [Scripts/c63487632.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63487632.lua) | 54 |
| Cyberdark End Dragon | `37542782` | [Scripts/c37542782.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37542782.lua) | 53 |
| Millennium-Eyes Restrict | `41578483` | [Scripts/c41578483.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41578483.lua) | 53 |
| Shadowreaver Knight 21 | `95506252` | [Scripts/c95506252.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95506252.lua) | 50 |
| ZW - Dragonic Halberd | `2896663` | [Scripts/c2896663.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2896663.lua) | 50 |
| DoomZ Command "D.O.O.M.D.U.R.G." | `68831625` | [Scripts/c68831625.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c68831625.lua) | 49 |
| Allure Dance | `68316358` | [Scripts/c68316358.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c68316358.lua) | 49 |
| Number 6: Chronomaly Atlandis | `9161357` | [Scripts/c9161357.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9161357.lua) | 49 |
| Blue-Eyes Tyrant Dragon | `11443677` | [Scripts/c11443677.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11443677.lua) | 49 |
| Nightmare-Eyes Restrict | `30138615` | [Scripts/c30138615.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30138615.lua) | 48 |
| DoomZ V Five - Amalthe | `28877382` | [Scripts/c28877382.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28877382.lua) | 48 |
| Therion "Reaper" Fum | `21727231` | [Scripts/c21727231.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21727231.lua) | 47 |
| Fiendsmith's Desirae | `82135803` | [Scripts/c82135803.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82135803.lua) | 47 |
| Vylon Disigma | `39987164` | [Scripts/c39987164.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39987164.lua) | 47 |
| Metalhold the Moving Blockade | `42237854` | [Scripts/c42237854.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42237854.lua) | 46 |
| Zaralaam the Dark Palace | `64230128` | [Scripts/c64230128.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c64230128.lua) | 46 |
| Therion "Lily" Borea | `83610035` | [Scripts/c83610035.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c83610035.lua) | 46 |
| Ultimate Leo Utopia Ray | `68679595` | [Scripts/c68679595.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c68679595.lua) | 46 |
| DoomZ VII Seven - Elara | `54265980` | [Scripts/c54265980.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54265980.lua) | 46 |
| Destiny HERO - Plasma | `83965310` | [Scripts/c83965310.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c83965310.lua) | 46 |
| Reincarnation Unveiling Mail | `68663427` | [Scripts/c68663427.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c68663427.lua) | 45 |
| Therion "King" Regulus | `10604644` | [Scripts/c10604644.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10604644.lua) | 45 |
| ...and 39 more |  |  |  |

## Script Examples

### Power Tool Braver Dragon (`63265554`)

Source: [Scripts/c63265554.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63265554.lua)

```lua
function c63265554.pncost(e,tp,eg,ep,ev,re,r,rp,chk)
	local c=e:GetHandler()
	local cg=c:GetEquipGroup()
	if chk==0 then return cg:IsExists(c63265554.cfilter,1,nil,tp) end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_TOGRAVE)
```

### DoomZ XII Zero - Drastea (`92472273`)

Source: [Scripts/c92472273.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92472273.lua)

```lua
end
function s.xyzcon(e,tp,eg,ep,ev,re,r,rp)
	local g=e:GetHandler():GetEquipGroup()
	return g:GetCount()>0 and not g:IsExists(aux.NOT(Card.IsCanOverlay),1,nil)
end
```

### Dragunity Arma Leyvaten (`63487632`)

Source: [Scripts/c63487632.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63487632.lua)

```lua
end
function c63487632.spfilter(c,tp)
	return c:GetEquipGroup():IsExists(Card.IsSetCard,1,nil,0x29) and c:IsAbleToRemoveAsCost()
		and Duel.GetMZoneCount(tp,c)>0
end
```
