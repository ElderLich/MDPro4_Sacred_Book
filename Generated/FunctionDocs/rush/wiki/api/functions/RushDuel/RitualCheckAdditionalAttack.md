# RushDuel.RitualCheckAdditionalAttack

Alias: `RD.RitualCheckAdditionalAttack`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.RitualCheckAdditionalAttack(any c, any rc) -> any
```

## Description

Rush Duel helper declared in `RDRitual.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
仪式召唤 - 使用攻击力
```

## Parameters

- `c` `any`: Type and behavior are not yet reviewed; see the source.
- `rc` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDRitual.lua:101`

```lua
function RushDuel.RitualCheckAdditionalAttack(c, rc)
	local x = c:GetAttack()
	if x > MAX_PARAMETER then
		return MAX_PARAMETER
	else
		return x
	end
end
```
