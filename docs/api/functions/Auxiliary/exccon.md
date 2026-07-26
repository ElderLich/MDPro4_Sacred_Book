# Auxiliary.exccon

## Signature

```lua
Auxiliary.exccon(Effect e) -> bool
```

## Description

Condition helper for effects that cannot be activated during the same turn their handler was sent to the GY, unless that handler was returned.

## Parameters

- `e` `Effect`

## Returns

- `bool`

## Source

- `Utilities/utility.lua:802`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **117** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.exccon`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Vernusylph and the Changing Season | `37313338` | [Scripts/c37313338.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37313338.lua) | 1 |
| Clown Crew Malabarisme | `83232904` | [Scripts/c83232904.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c83232904.lua) | 1 |
| Psychic Arsenal | `16238373` | [Scripts/c16238373.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16238373.lua) | 1 |
| Thunder Dragon Fusion | `95238394` | [Scripts/c95238394.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95238394.lua) | 1 |
| Witchcrafter Masterpiece | `55072170` | [Scripts/c55072170.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55072170.lua) | 1 |
| Infernity Paranoia | `86547356` | [Scripts/c86547356.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c86547356.lua) | 1 |
| The Terminus of the Burning Abyss | `44771289` | [Scripts/c44771289.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44771289.lua) | 1 |
| Doodlebook - Uh uh uh! | `94113093` | [Scripts/c94113093.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c94113093.lua) | 1 |
| Zoodiac Combo | `73881652` | [Scripts/c73881652.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c73881652.lua) | 1 |
| Noble Arms - Excaliburn | `46008667` | [Scripts/c46008667.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46008667.lua) | 1 |
| Beetrooper Landing | `13234975` | [Scripts/c13234975.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13234975.lua) | 1 |
| Winds Over the Ice Barrier | `17197110` | [Scripts/c17197110.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17197110.lua) | 1 |
| Zexal Catapult | `95664204` | [Scripts/c95664204.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95664204.lua) | 1 |
| Xyz Entrust | `81978611` | [Scripts/c81978611.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81978611.lua) | 1 |
| Speedroid Ultra Hound | `86976918` | [Scripts/c86976918.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c86976918.lua) | 1 |
| Rank-Up-Magic Skip Force | `58988903` | [Scripts/c58988903.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58988903.lua) | 1 |
| Gunkan Suship Daily Special | `24393683` | [Scripts/c24393683.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24393683.lua) | 1 |
| Crystron Entry | `52176579` | [Scripts/c52176579.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52176579.lua) | 1 |
| Regenesis Code | `67171933` | [Scripts/c67171933.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67171933.lua) | 1 |
| Interrupted Kaiju Slumber | `99330325` | [Scripts/c99330325.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c99330325.lua) | 1 |
| Gagaga Illusion | `73496100` | [Scripts/c73496100.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c73496100.lua) | 1 |
| Magician Navigation | `7922915` | [Scripts/c7922915.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7922915.lua) | 1 |
| Ragnaraika Hunting Dance | `89824842` | [Scripts/c89824842.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c89824842.lua) | 1 |
| Burnout | `25669282` | [Scripts/c25669282.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25669282.lua) | 1 |
| ...and 93 more |  |  |  |

## Script Examples

### Vernusylph and the Changing Season (`37313338`)

Source: [Scripts/c37313338.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37313338.lua)

```lua
end
function c37313338.spcon(e,tp,eg,ep,ev,re,r,rp)
	return Duel.GetTurnPlayer()~=tp and Duel.GetFieldGroupCount(tp,LOCATION_HAND,0)==0 and aux.exccon(e)
end
function c37313338.spfilter(c,e,tp)
```

### Clown Crew Malabarisme (`83232904`)

Source: [Scripts/c83232904.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c83232904.lua)

```lua
	e2:SetProperty(EFFECT_FLAG_CARD_TARGET)
	e2:SetCountLimit(1,id+o)
	e2:SetCondition(aux.exccon)
	e2:SetCost(s.thcost)
	e2:SetTarget(s.thtg)
```

### Psychic Arsenal (`16238373`)

Source: [Scripts/c16238373.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16238373.lua)

```lua
	e2:SetProperty(EFFECT_FLAG_CARD_TARGET)
	e2:SetCountLimit(1,id+o)
	e2:SetCondition(aux.exccon)
	e2:SetCost(aux.bfgcost)
	e2:SetTarget(s.tdtg)
```
