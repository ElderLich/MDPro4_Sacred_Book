# RushDuel.IsDefense

Alias: `RD.IsDefense`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsDefense(any card, any def) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 守备力为 def
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `def` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:91`

```lua
function RushDuel.IsDefense(card, def)
    return card:IsDefense(def) and not RushDuel.IsMaximumMode(card)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **190** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.IsDefense) with `RushDuel.IsDefense`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Nativity of the Monarchs](/examples/rush-cards/120244063) | `120244063` | [Rush/Scripts/c120244063.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120244063.lua) | 1 |
| [Dark-Guiding Kuriboh](/examples/rush-cards/120280009) | `120280009` | [Rush/Scripts/c120280009.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120280009.lua) | 1 |
| [Miracle Pick](/examples/rush-cards/120253052) | `120253052` | [Rush/Scripts/c120253052.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120253052.lua) | 1 |
| [Imaginary Arc Turbulence](/examples/rush-cards/120196013) | `120196013` | [Rush/Scripts/c120196013.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120196013.lua) | 1 |
| [Rising Protect](/examples/rush-cards/120304055) | `120304055` | [Rush/Scripts/c120304055.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120304055.lua) | 1 |
| [Shannah the Clad Dragon Researcher](/examples/rush-cards/120304017) | `120304017` | [Rush/Scripts/c120304017.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120304017.lua) | 1 |
| [Spiritualization Training](/examples/rush-cards/120301020) | `120301020` | [Rush/Scripts/c120301020.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120301020.lua) | 2 |
| [Star Protector Recapture](/examples/rush-cards/120306063) | `120306063` | [Rush/Scripts/c120306063.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306063.lua) | 2 |
| [Devil Foolish](/examples/rush-cards/120244026) | `120244026` | [Rush/Scripts/c120244026.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120244026.lua) | 2 |
| [Ecliceras Drakon](/examples/rush-cards/120109033) | `120109033` | [Rush/Scripts/c120109033.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120109033.lua) | 1 |
| [Star Cat Destronya](/examples/rush-cards/120235037) | `120235037` | [Rush/Scripts/c120235037.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120235037.lua) | 2 |
| Plasmatic Model Smart Owl | `120285019` | [Rush/Scripts/c120285019.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120285019.lua) | 1 |
| Abysskite Liem | `120249025` | [Rush/Scripts/c120249025.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120249025.lua) | 1 |
| Cosmostar the White Hole Polairy | `120293045` | [Rush/Scripts/c120293045.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120293045.lua) | 2 |
| Plasmatic Model Tool Ceto | `120301069` | [Rush/Scripts/c120301069.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120301069.lua) | 1 |
| Rising HERO Argent O | `120304042` | [Rush/Scripts/c120304042.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120304042.lua) | 1 |
| Intercepting Gaia | `120249061` | [Rush/Scripts/c120249061.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120249061.lua) | 1 |
| Under Dealer | `120290015` | [Rush/Scripts/c120290015.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120290015.lua) | 1 |
| Reborn Pattern | `120294064` | [Rush/Scripts/c120294064.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120294064.lua) | 1 |
| Despair and Desire | `120301034` | [Rush/Scripts/c120301034.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120301034.lua) | 1 |
| Speed Commander | `120301058` | [Rush/Scripts/c120301058.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120301058.lua) | 1 |
| Executie Emergency! | `120231040` | [Rush/Scripts/c120231040.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120231040.lua) | 1 |
| Lily's Syringe | `120272053` | [Rush/Scripts/c120272053.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120272053.lua) | 1 |
| Imaginary Leading Actor | `120271029` | [Rush/Scripts/c120271029.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120271029.lua) | 1 |
| ...and 166 more |  |  |  |

## Script Examples

### Nativity of the Monarchs (`120244063`)

Source: [Rush/Scripts/c120244063.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120244063.lua)

```lua
end
function cm.spfilter(c,e,tp)
	return c:IsLevelAbove(5) and RD.IsDefense(c,1000) and RD.IsCanBeSpecialSummoned(c,e,tp,POS_FACEUP_ATTACK)
end
function cm.condition(e,tp,eg,ep,ev,re,r,rp)
```

### Dark-Guiding Kuriboh (`120280009`)

Source: [Rush/Scripts/c120280009.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120280009.lua)

```lua
end
function cm.spfilter(c,e,tp)
	return (c:IsCode(list[1]) or (c:IsLevel(7) and RD.IsDefense(c,2100)))
		and RD.IsCanBeSpecialSummoned(c,e,tp,POS_FACEDOWN_DEFENSE)
end
```

### Miracle Pick (`120253052`)

Source: [Rush/Scripts/c120253052.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120253052.lua)

```lua
--Activate
function cm.costfilter(c,e,tp)
	return not c:IsPublic() and c:IsLevel(7) and c:IsAttribute(ATTRIBUTE_LIGHT+ATTRIBUTE_DARK) and c:IsRace(RACE_PSYCHO) and RD.IsDefense(c,0)
end
cm.cost=RD.CostShowHand(cm.costfilter,1,1)
```
