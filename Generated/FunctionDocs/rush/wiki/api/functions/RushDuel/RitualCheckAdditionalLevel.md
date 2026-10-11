# RushDuel.RitualCheckAdditionalLevel

Alias: `RD.RitualCheckAdditionalLevel`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.RitualCheckAdditionalLevel(any c, any rc) -> any
```

## Description

Rush Duel helper declared in `RDRitual.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
仪式召唤 - 使用等级
```

## Parameters

- `c` `any`: Type and behavior are not yet reviewed; see the source.
- `rc` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDRitual.lua:90`

```lua
function RushDuel.RitualCheckAdditionalLevel(c, rc)
	local raw_level = c:GetRitualLevel(rc)
	local lv1 = raw_level&0xffff
	local lv2 = raw_level>>16
	if lv2 > 0 then
		return math.min(lv1, lv2)
	else
		return lv1
	end
end
```
