# RushDuel.RegisterEquipEffect

Alias: `RD.RegisterEquipEffect`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.RegisterEquipEffect(Card card, function|nil condition, function|nil cost, function target, int|nil property) -> Effect
```

## Description

Registers a Rush Equip Spell activation and its equip limit. The target argument is a card predicate; this implementation chooses the monster during resolution. Returns the activation Effect for further configuration.

## Parameters

- `card` `Card`: Equip Spell.
- `condition` `function|nil`: Activation condition, or nil.
- `cost` `function|nil`: Cost callback, or nil.
- `target` `function`: Predicate receiving card, effect, player and a legality-check flag.
- `property` `int|nil`: Optional activation property flags.

## Returns

- `Effect`: Registered activation Effect.

## Source

`Rush/Utilities/RDEquip.lua:5`

```lua
function RushDuel.RegisterEquipEffect(card, condition, cost, target, property)
    -- Activate
    local e1 = Effect.CreateEffect(card)
    e1:SetCategory(CATEGORY_EQUIP)
    e1:SetType(EFFECT_TYPE_ACTIVATE)
    e1:SetCode(EVENT_FREE_CHAIN)
    if property ~= nil then
        e1:SetProperty(property)
    end
    if condition ~= nil then
        e1:SetCondition(condition)
    end
    if cost ~= nil then
        e1:SetCost(cost)
    end
    e1:SetTarget(RushDuel.EquipTarget(target))
    e1:SetOperation(RushDuel.EquipOperation(target))
    card:RegisterEffect(e1)
    -- Equip Limit
    local e2 = Effect.CreateEffect(card)
    e2:SetType(EFFECT_TYPE_SINGLE)
    e2:SetCode(EFFECT_EQUIP_LIMIT)
    e2:SetProperty(EFFECT_FLAG_CANNOT_DISABLE)
    e2:SetValue(RushDuel.EquipFilter(target))
    card:RegisterEffect(e2)
    return e1
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **49** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.RegisterEquipEffect) with `RushDuel.RegisterEquipEffect`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Abysskite Violate Halo | `120254055` | [Rush/Scripts/c120254055.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120254055.lua) | 1 |
| The Battle Bump | `120293075` | [Rush/Scripts/c120293075.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120293075.lua) | 1 |
| Lovely Blessing | `120260051` | [Rush/Scripts/c120260051.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120260051.lua) | 1 |
| Dyna Body Heat | `120274050` | [Rush/Scripts/c120274050.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120274050.lua) | 1 |
| Celeb Blade - Death Wild | `120254086` | [Rush/Scripts/c120254086.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120254086.lua) | 1 |
| Voidvelg Shroud | `120244051` | [Rush/Scripts/c120244051.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120244051.lua) | 1 |
| Aura Buster | `120249051` | [Rush/Scripts/c120249051.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120249051.lua) | 1 |
| Voidvelg Phalanx | `120235044` | [Rush/Scripts/c120235044.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120235044.lua) | 1 |
| Harpie's Electro Shield | `120247012` | [Rush/Scripts/c120247012.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120247012.lua) | 1 |
| The Sword of Zera | `120287010` | [Rush/Scripts/c120287010.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120287010.lua) | 1 |
| Road Arms - Sevens Lance | `120228050` | [Rush/Scripts/c120228050.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120228050.lua) | 1 |
| Cracking Claw | `120235043` | [Rush/Scripts/c120235043.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120235043.lua) | 1 |
| Qwerty Keyblade | `120228042` | [Rush/Scripts/c120228042.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120228042.lua) | 1 |
| Galactica Xiphos | `120228040` | [Rush/Scripts/c120228040.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120228040.lua) | 1 |
| Ancient Gear Change | `120271013` | [Rush/Scripts/c120271013.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120271013.lua) | 1 |
| Fiery Arms - Fretberge | `120228051` | [Rush/Scripts/c120228051.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120228051.lua) | 1 |
| Celeb Blouse - Death One Shoulder | `120290044` | [Rush/Scripts/c120290044.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290044.lua) | 1 |
| Celeb Robe - Death Wind | `120254087` | [Rush/Scripts/c120254087.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120254087.lua) | 1 |
| Road Arms - Sword Breaker | `120235045` | [Rush/Scripts/c120235045.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120235045.lua) | 1 |
| Destructor Claw Shield | `120247052` | [Rush/Scripts/c120247052.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120247052.lua) | 1 |
| Meteor Dragon's Nails | `120253058` | [Rush/Scripts/c120253058.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120253058.lua) | 1 |
| Helmet of the Master Craftsman | `120238045` | [Rush/Scripts/c120238045.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120238045.lua) | 1 |
| Plasmatic Model Maintenance | `120285056` | [Rush/Scripts/c120285056.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120285056.lua) | 1 |
| Chemicalize Volshield | `120272050` | [Rush/Scripts/c120272050.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120272050.lua) | 1 |
| ...and 25 more |  |  |  |

## Script Examples

### Abysskite Violate Halo (`120254055`)

Source: [Rush/Scripts/c120254055.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120254055.lua)

```lua
	RD.EnableChangeCode(c,list[1],LOCATION_GRAVE)
	--Activate
	RD.RegisterEquipEffect(c,nil,nil,cm.target)
	--Pierce
	local e1=Effect.CreateEffect(c)
```

### The Battle Bump (`120293075`)

Source: [Rush/Scripts/c120293075.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120293075.lua)

```lua
function cm.initial_effect(c)
	--Activate
	RD.RegisterEquipEffect(c,nil,nil,cm.target)
	--Atk Up
	local e1=Effect.CreateEffect(c)
```

### Lovely Blessing (`120260051`)

Source: [Rush/Scripts/c120260051.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120260051.lua)

```lua
function cm.initial_effect(c)
	--Activate
	RD.RegisterEquipEffect(c,nil,nil,cm.target)
	--Indes
	local e1=Effect.CreateEffect(c)
```
