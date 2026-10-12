# Auxiliary.PendOperationCheck

## Signature

```lua
Auxiliary.PendOperationCheck(int ft1, int ft2, int ft) -> function
```

## Description

Returns a group check that enforces the hand, Extra Deck, and total Monster Zone limits for a Pendulum Summon selection.
The returned function counts selected Extra Deck cards separately from non-Extra Deck cards before accepting the subgroup.

## Parameters

- `ft1` `int` - Maximum selected monsters from non-Extra Deck locations, usually the hand.
- `ft2` `int` - Maximum selected monsters from the face-up Extra Deck.
- `ft` `int` - Maximum total selected monsters.

## Returns

- `function` - Group check for Pendulum Summon zone limits.

## Source

- `Utilities/procedure.lua:2026`

## Guided Examples

Learn how to use this function in context:

- [Pendulum Procedure Guide](/learn/pendulum-procedure)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.PendOperationCheck) with `Auxiliary.PendOperationCheck`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Pendulum Evolution](/examples/cards/55795155) | `55795155` | [Scripts/c55795155.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c55795155.lua) | 1 |

## Script Examples

### Pendulum Evolution (`55795155`)

Source: [Scripts/c55795155.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c55795155.lua)

```lua
	tg=tg:Filter(aux.PConditionExtraFilterSpecific,nil,e,tp,lscale,rscale,e1)
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SPSUMMON)
	aux.GCheckAdditional=aux.PendOperationCheck(ft1,ft2,ft)
	local g=tg:SelectSubGroup(tp,aux.TRUE,false,1,math.min(#tg,ft))
	aux.GCheckAdditional=nil
```
