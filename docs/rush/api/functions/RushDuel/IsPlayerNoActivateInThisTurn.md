# RushDuel.IsPlayerNoActivateInThisTurn

Alias: `RD.IsPlayerNoActivateInThisTurn`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsPlayerNoActivateInThisTurn(any player, any code) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 玩家在这个回合没有发动过特定卡名的效果
```

## Parameters

- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `code` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:81`

```lua
function RushDuel.IsPlayerNoActivateInThisTurn(player, code)
    local codes = RushDuel.ActivateCodes[player + 1] or {}
    return not codes[code]
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **29** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.IsPlayerNoActivateInThisTurn) with `RushDuel.IsPlayerNoActivateInThisTurn`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [The Eye of Timaeus](/examples/rush-cards/120285065) | `120285065` | [Rush/Scripts/c120285065.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120285065.lua) | 1 |
| [Light of Bewitchment](/examples/rush-cards/120301074) | `120301074` | [Rush/Scripts/c120301074.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120301074.lua) | 1 |
| [Spiritualization Training](/examples/rush-cards/120301020) | `120301020` | [Rush/Scripts/c120301020.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120301020.lua) | 1 |
| [The Noodle Art of Flavor Shift](/examples/rush-cards/120300053) | `120300053` | [Rush/Scripts/c120300053.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300053.lua) | 1 |
| Instant Fusion | `120305053` | [Rush/Scripts/c120305053.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120305053.lua) | 1 |
| The Player Returning Alive | `120305036` | [Rush/Scripts/c120305036.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120305036.lua) | 1 |
| Despair and Desire | `120301034` | [Rush/Scripts/c120301034.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120301034.lua) | 1 |
| Lostream Reading | `120309043` | [Rush/Scripts/c120309043.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120309043.lua) | 1 |
| Memory of Sunlit | `120300051` | [Rush/Scripts/c120300051.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300051.lua) | 1 |
| Shadowforce Explosion | `120300042` | [Rush/Scripts/c120300042.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300042.lua) | 1 |
| Micha the Symbol of the Angels | `120309058` | [Rush/Scripts/c120309058.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120309058.lua) | 1 |
| Encounter of the Stars | `120305025` | [Rush/Scripts/c120305025.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120305025.lua) | 1 |
| Handbook to the Spiritual Arts | `120301019` | [Rush/Scripts/c120301019.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120301019.lua) | 1 |
| Book of Life | `120109058` | [Rush/Scripts/c120109058.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120109058.lua) | 1 |
| Beginning Skullrise | `120298014` | [Rush/Scripts/c120298014.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120298014.lua) | 1 |
| The Journeying Three Magi | `120304058` | [Rush/Scripts/c120304058.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304058.lua) | 1 |
| Midnight Reading | `120306061` | [Rush/Scripts/c120306061.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120306061.lua) | 1 |
| Speed Roll | `120301063` | [Rush/Scripts/c120301063.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120301063.lua) | 1 |
| Post-Stellar Shower Princess Cosmos | `120300056` | [Rush/Scripts/c120300056.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300056.lua) | 1 |
| The Allied Dark Magicians | `120309015` | [Rush/Scripts/c120309015.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120309015.lua) | 1 |
| Happy Journal | `120304048` | [Rush/Scripts/c120304048.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304048.lua) | 1 |
| Beacon of Dragon Destroyer | `120301066` | [Rush/Scripts/c120301066.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120301066.lua) | 1 |
| The United Front with Timaeus | `120309016` | [Rush/Scripts/c120309016.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120309016.lua) | 1 |
| Princess Cosmos' Astronomical Observation | `120293055` | [Rush/Scripts/c120293055.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120293055.lua) | 1 |
| ...and 5 more |  |  |  |

## Script Examples

### The Eye of Timaeus (`120285065`)

Source: [Rush/Scripts/c120285065.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120285065.lua)

```lua
end
function cm.condition(e,tp,eg,ep,ev,re,r,rp)
	return RD.IsPlayerNoActivateInThisTurn(tp,list[1])
end
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Light of Bewitchment (`120301074`)

Source: [Rush/Scripts/c120301074.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120301074.lua)

```lua
end
function cm.condition(e,tp,eg,ep,ev,re,r,rp)
	return RD.IsPlayerNoActivateInThisTurn(tp,list[1])
end
function cm.cost(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Spiritualization Training (`120301020`)

Source: [Rush/Scripts/c120301020.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120301020.lua)

```lua
end
function cm.condition(e,tp,eg,ep,ev,re,r,rp)
	return RD.IsPlayerNoActivateInThisTurn(tp,list[1])
end
cm.cost=RD.CostShowGroupHand(cm.costfilter,cm.costcheck,2,2,function(g)
```
