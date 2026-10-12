# RushDuel.AttachOpponentTribute

Alias: `RD.AttachOpponentTribute`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AttachOpponentTribute(any e, any card, any flag, any desc, any reset, any reset_player) -> any
```

## Description

Rush Duel helper declared in `RDAttach.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
赋予: 使用对方的怪兽解放
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `flag` `any`: Type and behavior are not yet reviewed; see the source.
- `desc` `any`: Type and behavior are not yet reviewed; see the source.
- `reset` `any`: Type and behavior are not yet reviewed; see the source.
- `reset_player` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAttach.lua:53`

```lua
function RushDuel.AttachOpponentTribute(e, card, flag, desc, reset, reset_player)
    card:RegisterFlagEffect(flag, reset, EFFECT_FLAG_CLIENT_HINT, 1, 0, desc)
    local e1 = Effect.CreateEffect(e:GetHandler())
    e1:SetType(EFFECT_TYPE_SINGLE)
    e1:SetCode(EFFECT_ADD_EXTRA_TRIBUTE)
    e1:SetProperty(EFFECT_FLAG_CANNOT_DISABLE + EFFECT_FLAG_UNCOPYABLE)
    e1:SetTargetRange(0, LOCATION_MZONE)
    e1:SetLabelObject(card)
    e1:SetTarget(function(e, c)
        return c == e:GetLabelObject() and card:GetFlagEffect(flag) ~= 0
    end)
    e1:SetValue(POS_FACEUP_ATTACK + POS_FACEDOWN_DEFENSE)
    local e2 = Effect.CreateEffect(e:GetHandler())
    e2:SetType(EFFECT_TYPE_FIELD + EFFECT_TYPE_GRANT)
    e2:SetTarget(Auxiliary.TargetBoolFunction(Card.IsType, TYPE_MONSTER))
    e2:SetTargetRange(LOCATION_HAND, 0)
    e2:SetLabelObject(e1)
    e2:SetReset(reset_player or reset)
    Duel.RegisterEffect(e2, e:GetHandlerPlayer())
    return e1, e2
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **4** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.AttachOpponentTribute) with `RushDuel.AttachOpponentTribute`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Royal Rebel's Extreme | `120306006` | [Rush/Scripts/c120306006.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306006.lua) | 1 |
| Tribute Impact | `120244046` | [Rush/Scripts/c120244046.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120244046.lua) | 1 |
| The Monarchs Stormforth | `120291022` | [Rush/Scripts/c120291022.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120291022.lua) | 1 |
| Offering to the Archfiend | `120277055` | [Rush/Scripts/c120277055.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120277055.lua) | 1 |

## Script Examples

### Royal Rebel's Extreme (`120306006`)

Source: [Rush/Scripts/c120306006.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306006.lua)

```lua
	local filter=RD.Filter(cm.filter,tp)
	RD.SelectAndDoAction(aux.Stringid(m,1),filter,tp,0,LOCATION_MZONE,1,1,nil,function(sg)
		local e1,e2=RD.AttachOpponentTribute(e,sg:GetFirst(),20309007,aux.Stringid(m,2),RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END,RESET_PHASE+PHASE_END)
		e1:SetValue(POS_FACEUP_ATTACK)
		e2:SetTarget(cm.sumtg)
```

### Tribute Impact (`120244046`)

Source: [Rush/Scripts/c120244046.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120244046.lua)

```lua
		local mg=g:SelectWithSumEqual(tp,Card.GetLevel,tc:GetLevel(),1,g:GetCount())
		if Duel.SendtoGrave(mg,REASON_EFFECT)~=0 and RD.IsCanAttachOpponentTribute(tc,tp,20244046) then
			RD.AttachOpponentTribute(e,tc,20244046,aux.Stringid(m,2),RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END,RESET_PHASE+PHASE_END)
		end
	end)
```

### The Monarchs Stormforth (`120291022`)

Source: [Rush/Scripts/c120291022.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120291022.lua)

```lua
	local filter=RD.Filter(cm.filter,tp)
	RD.SelectAndDoAction(aux.Stringid(m,1),filter,tp,0,LOCATION_MZONE,1,1,nil,function(sg)
		local e1,e2=RD.AttachOpponentTribute(e,sg:GetFirst(),20244046,aux.Stringid(m,2),RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END,RESET_PHASE+PHASE_END)
		e1:SetValue(POS_FACEUP_ATTACK)
	end)
```
