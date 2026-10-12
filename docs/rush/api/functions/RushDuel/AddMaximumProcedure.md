# RushDuel.AddMaximumProcedure

Alias: `RD.AddMaximumProcedure`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AddMaximumProcedure(Card card, int max_atk, int left_code, int right_code) -> void
```

## Description

Registers the center monster's Maximum Summon procedure, Maximum ATK and zone-limit effect. left_code and right_code identify the two components selected from hand. The pinned implementation stores components as overlays; use the matching Rush helpers when moving a Maximum monster.

## Parameters

- `card` `Card`: Center Maximum monster.
- `max_atk` `int`: ATK while in Maximum mode.
- `left_code` `int`: Left component passcode.
- `right_code` `int`: Right component passcode.

## Returns

No return values.

## Example

```lua
-- Inside the center card's initial_effect:
RD.AddMaximumProcedure(c, 4000, 120150001, 120150003)
```

## Source

`Rush/Utilities/RDMaximum.lua:37`

```lua
function RushDuel.AddMaximumProcedure(card, max_atk, left_code, right_code)
    if card:IsStatus(STATUS_COPYING_EFFECT) then
        return
    end
    -- 记录状态
    if card.maximum_attack == nil then
        local mt = getmetatable(card)
        mt.maximum_attack = max_atk
    end
    -- 极大召唤 手续
    RushDuel.AddHandSpecialSummonProcedure(card, HINTMSG_MAXSUMMON, RushDuel.MaximumSummonCondition(left_code, right_code), RushDuel.MaximumSummonTarget(left_code, right_code),
        RushDuel.MaximumSummonOperation(left_code, right_code), RushDuel.MaximumSummonValue, POS_FACEUP_ATTACK)
    -- 极大攻击力
    local e1 = Effect.CreateEffect(card)
    e1:SetType(EFFECT_TYPE_SINGLE)
    e1:SetCode(EFFECT_SET_BASE_ATTACK)
    e1:SetProperty(EFFECT_FLAG_SINGLE_RANGE + EFFECT_FLAG_CANNOT_DISABLE + EFFECT_FLAG_UNCOPYABLE)
    e1:SetRange(LOCATION_MZONE)
    e1:SetCondition(RushDuel.MaximumMode)
    e1:SetValue(max_atk)
    card:RegisterEffect(e1)
    -- 占用3个主要怪兽区域
    local e2 = Effect.CreateEffect(card)
    e2:SetType(EFFECT_TYPE_FIELD)
    e2:SetCode(EFFECT_MAX_MZONE)
    e2:SetProperty(EFFECT_FLAG_PLAYER_TARGET + EFFECT_FLAG_CANNOT_DISABLE + EFFECT_FLAG_UNCOPYABLE)
    e2:SetRange(LOCATION_MZONE)
    e2:SetTargetRange(1, 0)
    e2:SetCondition(RushDuel.MaximumMode)
    e2:SetValue(1)
    card:RegisterEffect(e2)
end
```

## Guided Examples

Learn how to use this function in context:

- [Rush Maximum, Fusion, And Ritual](/learn/rush-summon-procedures)

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **23** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.AddMaximumProcedure) with `RushDuel.AddMaximumProcedure`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Supreme Machine Magnum Overlord](/examples/rush-cards/120150002) | `120150002` | [Rush/Scripts/c120150002.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120150002.lua) | 1 |
| Roaring Firestorm Volcalize Phoenix | `120249016` | [Rush/Scripts/c120249016.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120249016.lua) | 1 |
| Super Galaxy King Lord of Galactica | `120254038` | [Rush/Scripts/c120254038.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120254038.lua) | 1 |
| Harpie Lady Sisters | `120247002` | [Rush/Scripts/c120247002.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120247002.lua) | 1 |
| Supreme Skystream Magnum Overlord | `120151002` | [Rush/Scripts/c120151002.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120151002.lua) | 1 |
| Shinesteel Ultra Dragon Devastar Okeabyss | `120239020` | [Rush/Scripts/c120239020.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120239020.lua) | 1 |
| Dynamic Dino Dynamix | `120151006` | [Rush/Scripts/c120151006.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120151006.lua) | 1 |
| Super Princess of the Flock - Max Mutton | `120293008` | [Rush/Scripts/c120293008.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120293008.lua) | 1 |
| Doomblaze Fiend Overlord Despairacion | `120231008` | [Rush/Scripts/c120231008.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120231008.lua) | 1 |
| Red-Eyes Maxi-Flare Dragon | `120274002` | [Rush/Scripts/c120274002.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120274002.lua) | 1 |
| Supreme Railartillery Magnum Overlord | `120239002` | [Rush/Scripts/c120239002.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120239002.lua) | 1 |
| Reporter Wars Scoopies | `120304008` | [Rush/Scripts/c120304008.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120304008.lua) | 1 |
| Abyssal Sea Dragon Abyss Kraken | `120239017` | [Rush/Scripts/c120239017.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120239017.lua) | 1 |
| Wish of OuTerverSe the World-Shattering Emperor | `120293059` | [Rush/Scripts/c120293059.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120293059.lua) | 1 |
| Abyssal Dragon Lord Abyss Poseidra | `120239014` | [Rush/Scripts/c120239014.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120239014.lua) | 1 |
| Mega Jointech Fortrex | `120249004` | [Rush/Scripts/c120249004.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120249004.lua) | 1 |
| Maximum Gadget the Moving Fortress | `120272016` | [Rush/Scripts/c120272016.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120272016.lua) | 1 |
| Blaze Fiend Overlords Beelucitaroth | `120231011` | [Rush/Scripts/c120231011.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120231011.lua) | 1 |
| Wyrm Excavator the Heavy Cavalry Draco | `120155022` | [Rush/Scripts/c120155022.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120155022.lua) | 1 |
| Mega Multistrike Dragon Dragias Burst | `120210002` | [Rush/Scripts/c120210002.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120210002.lua) | 1 |
| Supreme Beasteam Magnum Overlord | `120217002` | [Rush/Scripts/c120217002.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120217002.lua) | 1 |
| Hyper Engine Vast Vulcan | `120170015` | [Rush/Scripts/c120170015.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120170015.lua) | 1 |
| Yggdrago the Sky Emperor | `120150011` | [Rush/Scripts/c120150011.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120150011.lua) | 1 |

## Script Examples

### Supreme Machine Magnum Overlord (`120150002`)

Source: [Rush/Scripts/c120150002.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120150002.lua)

```lua
	RD.AddCodeList(c,list)
	--Maximum Summon
	RD.AddMaximumProcedure(c,3500,list[1],list[2])
	--Indes
	local e1=Effect.CreateEffect(c)
```

### Roaring Firestorm Volcalize Phoenix (`120249016`)

Source: [Rush/Scripts/c120249016.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120249016.lua)

```lua
	RD.AddCodeList(c,list)
	--Maximum Summon
	RD.AddMaximumProcedure(c,3500,list[1],list[2])
	--Damage
	local e1=Effect.CreateEffect(c)
```

### Super Galaxy King Lord of Galactica (`120254038`)

Source: [Rush/Scripts/c120254038.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120254038.lua)

```lua
	RD.AddCodeList(c,list)
	--Maximum Summon
	RD.AddMaximumProcedure(c,4000,list[1],list[2])
	--Tribute
	RD.CreateAdvanceCheck(c,cm.tricheck,1,20254038)
```
