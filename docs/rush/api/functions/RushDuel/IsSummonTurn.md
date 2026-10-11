# RushDuel.IsSummonTurn

Alias: `RD.IsSummonTurn`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsSummonTurn(Card card) -> bool
```

## Description

Checks REASON_SUMMON, STATUS_SUMMON_TURN and the Rush FLAG_SUMMON_TURN marker. The Rush bootstrap installs the tracking effects required by this predicate.

## Parameters

- `card` `Card`: Card to inspect.

## Returns

- `bool`: Whether the card satisfies the current-turn Normal Summon checks.

## Source

`Rush/Utilities/RDCondition.lua:30`

```lua
function RushDuel.IsSummonTurn(card)
    return card:IsReason(REASON_SUMMON) and card:IsStatus(STATUS_SUMMON_TURN) and card:GetFlagEffect(FLAG_SUMMON_TURN) ~= 0
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **81** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.IsSummonTurn) with `RushDuel.IsSummonTurn`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Ember the Ultra Assistant](/examples/rush-cards/120283035) | `120283035` | [Rush/Scripts/c120283035.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120283035.lua) | 1 |
| [Tubardiche the Music Princess](/examples/rush-cards/120247025) | `120247025` | [Rush/Scripts/c120247025.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120247025.lua) | 1 |
| [Moonforce Timo](/examples/rush-cards/120300015) | `120300015` | [Rush/Scripts/c120300015.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300015.lua) | 1 |
| [Preferlyre](/examples/rush-cards/120283046) | `120283046` | [Rush/Scripts/c120283046.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120283046.lua) | 1 |
| Royal Rebel's Heavy Metal | `120130031` | [Rush/Scripts/c120130031.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120130031.lua) | 1 |
| Galactica Supreme Oblivion | `120245003` | [Rush/Scripts/c120245003.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120245003.lua) | 1 |
| Voidvelg Divine Requiem | `120109037` | [Rush/Scripts/c120109037.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120109037.lua) | 1 |
| Under Dealer | `120290015` | [Rush/Scripts/c120290015.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290015.lua) | 1 |
| OuTerverSe Direct Driver | `120109056` | [Rush/Scripts/c120109056.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120109056.lua) | 1 |
| Poet Fairy | `120208021` | [Rush/Scripts/c120208021.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120208021.lua) | 1 |
| Fiarma the Ally Spark | `120298025` | [Rush/Scripts/c120298025.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120298025.lua) | 1 |
| Peit the Ally Spark | `120298024` | [Rush/Scripts/c120298024.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120298024.lua) | 1 |
| Darkness Transam Crisis | `120253004` | [Rush/Scripts/c120253004.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120253004.lua) | 1 |
| Sparkhearts Familiar | `120298027` | [Rush/Scripts/c120298027.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120298027.lua) | 1 |
| Sitarloot | `120283047` | [Rush/Scripts/c120283047.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120283047.lua) | 1 |
| Axe Shredder | `120228021` | [Rush/Scripts/c120228021.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120228021.lua) | 1 |
| Sparkhearts Hat | `120298026` | [Rush/Scripts/c120298026.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120298026.lua) | 1 |
| Royal Rebel's Extreme | `120306006` | [Rush/Scripts/c120306006.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120306006.lua) | 1 |
| Super Galaxy King Lord of Galactica | `120254038` | [Rush/Scripts/c120254038.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120254038.lua) | 1 |
| Ritche of Hope | `120287072` | [Rush/Scripts/c120287072.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120287072.lua) | 1 |
| False Moon | `120264034` | [Rush/Scripts/c120264034.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120264034.lua) | 1 |
| Royal Rebel's Doom Metal | `120170024` | [Rush/Scripts/c120170024.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120170024.lua) | 1 |
| Jointech Hero | `120249008` | [Rush/Scripts/c120249008.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120249008.lua) | 1 |
| Mezame the Ringing Alarm | `120199015` | [Rush/Scripts/c120199015.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120199015.lua) | 1 |
| ...and 57 more |  |  |  |

## Script Examples

### Ember the Ultra Assistant (`120283035`)

Source: [Rush/Scripts/c120283035.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120283035.lua)

```lua
end
function cm.condition(e,tp,eg,ep,ev,re,r,rp)
	return Duel.GetFieldGroupCount(tp,LOCATION_DECK,0)>9 and RD.IsSummonTurn(e:GetHandler())
end
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Tubardiche the Music Princess (`120247025`)

Source: [Rush/Scripts/c120247025.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120247025.lua)

```lua
function cm.condition(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	return RD.IsSummonTurn(c) and Duel.IsExistingMatchingCard(cm.confilter,tp,LOCATION_MZONE,0,1,c)
end
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Moonforce Timo (`120300015`)

Source: [Rush/Scripts/c120300015.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300015.lua)

```lua
end
function cm.condition(e,tp,eg,ep,ev,re,r,rp)
	return RD.IsSummonTurn(e:GetHandler()) and Duel.GetFieldGroupCount(tp,LOCATION_DECK,0)>9
end
cm.cost=RD.CostSendGroupToDeckSort(cm.costfilter,cm.check,LOCATION_HAND+LOCATION_GRAVE,2,2,true,SEQ_DECKBOTTOM,true,false)
```
