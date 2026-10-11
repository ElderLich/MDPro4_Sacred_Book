# RushDuel.IsCanChangePosition

Alias: `RD.IsCanChangePosition`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsCanChangePosition(any card, any effect, any player, any reason) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 可否改变表示形式
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `effect` `any`: Type and behavior are not yet reviewed; see the source.
- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `reason` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:111`

```lua
function RushDuel.IsCanChangePosition(card, effect, player, reason)
    if not card:IsCanChangePosition() or RushDuel.IsMaximumMode(card) then
        return false
    end
    return true
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **184** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.IsCanChangePosition) with `RushDuel.IsCanChangePosition`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Moonforce Ziggy](/examples/rush-cards/120300014) | `120300014` | [Rush/Scripts/c120300014.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300014.lua) | 1 |
| [Valkyrian Guard](/examples/rush-cards/120231066) | `120231066` | [Rush/Scripts/c120231066.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120231066.lua) | 1 |
| [Freshberry Collaboration](/examples/rush-cards/120301071) | `120301071` | [Rush/Scripts/c120301071.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120301071.lua) | 1 |
| [Fuden Issen](/examples/rush-cards/120309034) | `120309034` | [Rush/Scripts/c120309034.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120309034.lua) | 1 |
| [Sparkhearts Makma](/examples/rush-cards/120298023) | `120298023` | [Rush/Scripts/c120298023.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120298023.lua) | 1 |
| [Imaginary Arc Turbulence](/examples/rush-cards/120196013) | `120196013` | [Rush/Scripts/c120196013.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120196013.lua) | 1 |
| [Necromaid Trickment](/examples/rush-cards/120294063) | `120294063` | [Rush/Scripts/c120294063.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120294063.lua) | 1 |
| [Spice Cross Secret Recipe](/examples/rush-cards/120261060) | `120261060` | [Rush/Scripts/c120261060.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120261060.lua) | 1 |
| [Curse of the Magiclad Dragon](/examples/rush-cards/120304061) | `120304061` | [Rush/Scripts/c120304061.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304061.lua) | 1 |
| [Shannah the Clad Dragon Researcher](/examples/rush-cards/120304017) | `120304017` | [Rush/Scripts/c120304017.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304017.lua) | 1 |
| [Galactica Lost Oblivion](/examples/rush-cards/120277042) | `120277042` | [Rush/Scripts/c120277042.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120277042.lua) | 1 |
| [Heavenly Bliss](/examples/rush-cards/120203033) | `120203033` | [Rush/Scripts/c120203033.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120203033.lua) | 1 |
| [Lullalabind](/examples/rush-cards/120246073) | `120246073` | [Rush/Scripts/c120246073.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120246073.lua) | 1 |
| [Evolution Result Flash](/examples/rush-cards/120290063) | `120290063` | [Rush/Scripts/c120290063.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290063.lua) | 1 |
| [Lovely Wolf](/examples/rush-cards/120260046) | `120260046` | [Rush/Scripts/c120260046.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120260046.lua) | 1 |
| [Animagica Majesty](/examples/rush-cards/120277063) | `120277063` | [Rush/Scripts/c120277063.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120277063.lua) | 1 |
| [False Sun](/examples/rush-cards/120264033) | `120264033` | [Rush/Scripts/c120264033.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120264033.lua) | 1 |
| [Void Veil](/examples/rush-cards/120227029) | `120227029` | [Rush/Scripts/c120227029.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120227029.lua) | 1 |
| Plasmatic Model Smart Owl | `120285019` | [Rush/Scripts/c120285019.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120285019.lua) | 1 |
| Blaze Fiend Overlord Zebulth | `120287033` | [Rush/Scripts/c120287033.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120287033.lua) | 1 |
| Transam Scride | `120109036` | [Rush/Scripts/c120109036.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120109036.lua) | 1 |
| Hysteric Eyes | `120304063` | [Rush/Scripts/c120304063.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304063.lua) | 1 |
| Yamiterasu the Divine Ruler | `120199036` | [Rush/Scripts/c120199036.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120199036.lua) | 1 |
| Ether Escape | `120235062` | [Rush/Scripts/c120235062.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120235062.lua) | 1 |
| ...and 160 more |  |  |  |

## Script Examples

### Moonforce Ziggy (`120300014`)

Source: [Rush/Scripts/c120300014.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300014.lua)

```lua
--Lock Attack
function cm.costfilter(c,e,tp)
	return c:IsFaceup() and RD.IsCanChangePosition(c,e,tp,REASON_COST)
end
function cm.filter(c)
```

### Valkyrian Guard (`120231066`)

Source: [Rush/Scripts/c120231066.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120231066.lua)

```lua
end
function cm.posfilter(c,e,tp)
	return c:IsAttackPos() and RD.IsCanChangePosition(c,e,tp,REASON_EFFECT)
end
function cm.poscheck(g)
```

### Freshberry Collaboration (`120301071`)

Source: [Rush/Scripts/c120301071.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120301071.lua)

```lua
--Atk Up
function cm.filter(c,e,tp)
	return c:IsAttackPos() and RD.IsCanChangePosition(c,e,tp,REASON_EFFECT)
end
function cm.desfilter(c)
```
