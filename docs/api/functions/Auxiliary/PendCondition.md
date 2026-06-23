# Auxiliary.PendCondition

## Signature

```lua
Auxiliary.PendCondition(Effect e, Card|nil c, Group|nil og) -> bool
```

## Description

Condition function for the shared Pendulum Summon procedure.
It checks the two Pendulum Zones, current scales, hand and face-up Extra Deck candidate pools, available Monster Zones, once-per-turn state, extra Pendulum Summon effects, and whether at least one candidate can be Pendulum Summoned.

## Parameters

- `e` `Effect`
- `c` `Card|nil` - Procedure handler. When nil, the helper returns true for the core's availability probe.
- `og` `Group|nil` - Optional candidate group supplied by the core or another helper; nil uses the player's hand/Extra Deck candidates.

## Returns

- `bool` - true if a Pendulum Summon is available.

## Source

- `Utilities/procedure.lua:2004`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.PendCondition`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Pendulum Encore | `6992184` | [Scripts/c6992184.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6992184.lua) | 39 |

## Script Examples

### Pendulum Encore (`6992184`)

Source: [Scripts/c6992184.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6992184.lua)

```lua
	local g=Duel.GetMatchingGroup(Card.IsType,tp,LOCATION_HAND+LOCATION_EXTRA,0,exc,TYPE_PENDULUM)
	if #g==0 then return false end
	return aux.PendCondition(e,lpz,g)
end
function c6992184.cfilter(c,e,tp)
```
