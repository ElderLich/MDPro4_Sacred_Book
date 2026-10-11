# RushDuel.AttachEndPhase

Alias: `RD.AttachEndPhase`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AttachEndPhase(any e, any card, any player, any code, any operation, any desc, any once) -> any
```

## Description

Rush Duel helper declared in `RDAttach.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
赋予: 回合结束时特效
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `code` `any`: Type and behavior are not yet reviewed; see the source.
- `operation` `any`: Type and behavior are not yet reviewed; see the source.
- `desc` `any`: Type and behavior are not yet reviewed; see the source.
- `once` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAttach.lua:140`

```lua
function RushDuel.AttachEndPhase(e, card, player, code, operation, desc, once)
    if once then
        card:RegisterFlagEffect(0, RESET_EVENT + RESETS_STANDARD + RESET_PHASE + PHASE_END, EFFECT_FLAG_CLIENT_HINT, 1, code, desc)
    else
        card:RegisterFlagEffect(0, RESET_EVENT + RESETS_STANDARD, EFFECT_FLAG_CLIENT_HINT, 1, code, desc)
    end
    local e1 = Effect.CreateEffect(e:GetHandler())
    e1:SetType(EFFECT_TYPE_FIELD + EFFECT_TYPE_CONTINUOUS)
    e1:SetCode(EVENT_PHASE + PHASE_END)
    e1:SetCountLimit(1)
    e1:SetLabelObject(card)
    e1:SetCondition(function(e, tp, eg, ep, ev, re, r, rp)
        local tc = e:GetLabelObject()
        local fids = {tc:GetFlagEffectLabel(0)}
        for i = 1, #fids do
            if fids[i] == code then
                return true
            end
        end
        e:Reset()
        return false
    end)
    e1:SetOperation(operation)
    if once then
        e1:SetReset(RESET_PHASE + PHASE_END)
    end
    Duel.RegisterEffect(e1, player)
    return e1
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **10** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.AttachEndPhase) with `RushDuel.AttachEndPhase`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Rescue Rabbit](/examples/rush-cards/120109057) | `120109057` | [Rush/Scripts/c120109057.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120109057.lua) | 1 |
| Instant Fusion | `120305053` | [Rush/Scripts/c120305053.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120305053.lua) | 1 |
| Magical Weapoknight Xeno One | `120306038` | [Rush/Scripts/c120306038.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120306038.lua) | 1 |
| Etraynze the Shadow Flower Ninja | `120170029` | [Rush/Scripts/c120170029.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120170029.lua) | 1 |
| Rescue Cat | `120307008` | [Rush/Scripts/c120307008.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120307008.lua) | 1 |
| Darklord Zerato | `120228000` | [Rush/Scripts/c120228000.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120228000.lua) | 1 |
| Shadow Flower Spore | `120170048` | [Rush/Scripts/c120170048.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120170048.lua) | 1 |
| Power Shockborg | `120294022` | [Rush/Scripts/c120294022.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120294022.lua) | 1 |
| Garland the True Shadow Flower Ninja | `120170031` | [Rush/Scripts/c120170031.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120170031.lua) | 1 |
| Mega Multistrike Dragon Dragias Burst \[L\] | `120210001` | [Rush/Scripts/c120210001.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120210001.lua) | 1 |

## Script Examples

### Rescue Rabbit (`120109057`)

Source: [Rush/Scripts/c120109057.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120109057.lua)

```lua
		local g=Duel.GetOperatedGroup()
		g:ForEach(function(tc)
			RD.AttachEndPhase(e,tc,tp,m,cm.desop,aux.Stringid(m,1),true)
		end)
	end
```

### Instant Fusion (`120305053`)

Source: [Rush/Scripts/c120305053.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120305053.lua)

```lua
		if Duel.SpecialSummon(tc,SUMMON_TYPE_FUSION,tp,tp,false,false,POS_FACEUP)~=0 then
			RD.AttachCannotAttack(e,tc,aux.Stringid(m,1),RESET_EVENT+RESETS_STANDARD)
			RD.AttachEndPhase(e,tc,tp,m,cm.tgop,aux.Stringid(m,2),true)
		end
	end)
```

### Magical Weapoknight Xeno One (`120306038`)

Source: [Rush/Scripts/c120306038.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120306038.lua)

```lua
	local c=e:GetHandler()
	if c:IsFaceup() and c:IsRelateToEffect(e) then
		RD.AttachEndPhase(e,c,tp,m,cm.ntrop,aux.Stringid(m,1),true)
	end
end
```
