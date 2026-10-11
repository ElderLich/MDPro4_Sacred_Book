# RushDuel.IsMainPhase

Alias: `RD.IsMainPhase`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsMainPhase() -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 玩家的主要阶段
```

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:21`

```lua
function RushDuel.IsMainPhase()
    local player = Duel.GetTurnPlayer()
    if Duel.GetFlagEffect(player, FLAG_SKIP_MAIN_PHASE) ~= 0 then
        return false
    end
    local ph = Duel.GetCurrentPhase()
    return ph == PHASE_MAIN1 or ph == PHASE_MAIN2
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **4** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.IsMainPhase) with `RushDuel.IsMainPhase`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Major Breaking News!](/examples/rush-cards/120304060) | `120304060` | [Rush/Scripts/c120304060.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304060.lua) | 1 |
| Amusi Annoyance | `120249063` | [Rush/Scripts/c120249063.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120249063.lua) | 1 |
| It's Right Behind You! | `120217084` | [Rush/Scripts/c120217084.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120217084.lua) | 1 |
| Traditional Tax | `120235063` | [Rush/Scripts/c120235063.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120235063.lua) | 1 |

## Script Examples

### Major Breaking News! (`120304060`)

Source: [Rush/Scripts/c120304060.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304060.lua)

```lua
function cm.event(e,tp,eg,ep,ev,re,r,rp)
	local g=eg:Filter(Card.IsPreviousLocation,nil,LOCATION_DECK)
	if RD.IsMainPhase() then
		Duel.RaiseEvent(eg,EVENT_CUSTOM+m,re,r,rp,ep,g:GetCount())
	end
```

### Amusi Annoyance (`120249063`)

Source: [Rush/Scripts/c120249063.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120249063.lua)

```lua
function cm.event(e,tp,eg,ep,ev,re,r,rp)
	local g=eg:Filter(Card.IsPreviousLocation,nil,LOCATION_DECK)
	if RD.IsMainPhase() then
		Duel.RaiseEvent(eg,EVENT_CUSTOM+m,re,r,rp,ep,g:GetCount())
	end
```

### It's Right Behind You! (`120217084`)

Source: [Rush/Scripts/c120217084.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120217084.lua)

```lua
function cm.condition(e,tp,eg,ep,ev,re,r,rp)
	local phase=Duel.GetCurrentPhase()
	return ep~=tp and (phase==PHASE_DRAW or RD.IsMainPhase())
end
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
```
