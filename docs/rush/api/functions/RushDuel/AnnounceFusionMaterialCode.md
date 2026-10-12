# RushDuel.AnnounceFusionMaterialCode

Alias: `RD.AnnounceFusionMaterialCode`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AnnounceFusionMaterialCode(any player, any card, any target) -> any
```

## Description

Rush Duel helper declared in `RDFusion.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
宣言融合素材的卡名
```

## Parameters

- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `target` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDFusion.lua:653`

```lua
function RushDuel.AnnounceFusionMaterialCode(player, card, target)
    local codes = RushDuel.GetAnnouncableFusionMaterialCodes(card, target)
    if #codes > 0 then
        return RushDuel.AnnounceCodes(player, codes)
    else
        return nil
    end
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **6** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.AnnounceFusionMaterialCode) with `RushDuel.AnnounceFusionMaterialCode`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [The Noodle Art of Flavor Shift](/examples/rush-cards/120300053) | `120300053` | [Rush/Scripts/c120300053.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120300053.lua) | 1 |
| Variable Stellariser | `120277007` | [Rush/Scripts/c120277007.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120277007.lua) | 1 |
| Accel Wonder Dark | `120285005` | [Rush/Scripts/c120285005.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120285005.lua) | 1 |
| Rare Dragorite | `120294008` | [Rush/Scripts/c120294008.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120294008.lua) | 1 |
| Phantasm Maskmaster | `120271028` | [Rush/Scripts/c120271028.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120271028.lua) | 1 |
| Elemental HERO Prisma | `120272065` | [Rush/Scripts/c120272065.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120272065.lua) | 1 |

## Script Examples

### The Noodle Art of Flavor Shift (`120300053`)

Source: [Rush/Scripts/c120300053.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120300053.lua)

```lua
		ec=mg:GetFirst()
	end
	local ac=RD.AnnounceFusionMaterialCode(tp,ec,tc)
	Duel.SetTargetParam(ac)
	Duel.SetOperationInfo(0,CATEGORY_ANNOUNCE,nil,0,tp,0)
```

### Variable Stellariser (`120277007`)

Source: [Rush/Scripts/c120277007.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120277007.lua)

```lua
	if chk==0 then return true end
	local tc=e:GetLabelObject()
	local ac=RD.AnnounceFusionMaterialCode(tp,e:GetHandler(),tc)
	Duel.SetTargetParam(ac)
	Duel.SetOperationInfo(0,CATEGORY_ANNOUNCE,nil,0,tp,0)
```

### Accel Wonder Dark (`120285005`)

Source: [Rush/Scripts/c120285005.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120285005.lua)

```lua
	if chk==0 then return true end
	local tc=e:GetLabelObject()
	local ac=RD.AnnounceFusionMaterialCode(tp,e:GetHandler(),tc)
	Duel.SetTargetParam(ac)
	Duel.SetOperationInfo(0,CATEGORY_ANNOUNCE,nil,0,tp,0)
```
