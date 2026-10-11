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
