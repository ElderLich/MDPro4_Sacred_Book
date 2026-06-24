# Card.CheckActivateEffect

## Signature

```lua
Card.CheckActivateEffect(Card c, bool neglect_con, bool neglect_cost, bool copy_info) -> Effect|nil,Group|nil,int|nil,int|nil,Effect|nil,int|nil,int|nil
```

## Description

Checks whether c has an activation effect that can currently be activated.
If neglect_con is true, condition checks are skipped. If neglect_cost is true, cost checks are skipped.
When copy_info is true and the matching activation is not a free-chain activation, the returned values include the triggering event information: eg, ep, ev, re, r, and rp.
Returns no Lua values when no activation effect is currently usable, so local scripts usually compare the first result with nil.

## Parameters

- `c` `Card`
- `neglect_con` `bool` - true to skip the activation effect's condition check.
- `neglect_cost` `bool` - true to skip the activation effect's cost check.
- `copy_info` `bool` - true to copy triggering-event information for non-free-chain activations.

## Returns

- `Effect|nil` - The usable activation effect, or nil/no value if none is currently usable.
- `Group|nil` - eg when copy_info returns event data.
- `int|nil` - ep when copy_info returns event data.
- `int|nil` - ev when copy_info returns event data.
- `Effect|nil` - re when copy_info returns event data.
- `int|nil` - r when copy_info returns event data.
- `int|nil` - rp when copy_info returns event data.

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3545`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **32** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.CheckActivateEffect`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Barian's Chaos Draw](/examples/cards/97769122) | `97769122` | [Scripts/c97769122.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97769122.lua) | 63 |
| [Transonic Bird](/examples/cards/34072799) | `34072799` | [Scripts/c34072799.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34072799.lua) | 61 |
| [Chef de Nouvelles](/examples/cards/29251488) | `29251488` | [Scripts/c29251488.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29251488.lua) | 60 |
| Witchcrafter Genni | `64756282` | [Scripts/c64756282.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c64756282.lua) | 56 |
| Angello Vaalmonica | `3048768` | [Scripts/c3048768.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3048768.lua) | 54 |
| Dimonno Vaalmonica | `30432463` | [Scripts/c30432463.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30432463.lua) | 53 |
| Zebufera, Vaalmonican Hallow Heathen | `2815176` | [Scripts/c2815176.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2815176.lua) | 52 |
| Witchcrafter Pupils | `69964858` | [Scripts/c69964858.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c69964858.lua) | 52 |
| Darklord Eveningstar | `10136446` | [Scripts/c10136446.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10136446.lua) | 50 |
| Dinomorphia Kentregina | `48832775` | [Scripts/c48832775.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48832775.lua) | 49 |
| Predaplant Verte Anaconda | `70369116` | [Scripts/c70369116.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70369116.lua) | 49 |
| Joker's Wild | `81945678` | [Scripts/c81945678.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81945678.lua) | 47 |
| Dinomorphia Reversion | `28292031` | [Scripts/c28292031.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28292031.lua) | 46 |
| Seventh Ascension | `23153227` | [Scripts/c23153227.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23153227.lua) | 45 |
| Darklord Tezcatlipoca | `88234365` | [Scripts/c88234365.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88234365.lua) | 45 |
| Darklord Amdusc | `51728779` | [Scripts/c51728779.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c51728779.lua) | 45 |
| Stars Align across the Milky Way | `20417688` | [Scripts/c20417688.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20417688.lua) | 45 |
| Ruler of the End of the World | `3739500` | [Scripts/c3739500.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3739500.lua) | 44 |
| Darklord Ixchel | `52840267` | [Scripts/c52840267.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52840267.lua) | 44 |
| Traptrix Rafflesia | `6511113` | [Scripts/c6511113.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6511113.lua) | 42 |
| Darklord Nasten | `25339070` | [Scripts/c25339070.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25339070.lua) | 40 |
| Double Spell | `24096228` | [Scripts/c24096228.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24096228.lua) | 40 |
| Darklord Nergal | `18168997` | [Scripts/c18168997.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18168997.lua) | 38 |
| Numeron Network | `41418852` | [Scripts/c41418852.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41418852.lua) | 37 |
| ...and 8 more |  |  |  |

## Script Examples

### Barian's Chaos Draw (`97769122`)

Source: [Scripts/c97769122.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97769122.lua)

```lua
function c97769122.cpfilter(c)
	return c:GetType()==TYPE_SPELL and c:IsSetCard(0x175) and c:IsAbleToGraveAsCost()
		and c:CheckActivateEffect(true,true,false)~=nil
end
function c97769122.cptg(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Transonic Bird (`34072799`)

Source: [Scripts/c34072799.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34072799.lua)

```lua
end
function c34072799.cfilter(c)
	return c:GetType()==TYPE_SPELL+TYPE_RITUAL and c:IsAbleToGraveAsCost() and c:CheckActivateEffect(true,true,false)~=nil
end
function c34072799.rscost(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Chef de Nouvelles (`29251488`)

Source: [Scripts/c29251488.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29251488.lua)

```lua
end
function s.rfilter(c)
	return c:IsSetCard(0x197) and c:IsAllTypes(TYPE_RITUAL+TYPE_SPELL) and c:CheckActivateEffect(false,true,false)~=nil and c:IsAbleToRemoveAsCost()
end
function s.rsptg(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
```
