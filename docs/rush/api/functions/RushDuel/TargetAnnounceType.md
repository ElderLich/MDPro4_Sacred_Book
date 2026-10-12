# RushDuel.TargetAnnounceType

Alias: `RD.TargetAnnounceType`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.TargetAnnounceType(any player) -> any
```

## Description

Rush Duel helper declared in `RDTarget.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
对玩家效果: 宣言卡片的种类（怪兽·魔法·陷阱）
```

## Parameters

- `player` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDTarget.lua:29`

```lua
function RushDuel.TargetAnnounceType(player)
    Duel.SetTargetParam(Duel.AnnounceType(player))
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **4** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.TargetAnnounceType) with `RushDuel.TargetAnnounceType`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Reporter Wars Scoopies \[L\] | `120304007` | [Rush/Scripts/c120304007.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120304007.lua) | 1 |
| High-Speed Machine ENG | `120304012` | [Rush/Scripts/c120304012.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120304012.lua) | 1 |
| Happy Journal | `120304048` | [Rush/Scripts/c120304048.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120304048.lua) | 1 |
| Reporter Lilim | `120304011` | [Rush/Scripts/c120304011.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120304011.lua) | 1 |

## Script Examples

### Reporter Wars Scoopies [L] (`120304007`)

Source: [Rush/Scripts/c120304007.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120304007.lua)

```lua
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.GetFieldGroupCount(tp,0,LOCATION_DECK)>0 end
	RD.TargetAnnounceType(tp)
	Duel.SetOperationInfo(0,CATEGORY_RECOVER,nil,0,tp,400)
end
```

### High-Speed Machine ENG (`120304012`)

Source: [Rush/Scripts/c120304012.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120304012.lua)

```lua
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.GetFieldGroupCount(tp,0,LOCATION_DECK)>0 end
	RD.TargetAnnounceType(tp)
end
function cm.operation(e,tp,eg,ep,ev,re,r,rp)
```

### Happy Journal (`120304048`)

Source: [Rush/Scripts/c120304048.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120304048.lua)

```lua
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.GetFieldGroupCount(tp,0,LOCATION_DECK)>1 end
	RD.TargetAnnounceType(tp)
end
function cm.activate(e,tp,eg,ep,ev,re,r,rp)
```
