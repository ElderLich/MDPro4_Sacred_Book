# RushDuel.AddCodeList

Alias: `RD.AddCodeList`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AddCodeList(Card card, ... int|table) -> void
```

## Description

Accepts passcodes or flat tables of passcodes, registering each through Auxiliary.AddCodeList. This is mention metadata for other scripts; it does not create a Summon procedure or change the card's name.

## Parameters

- `card` `Card`: Card whose script mentions these passcodes.
- `...` `int|table`: Passcodes or flat tables of passcodes.

## Returns

No return values.

## Source

`Rush/Utilities/RDBase.lua:244`

```lua
function RushDuel.AddCodeList(card, ...)
    for _, list in ipairs {...} do
        local type = Auxiliary.GetValueType(list)
        if type == "number" then
            Auxiliary.AddCodeList(card, list)
        elseif type == "table" then
            Auxiliary.AddCodeList(card, table.unpack(list))
        end
    end
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **1134** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.AddCodeList) with `RushDuel.AddCodeList`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Lufer the Symbol of the Devils](/examples/rush-cards/120309059) | `120309059` | [Rush/Scripts/c120309059.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120309059.lua) | 1 |
| [The Eye of Timaeus](/examples/rush-cards/120285065) | `120285065` | [Rush/Scripts/c120285065.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120285065.lua) | 1 |
| [Valkyrian Guard](/examples/rush-cards/120231066) | `120231066` | [Rush/Scripts/c120231066.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120231066.lua) | 1 |
| [Volcalizing Salamandeus](/examples/rush-cards/120272039) | `120272039` | [Rush/Scripts/c120272039.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120272039.lua) | 1 |
| [Voidalfr Star Mayfly](/examples/rush-cards/120300034) | `120300034` | [Rush/Scripts/c120300034.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120300034.lua) | 1 |
| [Brassdes of the Wicked Wheels](/examples/rush-cards/120304033) | `120304033` | [Rush/Scripts/c120304033.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120304033.lua) | 1 |
| [Light of Bewitchment](/examples/rush-cards/120301074) | `120301074` | [Rush/Scripts/c120301074.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120301074.lua) | 1 |
| [Dark-Guiding Kuriboh](/examples/rush-cards/120280009) | `120280009` | [Rush/Scripts/c120280009.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120280009.lua) | 1 |
| [Dolphin Counterattack](/examples/rush-cards/120199058) | `120199058` | [Rush/Scripts/c120199058.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120199058.lua) | 1 |
| [Pot of Duality](/examples/rush-cards/120271002) | `120271002` | [Rush/Scripts/c120271002.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120271002.lua) | 1 |
| [Vapor Lancer the Super Graphagas](/examples/rush-cards/120260063) | `120260063` | [Rush/Scripts/c120260063.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120260063.lua) | 1 |
| [Ember the Ultra Assistant](/examples/rush-cards/120283035) | `120283035` | [Rush/Scripts/c120283035.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120283035.lua) | 1 |
| [Wako Gozen Riletta](/examples/rush-cards/120309021) | `120309021` | [Rush/Scripts/c120309021.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120309021.lua) | 1 |
| [Sparkhearts Makma](/examples/rush-cards/120298023) | `120298023` | [Rush/Scripts/c120298023.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120298023.lua) | 1 |
| [Major Breaking News!](/examples/rush-cards/120304060) | `120304060` | [Rush/Scripts/c120304060.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120304060.lua) | 1 |
| [Wish of the Skysavior](/examples/rush-cards/120253064) | `120253064` | [Rush/Scripts/c120253064.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120253064.lua) | 1 |
| [Fairy of the Stars](/examples/rush-cards/120305016) | `120305016` | [Rush/Scripts/c120305016.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120305016.lua) | 1 |
| [Rising Protect](/examples/rush-cards/120304055) | `120304055` | [Rush/Scripts/c120304055.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120304055.lua) | 1 |
| [The Black Witch Facing the Temple](/examples/rush-cards/120309048) | `120309048` | [Rush/Scripts/c120309048.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120309048.lua) | 1 |
| [Curse of the Magiclad Dragon](/examples/rush-cards/120304061) | `120304061` | [Rush/Scripts/c120304061.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120304061.lua) | 1 |
| [Insect Taurus](/examples/rush-cards/120300060) | `120300060` | [Rush/Scripts/c120300060.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120300060.lua) | 1 |
| [Jinzo the Machine Menace](/examples/rush-cards/120257028) | `120257028` | [Rush/Scripts/c120257028.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120257028.lua) | 1 |
| [Galactica Lost Oblivion](/examples/rush-cards/120277042) | `120277042` | [Rush/Scripts/c120277042.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120277042.lua) | 1 |
| [Magician's Sense](/examples/rush-cards/120246088) | `120246088` | [Rush/Scripts/c120246088.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120246088.lua) | 1 |
| ...and 1110 more |  |  |  |

## Script Examples

### Lufer the Symbol of the Devils (`120309059`)

Source: [Rush/Scripts/c120309059.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120309059.lua)

```lua
cm.name="恶魔之印 卢法"
function cm.initial_effect(c)
	RD.AddCodeList(c,list)
	--Activate
	local e1=Effect.CreateEffect(c)
```

### The Eye of Timaeus (`120285065`)

Source: [Rush/Scripts/c120285065.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120285065.lua)

```lua
cm.name="蒂迈欧之眼"
function cm.initial_effect(c)
	RD.AddCodeList(c,list)
	--Activate
	local e1=Effect.CreateEffect(c)
```

### Valkyrian Guard (`120231066`)

Source: [Rush/Scripts/c120231066.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120231066.lua)

```lua
cm.name="女武神防御"
function cm.initial_effect(c)
	RD.AddCodeList(c,list)
	--Activate
	local e1=Effect.CreateEffect(c)
```
