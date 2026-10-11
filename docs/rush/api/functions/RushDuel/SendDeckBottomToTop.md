# RushDuel.SendDeckBottomToTop

Alias: `RD.SendDeckBottomToTop`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.SendDeckBottomToTop(any player, any count) -> any
```

## Description

Rush Duel helper declared in `RDFunction.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
将玩家卡组最下面的N张卡移到卡组最上面
```

## Parameters

- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `count` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDFunction.lua:145`

```lua
function RushDuel.SendDeckBottomToTop(player, count)
    local g = Duel.GetFieldGroup(player, LOCATION_DECK, 0)
    for i = 1, count do
        Duel.MoveSequence(g:GetMinGroup(Card.GetSequence):GetFirst(), 0)
    end
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **3** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.SendDeckBottomToTop) with `RushDuel.SendDeckBottomToTop`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Extra! Extra! Hot Off the Press | `120304049` | [Rush/Scripts/c120304049.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304049.lua) | 1 |
| Hot Off the Press | `120199048` | [Rush/Scripts/c120199048.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120199048.lua) | 1 |
| Searching Union | `120305012` | [Rush/Scripts/c120305012.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120305012.lua) | 1 |

## Script Examples

### Extra! Extra! Hot Off the Press (`120304049`)

Source: [Rush/Scripts/c120304049.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304049.lua)

```lua
function cm.activate(e,tp,eg,ep,ev,re,r,rp)
	if Duel.GetFieldGroupCount(tp,0,LOCATION_DECK)<3 then return end
	RD.SendDeckBottomToTop(1-tp,3)
	Duel.ConfirmDecktop(1-tp,3)
	local g=Duel.GetDecktopGroup(1-tp,3)
```

### Hot Off the Press (`120199048`)

Source: [Rush/Scripts/c120199048.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120199048.lua)

```lua
function cm.activate(e,tp,eg,ep,ev,re,r,rp)
	if Duel.GetFieldGroupCount(tp,0,LOCATION_DECK)<5 then return end
	RD.SendDeckBottomToTop(1-tp,5)
	Duel.ConfirmDecktop(1-tp,5)
	local dam=Duel.GetDecktopGroup(1-tp,5):FilterCount(cm.filter,nil)*400
```

### Searching Union (`120305012`)

Source: [Rush/Scripts/c120305012.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120305012.lua)

```lua
function cm.activate(e,tp,eg,ep,ev,re,r,rp)
	if Duel.GetFieldGroupCount(tp,LOCATION_DECK,0)<5 then return end
	RD.SendDeckBottomToTop(tp,5)
	local sg=RD.RevealDeckTopAndCanSelect(tp,5,aux.Stringid(m,1),HINTMSG_ATOHAND,cm.thfilter,1,2)
	if sg:GetCount()>0 then
```
