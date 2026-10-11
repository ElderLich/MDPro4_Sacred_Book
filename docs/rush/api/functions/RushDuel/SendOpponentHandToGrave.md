# RushDuel.SendOpponentHandToGrave

Alias: `RD.SendOpponentHandToGrave`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.SendOpponentHandToGrave(any tp, any hint, any min, any max) -> any
```

## Description

Rush Duel helper declared in `RDAction.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
操作: 随机选对方的手卡送去墓地
```

## Parameters

- `tp` `any`: Type and behavior are not yet reviewed; see the source.
- `hint` `any`: Type and behavior are not yet reviewed; see the source.
- `min` `any`: Type and behavior are not yet reviewed; see the source.
- `max` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAction.lua:317`

```lua
function RushDuel.SendOpponentHandToGrave(tp, hint, min, max)
    local g = Duel.GetFieldGroup(tp, 0, LOCATION_HAND)
    local ct = #g
    if ct < min then
        return 0
    end
    local ops = {}
    for i = min, math.min(max, ct) do
        table.insert(ops, i)
    end
    local ac = 0
    if #ops == 1 then
        ac = table.remove(ops)
    elseif #ops > 1 then
        Duel.Hint(HINT_SELECTMSG, tp, HINTMSG_OPERATE_COUNT)
        ac = Duel.AnnounceNumber(tp, table.unpack(ops))
    end
    if ac > 0 then
        local sg = g:RandomSelect(tp, ac)
        return Duel.SendtoGrave(sg, REASON_EFFECT)
    end
    return 0
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **7** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.SendOpponentHandToGrave) with `RushDuel.SendOpponentHandToGrave`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Amusi Annoyance | `120249063` | [Rush/Scripts/c120249063.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120249063.lua) | 1 |
| Void Intercept | `120227028` | [Rush/Scripts/c120227028.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120227028.lua) | 1 |
| Frightening Fan Mail | `120217080` | [Rush/Scripts/c120217080.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120217080.lua) | 1 |
| Thestalos the Firestorm Monarch | `120248001` | [Rush/Scripts/c120248001.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120248001.lua) | 1 |
| Royal Rebel's Shout | `120140018` | [Rush/Scripts/c120140018.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120140018.lua) | 1 |
| Traditional Tax | `120235063` | [Rush/Scripts/c120235063.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120235063.lua) | 1 |
| Handsray Destleo | `120109012` | [Rush/Scripts/c120109012.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120109012.lua) | 1 |

## Script Examples

### Amusi Annoyance (`120249063`)

Source: [Rush/Scripts/c120249063.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120249063.lua)

```lua
	local ct=Duel.GetFieldGroupCount(tp,0,LOCATION_HAND)
	if RD.Damage(nil,ct*300)~=0 and ev>0 then
		RD.SendOpponentHandToGrave(tp,aux.Stringid(m,1),1,1)
	end
end
```

### Void Intercept (`120227028`)

Source: [Rush/Scripts/c120227028.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120227028.lua)

```lua
end
function cm.activate(e,tp,eg,ep,ev,re,r,rp)
	if RD.SendOpponentHandToGrave(tp,aux.Stringid(m,1),1,1)~=0
		and Duel.GetFieldGroupCount(tp,0,LOCATION_HAND)>=2 then
		RD.CanDraw(aux.Stringid(m,2),1-tp,1,true)
```

### Frightening Fan Mail (`120217080`)

Source: [Rush/Scripts/c120217080.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120217080.lua)

```lua
function cm.activate(e,tp,eg,ep,ev,re,r,rp)
	local ct=Duel.GetMatchingGroupCount(cm.filter,tp,LOCATION_MZONE,0,nil)
	local dam=RD.SendOpponentHandToGrave(tp,aux.Stringid(m,1),1,ct)*300
	if dam>0 then
		Duel.Damage(1-tp,dam,REASON_EFFECT)
```
