# RushDuel.RevealDeckTopAndCanSelectGroup

Alias: `RD.RevealDeckTopAndCanSelectGroup`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.RevealDeckTopAndCanSelectGroup(any player, any count, any desc, any hint, any filter, any check, any min, any max, ... any) -> any
```

## Description

Rush Duel helper declared in `RDAction.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
操作: 翻开卡组并可以选择卡 (子卡片组)
```

## Parameters

- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `count` `any`: Type and behavior are not yet reviewed; see the source.
- `desc` `any`: Type and behavior are not yet reviewed; see the source.
- `hint` `any`: Type and behavior are not yet reviewed; see the source.
- `filter` `any`: Type and behavior are not yet reviewed; see the source.
- `check` `any`: Type and behavior are not yet reviewed; see the source.
- `min` `any`: Type and behavior are not yet reviewed; see the source.
- `max` `any`: Type and behavior are not yet reviewed; see the source.
- `...` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAction.lua:456`

```lua
function RushDuel.RevealDeckTopAndCanSelectGroup(player, count, desc, hint, filter, check, min, max, ...)
    Duel.ConfirmDecktop(player, count)
    local g = Duel.GetDecktopGroup(player, count)
    local mg = g:Filter(filter, nil, ...)
    if mg:CheckSubGroup(check, min, max, ...) then
        local sg = RushDuel.CanSelect(desc, hint, player, mg, check, min, max, ...)
        if sg and #sg > 0 then
            g:Sub(sg)
            return sg, g
        end
    end
    return Group.CreateGroup(), g
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **7** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.RevealDeckTopAndCanSelectGroup) with `RushDuel.RevealDeckTopAndCanSelectGroup`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Moonforce Sheila](/examples/rush-cards/120300013) | `120300013` | [Rush/Scripts/c120300013.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300013.lua) | 1 |
| Hydrangea the Shadow Flower Tea Master | `120304029` | [Rush/Scripts/c120304029.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304029.lua) | 1 |
| Absolute Lord of D. | `120252005` | [Rush/Scripts/c120252005.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120252005.lua) | 1 |
| Power Capsule Red | `120294056` | [Rush/Scripts/c120294056.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120294056.lua) | 1 |
| Yorishiro of the Lion | `120294027` | [Rush/Scripts/c120294027.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120294027.lua) | 1 |
| Star Protector Calling | `120306046` | [Rush/Scripts/c120306046.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120306046.lua) | 1 |
| Encounter with the Sacred Tree | `120306049` | [Rush/Scripts/c120306049.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120306049.lua) | 1 |

## Script Examples

### Moonforce Sheila (`120300013`)

Source: [Rush/Scripts/c120300013.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300013.lua)

```lua
function cm.operation(e,tp,eg,ep,ev,re,r,rp)
	if Duel.GetFieldGroupCount(tp,LOCATION_DECK,0)<4 then return end
	local sg,g=RD.RevealDeckTopAndCanSelectGroup(tp,4,aux.Stringid(m,1),HINTMSG_ATOHAND,cm.filter,cm.check,1,2)
	if sg:GetCount()>0 then
		Duel.DisableShuffleCheck()
```

### Hydrangea the Shadow Flower Tea Master (`120304029`)

Source: [Rush/Scripts/c120304029.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304029.lua)

```lua
function cm.operation(e,tp,eg,ep,ev,re,r,rp)
	if Duel.GetFieldGroupCount(tp,LOCATION_DECK,0)<5 then return end
	local sg,g=RD.RevealDeckTopAndCanSelectGroup(tp,5,aux.Stringid(m,1),HINTMSG_ATOHAND,cm.filter,cm.check,1,2)
	if sg:GetCount()>0 then
		Duel.DisableShuffleCheck()
```

### Absolute Lord of D. (`120252005`)

Source: [Rush/Scripts/c120252005.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120252005.lua)

```lua
function cm.operation(e,tp,eg,ep,ev,re,r,rp)
	if Duel.GetFieldGroupCount(tp,LOCATION_DECK,0)<4 then return end
	local sg=RD.RevealDeckTopAndCanSelectGroup(tp,4,aux.Stringid(m,1),HINTMSG_ATOHAND,cm.filter,cm.check,1,2)
	if sg:GetCount()>0 then
		RD.SendToHandAndExists(sg,e,tp,REASON_EFFECT)
```
