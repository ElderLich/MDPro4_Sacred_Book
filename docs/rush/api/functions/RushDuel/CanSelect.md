# RushDuel.CanSelect

Alias: `RD.CanSelect`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CanSelect(any desc, any hint, any player, any group, any check, any min, any max, ... any) -> Group|nil
```

## Description

Asks the player whether to select. Declining returns nil; canceling the card selection returns to the yes/no prompt. A completed selection returns its Group.

## Parameters

- `desc` `any`: Type and behavior are not yet reviewed; see the source.
- `hint` `any`: Type and behavior are not yet reviewed; see the source.
- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `group` `any`: Type and behavior are not yet reviewed; see the source.
- `check` `any`: Type and behavior are not yet reviewed; see the source.
- `min` `any`: Type and behavior are not yet reviewed; see the source.
- `max` `any`: Type and behavior are not yet reviewed; see the source.
- `...` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `Group|nil`: Selected Group, or nil when the player declines.

## Source

`Rush/Utilities/RDFunction.lua:45`

```lua
function RushDuel.CanSelect(desc, hint, player, group, check, min, max, ...)
    ::cancel::
    if Duel.SelectYesNo(player, desc) then
        local sg = RushDuel.Select(hint, player, group, check, true, min, max, ...)
        if sg == nil then
            goto cancel
        else
            return sg
        end
    else
        return nil
    end
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CanSelect) with `RushDuel.CanSelect`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Machine Inspector | `120257057` | [Rush/Scripts/c120257057.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120257057.lua) | 1 |

## Script Examples

### Machine Inspector (`120257057`)

Source: [Rush/Scripts/c120257057.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120257057.lua)

```lua
	local draw=false
	if mg:GetCount()>0 then
		local sg=RD.CanSelect(aux.Stringid(m,1),HINTMSG_TOGRAVE,tp,mg,nil,1,2)
		if sg then
			Duel.DisableShuffleCheck()
```
