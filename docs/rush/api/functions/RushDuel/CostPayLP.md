# RushDuel.CostPayLP

Alias: `RD.CostPayLP`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CostPayLP(int lp) -> function
```

## Description

Returns a cost callback that checks Duel.CheckLPCost during chk==0, then pays the specified LP when the cost is performed.

## Parameters

- `lp` `int`: LP to pay.

## Returns

- `function`: Cost callback for Effect.SetCost.

## Example

```lua
e1:SetCost(RD.CostPayLP(1000))
```

## Source

`Rush/Utilities/RDCost.lua:196`

```lua
function RushDuel.CostPayLP(lp)
    return function(e, tp, eg, ep, ev, re, r, rp, chk)
        if chk == 0 then
            return Duel.CheckLPCost(tp, lp)
        end
        Duel.PayLPCost(tp, lp)
        return true
    end
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **97** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CostPayLP) with `RushDuel.CostPayLP`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Chaos Emperor Dragon - Envoy of the End](/examples/rush-cards/120305001) | `120305001` | [Rush/Scripts/c120305001.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120305001.lua) | 1 |
| [Magical Retribution](/examples/rush-cards/120254028) | `120254028` | [Rush/Scripts/c120254028.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120254028.lua) | 1 |
| Instant Fusion | `120305053` | [Rush/Scripts/c120305053.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120305053.lua) | 1 |
| Prophecy Phrase the Colors of the Wind | `120228024` | [Rush/Scripts/c120228024.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120228024.lua) | 1 |
| Lovely Ange | `120272026` | [Rush/Scripts/c120272026.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120272026.lua) | 1 |
| Pirate of the Apport Winds | `120228025` | [Rush/Scripts/c120228025.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120228025.lua) | 1 |
| Beast Gear Sage Roller Stag | `120222033` | [Rush/Scripts/c120222033.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120222033.lua) | 1 |
| Back Jersey | `120228063` | [Rush/Scripts/c120228063.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120228063.lua) | 1 |
| Bandijo the Battle Ballad | `120228026` | [Rush/Scripts/c120228026.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120228026.lua) | 1 |
| CAN - Eb:D | `120283034` | [Rush/Scripts/c120283034.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120283034.lua) | 1 |
| Vic Viper Beginning | `120294026` | [Rush/Scripts/c120294026.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120294026.lua) | 1 |
| Worker Warrior - Sinister Chairman | `120196038` | [Rush/Scripts/c120196038.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120196038.lua) | 1 |
| Dragon Knight of Dark | `120294009` | [Rush/Scripts/c120294009.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120294009.lua) | 1 |
| Surtr the Brilliant Magical Sword | `120306100` | [Rush/Scripts/c120306100.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306100.lua) | 1 |
| Bowing Brotherhood | `120188027` | [Rush/Scripts/c120188027.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120188027.lua) | 1 |
| Prime Bandijo | `120257006` | [Rush/Scripts/c120257006.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120257006.lua) | 1 |
| Prime Bandijo | `120273003` | [Rush/Scripts/c120273003.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120273003.lua) | 1 |
| Supreme Dog Ropero | `120239022` | [Rush/Scripts/c120239022.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120239022.lua) | 1 |
| Awakened Stegoceratops | `120277018` | [Rush/Scripts/c120277018.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120277018.lua) | 1 |
| Seraph of Darkness | `120228030` | [Rush/Scripts/c120228030.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120228030.lua) | 1 |
| Shinesteel Ultra Dragon Devastar Okeabyss \[L\] | `120239019` | [Rush/Scripts/c120239019.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120239019.lua) | 1 |
| Animal Doctor Lily | `120272022` | [Rush/Scripts/c120272022.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120272022.lua) | 1 |
| Agent Mislead | `120249021` | [Rush/Scripts/c120249021.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120249021.lua) | 1 |
| Shaman Octopus | `120130034` | [Rush/Scripts/c120130034.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120130034.lua) | 1 |
| ...and 73 more |  |  |  |

## Script Examples

### Chaos Emperor Dragon - Envoy of the End (`120305001`)

Source: [Rush/Scripts/c120305001.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120305001.lua)

```lua
		and Duel.GetCustomActivityCount(m,tp,ACTIVITY_CHAIN)==0
end
cm.cost=RD.CostPayLP(1000)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsExistingMatchingCard(cm.filter,tp,LOCATION_HAND+LOCATION_ONFIELD,LOCATION_HAND+LOCATION_ONFIELD,1,nil) end
```

### Magical Retribution (`120254028`)

Source: [Rush/Scripts/c120254028.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120254028.lua)

```lua
	return eg:IsExists(cm.confilter,1,nil,tp,rp)
end
cm.cost=RD.CostPayLP(800)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsExistingMatchingCard(cm.desfilter,tp,0,LOCATION_ONFIELD,1,nil) end
```

### Instant Fusion (`120305053`)

Source: [Rush/Scripts/c120305053.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120305053.lua)

```lua
	return RD.IsPlayerNoActivateInThisTurn(tp,list[1])
end
cm.cost=RD.CostPayLP(1000)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return aux.MustMaterialCheck(nil,tp,EFFECT_MUST_BE_FMATERIAL)
```
