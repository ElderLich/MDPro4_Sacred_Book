# Duel.DisableSelfDestroyCheck

## Signature

```lua
Duel.DisableSelfDestroyCheck([bool disable]) -> void
```

## Description

Sets whether the core's self-destruction check is disabled; omitting disable disables the check.

## Parameters

- `disable` `bool` optional - default: true

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4913`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **4** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.DisableSelfDestroyCheck) with `Duel.DisableSelfDestroyCheck`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Cursed Copycat Noble Arms | `23249029` | [Scripts/c23249029.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23249029.lua) | 2 |
| Advanced Crystal Beast Ruby Carbuncle | `83575471` | [Scripts/c83575471.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c83575471.lua) | 2 |
| Mikanko Water Arabesque | `43527730` | [Scripts/c43527730.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43527730.lua) | 2 |
| Decoy Dragon | `2732323` | [Scripts/c2732323.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2732323.lua) | 2 |

## Script Examples

### Cursed Copycat Noble Arms (`23249029`)

Source: [Scripts/c23249029.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23249029.lua)

```lua
	local g=Duel.SelectMatchingCard(tp,s.spfilter,tp,LOCATION_DECK,0,1,1,nil,e,tp,ec)
	local tc=g:GetFirst()
	Duel.DisableSelfDestroyCheck()
	if tc and Duel.SpecialSummon(tc,0,tp,tp,false,false,POS_FACEUP)~=0 and Duel.Equip(tp,c,tc) then
		--Add Equip limit
```

### Advanced Crystal Beast Ruby Carbuncle (`83575471`)

Source: [Scripts/c83575471.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c83575471.lua)

```lua
			local gc=g:GetCount()
			if gc>0 and Duel.SelectYesNo(tp,aux.Stringid(83575471,0)) then
				Duel.DisableSelfDestroyCheck()
				Duel.SpecialSummonComplete()
				Duel.BreakEffect()
```

### Mikanko Water Arabesque (`43527730`)

Source: [Scripts/c43527730.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43527730.lua)

```lua
	local g=Duel.SelectMatchingCard(tp,c43527730.spfilter,tp,LOCATION_HAND+LOCATION_DECK,0,1,1,nil,e,tp,ec:GetOriginalCodeRule())
	local tc=g:GetFirst()
	Duel.DisableSelfDestroyCheck()
	if tc and Duel.SpecialSummon(tc,0,tp,tp,false,false,POS_FACEUP)~=0 and Duel.Equip(tp,c,tc) then
		--Add Equip limit
```
