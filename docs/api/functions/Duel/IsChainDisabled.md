# Duel.IsChainDisabled

## Signature

```lua
Duel.IsChainDisabled(int chainc) -> bool
```

## Description

Checks whether chainc has already been negated.

## Parameters

- `chainc` `int`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5063`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **11** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.IsChainDisabled) with `Duel.IsChainDisabled`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Nervedo the Shadebeast Power Patron | `17473466` | [Scripts/c17473466.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17473466.lua) | 1 |
| Tensei Ryu-Ge Anva | `56322832` | [Scripts/c56322832.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56322832.lua) | 1 |
| Solfachord Solfegia | `84693918` | [Scripts/c84693918.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84693918.lua) | 1 |
| Horoscope Sorcerer, the Stargazer Magician | `1186447` | [Scripts/c1186447.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1186447.lua) | 1 |
| Cerulean Skyfire | `54828837` | [Scripts/c54828837.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54828837.lua) | 1 |
| D/D Savant Newton | `19302550` | [Scripts/c19302550.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c19302550.lua) | 1 |
| D/D Savant Copernicus | `46796664` | [Scripts/c46796664.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46796664.lua) | 1 |
| Dinomist Brachion | `368382` | [Scripts/c368382.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c368382.lua) | 1 |
| Dinomist Plesios | `38988538` | [Scripts/c38988538.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38988538.lua) | 1 |
| Dinomist Ankylos | `32134638` | [Scripts/c32134638.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32134638.lua) | 1 |
| White Wing Magician | `11067666` | [Scripts/c11067666.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11067666.lua) | 1 |

## Script Examples

### Nervedo the Shadebeast Power Patron (`17473466`)

Source: [Scripts/c17473466.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17473466.lua)

```lua
		and re:IsActiveType(TYPE_MONSTER)
		and Duel.GetFlagEffect(tp,id)==0
		and Duel.IsChainDisablable(ev) and not Duel.IsChainDisabled(ev)
end
function s.negop(e,tp,eg,ep,ev,re,r,rp)
```

### Tensei Ryu-Ge Anva (`56322832`)

Source: [Scripts/c56322832.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56322832.lua)

```lua
	return rp==1-tp and p==tp and te and te:GetHandler():IsSetCard(0x1c0) and te:IsActiveType(TYPE_SPELL)
		and Duel.GetFlagEffect(tp,id)==0
		and Duel.IsChainDisablable(ev) and not Duel.IsChainDisabled(ev)
end
function s.negop(e,tp,eg,ep,ev,re,r,rp)
```

### Solfachord Solfegia (`84693918`)

Source: [Scripts/c84693918.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84693918.lua)

```lua
		and re:IsActiveType(TYPE_MONSTER)
		and Duel.IsExistingMatchingCard(s.cfilter,tp,LOCATION_MZONE,0,1,nil)
		and Duel.IsChainDisablable(ev) and not Duel.IsChainDisabled(ev)
end
function s.negop(e,tp,eg,ep,ev,re,r,rp)
```
