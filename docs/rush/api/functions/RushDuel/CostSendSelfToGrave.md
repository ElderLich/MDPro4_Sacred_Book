# RushDuel.CostSendSelfToGrave

Alias: `RD.CostSendSelfToGrave`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CostSendSelfToGrave() -> any
```

## Description

Rush Duel helper declared in `RDCost.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
代价: 把自己场上表侧表示的这张卡送去墓地
```

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCost.lua:289`

```lua
function RushDuel.CostSendSelfToGrave()
    return function(e, tp, eg, ep, ev, re, r, rp, chk)
        if chk == 0 then
            return e:GetHandler():IsAbleToGraveAsCost()
        end
        Duel.SendtoGrave(RushDuel.ToMaximunGroup(e:GetHandler()), REASON_COST)
        return true
    end
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **55** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CostSendSelfToGrave) with `RushDuel.CostSendSelfToGrave`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Jinzo the Machine Menace](/examples/rush-cards/120257028) | `120257028` | [Rush/Scripts/c120257028.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120257028.lua) | 1 |
| Galactica Dejavu | `120244003` | [Rush/Scripts/c120244003.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120244003.lua) | 1 |
| Plasmatic Model Tool Ceto | `120301069` | [Rush/Scripts/c120301069.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120301069.lua) | 1 |
| Fusionic Revivern | `120109030` | [Rush/Scripts/c120109030.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120109030.lua) | 1 |
| Ice Age Pounder | `120304027` | [Rush/Scripts/c120304027.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120304027.lua) | 1 |
| Rescue Cat | `120307008` | [Rush/Scripts/c120307008.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120307008.lua) | 1 |
| Grand Legendary Priest | `120271043` | [Rush/Scripts/c120271043.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120271043.lua) | 1 |
| The Ultimate Flag | `120294019` | [Rush/Scripts/c120294019.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120294019.lua) | 1 |
| Supreme Skystream Magnum Overlord | `120151002` | [Rush/Scripts/c120151002.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120151002.lua) | 1 |
| Surtr the Brilliant Magical Sword | `120306100` | [Rush/Scripts/c120306100.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306100.lua) | 1 |
| Familiar of the Earth Spiritualist | `120301013` | [Rush/Scripts/c120301013.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120301013.lua) | 1 |
| Familiar of the Water Spiritualist | `120301014` | [Rush/Scripts/c120301014.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120301014.lua) | 1 |
| Familiar of the Fire Spiritualist | `120301015` | [Rush/Scripts/c120301015.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120301015.lua) | 1 |
| Familiar of the Wind Spiritualist | `120301016` | [Rush/Scripts/c120301016.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120301016.lua) | 1 |
| Mr. Alchemy | `120196020` | [Rush/Scripts/c120196020.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120196020.lua) | 1 |
| Striping Wyvern | `120253005` | [Rush/Scripts/c120253005.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120253005.lua) | 1 |
| Valkyrion the Unity Warrior | `120260025` | [Rush/Scripts/c120260025.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120260025.lua) | 1 |
| Ember the Hyper Assistant | `120249014` | [Rush/Scripts/c120249014.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120249014.lua) | 1 |
| Unfulfilled Goblin | `120203039` | [Rush/Scripts/c120203039.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120203039.lua) | 1 |
| Meinir the Defiant Soulclad Spirit | `120298009` | [Rush/Scripts/c120298009.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120298009.lua) | 1 |
| Shining Shamaness | `120254082` | [Rush/Scripts/c120254082.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120254082.lua) | 1 |
| Contact Dark Matter Omega Voyager | `120264002` | [Rush/Scripts/c120264002.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120264002.lua) | 1 |
| Voidvelg Meteon | `120227018` | [Rush/Scripts/c120227018.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120227018.lua) | 1 |
| Reporter Raccoon | `120199029` | [Rush/Scripts/c120199029.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120199029.lua) | 1 |
| ...and 31 more |  |  |  |

## Script Examples

### Jinzo the Machine Menace (`120257028`)

Source: [Rush/Scripts/c120257028.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120257028.lua)

```lua
	return c:IsFacedown() and c:GetSequence()<5
end
cm.cost=RD.CostSendSelfToGrave()
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.GetMZoneCount(tp,e:GetHandler())>0
```

### Galactica Dejavu (`120244003`)

Source: [Rush/Scripts/c120244003.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120244003.lua)

```lua
	return RD.IsLPAbove(1-tp,4000)
end
cm.cost=RD.CostSendSelfToGrave()
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsPlayerCanDiscardDeck(tp,1) end
```

### Plasmatic Model Tool Ceto (`120301069`)

Source: [Rush/Scripts/c120301069.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120301069.lua)

```lua
	return c:IsCode(list[1]) and c:IsAbleToHand()
end
cm.cost=RD.CostSendSelfToGrave()
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return not Duel.IsPlayerAffectedByEffect(tp,59822133)
```
