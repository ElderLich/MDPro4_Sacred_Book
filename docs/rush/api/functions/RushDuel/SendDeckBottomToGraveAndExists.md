# RushDuel.SendDeckBottomToGraveAndExists

Alias: `RD.SendDeckBottomToGraveAndExists`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.SendDeckBottomToGraveAndExists(any player, any card_count, any filter, any count, any expect) -> any
```

## Description

Rush Duel helper declared in `RDAction.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
操作: 从卡组下面把卡送去墓地
```

## Parameters

- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `card_count` `any`: Type and behavior are not yet reviewed; see the source.
- `filter` `any`: Type and behavior are not yet reviewed; see the source.
- `count` `any`: Type and behavior are not yet reviewed; see the source.
- `expect` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAction.lua:308`

```lua
function RushDuel.SendDeckBottomToGraveAndExists(player, card_count, filter, count, expect)
    local dg = RushDuel.GetDeckBottomGroup(player, card_count)
    if #dg == 0 then
        return false
    end
    Duel.DisableShuffleCheck()
    return Duel.SendtoGrave(dg, REASON_EFFECT) ~= 0 and RushDuel.IsOperatedGroupExists(filter, count, expect)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **2** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.SendDeckBottomToGraveAndExists) with `RushDuel.SendDeckBottomToGraveAndExists`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Iris the Rare Shadow Flower | `120228018` | [Rush/Scripts/c120228018.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120228018.lua) | 1 |
| Necromaid Carriage | `120294018` | [Rush/Scripts/c120294018.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120294018.lua) | 1 |

## Script Examples

### Iris the Rare Shadow Flower (`120228018`)

Source: [Rush/Scripts/c120228018.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120228018.lua)

```lua
		if not Duel.IsPlayerCanDiscardDeck(tp,1) then return end
		Duel.BreakEffect()
		if RD.SendDeckBottomToGraveAndExists(tp,1,cm.exfilter,1,nil) then
			RD.CanSelectAndSpecialSummon(aux.Stringid(m,1),aux.NecroValleyFilter(cm.spfilter),tp,LOCATION_GRAVE,0,1,1,nil,e,POS_FACEUP)
		end
```

### Necromaid Carriage (`120294018`)

Source: [Rush/Scripts/c120294018.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120294018.lua)

```lua
end
function cm.operation(e,tp,eg,ep,ev,re,r,rp)
	if RD.SendDeckBottomToGraveAndExists(tp,1) then
		local tc=Duel.GetOperatedGroup():GetFirst()
		if tc:IsRace(RACE_ZOMBIE) and tc:IsLocation(LOCATION_GRAVE)
```
