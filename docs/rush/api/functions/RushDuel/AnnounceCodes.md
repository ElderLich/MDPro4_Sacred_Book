# RushDuel.AnnounceCodes

Alias: `RD.AnnounceCodes`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AnnounceCodes(any player, any codes) -> any
```

## Description

Rush Duel helper declared in `RDFunction.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
让玩家从多个卡名中宣言一个
```

## Parameters

- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `codes` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDFunction.lua:200`

```lua
function RushDuel.AnnounceCodes(player, codes)
    if #codes == 0 then
        return nil
    end
    local afilter = {codes[1], OPCODE_ISCODE}
    if #codes > 1 then
        for i = 2, #codes do
            table.insert(afilter, codes[i])
            table.insert(afilter, OPCODE_ISCODE)
            table.insert(afilter, OPCODE_OR)
        end
    end
    Duel.Hint(HINT_SELECTMSG, player, HINTMSG_CODE)
    return Duel.AnnounceCard(player, table.unpack(afilter))
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **2** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.AnnounceCodes) with `RushDuel.AnnounceCodes`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Instant Gift](/examples/rush-cards/120306059) | `120306059` | [Rush/Scripts/c120306059.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120306059.lua) | 1 |
| Union Supporter | `120305011` | [Rush/Scripts/c120305011.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120305011.lua) | 1 |

## Script Examples

### Instant Gift (`120306059`)

Source: [Rush/Scripts/c120306059.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120306059.lua)

```lua
		end
	end
	local ac=RD.AnnounceCodes(tp,codes)
	Duel.SetTargetParam(ac)
	Duel.SetOperationInfo(0,CATEGORY_ANNOUNCE,nil,0,tp,0)
```

### Union Supporter (`120305011`)

Source: [Rush/Scripts/c120305011.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120305011.lua)

```lua
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return true end
	local code=RD.AnnounceCodes(tp,list)
	Duel.SetTargetParam(code)
	Duel.SetOperationInfo(0,CATEGORY_ANNOUNCE,nil,0,tp,0)
```
