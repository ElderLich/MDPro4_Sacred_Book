# RushDuel.IsCanBeDoubleFusionMaterial

Alias: `RD.IsCanBeDoubleFusionMaterial`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsCanBeDoubleFusionMaterial(any card, any code) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 是否可以作为2只数量的融合术素材
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `code` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:151`

```lua
function RushDuel.IsCanBeDoubleFusionMaterial(card, code)
    local effects = {card:IsHasEffect(EFFECT_DOUBLE_FUSION_MATERIAL)}
    for i, effect in ipairs(effects) do
        local value = effect:GetValue()
        if value == code then
            return true
        end
    end
    return false
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **3** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.IsCanBeDoubleFusionMaterial) with `RushDuel.IsCanBeDoubleFusionMaterial`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Tamabot King Golem | `120285039` | [Rush/Scripts/c120285039.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120285039.lua) | 1 |
| Deep Space Yggdrago | `120260007` | [Rush/Scripts/c120260007.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120260007.lua) | 1 |
| Blue-Eyes Ultimate Dragon | `120252001` | [Rush/Scripts/c120252001.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120252001.lua) | 1 |

## Script Examples

### Tamabot King Golem (`120285039`)

Source: [Rush/Scripts/c120285039.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120285039.lua)

```lua
end
function cm.exfilter(c)
	return RD.IsCanBeDoubleFusionMaterial(c,120285039)
end
function cm.check(g,tp,fc,chkf)
```

### Deep Space Yggdrago (`120260007`)

Source: [Rush/Scripts/c120260007.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120260007.lua)

```lua
end
function cm.exfilter(c)
	return RD.IsCanBeDoubleFusionMaterial(c,120260007)
end
function cm.check(g,tp,fc,chkf)
```

### Blue-Eyes Ultimate Dragon (`120252001`)

Source: [Rush/Scripts/c120252001.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120252001.lua)

```lua
end
function cm.exfilter(c)
	return RD.IsCanBeDoubleFusionMaterial(c,120252001)
end
function cm.check(g,tp,fc,chkf)
```
