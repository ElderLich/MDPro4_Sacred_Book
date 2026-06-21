# Auxiliary.CreateMaterialReasonCardRelation

## Signature

```lua
Auxiliary.CreateMaterialReasonCardRelation(Card c, Effect te) -> void
```

## Description

Registers an EVENT_BE_MATERIAL continuous effect on c so that, when c is used as material, the Summoned monster creates an effect relation with te.

## Parameters

- `c` `Card`
- `te` `Effect`

## Source

- `Utilities/utility.lua:859`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **12** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.CreateMaterialReasonCardRelation`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Cupid Pitch | `21915012` | [Scripts/c21915012.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21915012.lua) | 54 |
| Update Jammer | `88093706` | [Scripts/c88093706.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88093706.lua) | 47 |
| Speedroid Gum Prize | `70939418` | [Scripts/c70939418.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70939418.lua) | 46 |
| Gluttonous Reptolphin Greethys | `8576764` | [Scripts/c8576764.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8576764.lua) | 37 |
| Triggering Wurm | `95504778` | [Scripts/c95504778.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95504778.lua) | 37 |
| Gouki Tagpartner | `67586735` | [Scripts/c67586735.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67586735.lua) | 35 |
| Hyper Synchron | `40348946` | [Scripts/c40348946.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40348946.lua) | 32 |
| Dinowrestler Capaptera | `93507434` | [Scripts/c93507434.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93507434.lua) | 30 |
| Speedroid Block-n-Roll | `69550259` | [Scripts/c69550259.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c69550259.lua) | 27 |
| Vice Berserker | `43014054` | [Scripts/c43014054.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43014054.lua) | 24 |
| Swap Cleric | `30968774` | [Scripts/c30968774.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30968774.lua) | 24 |
| Counselor Lily | `5519829` | [Scripts/c5519829.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5519829.lua) | 24 |

## Script Examples

### Cupid Pitch (`21915012`)

Source: [Scripts/c21915012.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21915012.lua)

```lua
	e3:SetOperation(c21915012.thop)
	c:RegisterEffect(e3)
	aux.CreateMaterialReasonCardRelation(c,e3)
end
function c21915012.matfilter(c)
```

### Update Jammer (`88093706`)

Source: [Scripts/c88093706.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88093706.lua)

```lua
	e2:SetOperation(c88093706.efop)
	c:RegisterEffect(e2)
	aux.CreateMaterialReasonCardRelation(c,e2)
end
function c88093706.mfilter(c)
```

### Speedroid Gum Prize (`70939418`)

Source: [Scripts/c70939418.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70939418.lua)

```lua
	e3:SetOperation(c70939418.ddop)
	c:RegisterEffect(e3)
	aux.CreateMaterialReasonCardRelation(c,e3)
end
function c70939418.spcon(e,tp,eg,ep,ev,re,r,rp)
```
