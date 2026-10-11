# RushDuel.MaximumMode

Alias: `RD.MaximumMode`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.MaximumMode(Effect e) -> bool|nil
```

## Description

Effect-condition callback: checks that the handler has EFFECT_MAXIMUM_MODE and at least one overlay component. Use RD.IsMaximumMode for a predicate receiving a Card.

## Parameters

- `e` `Effect`: Effect whose handler is checked.

## Returns

- `bool|nil`: Truthy when the Maximum marker and components are present.

## Source

`Rush/Utilities/RDMaximum.lua:133`

```lua
function RushDuel.MaximumMode(e)
    local c = e:GetHandler()
    return c:IsHasEffect(EFFECT_MAXIMUM_MODE) and c:GetOverlayCount() > 0
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **47** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.MaximumMode) with `RushDuel.MaximumMode`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Super Galaxy King Lord of Galactica \[R\]](/examples/rush-cards/120254039) | `120254039` | [Rush/Scripts/c120254039.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120254039.lua) | 1 |
| [Supreme Machine Magnum Overlord \[L\]](/examples/rush-cards/120150001) | `120150001` | [Rush/Scripts/c120150001.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120150001.lua) | 1 |
| [Supreme Machine Magnum Overlord](/examples/rush-cards/120150002) | `120150002` | [Rush/Scripts/c120150002.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120150002.lua) | 1 |
| Supreme Skystream Magnum Overlord \[L\] | `120151001` | [Rush/Scripts/c120151001.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120151001.lua) | 1 |
| Roaring Firestorm Volcalize Phoenix | `120249016` | [Rush/Scripts/c120249016.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120249016.lua) | 1 |
| OuTerverSe Wish of Angeleva | `120293061` | [Rush/Scripts/c120293061.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120293061.lua) | 1 |
| OuTerverSe Wish of Devilgear | `120293062` | [Rush/Scripts/c120293062.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120293062.lua) | 1 |
| Supreme Skystream Magnum Overlord | `120151002` | [Rush/Scripts/c120151002.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120151002.lua) | 1 |
| Wish of OuTerverSe the World-Shattering Emperor \[L\] | `120293058` | [Rush/Scripts/c120293058.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120293058.lua) | 1 |
| Wyrm Excavator the Heavy Cavalry Draco \[R\] | `120155023` | [Rush/Scripts/c120155023.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120155023.lua) | 1 |
| Shinesteel Ultra Dragon Devastar Okeabyss | `120239020` | [Rush/Scripts/c120239020.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120239020.lua) | 1 |
| Dynamic Dino Dynamix | `120151006` | [Rush/Scripts/c120151006.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120151006.lua) | 1 |
| Hyper Engine Vast Vulcan \[L\] | `120170014` | [Rush/Scripts/c120170014.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120170014.lua) | 1 |
| Hyper Engine Vast Vulcan \[R\] | `120170016` | [Rush/Scripts/c120170016.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120170016.lua) | 1 |
| Supreme Beasteam Magnum Overlord \[R\] | `120217003` | [Rush/Scripts/c120217003.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120217003.lua) | 1 |
| Red-Eyes Maxi-Flare Dragon | `120274002` | [Rush/Scripts/c120274002.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120274002.lua) | 1 |
| Supreme Skystream Magnum Overlord \[R\] | `120151003` | [Rush/Scripts/c120151003.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120151003.lua) | 1 |
| Dynamight Dino Dynamix \[L\] | `120274031` | [Rush/Scripts/c120274031.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120274031.lua) | 1 |
| Mega Multistrike Dragon Dragias Burst \[L\] | `120210001` | [Rush/Scripts/c120210001.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120210001.lua) | 1 |
| Supreme Machine Magnum Overlord \[R\] | `120150003` | [Rush/Scripts/c120150003.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120150003.lua) | 1 |
| Yggdrago the Sky Emperor \[R\] | `120150012` | [Rush/Scripts/c120150012.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120150012.lua) | 1 |
| Yggdrago the Sky Emperor \[L\] | `120150010` | [Rush/Scripts/c120150010.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120150010.lua) | 1 |
| Mega Multistrike Dragon Dragias Burst \[R\] | `120210003` | [Rush/Scripts/c120210003.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120210003.lua) | 1 |
| Abyssal Sea Dragon Abyss Kraken | `120239017` | [Rush/Scripts/c120239017.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120239017.lua) | 1 |
| ...and 23 more |  |  |  |

## Script Examples

### Super Galaxy King Lord of Galactica [R] (`120254039`)

Source: [Rush/Scripts/c120254039.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120254039.lua)

```lua
	e1:SetRange(LOCATION_MZONE)
	e1:SetLabel(m)
	e1:SetCondition(RD.MaximumMode)
	e1:SetTarget(cm.target)
	e1:SetOperation(cm.operation)
```

### Supreme Machine Magnum Overlord [L] (`120150001`)

Source: [Rush/Scripts/c120150001.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120150001.lua)

```lua
--Atk Up
function cm.condition(e,tp,eg,ep,ev,re,r,rp)
	return RD.MaximumMode(e) and RD.IsLPBelowOpponent(tp,1)
end
cm.cost=RD.CostSendHandToGrave(Card.IsAbleToGraveAsCost,1,1)
```

### Supreme Machine Magnum Overlord (`120150002`)

Source: [Rush/Scripts/c120150002.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120150002.lua)

```lua
	e1:SetProperty(EFFECT_FLAG_SINGLE_RANGE)
	e1:SetRange(LOCATION_MZONE)
	e1:SetCondition(RD.MaximumMode)
	e1:SetValue(cm.indval)
	c:RegisterEffect(e1)
```
