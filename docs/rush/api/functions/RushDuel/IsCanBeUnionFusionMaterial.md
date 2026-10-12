# RushDuel.IsCanBeUnionFusionMaterial

Alias: `RD.IsCanBeUnionFusionMaterial`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsCanBeUnionFusionMaterial(any card, any code) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 是否可以作为2只不同卡名的融合术素材
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `code` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:162`

```lua
function RushDuel.IsCanBeUnionFusionMaterial(card, code)
    local effects = {card:IsHasEffect(EFFECT_UNION_FUSION_MATERIAL)}
    for i, effect in ipairs(effects) do
        local code1, code2 = effect:GetLabel()
        if code1 == code or code2 == code then
            return true
        end
    end
    return false
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **2** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.IsCanBeUnionFusionMaterial) with `RushDuel.IsCanBeUnionFusionMaterial`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [YXZ-Cannon Dragon](/examples/rush-cards/120305004) | `120305004` | [Rush/Scripts/c120305004.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120305004.lua) | 3 |
| XYZ-Dragon Cannon | `120305003` | [Rush/Scripts/c120305003.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120305003.lua) | 3 |

## Script Examples

### YXZ-Cannon Dragon (`120305004`)

Source: [Rush/Scripts/c120305004.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120305004.lua)

```lua
function cm.matfilter(c,fc,sub)
	return c:IsFusionCode(list[1],list[2],list[3]) or (sub and c:CheckFusionSubstitute(fc))
		or RD.IsCanBeUnionFusionMaterial(c,list[1]) or RD.IsCanBeUnionFusionMaterial(c,list[2])
		or RD.IsCanBeUnionFusionMaterial(c,list[3])
end
```

### XYZ-Dragon Cannon (`120305003`)

Source: [Rush/Scripts/c120305003.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120305003.lua)

```lua
function cm.matfilter(c,fc,sub)
	return c:IsFusionCode(list[1],list[2],list[3]) or (sub and c:CheckFusionSubstitute(fc))
		or RD.IsCanBeUnionFusionMaterial(c,list[1]) or RD.IsCanBeUnionFusionMaterial(c,list[2])
		or RD.IsCanBeUnionFusionMaterial(c,list[3])
end
```
