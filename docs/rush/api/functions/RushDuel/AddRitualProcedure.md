# RushDuel.AddRitualProcedure

Alias: `RD.AddRitualProcedure`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AddRitualProcedure(Card card) -> void
```

## Description

Registers the Rush Ritual monster's type-adjustment effect, removing the TYPE_FUSION compatibility bit. This helper does not create a Ritual Spell activation or summon anything; the spell uses CreateRitualEffect.

## Parameters

- `card` `Card`: Rush Ritual monster.

## Returns

No return values.

## Source

`Rush/Utilities/RDRitual.lua:32`

```lua
function RushDuel.AddRitualProcedure(card)
    if card:IsStatus(STATUS_COPYING_EFFECT) then
        return
    end
    local e = Effect.CreateEffect(card)
    e:SetType(EFFECT_TYPE_SINGLE)
    e:SetCode(EFFECT_REMOVE_TYPE)
    e:SetProperty(EFFECT_FLAG_CANNOT_DISABLE + EFFECT_FLAG_UNCOPYABLE + EFFECT_FLAG_SET_AVAILABLE)
    e:SetRange(0xff)
    e:SetValue(TYPE_FUSION)
    card:RegisterEffect(e)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **48** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.AddRitualProcedure) with `RushDuel.AddRitualProcedure`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Wako Gozen Riletta](/examples/rush-cards/120309021) | `120309021` | [Rush/Scripts/c120309021.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120309021.lua) | 1 |
| Souffraruda the Defiant Soulclad Scripture | `120298002` | [Rush/Scripts/c120298002.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120298002.lua) | 1 |
| Ever-Grace Princess Hina | `120290038` | [Rush/Scripts/c120290038.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290038.lua) | 1 |
| Reshef the Dark Being | `120306069` | [Rush/Scripts/c120306069.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120306069.lua) | 1 |
| Healthie Tigasati | `120306042` | [Rush/Scripts/c120306042.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120306042.lua) | 1 |
| Plasmatic Model Another Rising Lystella | `120290034` | [Rush/Scripts/c120290034.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290034.lua) | 1 |
| Ever-Grace Princess Mai | `120287014` | [Rush/Scripts/c120287014.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120287014.lua) | 1 |
| Twin Blaze Fiend Angel Lunael | `120287032` | [Rush/Scripts/c120287032.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120287032.lua) | 1 |
| Necromaid Re:D | `120294045` | [Rush/Scripts/c120294045.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120294045.lua) | 1 |
| Zerato, Angel of the Sanctuary | `120290035` | [Rush/Scripts/c120290035.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290035.lua) | 1 |
| Hungreed Burger | `120290033` | [Rush/Scripts/c120290033.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290033.lua) | 1 |
| Luna Moonforce Alba | `120300038` | [Rush/Scripts/c120300038.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300038.lua) | 1 |
| Yae the Secret Special Investigations Mermaid | `120306043` | [Rush/Scripts/c120306043.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120306043.lua) | 1 |
| Necromaid Lurker | `120294044` | [Rush/Scripts/c120294044.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120294044.lua) | 1 |
| Isyria, Deity of the Monumenthes | `120300037` | [Rush/Scripts/c120300037.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300037.lua) | 1 |
| Mazera, Devil of the Den | `120290036` | [Rush/Scripts/c120290036.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290036.lua) | 1 |
| Sparkhearts Passion Girl | `120298018` | [Rush/Scripts/c120298018.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120298018.lua) | 1 |
| Luna Moonforce Mochi | `120300039` | [Rush/Scripts/c120300039.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300039.lua) | 1 |
| Healthie Elizalamilla | `120306041` | [Rush/Scripts/c120306041.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120306041.lua) | 1 |
| Plasmatic Model Rising Lystella | `120285047` | [Rush/Scripts/c120285047.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120285047.lua) | 1 |
| Legendary Lineage Saber | `120285049` | [Rush/Scripts/c120285049.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120285049.lua) | 1 |
| Zera the Evil Fiend | `120287002` | [Rush/Scripts/c120287002.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120287002.lua) | 1 |
| Twin Blaze Fiend Angel Archel | `120287031` | [Rush/Scripts/c120287031.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120287031.lua) | 1 |
| Sparkhearts Passion Makma | `120298020` | [Rush/Scripts/c120298020.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120298020.lua) | 1 |
| ...and 24 more |  |  |  |

## Script Examples

### Wako Gozen Riletta (`120309021`)

Source: [Rush/Scripts/c120309021.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120309021.lua)

```lua
function cm.initial_effect(c)
	RD.AddCodeList(c,list)
	RD.AddRitualProcedure(c)
	--Destroy
	local e1=Effect.CreateEffect(c)
```

### Souffraruda the Defiant Soulclad Scripture (`120298002`)

Source: [Rush/Scripts/c120298002.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120298002.lua)

```lua
function cm.initial_effect(c)
	RD.AddCodeList(c,list)
	RD.AddRitualProcedure(c)
	--Damage
	local e1=Effect.CreateEffect(c)
```

### Ever-Grace Princess Hina (`120290038`)

Source: [Rush/Scripts/c120290038.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290038.lua)

```lua
function cm.initial_effect(c)
	RD.AddCodeList(c,list)
	RD.AddRitualProcedure(c)
	--Destroy
	local e1=Effect.CreateEffect(c)
```
