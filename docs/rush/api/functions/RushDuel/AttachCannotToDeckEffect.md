# RushDuel.AttachCannotToDeckEffect

Alias: `RD.AttachCannotToDeckEffect`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AttachCannotToDeckEffect(any e, any card, any value, any desc, any reset, any forced) -> any
```

## Description

Rush Duel helper declared in `RDAttach.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
赋予: 不会因效果回到手卡
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

`Rush/Utilities/RDAttach.lua:95`

```lua
function RushDuel.AttachCannotToDeckEffect(e, card, value, desc, reset, forced)
    return RushDuel.CreateSingleEffect(e, desc, card, EFFECT_CANNOT_TO_DECK_EFFECT, value, reset, forced)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.AttachCannotToDeckEffect) with `RushDuel.AttachCannotToDeckEffect`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Lufer the Symbol of the Devils](/examples/rush-cards/120309059) | `120309059` | [Rush/Scripts/c120309059.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120309059.lua) | 1 |

## Script Examples

### Lufer the Symbol of the Devils (`120309059`)

Source: [Rush/Scripts/c120309059.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120309059.lua)

```lua
			RD.AttachEffectIndes(e,tc,cm.indval,aux.Stringid(m,2),reset)
			RD.AttachCannotToHandEffect(e,tc,1,aux.Stringid(m,3),reset)
			RD.AttachCannotToDeckEffect(e,tc,1,aux.Stringid(m,4),reset)
		end)
		if Duel.IsExistingMatchingCard(cm.exfilter,tp,LOCATION_GRAVE,0,1,nil) then
```
