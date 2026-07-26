# Auxiliary.PhantasmsSpSummonType

## Signature

```lua
Auxiliary.PhantasmsSpSummonType(Card c) -> bool
```

## Description

Returns whether c is a Special Summon procedure monster, used by Phantasm Special Summon helpers.

## Parameters

- `c` `Card`

## Returns

- `bool`

## Source

- `Utilities/utility.lua:2037`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **3** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.PhantasmsSpSummonType`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Destruction Chant of the Sacred Beast | `50147815` | [Scripts/c50147815.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50147815.lua) | 2 |
| Fallen Paradise of the Sacred Beasts | `65861210` | [Scripts/c65861210.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65861210.lua) | 2 |
| The Orchestrator of the Sacred Beasts | `22734799` | [Scripts/c22734799.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22734799.lua) | 2 |

## Script Examples

### Destruction Chant of the Sacred Beast (`50147815`)

Source: [Scripts/c50147815.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50147815.lua)

```lua
function s.spfilter(c,e,tp)
	if not c:IsSetCard(0x1144) or not c:IsType(TYPE_MONSTER) then return false end
	return c:IsCanBeSpecialSummoned(e,0,tp,false,aux.PhantasmsSpSummonType(c),POS_FACEUP_DEFENSE)
end
function s.target(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Fallen Paradise of the Sacred Beasts (`65861210`)

Source: [Scripts/c65861210.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65861210.lua)

```lua
function s.spfilter(c,e,tp)
	if not c:IsFaceupEx() or not c:IsSetCard(0x1144) then return false end
	return c:IsCanBeSpecialSummoned(e,0,tp,false,aux.PhantasmsSpSummonType(c))
end
function s.spop(e,tp,eg,ep,ev,re,r,rp)
```

### The Orchestrator of the Sacred Beasts (`22734799`)

Source: [Scripts/c22734799.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22734799.lua)

```lua
function s.spfilter(c,e,tp)
	if not c:IsSetCard(0x1144) or c:IsLevel(8) then return false end
	return c:IsCanBeSpecialSummoned(e,0,tp,false,aux.PhantasmsSpSummonType(c),POS_FACEUP_DEFENSE)
end
function s.spsummon(c,tp)
```
