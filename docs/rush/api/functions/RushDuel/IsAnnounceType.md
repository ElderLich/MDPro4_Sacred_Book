# RushDuel.IsAnnounceType

Alias: `RD.IsAnnounceType`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsAnnounceType(any card) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 是宣言的种类
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:86`

```lua
function RushDuel.IsAnnounceType(card)
    local announce = Duel.GetChainInfo(0, CHAININFO_TARGET_PARAM)
    return (announce == 0 and card:IsType(TYPE_MONSTER)) or (announce == 1 and card:IsType(TYPE_SPELL)) or (announce == 2 and card:IsType(TYPE_TRAP))
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **4** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.IsAnnounceType) with `RushDuel.IsAnnounceType`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Reporter Wars Scoopies \[L\] | `120304007` | [Rush/Scripts/c120304007.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304007.lua) | 1 |
| High-Speed Machine ENG | `120304012` | [Rush/Scripts/c120304012.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304012.lua) | 1 |
| Happy Journal | `120304048` | [Rush/Scripts/c120304048.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304048.lua) | 1 |
| Reporter Lilim | `120304011` | [Rush/Scripts/c120304011.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304011.lua) | 1 |

## Script Examples

### Reporter Wars Scoopies [L] (`120304007`)

Source: [Rush/Scripts/c120304007.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304007.lua)

```lua
	Duel.ConfirmDecktop(1-tp,1)
	local tc=Duel.GetDecktopGroup(1-tp,1):GetFirst()
	if RD.IsAnnounceType(tc) then
		if Duel.Recover(tp,400,REASON_EFFECT)~=0 and RD.IsMaximumMode(e:GetHandler()) then
			RD.CanSelectAndDoAction(aux.Stringid(m,1),HINTMSG_DESTROY,nil,tp,0,LOCATION_ONFIELD,1,1,nil,function(g)
```

### High-Speed Machine ENG (`120304012`)

Source: [Rush/Scripts/c120304012.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304012.lua)

```lua
	Duel.ConfirmDecktop(1-tp,1)
	local tc=Duel.GetDecktopGroup(1-tp,1):GetFirst()
	if RD.IsAnnounceType(tc) then
		RD.CanSelectAndDoAction(aux.Stringid(m,1),HINTMSG_ATOHAND,aux.NecroValleyFilter(cm.thfilter),tp,LOCATION_GRAVE,0,1,1,nil,function(g)
			if RD.SendToHandAndExists(g,e,tp,REASON_EFFECT) then
```

### Happy Journal (`120304048`)

Source: [Rush/Scripts/c120304048.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304048.lua)

```lua
	if Duel.GetFieldGroupCount(tp,0,LOCATION_DECK)<2 then return end
	Duel.ConfirmDecktop(1-tp,2)
	local ct=Duel.GetDecktopGroup(1-tp,2):FilterCount(RD.IsAnnounceType,nil)
	if ct>0 then
		Duel.Draw(tp,ct,REASON_EFFECT)
```
