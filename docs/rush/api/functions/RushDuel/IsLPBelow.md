# RushDuel.IsLPBelow

Alias: `RD.IsLPBelow`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsLPBelow(any player, any lp) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 玩家的LP在 lp 以下
```

## Parameters

- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `lp` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:65`

```lua
function RushDuel.IsLPBelow(player, lp)
    return Duel.GetLP(player) <= lp
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **10** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.IsLPBelow) with `RushDuel.IsLPBelow`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Strong Boy Sevens Road | `120212001` | [Rush/Scripts/c120212001.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120212001.lua) | 1 |
| Dian Keto the Cooking Master | `120217052` | [Rush/Scripts/c120217052.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120217052.lua) | 1 |
| Player #C39: Home Run Smasher | `120205016` | [Rush/Scripts/c120205016.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120205016.lua) | 1 |
| Stealthagic | `120235042` | [Rush/Scripts/c120235042.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120235042.lua) | 2 |
| Dark Matter Elysium | `120272043` | [Rush/Scripts/c120272043.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120272043.lua) | 1 |
| Predator Ganleon | `120205021` | [Rush/Scripts/c120205021.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120205021.lua) | 1 |
| Romic n' Roller | `120130024` | [Rush/Scripts/c120130024.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120130024.lua) | 1 |
| Esperade the Smashing Superstar | `120130025` | [Rush/Scripts/c120130025.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120130025.lua) | 1 |
| Esperade the Smashing Superstar | `120253000` | [Rush/Scripts/c120253000.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120253000.lua) | 1 |
| Neo-Spacian Air Hummingbird | `120272021` | [Rush/Scripts/c120272021.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120272021.lua) | 1 |

## Script Examples

### Strong Boy Sevens Road (`120212001`)

Source: [Rush/Scripts/c120212001.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120212001.lua)

```lua
		local atk=g:GetClassCount(Card.GetAttribute)*200
		RD.AttachAtkDef(e,c,atk,0,RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
		if RD.IsLPBelow(1-tp,700) then
			-- 700,000,000 overflow
			Duel.Damage(1-tp,7000000,REASON_EFFECT)
```

### Dian Keto the Cooking Master (`120217052`)

Source: [Rush/Scripts/c120217052.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120217052.lua)

```lua
	if RD.SendDeckTopToGraveAndExists(tp,3) then
		local rec=Duel.GetOperatedGroup():FilterCount(cm.exfilter,nil)*1000
		if rec~=0 and RD.IsLPBelow(tp,2000) and Duel.SelectYesNo(tp,aux.Stringid(m,1)) then
			Duel.Recover(tp,rec,REASON_EFFECT)
		end
```

### Player #C39: Home Run Smasher (`120205016`)

Source: [Rush/Scripts/c120205016.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120205016.lua)

```lua
	if c:IsFaceup() and c:IsRelateToEffect(e) then
		RD.AttachAtkDef(e,c,1500,0,RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
		if RD.IsLPBelow(tp,1000) then
			RD.CanSelectAndDoAction(aux.Stringid(m,1),aux.Stringid(m,2),Card.IsFaceup,tp,0,LOCATION_MZONE,1,1,nil,function(g)
				RD.AttachAtkDef(e,g:GetFirst(),-3000,0,RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
```
