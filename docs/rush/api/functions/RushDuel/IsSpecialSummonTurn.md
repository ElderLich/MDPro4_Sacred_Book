# RushDuel.IsSpecialSummonTurn

Alias: `RD.IsSpecialSummonTurn`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsSpecialSummonTurn(Card card) -> bool
```

## Description

Checks REASON_SPSUMMON, STATUS_SPSUMMON_TURN and the Rush FLAG_SUMMON_TURN marker. The Rush bootstrap installs the tracking effects required by this predicate.

## Parameters

- `card` `Card`: Card to inspect.

## Returns

- `bool`: Whether the card satisfies the current-turn Special Summon checks.

## Source

`Rush/Utilities/RDCondition.lua:38`

```lua
function RushDuel.IsSpecialSummonTurn(card)
    return card:IsReason(REASON_SPSUMMON) and card:IsStatus(STATUS_SPSUMMON_TURN) and card:GetFlagEffect(FLAG_SUMMON_TURN) ~= 0
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.IsSpecialSummonTurn) with `RushDuel.IsSpecialSummonTurn`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Jointech Tridynabase | `120257041` | [Rush/Scripts/c120257041.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120257041.lua) | 1 |

## Script Examples

### Jointech Tridynabase (`120257041`)

Source: [Rush/Scripts/c120257041.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120257041.lua)

```lua
function cm.atkcon(e)
	local c=e:GetHandler()
	return RD.IsSpecialSummonTurn(c) and c:GetFlagEffect(20257041)~=0
end
--Fusion Success
```
