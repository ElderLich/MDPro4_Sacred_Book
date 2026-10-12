# RushDuel.GetBaseAttackOnTribute

Alias: `RD.GetBaseAttackOnTribute`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.GetBaseAttackOnTribute(any c) -> any
```

## Description

Rush Duel helper declared in `RDFunction.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
获取被上级召唤解放时的基础攻击力
```

## Parameters

- `c` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDFunction.lua:178`

```lua
function RushDuel.GetBaseAttackOnTribute(c)
    local atk
    if RushDuel.IsMaximumMode(c) then
        atk = c.maximum_attack
    else
        atk = c:GetTextAttack()
    end
    return math.max(0, atk)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **4** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.GetBaseAttackOnTribute) with `RushDuel.GetBaseAttackOnTribute`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| God Maju Garzett | `120261043` | [Rush/Scripts/c120261043.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120261043.lua) | 1 |
| Dark Matter Enigmata | `120261048` | [Rush/Scripts/c120261048.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120261048.lua) | 1 |
| Maju Garzett | `120238004` | [Rush/Scripts/c120238004.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120238004.lua) | 1 |
| Great Maju Garzett | `120238019` | [Rush/Scripts/c120238019.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120238019.lua) | 1 |

## Script Examples

### God Maju Garzett (`120261043`)

Source: [Rush/Scripts/c120261043.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120261043.lua)

```lua
function cm.getter(c)
	if c:IsType(TYPE_EFFECT) then
		return RD.GetBaseAttackOnTribute(c)
	else
		return 0
```

### Dark Matter Enigmata (`120261048`)

Source: [Rush/Scripts/c120261048.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120261048.lua)

```lua
	local g=c:GetMaterial()
	g:ForEach(function(tc)
		atk=atk+RD.GetBaseAttackOnTribute(tc)
	end)
	if atk>0 then
```

### Maju Garzett (`120238004`)

Source: [Rush/Scripts/c120238004.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120238004.lua)

```lua
--Material Check
function cm.getter(c)
	return RD.GetBaseAttackOnTribute(c)
end
--Atk Up
```
