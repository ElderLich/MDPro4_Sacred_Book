# RushDuel.TargetDiscardDeck

Alias: `RD.TargetDiscardDeck`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.TargetDiscardDeck(any player, any count) -> any
```

## Description

Rush Duel helper declared in `RDTarget.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
对玩家效果: 盲堆 - 对象
```

## Parameters

- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `count` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDTarget.lua:23`

```lua
function RushDuel.TargetDiscardDeck(player, count)
    Duel.SetTargetPlayer(player)
    Duel.SetTargetParam(count)
    Duel.SetOperationInfo(0, CATEGORY_DECKDES, nil, 0, player, count)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **17** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.TargetDiscardDeck) with `RushDuel.TargetDiscardDeck`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Insect Taurus](/examples/rush-cards/120300060) | `120300060` | [Rush/Scripts/c120300060.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120300060.lua) | 1 |
| Tama Tama Gachance | `120109053` | [Rush/Scripts/c120109053.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120109053.lua) | 1 |
| Music Princess's Substitute | `120290043` | [Rush/Scripts/c120290043.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120290043.lua) | 1 |
| Temporary Storm Blockade | `120203030` | [Rush/Scripts/c120203030.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120203030.lua) | 1 |
| Best Bite | `120183048` | [Rush/Scripts/c120183048.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120183048.lua) | 1 |
| Darkness Fource Seeker | `120217007` | [Rush/Scripts/c120217007.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120217007.lua) | 1 |
| Royal Rebel's Starting | `120306045` | [Rush/Scripts/c120306045.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306045.lua) | 1 |
| Destructor Survey | `120247053` | [Rush/Scripts/c120247053.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120247053.lua) | 1 |
| Wolftastic Mean Mutt | `120222050` | [Rush/Scripts/c120222050.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120222050.lua) | 1 |
| Rising Light Angel Essel | `120249037` | [Rush/Scripts/c120249037.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120249037.lua) | 1 |
| Cat-trois Choice | `120249055` | [Rush/Scripts/c120249055.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120249055.lua) | 1 |
| Hungry Donut | `120290020` | [Rush/Scripts/c120290020.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120290020.lua) | 1 |
| Vande the Electric Lion | `120257019` | [Rush/Scripts/c120257019.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120257019.lua) | 1 |
| Heavenly Invitation | `120239054` | [Rush/Scripts/c120239054.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120239054.lua) | 1 |
| Meteor Larva | `120227019` | [Rush/Scripts/c120227019.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120227019.lua) | 1 |
| Psychic Burial | `120160004` | [Rush/Scripts/c120160004.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120160004.lua) | 1 |
| Heat Hyena | `120183032` | [Rush/Scripts/c120183032.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120183032.lua) | 1 |

## Script Examples

### Insect Taurus (`120300060`)

Source: [Rush/Scripts/c120300060.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120300060.lua)

```lua
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsPlayerCanDiscardDeck(tp,2) end
	RD.TargetDiscardDeck(tp,2)
end
function cm.activate(e,tp,eg,ep,ev,re,r,rp)
```

### Tama Tama Gachance (`120109053`)

Source: [Rush/Scripts/c120109053.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120109053.lua)

```lua
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsPlayerCanDiscardDeck(tp,3) end
	RD.TargetDiscardDeck(tp,3)
end
function cm.activate(e,tp,eg,ep,ev,re,r,rp)
```

### Music Princess's Substitute (`120290043`)

Source: [Rush/Scripts/c120290043.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120290043.lua)

```lua
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsPlayerCanDiscardDeck(tp,3) end
	RD.TargetDiscardDeck(tp,3)
end
function cm.activate(e,tp,eg,ep,ev,re,r,rp)
```
