# Auxiliary.IsInGroup

## Signature

```lua
Auxiliary.IsInGroup(Card c, Group g) -> bool
```

## Description

Returns true if g contains c.

## Parameters

- `c` `Card`
- `g` `Group`

## Returns

- `bool` - true if g contains c.

## Source

- `Utilities/utility.lua:597`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **30** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.IsInGroup`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Barian's Chaos Draw](/examples/cards/97769122) | `97769122` | [Scripts/c97769122.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97769122.lua) | 63 |
| [El Shaddoll Meshachrer](/examples/cards/32467459) | `32467459` | [Scripts/c32467459.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32467459.lua) | 61 |
| Starving Venom Wing Dragon | `5148778` | [Scripts/c5148778.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5148778.lua) | 60 |
| Frightfur Meister | `77522571` | [Scripts/c77522571.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77522571.lua) | 59 |
| Kuribeh | `34419588` | [Scripts/c34419588.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34419588.lua) | 57 |
| Heavy Interlock | `20071842` | [Scripts/c20071842.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20071842.lua) | 56 |
| Token Support | `53545926` | [Scripts/c53545926.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53545926.lua) | 51 |
| Tragic Twin Twined Jewels | `81143465` | [Scripts/c81143465.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81143465.lua) | 51 |
| Dawn Angel Kambi | `12500059` | [Scripts/c12500059.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12500059.lua) | 51 |
| Hrimnir the Divine Follower | `49904658` | [Scripts/c49904658.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49904658.lua) | 51 |
| CXyz Gimmick Puppet Fanatix Machinix | `3685372` | [Scripts/c3685372.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3685372.lua) | 50 |
| Toon Black Luster Soldier | `28711704` | [Scripts/c28711704.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28711704.lua) | 50 |
| Nouvelles Recipe Book "Recettes de Nouvellez" | `61944066` | [Scripts/c61944066.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61944066.lua) | 49 |
| Galaxy Photon Dragon | `85747929` | [Scripts/c85747929.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85747929.lua) | 49 |
| Winds Over the Ice Barrier | `17197110` | [Scripts/c17197110.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17197110.lua) | 49 |
| Rasterliger | `88000953` | [Scripts/c88000953.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88000953.lua) | 49 |
| Shining Sarcophagus | `79791878` | [Scripts/c79791878.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c79791878.lua) | 48 |
| Generaider Boss Bite | `720147` | [Scripts/c720147.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c720147.lua) | 47 |
| Mysterion the Dragon Crown | `13735899` | [Scripts/c13735899.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13735899.lua) | 45 |
| Kuribah | `44632120` | [Scripts/c44632120.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44632120.lua) | 45 |
| Bonding - D2O | `79402185` | [Scripts/c79402185.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c79402185.lua) | 43 |
| Valkyrion the Magna Warrior | `75347539` | [Scripts/c75347539.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75347539.lua) | 42 |
| Lyrilusc - Ensemblue Robin | `72971064` | [Scripts/c72971064.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c72971064.lua) | 41 |
| Dovelgus, Generaider Boss of Iron | `76382116` | [Scripts/c76382116.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76382116.lua) | 39 |
| ...and 6 more |  |  |  |

## Script Examples

### Barian's Chaos Draw (`97769122`)

Source: [Scripts/c97769122.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97769122.lua)

```lua
end
function c97769122.matfilter(sg,tp,g)
	if sg:Filter(aux.IsInGroup,nil,g):GetCount()~=g:GetCount() then return false end
	return Duel.IsExistingMatchingCard(c97769122.xyzfilter,tp,LOCATION_EXTRA,0,1,nil,sg)
end
```

### El Shaddoll Meshachrer (`32467459`)

Source: [Scripts/c32467459.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32467459.lua)

```lua
function s.FShaddollCheck(g,gc,fc,tp,c,chkf,exg)
	if gc and not g:IsContains(gc) then return false end
	if exg and g:FilterCount(aux.IsInGroup,nil,exg)>1 then return false end
	if g:IsExists(aux.TuneMagicianCheckX,1,nil,g,EFFECT_TUNE_MAGICIAN_F) then return false end
	if not aux.MustMaterialCheck(g,tp,EFFECT_MUST_BE_FMATERIAL) then return false end
```

### Starving Venom Wing Dragon (`5148778`)

Source: [Scripts/c5148778.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5148778.lua)

```lua
	else
		Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_TARGET)
		sg=Duel.SelectTarget(tp,aux.IsInGroup,tp,LOCATION_MZONE,LOCATION_MZONE,1,1,nil,g)
	end
	Duel.SetOperationInfo(0,CATEGORY_DISABLE,sg,1,0,0)
```
