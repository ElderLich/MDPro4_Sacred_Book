# RushDuel.SendToDeckBottom

Alias: `RD.SendToDeckBottom`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.SendToDeckBottom(any target, any effect, any player, any reason) -> any
```

## Description

Rush Duel helper declared in `RDAction.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
操作: 返回卡组下面 (排序)
```

## Parameters

- `target` `any`: Type and behavior are not yet reviewed; see the source.
- `effect` `any`: Type and behavior are not yet reviewed; see the source.
- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `reason` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAction.lua:401`

```lua
function RushDuel.SendToDeckBottom(target, effect, player, reason)
    local hints = Group.CreateGroup()
    local group = RushDuel.ToGroup(target):Filter(RushDuel.FilterToDeckTarget, nil, effect, player, reason, hints)
    local g = RushDuel.ToMaximunGroup(group)
    local tc = hints:GetFirst()
    if tc then
        Duel.Hint(HINT_CARD, 0, tc:GetOriginalCode())
    end
    if #g == 0 then
        return 0
    end
    local og, ct = RushDuel.SendToDeckSort(g, SEQ_DECKBOTTOM, REASON_EFFECT, player)
    return ct
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **44** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.SendToDeckBottom) with `RushDuel.SendToDeckBottom`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Chaos Emperor Dragon - Envoy of the End](/examples/rush-cards/120305001) | `120305001` | [Rush/Scripts/c120305001.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120305001.lua) | 1 |
| [Moonforce Ziggy](/examples/rush-cards/120300014) | `120300014` | [Rush/Scripts/c120300014.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300014.lua) | 1 |
| [Abyssal Dragon Lord Abyss Poseidra \[L\]](/examples/rush-cards/120239013) | `120239013` | [Rush/Scripts/c120239013.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120239013.lua) | 1 |
| [Wish of the Skysavior](/examples/rush-cards/120253064) | `120253064` | [Rush/Scripts/c120253064.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120253064.lua) | 1 |
| Sacred Tower in Collapse | `120290064` | [Rush/Scripts/c120290064.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290064.lua) | 1 |
| Icelyn the Super Assistant | `120254064` | [Rush/Scripts/c120254064.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120254064.lua) | 1 |
| Etraynze the Shadow Flower Ninja | `120170029` | [Rush/Scripts/c120170029.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120170029.lua) | 1 |
| Rurigra the Eternal | `120285028` | [Rush/Scripts/c120285028.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120285028.lua) | 1 |
| Cathedral of Arthenée | `120306065` | [Rush/Scripts/c120306065.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120306065.lua) | 1 |
| Celeb Rose Influencers | `120257044` | [Rush/Scripts/c120257044.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120257044.lua) | 1 |
| Whispurring Fairy | `120277047` | [Rush/Scripts/c120277047.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120277047.lua) | 1 |
| Abysslayer Apsaras | `120239028` | [Rush/Scripts/c120239028.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120239028.lua) | 1 |
| Worker Warrior - Sinister Chairman | `120196038` | [Rush/Scripts/c120196038.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120196038.lua) | 1 |
| Black Luster Soljersey - Envoy of the Drying | `120228017` | [Rush/Scripts/c120228017.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120228017.lua) | 1 |
| Lovely Connect | `120300054` | [Rush/Scripts/c120300054.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300054.lua) | 1 |
| Cute Lovely Anela | `120260042` | [Rush/Scripts/c120260042.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120260042.lua) | 1 |
| Splendid Slash | `120254070` | [Rush/Scripts/c120254070.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120254070.lua) | 1 |
| Wynn the Wind Spiritualist | `120301012` | [Rush/Scripts/c120301012.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120301012.lua) | 1 |
| Imaginary Reactor | `120271025` | [Rush/Scripts/c120271025.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120271025.lua) | 1 |
| Zeptron | `120150016` | [Rush/Scripts/c120150016.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120150016.lua) | 1 |
| Caius the Shadow Monarch | `120291001` | [Rush/Scripts/c120291001.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120291001.lua) | 1 |
| Shadow Flower Spore | `120170048` | [Rush/Scripts/c120170048.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120170048.lua) | 1 |
| Garland the True Shadow Flower Ninja | `120170031` | [Rush/Scripts/c120170031.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120170031.lua) | 1 |
| Silent Learning | `120150006` | [Rush/Scripts/c120150006.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120150006.lua) | 1 |
| ...and 20 more |  |  |  |

## Script Examples

### Chaos Emperor Dragon - Envoy of the End (`120305001`)

Source: [Rush/Scripts/c120305001.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120305001.lua)

```lua
function cm.spop(e,tp,eg,ep,ev,re,r,rp,c)
	local sg=e:GetLabelObject()
	RD.SendToDeckBottom(sg,e,tp,REASON_SPSUMMON)
	sg:DeleteGroup()
end
```

### Moonforce Ziggy (`120300014`)

Source: [Rush/Scripts/c120300014.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300014.lua)

```lua
			RD.CanSelectAndDoAction(aux.Stringid(m,3),HINTMSG_TODECK,aux.NecroValleyFilter(cm.tdfilter),tp,LOCATION_GRAVE,0,1,1,nil,function(g)
				local c=e:GetHandler()
				if RD.SendToDeckBottom(g,e,tp,REASON_EFFECT)~=0
					and c:IsFaceup() and c:IsRelateToEffect(e) then
					RD.AttachAtkDef(e,c,0,500,RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END+RESET_OPPO_TURN)
```

### Abyssal Dragon Lord Abyss Poseidra [L] (`120239013`)

Source: [Rush/Scripts/c120239013.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120239013.lua)

```lua
	local g=Duel.GetMatchingGroup(cm.costfilter,tp,LOCATION_GRAVE,0,nil)
	if chk==0 then return g:GetCount()>0 end
	RD.SendToDeckBottom(g,e,tp,REASON_COST)
	if RD.IsOperatedGroupExists(cm.exfilter,3,nil) then
		e:SetValue(1)
```
