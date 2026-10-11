# RushDuel.EnableMaximumMode

Alias: `RD.EnableMaximumMode`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.EnableMaximumMode(Card card, int reset) -> void
```

## Description

Registers an EFFECT_MAXIMUM_MODE marker with the supplied reset. It does not create components or perform a Maximum Summon by itself.

## Parameters

- `card` `Card`: Card receiving the marker.
- `reset` `int`: Reset flags for the marker effect.

## Returns

No return values.

## Source

`Rush/Utilities/RDMaximum.lua:123`

```lua
function RushDuel.EnableMaximumMode(card, reset)
    local e = Effect.CreateEffect(card)
    e:SetType(EFFECT_TYPE_SINGLE)
    e:SetCode(EFFECT_MAXIMUM_MODE)
    e:SetProperty(EFFECT_FLAG_CANNOT_DISABLE)
    e:SetRange(LOCATION_MZONE)
    e:SetReset(reset)
    card:RegisterEffect(e, true)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.EnableMaximumMode) with `RushDuel.EnableMaximumMode`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Time Machine | `120272058` | [Rush/Scripts/c120272058.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120272058.lua) | 1 |

## Script Examples

### Time Machine (`120272058`)

Source: [Rush/Scripts/c120272058.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120272058.lua)

```lua
				tc:SetMaterial(og)
				Duel.Overlay(tc,og)
				RD.EnableMaximumMode(tc,RESET_EVENT+RESETS_STANDARD)
			end
		else
```
