# RushDuel.IsPreviousMaximumMode

Alias: `RD.IsPreviousMaximumMode`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsPreviousMaximumMode(Card card) -> bool
```

## Description

Checks the Maximum type bit, Maximum Summon type and previous on-field overlay count. Use when an effect needs to know that components were attached before the card left the field.

## Parameters

- `card` `Card`: Card to inspect.

## Returns

- `bool`: Whether the previous-Maximum check passes.

## Source

`Rush/Utilities/RDCondition.lua:17`

```lua
function RushDuel.IsPreviousMaximumMode(card)
    return card:IsType(TYPE_MAXIMUM) and card:IsSummonType(SUMMON_TYPE_MAXIMUM) and card:GetPreviousOverlayCountOnField()>0
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **2** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.IsPreviousMaximumMode) with `RushDuel.IsPreviousMaximumMode`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Time Machine | `120272058` | [Rush/Scripts/c120272058.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120272058.lua) | 1 |
| Altar of the Twin Blaze Fiends | `120287036` | [Rush/Scripts/c120287036.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120287036.lua) | 1 |

## Script Examples

### Time Machine (`120272058`)

Source: [Rush/Scripts/c120272058.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120272058.lua)

```lua
		and tc:IsCanBeSpecialSummoned(e,0,tp,false,false,tc:GetPreviousPosition(),tc:GetPreviousControler()) end
	tc:CreateEffectRelation(e)
	if RD.IsPreviousMaximumMode(tc) then
		e:SetLabel(1)
	else
```

### Altar of the Twin Blaze Fiends (`120287036`)

Source: [Rush/Scripts/c120287036.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120287036.lua)

```lua
end
function cm.exfilter(c)
	return RD.IsPreviousMaximumMode(c)
end
function cm.operation(e,tp,eg,ep,ev,re,r,rp,mat,rc)
```
