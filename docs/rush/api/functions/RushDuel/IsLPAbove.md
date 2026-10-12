# RushDuel.IsLPAbove

Alias: `RD.IsLPAbove`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsLPAbove(any player, any lp) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 玩家的LP在 lp 以上
```

## Parameters

- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `lp` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:61`

```lua
function RushDuel.IsLPAbove(player, lp)
    return Duel.GetLP(player) >= lp
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **3** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.IsLPAbove) with `RushDuel.IsLPAbove`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Galactica Dejavu | `120244003` | [Rush/Scripts/c120244003.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120244003.lua) | 1 |
| Gingangel, the Deluxe Sushi Fairy | `120155030` | [Rush/Scripts/c120155030.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120155030.lua) | 1 |
| Buffered Slime | `120235064` | [Rush/Scripts/c120235064.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120235064.lua) | 1 |

## Script Examples

### Galactica Dejavu (`120244003`)

Source: [Rush/Scripts/c120244003.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120244003.lua)

```lua
end
function cm.condition(e,tp,eg,ep,ev,re,r,rp)
	return RD.IsLPAbove(1-tp,4000)
end
cm.cost=RD.CostSendSelfToGrave()
```

### Gingangel, the Deluxe Sushi Fairy (`120155030`)

Source: [Rush/Scripts/c120155030.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120155030.lua)

```lua
end
function cm.condition(e,tp,eg,ep,ev,re,r,rp)
	return RD.IsLPAbove(1-tp,4000)
end
cm.cost=RD.CostSendHandToGrave(Card.IsAbleToGraveAsCost,2,2)
```

### Buffered Slime (`120235064`)

Source: [Rush/Scripts/c120235064.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120235064.lua)

```lua
	if Duel.DiscardDeck(tp,1,REASON_EFFECT)==0 then return end
	RD.CreateNoBattleDamageEffect(e,aux.Stringid(m,1),tp,1,0,RESET_PHASE+PHASE_END)
	if RD.IsLPAbove(tp,3000) then
		Duel.Damage(tp,2000,REASON_EFFECT)
	end
```
