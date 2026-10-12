# RushDuel.IsCanAttachCannotToDeckEffect

Alias: `RD.IsCanAttachCannotToDeckEffect`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsCanAttachCannotToDeckEffect(any card, any value) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 可否赋予效果 - 不会因效果回到手卡
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `value` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:331`

```lua
function RushDuel.IsCanAttachCannotToDeckEffect(card, value)
    local values = RushDuel.GetEffectValues(card, EFFECT_CANNOT_TO_DECK_EFFECT)
    for _, val in ipairs(values) do
        if val == 1 then
            return false
        end
    end
    return true
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.IsCanAttachCannotToDeckEffect) with `RushDuel.IsCanAttachCannotToDeckEffect`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Lufer the Symbol of the Devils](/examples/rush-cards/120309059) | `120309059` | [Rush/Scripts/c120309059.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120309059.lua) | 1 |

## Script Examples

### Lufer the Symbol of the Devils (`120309059`)

Source: [Rush/Scripts/c120309059.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120309059.lua)

```lua
		and (RD.IsCanAttachEffectIndes(c,tp,cm.indval)
		or RD.IsCanAttachCannotToHandEffect(c,1)
		or RD.IsCanAttachCannotToDeckEffect(c,1))
end
function cm.exfilter(c)
```
