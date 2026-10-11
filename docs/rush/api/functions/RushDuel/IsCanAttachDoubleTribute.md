# RushDuel.IsCanAttachDoubleTribute

Alias: `RD.IsCanAttachDoubleTribute`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsCanAttachDoubleTribute(any card, any value) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 可否赋予效果 - 双重解放
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `value` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:277`

```lua
function RushDuel.IsCanAttachDoubleTribute(card, value)
    if Duel.IsPlayerAffectedByEffect(card:GetControler(), EFFECT_CANNOT_DOUBLE_TRIBUTE) then
        return false
    end
    if card:IsHasEffect(EFFECT_UNRELEASABLE_SUM) then
        return false
    end
    local values = RushDuel.GetEffectValues(card, EFFECT_DOUBLE_TRIBUTE)
    return RushDuel.CheckValueDoubleTribute(values, value)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **13** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.IsCanAttachDoubleTribute) with `RushDuel.IsCanAttachDoubleTribute`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Voidalfr Antromeda | `120300005` | [Rush/Scripts/c120300005.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300005.lua) | 1 |
| Spark Voltegg | `120246006` | [Rush/Scripts/c120246006.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120246006.lua) | 1 |
| Civil Twirider | `120304004` | [Rush/Scripts/c120304004.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304004.lua) | 1 |
| Bluegrass Stealer | `120228022` | [Rush/Scripts/c120228022.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120228022.lua) | 1 |
| Excutie Power Up! | `120208052` | [Rush/Scripts/c120208052.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120208052.lua) | 1 |
| Double Twin Dragon | `120231051` | [Rush/Scripts/c120231051.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120231051.lua) | 1 |
| Royal Rebel's Guardian | `120254078` | [Rush/Scripts/c120254078.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120254078.lua) | 1 |
| Delirium Teega | `120300025` | [Rush/Scripts/c120300025.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300025.lua) | 1 |
| Voidvelg Globule | `120227015` | [Rush/Scripts/c120227015.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120227015.lua) | 1 |
| Dododo Second | `120199025` | [Rush/Scripts/c120199025.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120199025.lua) | 1 |
| Ultimate Flag Beast Surge Bicorn | `120181011` | [Rush/Scripts/c120181011.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120181011.lua) | 1 |
| Blasting Bird | `120170033` | [Rush/Scripts/c120170033.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120170033.lua) | 1 |
| Card 120135002 | `120135002` | [Rush/Scripts/c120135002.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120135002.lua) | 1 |

## Script Examples

### Voidalfr Antromeda (`120300005`)

Source: [Rush/Scripts/c120300005.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300005.lua)

```lua
end
function cm.condition(e,tp,eg,ep,ev,re,r,rp)
	return RD.IsCanAttachDoubleTribute(e:GetHandler(),cm.trival)
end
cm.cost=RD.CostSendDeckTopToGrave(1)
```

### Spark Voltegg (`120246006`)

Source: [Rush/Scripts/c120246006.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120246006.lua)

```lua
end
function cm.condition(e,tp,eg,ep,ev,re,r,rp)
	return RD.IsCanAttachDoubleTribute(e:GetHandler(),cm.trival)
end
cm.cost=RD.CostSendGraveToDeck(cm.costfilter,1,1)
```

### Civil Twirider (`120304004`)

Source: [Rush/Scripts/c120304004.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304004.lua)

```lua
end
function cm.condition(e,tp,eg,ep,ev,re,r,rp)
	return RD.IsCanAttachDoubleTribute(e:GetHandler(),cm.trival)
end
cm.cost=RD.CostSendGraveToDeck(cm.costfilter,2,2)
```
