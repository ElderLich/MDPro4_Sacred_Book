# RushDuel.IsNormalSpell

Alias: `RD.IsNormalSpell`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsNormalSpell(any card) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 卡片是通常魔法卡
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:5`

```lua
function RushDuel.IsNormalSpell(card)
    return card:GetType()==TYPE_SPELL or card:GetType()==TYPE_SPELL+TYPE_LEGEND
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **7** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.IsNormalSpell) with `RushDuel.IsNormalSpell`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Voidvelg Gehennamagia](/examples/rush-cards/120109048) | `120109048` | [Rush/Scripts/c120109048.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120109048.lua) | 2 |
| Sevens Road Ultima Witch | `120261045` | [Rush/Scripts/c120261045.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120261045.lua) | 1 |
| Twilight Companion - Dralia | `120304068` | [Rush/Scripts/c120304068.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120304068.lua) | 1 |
| Pitch-Dark Eradicator Sorcerer | `120309008` | [Rush/Scripts/c120309008.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120309008.lua) | 1 |
| Yabume the Frost-Purifying Purebreed | `120298045` | [Rush/Scripts/c120298045.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120298045.lua) | 1 |
| Draconic Peace Bomber | `120294062` | [Rush/Scripts/c120294062.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120294062.lua) | 1 |
| Altierra the Skysavior Transience | `120235039` | [Rush/Scripts/c120235039.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120235039.lua) | 1 |

## Script Examples

### Voidvelg Gehennamagia (`120109048`)

Source: [Rush/Scripts/c120109048.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120109048.lua)

```lua
--To Hand
function cm.exfilter(c)
	return RD.IsNormalSpell(c)
end
function cm.filter(c)
```

### Sevens Road Ultima Witch (`120261045`)

Source: [Rush/Scripts/c120261045.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120261045.lua)

```lua
end
function cm.aclimit(e,re,tp,chk)
	return RD.IsNormalSpell(re:GetHandler()) and re:IsHasType(EFFECT_TYPE_ACTIVATE)
		and re:IsActiveType(TYPE_SPELL)
end
```

### Twilight Companion - Dralia (`120304068`)

Source: [Rush/Scripts/c120304068.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120304068.lua)

```lua
end
function cm.tdfilter(c)
	return not RD.IsNormalSpell(c) and c:IsType(TYPE_SPELL) and c:IsAbleToDeck()
end
cm.cost=RD.CostSendGraveToDeckBottom(cm.costfilter,2,2)
```
