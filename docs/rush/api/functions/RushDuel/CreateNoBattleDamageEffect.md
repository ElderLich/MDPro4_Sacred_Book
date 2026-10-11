# RushDuel.CreateNoBattleDamageEffect

Alias: `RD.CreateNoBattleDamageEffect`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CreateNoBattleDamageEffect(any e, any desc, any player, any s_range, any o_range, any reset) -> any
```

## Description

Rush Duel helper declared in `RDLimit.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
创建限制: 不会受到战斗伤害
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `desc` `any`: Type and behavior are not yet reviewed; see the source.
- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `s_range` `any`: Type and behavior are not yet reviewed; see the source.
- `o_range` `any`: Type and behavior are not yet reviewed; see the source.
- `reset` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDLimit.lua:398`

```lua
function RushDuel.CreateNoBattleDamageEffect(e, desc, player, s_range, o_range, reset)
    local e1 = Effect.CreateEffect(e:GetHandler())
    e1:SetDescription(desc)
    e1:SetType(EFFECT_TYPE_FIELD)
    e1:SetCode(EFFECT_AVOID_BATTLE_DAMAGE)
    e1:SetProperty(EFFECT_FLAG_PLAYER_TARGET + EFFECT_FLAG_CLIENT_HINT)
    e1:SetTargetRange(s_range, o_range)
    e1:SetValue(1)
    e1:SetReset(reset)
    Duel.RegisterEffect(e1, player)
    return e1
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **4** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CreateNoBattleDamageEffect) with `RushDuel.CreateNoBattleDamageEffect`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Peace &amp; Rock n' Roll | `120253061` | [Rush/Scripts/c120253061.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120253061.lua) | 1 |
| Reporting from the Scene! | `120199062` | [Rush/Scripts/c120199062.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120199062.lua) | 1 |
| Buffered Slime | `120235064` | [Rush/Scripts/c120235064.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120235064.lua) | 1 |
| Cheater's Hidden Ball Trick | `120259005` | [Rush/Scripts/c120259005.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120259005.lua) | 1 |

## Script Examples

### Peace & Rock n' Roll (`120253061`)

Source: [Rush/Scripts/c120253061.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120253061.lua)

```lua
	RD.SelectAndDoAction(HINTMSG_DESTROY,nil,tp,0,LOCATION_MZONE,1,1,nil,function(g)
		if Duel.Destroy(g,REASON_EFFECT)~=0 and Duel.GetLP(tp)<=2000 then
			RD.CreateNoBattleDamageEffect(e,aux.Stringid(m,1),tp,1,0,RESET_PHASE+PHASE_END)
			RD.CreateNoEffectDamageEffect(e,aux.Stringid(m,2),cm.damval,tp,1,0,RESET_PHASE+PHASE_END)
		end
```

### Reporting from the Scene! (`120199062`)

Source: [Rush/Scripts/c120199062.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120199062.lua)

```lua
	local p=Duel.GetChainInfo(0,CHAININFO_TARGET_PLAYER)
	if RD.Damage()~=0 and p==1-tp then
		RD.CreateNoBattleDamageEffect(e,aux.Stringid(m,1),tp,1,0,RESET_PHASE+PHASE_END)
	end
end
```

### Buffered Slime (`120235064`)

Source: [Rush/Scripts/c120235064.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120235064.lua)

```lua
function cm.activate(e,tp,eg,ep,ev,re,r,rp)
	if Duel.DiscardDeck(tp,1,REASON_EFFECT)==0 then return end
	RD.CreateNoBattleDamageEffect(e,aux.Stringid(m,1),tp,1,0,RESET_PHASE+PHASE_END)
	if RD.IsLPAbove(tp,3000) then
		Duel.Damage(tp,2000,REASON_EFFECT)
```
