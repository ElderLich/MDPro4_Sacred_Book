# RushDuel.AttachBattleRedirect

Alias: `RD.AttachBattleRedirect`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AttachBattleRedirect(any e, any card, any value, any desc, any reset, any forced) -> any
```

## Description

Rush Duel helper declared in `RDAttach.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
赋予: 战破重定向
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `value` `any`: Type and behavior are not yet reviewed; see the source.
- `desc` `any`: Type and behavior are not yet reviewed; see the source.
- `reset` `any`: Type and behavior are not yet reviewed; see the source.
- `forced` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAttach.lua:38`

```lua
function RushDuel.AttachBattleRedirect(e, card, value, desc, reset, forced)
    return RushDuel.CreateSingleEffect(e, desc, card, EFFECT_BATTLE_DESTROY_REDIRECT, value, reset, forced)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.AttachBattleRedirect) with `RushDuel.AttachBattleRedirect`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Dark Magician of Chaos | `120307001` | [Rush/Scripts/c120307001.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120307001.lua) | 1 |

## Script Examples

### Dark Magician of Chaos (`120307001`)

Source: [Rush/Scripts/c120307001.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120307001.lua)

```lua
	local c=e:GetHandler()
	if c:IsFaceup() and c:IsRelateToEffect(e) then
		RD.AttachBattleRedirect(e,c,LOCATION_DECKBOT,aux.Stringid(m,1),RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
	end
	RD.CreateCannotActivateSameCodeEffect(e,aux.Stringid(m,2),m,tp,list[1])
```
