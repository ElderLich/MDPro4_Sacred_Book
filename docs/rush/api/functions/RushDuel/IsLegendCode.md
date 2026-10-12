# RushDuel.IsLegendCode

Alias: `RD.IsLegendCode`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsLegendCode(any card, ... any) -> any
```

## Description

Rush Duel helper declared in `RDLegend.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 是否为传说卡的卡名
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `...` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDLegend.lua:31`

```lua
function RushDuel.IsLegendCode(card, ...)
    return card:IsCode(table.unpack({...}))
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **54** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.IsLegendCode) with `RushDuel.IsLegendCode`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [The Eye of Timaeus](/examples/rush-cards/120285065) | `120285065` | [Rush/Scripts/c120285065.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120285065.lua) | 2 |
| [Jinzo the Machine Menace](/examples/rush-cards/120257028) | `120257028` | [Rush/Scripts/c120257028.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120257028.lua) | 1 |
| Fusionic Revivern | `120109030` | [Rush/Scripts/c120109030.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120109030.lua) | 1 |
| Treasure of Eyes of Blue | `120252035` | [Rush/Scripts/c120252035.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120252035.lua) | 1 |
| Masenkou, the Lashing Light | `120238044` | [Rush/Scripts/c120238044.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120238044.lua) | 1 |
| The Swordsman Who Doles Out Victory | `120290023` | [Rush/Scripts/c120290023.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120290023.lua) | 1 |
| Maraimei, the Igniting Inferno | `120170063` | [Rush/Scripts/c120170063.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120170063.lua) | 1 |
| Jointech Arcscorpio | `120249006` | [Rush/Scripts/c120249006.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120249006.lua) | 1 |
| Unfulfilled Goblin | `120203039` | [Rush/Scripts/c120203039.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120203039.lua) | 1 |
| Imaginary Reactor | `120271025` | [Rush/Scripts/c120271025.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120271025.lua) | 1 |
| Voidvelg Apocalypse | `120231047` | [Rush/Scripts/c120231047.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120231047.lua) | 1 |
| Black Dragon's Roar | `120203053` | [Rush/Scripts/c120203053.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120203053.lua) | 1 |
| Hyper Ritzy King Rex | `120196037` | [Rush/Scripts/c120196037.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120196037.lua) | 1 |
| Progress Potter | `120217035` | [Rush/Scripts/c120217035.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120217035.lua) | 1 |
| Malevolent Seller | `120238040` | [Rush/Scripts/c120238040.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120238040.lua) | 1 |
| Sword &amp; Shield | `120155052` | [Rush/Scripts/c120155052.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120155052.lua) | 1 |
| Shield in the Right Hand | `120246048` | [Rush/Scripts/c120246048.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120246048.lua) | 2 |
| Makiu, the Magical Mist | `120205058` | [Rush/Scripts/c120205058.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120205058.lua) | 1 |
| Dark Magician's Curtain | `120238012` | [Rush/Scripts/c120238012.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120238012.lua) | 1 |
| Archfiend's Revival | `120170062` | [Rush/Scripts/c120170062.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120170062.lua) | 1 |
| Upgrade Goblin | `120151048` | [Rush/Scripts/c120151048.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120151048.lua) | 1 |
| Engine of Destruction | `120254021` | [Rush/Scripts/c120254021.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120254021.lua) | 1 |
| Voidvelg Protostar | `120235033` | [Rush/Scripts/c120235033.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120235033.lua) | 1 |
| Wizened Dark Magician | `120246082` | [Rush/Scripts/c120246082.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120246082.lua) | 1 |
| ...and 30 more |  |  |  |

## Script Examples

### The Eye of Timaeus (`120285065`)

Source: [Rush/Scripts/c120285065.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120285065.lua)

```lua
--Activate
function cm.matfilter1(c,e,tp)
	return c:IsFaceup() and RD.IsLegendCode(c,list[2]) and c:IsCanBeFusionMaterial()
		and not c:IsImmuneToEffect(e) and aux.MustMaterialCheck(c,tp,EFFECT_MUST_BE_FMATERIAL)
end
```

### Jinzo the Machine Menace (`120257028`)

Source: [Rush/Scripts/c120257028.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120257028.lua)

```lua
--Special Summon
function cm.spfilter(c,e,tp)
	return RD.IsLegendCode(c,list[1]) and RD.IsCanBeSpecialSummoned(c,e,tp,POS_FACEUP)
end
function cm.exfilter(c)
```

### Fusionic Revivern (`120109030`)

Source: [Rush/Scripts/c120109030.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120109030.lua)

```lua
end
function cm.thfilter(c)
	return (c:IsCode(list[1]) or RD.IsLegendCode(c,list[2])) and c:IsAbleToHand()
end
function cm.condition(e,tp,eg,ep,ev,re,r,rp)
```
