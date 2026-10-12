# RushDuel.CostSendDeckTopToGrave

Alias: `RD.CostSendDeckTopToGrave`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CostSendDeckTopToGrave(int count, [function|nil set_label], [function|nil set_object]) -> function
```

## Description

Returns a cost callback that checks whether the player can send count cards from the Deck as cost, then calls Duel.DiscardDeck with REASON_COST. Optional callbacks store information from the operated Group on the Effect.

## Parameters

- `count` `int`: Cards to send from the Deck top.
- `set_label` `function|nil` (optional): Computes a numeric label from the operated Group.
- `set_object` `function|nil` (optional): Computes a label object from the operated Group.

## Returns

- `function`: Cost callback.

## Source

`Rush/Utilities/RDCost.lua:240`

```lua
function RushDuel.CostSendDeckTopToGrave(count, set_label, set_object)
    return function(e, tp, eg, ep, ev, re, r, rp, chk)
        if chk == 0 then
            return Duel.IsPlayerCanDiscardDeckAsCost(tp, count)
        end
        if Duel.DiscardDeck(tp, count, REASON_COST) ~= 0 and (set_label ~= nil or set_object ~= nil) then
            local og = Duel.GetOperatedGroup()
            RushDuel.SetLabelAndObject(e, og, set_label, set_object)
        end
        return true
    end
end
```

## Guided Examples

Learn how to use this function in context:

- [Rush Duel Scripting](/learn/rush-duel-scripting)

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **310** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CostSendDeckTopToGrave) with `RushDuel.CostSendDeckTopToGrave`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Brassdes of the Wicked Wheels](/examples/rush-cards/120304033) | `120304033` | [Rush/Scripts/c120304033.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120304033.lua) | 1 |
| [Dark-Guiding Kuriboh](/examples/rush-cards/120280009) | `120280009` | [Rush/Scripts/c120280009.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120280009.lua) | 1 |
| [Planet Aegis](/examples/rush-cards/120297006) | `120297006` | [Rush/Scripts/c120297006.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120297006.lua) | 1 |
| [Red-Eyes Mars Dragon](/examples/rush-cards/120306034) | `120306034` | [Rush/Scripts/c120306034.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306034.lua) | 1 |
| Qadi of the Monumenthes | `120300009` | [Rush/Scripts/c120300009.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120300009.lua) | 1 |
| Yamiterasu the Divine Ruler | `120199036` | [Rush/Scripts/c120199036.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120199036.lua) | 1 |
| Harpie Lady Feather Duster | `120279002` | [Rush/Scripts/c120279002.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120279002.lua) | 1 |
| OuTerverSe Direct Driver | `120109056` | [Rush/Scripts/c120109056.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120109056.lua) | 1 |
| Despair and Desire | `120301034` | [Rush/Scripts/c120301034.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120301034.lua) | 1 |
| Fiarma the Ally Spark | `120298025` | [Rush/Scripts/c120298025.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120298025.lua) | 1 |
| Transam Road Linac | `120235030` | [Rush/Scripts/c120235030.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120235030.lua) | 1 |
| Sevens Road Charmy Witch | `120260062` | [Rush/Scripts/c120260062.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120260062.lua) | 1 |
| Peit the Ally Spark | `120298024` | [Rush/Scripts/c120298024.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120298024.lua) | 1 |
| Wooly Wonderland - Graveyard Grudge | `120208055` | [Rush/Scripts/c120208055.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120208055.lua) | 1 |
| Super Galaxy King Lord of Galactica \[L\] | `120254037` | [Rush/Scripts/c120254037.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120254037.lua) | 1 |
| Imaginary Leading Actor | `120271029` | [Rush/Scripts/c120271029.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120271029.lua) | 1 |
| Royal Rebel's Extreme | `120306006` | [Rush/Scripts/c120306006.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306006.lua) | 1 |
| Battletested Curse of Dragon | `120249031` | [Rush/Scripts/c120249031.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120249031.lua) | 1 |
| UMP Sky Forbia | `120306017` | [Rush/Scripts/c120306017.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306017.lua) | 1 |
| Voidalfr Buprestruve | `120300003` | [Rush/Scripts/c120300003.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120300003.lua) | 1 |
| Owlchannel | `120253031` | [Rush/Scripts/c120253031.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120253031.lua) | 1 |
| Blue-Eyes Vision Dragon | `120252004` | [Rush/Scripts/c120252004.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120252004.lua) | 1 |
| Dimension Riletta | `120309024` | [Rush/Scripts/c120309024.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120309024.lua) | 1 |
| Battletested Gaia The Fierce Knight | `120249032` | [Rush/Scripts/c120249032.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120249032.lua) | 1 |
| ...and 286 more |  |  |  |

## Script Examples

### Brassdes of the Wicked Wheels (`120304033`)

Source: [Rush/Scripts/c120304033.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120304033.lua)

```lua
	return RD.IsSpecialSummonMainPhase(e:GetHandler())
end
cm.cost=RD.CostSendDeckTopToGrave(3)
function cm.operation(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
```

### Dark-Guiding Kuriboh (`120280009`)

Source: [Rush/Scripts/c120280009.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120280009.lua)

```lua
		and RD.IsCanBeSpecialSummoned(c,e,tp,POS_FACEDOWN_DEFENSE)
end
cm.cost=RD.CostSendDeckTopToGrave(2)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsExistingMatchingCard(cm.filter,tp,0,LOCATION_MZONE,1,nil) end
```

### Planet Aegis (`120297006`)

Source: [Rush/Scripts/c120297006.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120297006.lua)

```lua
	end
end
cm.cost=RD.CostSendDeckTopToGrave(2)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsExistingMatchingCard(cm.filter1,tp,LOCATION_MZONE,0,1,nil) end
```
