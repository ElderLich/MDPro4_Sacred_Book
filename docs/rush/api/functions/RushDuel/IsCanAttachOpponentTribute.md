# RushDuel.IsCanAttachOpponentTribute

Alias: `RD.IsCanAttachOpponentTribute`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsCanAttachOpponentTribute(any card, any player, any flag) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 可否赋予效果 - 使用对方的怪兽解放
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `flag` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:299`

```lua
function RushDuel.IsCanAttachOpponentTribute(card, player, flag)
    if Duel.IsPlayerAffectedByEffect(player, EFFECT_CANNOT_SINGLE_TRIBUTE) and Duel.IsPlayerAffectedByEffect(player, EFFECT_CANNOT_DOUBLE_TRIBUTE) then
        return false
    end
    return not card:IsHasEffect(EFFECT_UNRELEASABLE_SUM) and card:GetFlagEffect(flag) == 0
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **4** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.IsCanAttachOpponentTribute) with `RushDuel.IsCanAttachOpponentTribute`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Royal Rebel's Extreme | `120306006` | [Rush/Scripts/c120306006.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306006.lua) | 2 |
| Tribute Impact | `120244046` | [Rush/Scripts/c120244046.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120244046.lua) | 1 |
| The Monarchs Stormforth | `120291022` | [Rush/Scripts/c120291022.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120291022.lua) | 1 |
| Offering to the Archfiend | `120277055` | [Rush/Scripts/c120277055.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120277055.lua) | 2 |

## Script Examples

### Royal Rebel's Extreme (`120306006`)

Source: [Rush/Scripts/c120306006.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306006.lua)

```lua
--Release
function cm.filter(c,tp)
	return RD.IsCanAttachOpponentTribute(c,tp,20244046)
		and RD.IsCanAttachOpponentTribute(c,tp,20309007)
end
```

### Tribute Impact (`120244046`)

Source: [Rush/Scripts/c120244046.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120244046.lua)

```lua
		Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_TOGRAVE)
		local mg=g:SelectWithSumEqual(tp,Card.GetLevel,tc:GetLevel(),1,g:GetCount())
		if Duel.SendtoGrave(mg,REASON_EFFECT)~=0 and RD.IsCanAttachOpponentTribute(tc,tp,20244046) then
			RD.AttachOpponentTribute(e,tc,20244046,aux.Stringid(m,2),RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END,RESET_PHASE+PHASE_END)
		end
```

### The Monarchs Stormforth (`120291022`)

Source: [Rush/Scripts/c120291022.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120291022.lua)

```lua
--Activate
function cm.filter(c,tp)
	return RD.IsCanAttachOpponentTribute(c,tp,20244046)
end
function cm.condition(e,tp,eg,ep,ev,re,r,rp)
```
