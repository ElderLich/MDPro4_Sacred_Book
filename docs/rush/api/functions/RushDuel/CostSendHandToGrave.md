# RushDuel.CostSendHandToGrave

Alias: `RD.CostSendHandToGrave`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CostSendHandToGrave(function filter, int|function min, int|function max, [function|nil set_label_before], [function|nil set_object_before], [function|nil set_label_after], [function|nil set_object_after]) -> function
```

## Description

Returns a cost callback that selects min to max matching cards from the controller's hand and sends them to the Graveyard with REASON_COST, excluding the effect handler. The filter must include any required cost-legality check such as Card.IsAbleToGraveAsCost; this wrapper does not add that predicate.
The callback honors EFFECT_NO_COST_SEND_HAND_TO_GRAVE through RD.NoCostCheck. min and max can be numbers or callbacks evaluated with the cost arguments. Optional label callbacks receive the selected Group before sending or the operated Group after a successful send.

## Parameters

- `filter` `function`: Card filter receiving card, effect, player and remaining cost callback arguments.
- `min` `int|function`: Minimum count or callback computing it.
- `max` `int|function`: Maximum count or callback computing it.
- `set_label_before` `function|nil` (optional): Computes the effect label from the selected Group before sending.
- `set_object_before` `function|nil` (optional): Computes the label object from the selected Group before sending.
- `set_label_after` `function|nil` (optional): Computes the effect label from the operated Group after a successful send.
- `set_object_after` `function|nil` (optional): Computes the label object from the operated Group after a successful send.

## Returns

- `function`: Cost callback for Effect.SetCost; tests availability for chk==0, then performs payment.

## Example

```lua
e1:SetCost(RD.CostSendHandToGrave(Card.IsAbleToGraveAsCost, 1, 1))
```

## Source

`Rush/Utilities/RDCost.lua:299`

```lua
function RushDuel.CostSendHandToGrave(filter, min, max, set_label_before, set_object_before, set_label_after,
    set_object_after)
    local cost = RushDuel.CostSendMatchToGrave(filter, LOCATION_HAND, min, max, true, false, false, set_label_before,
        set_object_before, set_label_after, set_object_after)
    return RushDuel.NoCostCheck(cost, EFFECT_NO_COST_SEND_HAND_TO_GRAVE)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **315** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CostSendHandToGrave) with `RushDuel.CostSendHandToGrave`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Analyze Phlogiston](/examples/rush-cards/120226001) | `120226001` | [Rush/Scripts/c120226001.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120226001.lua) | 1 |
| [Vapor Lancer the Super Graphagas](/examples/rush-cards/120260063) | `120260063` | [Rush/Scripts/c120260063.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120260063.lua) | 1 |
| [Wako Gozen Riletta](/examples/rush-cards/120309021) | `120309021` | [Rush/Scripts/c120309021.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120309021.lua) | 1 |
| [The Black Witch Facing the Temple](/examples/rush-cards/120309048) | `120309048` | [Rush/Scripts/c120309048.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120309048.lua) | 1 |
| [Dimension Oper](/examples/rush-cards/120309025) | `120309025` | [Rush/Scripts/c120309025.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120309025.lua) | 1 |
| [Voidvelg Gehennamagia](/examples/rush-cards/120109048) | `120109048` | [Rush/Scripts/c120109048.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120109048.lua) | 1 |
| [Botonaginata the Music Princess](/examples/rush-cards/120290009) | `120290009` | [Rush/Scripts/c120290009.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290009.lua) | 1 |
| [Supreme Machine Magnum Overlord \[L\]](/examples/rush-cards/120150001) | `120150001` | [Rush/Scripts/c120150001.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120150001.lua) | 1 |
| [Mystic Dealer](/examples/rush-cards/120105006) | `120105006` | [Rush/Scripts/c120105006.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120105006.lua) | 1 |
| Icelyn the Super Assistant | `120254064` | [Rush/Scripts/c120254064.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120254064.lua) | 1 |
| Abysskite Liem | `120249025` | [Rush/Scripts/c120249025.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120249025.lua) | 1 |
| Jointech Digup | `120249047` | [Rush/Scripts/c120249047.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120249047.lua) | 1 |
| Dark Hole Device | `120249050` | [Rush/Scripts/c120249050.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120249050.lua) | 1 |
| Shiny Shady | `120260079` | [Rush/Scripts/c120260079.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120260079.lua) | 1 |
| Under Dealer | `120290015` | [Rush/Scripts/c120290015.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290015.lua) | 1 |
| Lostream Shell | `120309039` | [Rush/Scripts/c120309039.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120309039.lua) | 1 |
| Super Princess of the Flock - Max Mutton \[L\] | `120293007` | [Rush/Scripts/c120293007.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120293007.lua) | 1 |
| The Player Returning Alive | `120305036` | [Rush/Scripts/c120305036.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120305036.lua) | 1 |
| The Trinity Dragiastar | `120109031` | [Rush/Scripts/c120109031.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120109031.lua) | 1 |
| Lana the Holy Wind of Healing | `120298044` | [Rush/Scripts/c120298044.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120298044.lua) | 1 |
| The Dragiastar | `120235035` | [Rush/Scripts/c120235035.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120235035.lua) | 1 |
| Destructor Emperor Bakhakaiser | `120264045` | [Rush/Scripts/c120264045.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120264045.lua) | 1 |
| The Flame Dragon Haunting the Temple | `120309047` | [Rush/Scripts/c120309047.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120309047.lua) | 1 |
| Grace Princess Emaki | `120300021` | [Rush/Scripts/c120300021.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300021.lua) | 1 |
| ...and 291 more |  |  |  |

## Script Examples

### Analyze Phlogiston (`120226001`)

Source: [Rush/Scripts/c120226001.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120226001.lua)

```lua
	return g:GetSum(Card.GetLevel,nil)==lv
end
cm.cost=RD.CostSendHandToGrave(cm.costfilter,1,1)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	local g=Duel.GetMatchingGroup(cm.desfilter,tp,0,LOCATION_MZONE,nil)
```

### Vapor Lancer the Super Graphagas (`120260063`)

Source: [Rush/Scripts/c120260063.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120260063.lua)

```lua
	return Duel.IsExistingMatchingCard(Card.IsFaceup,tp,0,LOCATION_ONFIELD,1,nil)
end
cm.cost=RD.CostSendHandToGrave(Card.IsAbleToGraveAsCost,1,1)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsPlayerCanDiscardDeck(tp,3) end
```

### Wako Gozen Riletta (`120309021`)

Source: [Rush/Scripts/c120309021.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120309021.lua)

```lua
	return RD.IsSpecialSummonMainPhase(e:GetHandler(),SUMMON_TYPE_RITUAL)
end
cm.cost=RD.CostSendHandToGrave(Card.IsAbleToGraveAsCost,1,1)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsExistingMatchingCard(nil,tp,0,LOCATION_ONFIELD,1,nil) end
```
