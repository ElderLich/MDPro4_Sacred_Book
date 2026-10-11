# RushDuel.EnableChangeCode

Alias: `RD.EnableChangeCode`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.EnableChangeCode(any c, any code, any location, any condition) -> any
```

## Description

Rush Duel helper declared in `RDLegend.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
永续改变卡名
```

## Parameters

- `c` `any`: Type and behavior are not yet reviewed; see the source.
- `code` `any`: Type and behavior are not yet reviewed; see the source.
- `location` `any`: Type and behavior are not yet reviewed; see the source.
- `condition` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDLegend.lua:46`

```lua
function RushDuel.EnableChangeCode(c, code, location, condition)
    Auxiliary.AddCodeList(c, code)
    local loc = c:GetOriginalType() & TYPE_MONSTER ~= 0 and LOCATION_MZONE or LOCATION_SZONE
    local e1 = Effect.CreateEffect(c)
    e1:SetType(EFFECT_TYPE_SINGLE)
    e1:SetCode(EFFECT_CHANGE_CODE)
    e1:SetProperty(EFFECT_FLAG_SINGLE_RANGE)
    e1:SetRange(location or loc)
    if condition ~= nil then
        e1:SetCondition(condition)
    end
    e1:SetValue(code)
    c:RegisterEffect(e1)
    return e1
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **102** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.EnableChangeCode) with `RushDuel.EnableChangeCode`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Major Breaking News!](/examples/rush-cards/120304060) | `120304060` | [Rush/Scripts/c120304060.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304060.lua) | 1 |
| [YXZ-Cannon Dragon](/examples/rush-cards/120305004) | `120305004` | [Rush/Scripts/c120305004.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120305004.lua) | 1 |
| [Red-Eyes Mars Dragon](/examples/rush-cards/120306034) | `120306034` | [Rush/Scripts/c120306034.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120306034.lua) | 1 |
| [Botonaginata the Music Princess](/examples/rush-cards/120290009) | `120290009` | [Rush/Scripts/c120290009.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290009.lua) | 1 |
| Dark Hole Device | `120249050` | [Rush/Scripts/c120249050.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120249050.lua) | 1 |
| Super Princess of the Flock - Max Mutton \[L\] | `120293007` | [Rush/Scripts/c120293007.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120293007.lua) | 1 |
| OuTerverSe Direct Driver | `120109056` | [Rush/Scripts/c120109056.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120109056.lua) | 1 |
| Extra! Extra! Hot Off the Press | `120304049` | [Rush/Scripts/c120304049.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304049.lua) | 1 |
| OuTerverSe Burst Oblivion | `120290008` | [Rush/Scripts/c120290008.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290008.lua) | 1 |
| Etraynze the Shadow Flower Restricter | `120254041` | [Rush/Scripts/c120254041.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120254041.lua) | 1 |
| Abysskite Kaleido-Dress | `120290061` | [Rush/Scripts/c120290061.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290061.lua) | 1 |
| OuTerverSe Wish of Angeleva | `120293061` | [Rush/Scripts/c120293061.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120293061.lua) | 2 |
| OuTerverSe Wish of Devilgear | `120293062` | [Rush/Scripts/c120293062.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120293062.lua) | 2 |
| Star Sanctuary of Beginning | `120305027` | [Rush/Scripts/c120305027.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120305027.lua) | 1 |
| OuTerverSe Byugyuwazzo | `120290006` | [Rush/Scripts/c120290006.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290006.lua) | 1 |
| OuTerverSe Toxic Blob | `120290028` | [Rush/Scripts/c120290028.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290028.lua) | 1 |
| Dragon Knight of Dark | `120294009` | [Rush/Scripts/c120294009.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120294009.lua) | 1 |
| OuTerverSe Bug Fungus | `120290002` | [Rush/Scripts/c120290002.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290002.lua) | 1 |
| Skull Archfiend of Confusion | `120277023` | [Rush/Scripts/c120277023.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120277023.lua) | 1 |
| Wish of OuTerverSe the World-Shattering Emperor \[L\] | `120293058` | [Rush/Scripts/c120293058.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120293058.lua) | 1 |
| The Swordsman Who Doles Out Victory | `120290023` | [Rush/Scripts/c120290023.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290023.lua) | 1 |
| Super Princess of the Flock - Max Mutton \[R\] | `120293009` | [Rush/Scripts/c120293009.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120293009.lua) | 1 |
| Etraynze the Sprinting Shadow Flower Ninja | `120285012` | [Rush/Scripts/c120285012.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120285012.lua) | 1 |
| Abysskite Violate Halo | `120254055` | [Rush/Scripts/c120254055.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120254055.lua) | 1 |
| ...and 78 more |  |  |  |

## Script Examples

### Major Breaking News! (`120304060`)

Source: [Rush/Scripts/c120304060.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304060.lua)

```lua
	RD.AddCodeList(c,list)
	--Change Code
	RD.EnableChangeCode(c,list[1],LOCATION_GRAVE)
	--Activate
	local e1=Effect.CreateEffect(c)
```

### YXZ-Cannon Dragon (`120305004`)

Source: [Rush/Scripts/c120305004.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120305004.lua)

```lua
	RD.EnableUnionFusion(c,aux.Stringid(m,0))
	--Change Code
	RD.EnableChangeCode(c,list[4],LOCATION_EXTRA)
	--Special Summon
	local e1=Effect.CreateEffect(c)
```

### Red-Eyes Mars Dragon (`120306034`)

Source: [Rush/Scripts/c120306034.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120306034.lua)

```lua
	RD.AddCodeList(c,list)
	--Change Code
	RD.EnableChangeCode(c,list[1],LOCATION_HAND+LOCATION_GRAVE)
	--Change Code
	local e1=Effect.CreateEffect(c)
```
