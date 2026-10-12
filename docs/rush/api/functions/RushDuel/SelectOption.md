# RushDuel.SelectOption

Alias: `RD.SelectOption`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.SelectOption(int player, ... table) -> any|nil
```

## Description

Accepts option tables {available, description, value}. Unavailable options are omitted; a sole option is announced automatically. Returns the chosen value (or its original one-based option index), not Duel.SelectOption's zero-based menu index.
The default is implemented as value or index: both nil and false use the original one-based index, while numeric 0 is preserved because it is truthy in Lua. With no available options this helper returns nil.

## Parameters

- `player` `int`: Selecting player, 0 or 1.
- `...` `table`: Each option is {available, description, value}; value may be omitted.

## Returns

- `any|nil`: Chosen option value; nil when no options are available.

## Source

`Rush/Utilities/RDFunction.lua:59`

```lua
function RushDuel.SelectOption(player, ...)
    local options = {...}
    local ops = {}
    local opvals = {}
    for i = 1, #options do
        if options[i][1] then
            table.insert(ops, options[i][2])
            table.insert(opvals, options[i][3] or i)
        end
    end
    if #ops == 0 then return nil end
    if #ops == 1 then
        Duel.Hint(HINT_OPSELECTED, 1 - player, ops[1])
        return opvals[1]
    end
    local select = Duel.SelectOption(player, table.unpack(ops))
    return opvals[select + 1]
end
```

## Guided Examples

Learn how to use this function in context:

- [Rush Selection, Actions, And Temporary Stats](/learn/rush-selection-and-actions)

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **5** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.SelectOption) with `RushDuel.SelectOption`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [The Eye of Timaeus](/examples/rush-cards/120285065) | `120285065` | [Rush/Scripts/c120285065.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120285065.lua) | 1 |
| Evil Bowler | `120271027` | [Rush/Scripts/c120271027.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120271027.lua) | 1 |
| Mässig Anglurr | `120304037` | [Rush/Scripts/c120304037.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120304037.lua) | 1 |
| Voidvelg Stork | `120300001` | [Rush/Scripts/c120300001.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120300001.lua) | 1 |
| Speed Trooper | `120301061` | [Rush/Scripts/c120301061.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120301061.lua) | 1 |

## Script Examples

### The Eye of Timaeus (`120285065`)

Source: [Rush/Scripts/c120285065.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120285065.lua)

```lua
	local mat2=mat:Filter(Card.IsCode,nil,list[3])
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_CODE)
	local code=RD.SelectOption(tp,
		{mat1:GetCount()>0,aux.Stringid(m,1),list[2]},
		{mat2:GetCount()>0,aux.Stringid(m,2),list[3]}
```

### Evil Bowler (`120271027`)

Source: [Rush/Scripts/c120271027.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120271027.lua)

```lua
		local b1=RD.IsCanChangeRace(tc,RACE_FIEND)
		local b2=RD.IsCanChangeRace(tc,race)
		local op=RD.SelectOption(tp,{b1,aux.Stringid(m,1)},{b2,aux.Stringid(m,2)})
		if op==1 then
			RD.ChangeRace(e,tc,RACE_FIEND,RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
```

### Mässig Anglurr (`120304037`)

Source: [Rush/Scripts/c120304037.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120304037.lua)

```lua
end
function cm.operation(e,tp,eg,ep,ev,re,r,rp)
	local op=RD.SelectOption(tp,
		{Duel.IsPlayerCanDiscardDeck(tp,2),aux.Stringid(m,1)},
		{Duel.IsPlayerCanDiscardDeck(1-tp,2),aux.Stringid(m,2)})
```
