# RushDuel.CanSetCard

Alias: `RD.CanSetCard`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CanSetCard(any player, any desc, any card, any effect, any break_effect) -> any
```

## Description

Rush Duel helper declared in `RDAction.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
可选操作: 把怪兽或魔陷盖放
```

## Parameters

- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `desc` `any`: Type and behavior are not yet reviewed; see the source.
- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `effect` `any`: Type and behavior are not yet reviewed; see the source.
- `break_effect` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAction.lua:533`

```lua
function RushDuel.CanSetCard(player, desc, card, effect, break_effect)
    local b1 = card:IsType(TYPE_MONSTER) and Duel.GetLocationCount(player, LOCATION_MZONE) > 0 and card:IsCanBeSpecialSummoned(effect, 0, player, false, false, POS_FACEDOWN_DEFENSE)
    local b2 = card:IsType(TYPE_SPELL + TYPE_TRAP) and card:IsSSetable() and (card:IsType(TYPE_FIELD) or Duel.GetLocationCount(player, LOCATION_SZONE) > 0)
    if (b1 or b2) and Duel.SelectEffectYesNo(player, card, desc) then
        if break_effect then
            Duel.BreakEffect()
        end
        if b1 then
            Duel.SpecialSummon(card, 0, player, player, false, false, POS_FACEDOWN_DEFENSE)
            Duel.ConfirmCards(1 - player, card)
            return true
        else
            Duel.SSet(player, card)
            return true
        end
    end
    return false
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CanSetCard) with `RushDuel.CanSetCard`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Threat from Outer Space | `120257059` | [Rush/Scripts/c120257059.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120257059.lua) | 1 |

## Script Examples

### Threat from Outer Space (`120257059`)

Source: [Rush/Scripts/c120257059.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120257059.lua)

```lua
		local tc=Duel.GetOperatedGroup():GetFirst()
		if not aux.NecroValleyFilter()(tc) then return end
		local set=RD.CanSetCard(tp,aux.Stringid(m,1),tc,e,true)
		if set and tc:IsLevel(2) and tc:IsSummonLocation(LOCATION_GRAVE) then
			RD.CanSelectAndDoAction(aux.Stringid(m,2),HINTMSG_DESTROY,cm.desfilter,tp,0,LOCATION_ONFIELD,1,1,nil,function(g)
```
