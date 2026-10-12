# RushDuel.IsCanChangeRace

Alias: `RD.IsCanChangeRace`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsCanChangeRace(any card, any race) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 可以被改变种族
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `race` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:355`

```lua
function RushDuel.IsCanChangeRace(card, race)
    local effects = {card:IsHasEffect(EFFECT_CHANGE_RACE)}
    local curret = card:GetOriginalRace()
    local active = nil
    for i, effect in ipairs(effects) do
        local value = effect:GetValue()
        if value ~= curret or effect:GetLabel() == FLAG_ATTACH_EFFECT then
            curret = value
            active = effect
        end
    end
    -- 被改变了种族
    if active then
        if active:GetLabel() ~= FLAG_ATTACH_EFFECT then
            -- 不是赋予类效果，可以随便更改
            return true
        else
            return not card:IsRace(curret)
        end
    else
        return not card:IsRace(race)
    end
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **26** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.IsCanChangeRace) with `RushDuel.IsCanChangeRace`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| OuTerverSe Direct Driver | `120109056` | [Rush/Scripts/c120109056.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120109056.lua) | 1 |
| OuTerverSe Burst Oblivion | `120290008` | [Rush/Scripts/c120290008.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120290008.lua) | 1 |
| OuTerverSe Wish of Angeleva | `120293061` | [Rush/Scripts/c120293061.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120293061.lua) | 1 |
| OuTerverSe Wish of Devilgear | `120293062` | [Rush/Scripts/c120293062.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120293062.lua) | 1 |
| OuTerverSe Byugyuwazzo | `120290006` | [Rush/Scripts/c120290006.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120290006.lua) | 1 |
| OuTerverSe Toxic Blob | `120290028` | [Rush/Scripts/c120290028.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120290028.lua) | 1 |
| Delirium Shewel | `120274058` | [Rush/Scripts/c120274058.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120274058.lua) | 1 |
| OuTerverSe Bug Fungus | `120290002` | [Rush/Scripts/c120290002.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120290002.lua) | 1 |
| Wish of OuTerverSe the World-Shattering Emperor \[L\] | `120293058` | [Rush/Scripts/c120293058.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120293058.lua) | 1 |
| OuTerverSe Mother Fungus | `120293063` | [Rush/Scripts/c120293063.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120293063.lua) | 1 |
| OuTerverSe Sylphy Seyfert | `120290007` | [Rush/Scripts/c120290007.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120290007.lua) | 1 |
| Delirium Drone | `120274059` | [Rush/Scripts/c120274059.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120274059.lua) | 1 |
| OuTerverSe Rainpale | `120290004` | [Rush/Scripts/c120290004.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120290004.lua) | 1 |
| Delirium Polynea | `120277033` | [Rush/Scripts/c120277033.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120277033.lua) | 1 |
| Delirium Mariquita | `120274057` | [Rush/Scripts/c120274057.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120274057.lua) | 1 |
| OuTerverSe Anubistar | `120290003` | [Rush/Scripts/c120290003.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120290003.lua) | 1 |
| OuTerverSe Acid Blob | `120290001` | [Rush/Scripts/c120290001.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120290001.lua) | 1 |
| Evil Bowler | `120271027` | [Rush/Scripts/c120271027.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120271027.lua) | 2 |
| OuTerverSe Needle Maker | `120290005` | [Rush/Scripts/c120290005.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120290005.lua) | 1 |
| OuTerverSe Endless Doom Oblivion | `120290029` | [Rush/Scripts/c120290029.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120290029.lua) | 1 |
| Accel Wonder Flare | `120186010` | [Rush/Scripts/c120186010.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120186010.lua) | 1 |
| Bio Mechmantis | `120208030` | [Rush/Scripts/c120208030.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120208030.lua) | 1 |
| Delirium Teega | `120300025` | [Rush/Scripts/c120300025.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120300025.lua) | 1 |
| Delirium Papillon | `120222035` | [Rush/Scripts/c120222035.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120222035.lua) | 1 |
| ...and 2 more |  |  |  |

## Script Examples

### OuTerverSe Direct Driver (`120109056`)

Source: [Rush/Scripts/c120109056.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120109056.lua)

```lua
function cm.condition(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	return RD.IsSummonTurn(c) and RD.IsCanChangeRace(c,RACE_GALAXY)
end
cm.cost=RD.CostSendDeckTopToGrave(1)
```

### OuTerverSe Burst Oblivion (`120290008`)

Source: [Rush/Scripts/c120290008.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120290008.lua)

```lua
end
function cm.condition(e,tp,eg,ep,ev,re,r,rp)
	return RD.IsCanChangeRace(e:GetHandler(),RACE_GALAXY)
end
cm.cost=RD.CostSendHandToGrave(Card.IsAbleToGraveAsCost,1,1)
```

### OuTerverSe Wish of Angeleva (`120293061`)

Source: [Rush/Scripts/c120293061.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120293061.lua)

```lua
		if RD.SendToHandAndExists(g,e,tp,REASON_EFFECT)
			and c:IsFaceup() and c:IsRelateToEffect(e)
			and RD.IsCanChangeRace(c,RACE_GALAXY)
			and Duel.SelectEffectYesNo(tp,c,aux.Stringid(m,1)) then
			Duel.BreakEffect()
```
