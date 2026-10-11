# Auxiliary.PendOperation

## Signature

```lua
Auxiliary.PendOperation(Effect e, int tp, Group eg, int ep, int ev, Effect re, int r, int rp, Card c, Group sg, Group|nil og) -> void
```

## Description

Operation function for the shared Pendulum Summon procedure.
It chooses the regular or extra Pendulum Summon option, computes hand, Extra Deck, and total Monster Zone limits, selects a legal subgroup, updates the shared checklist or consumes the extra effect's count limit, and merges the selected cards into sg for the core group Summon path.

## Parameters

- `e` `Effect`
- `tp` `int`
- `eg` `Group`
- `ep` `int`
- `ev` `int`
- `re` `Effect`
- `r` `int`
- `rp` `int`
- `c` `Card` - Left Pendulum Zone card whose procedure is being used.
- `sg` `Group` - Core-provided group that receives the selected Pendulum Summon monsters.
- `og` `Group|nil` - Optional candidate group; nil rebuilds candidates from the player's hand and face-up Extra Deck.

## Source

- `Utilities/procedure.lua:2033`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.PendOperation) with `Auxiliary.PendOperation`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Pendulum Encore | `6992184` | [Scripts/c6992184.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6992184.lua) | 1 |

## Script Examples

### Pendulum Encore (`6992184`)

Source: [Scripts/c6992184.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6992184.lua)

```lua
	--the summon should be done after the chain end
	local sg=Group.CreateGroup()
	aux.PendOperation(e,tp,eg,ep,ev,re,r,rp,lpz,sg,g)
	Duel.RaiseEvent(sg,EVENT_SPSUMMON_SUCCESS_G_P,e,REASON_EFFECT,tp,tp,0)
	Duel.SpecialSummon(sg,SUMMON_TYPE_PENDULUM,tp,tp,true,true,POS_FACEUP)
```
