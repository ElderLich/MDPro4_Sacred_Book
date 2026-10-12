# RushDuel.UnionEquip

Alias: `RD.UnionEquip`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.UnionEquip(any tp, any c, any ec) -> any
```

## Description

Rush Duel helper declared in `RDUnion.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
进行同盟装备
```

## Parameters

- `tp` `any`: Type and behavior are not yet reviewed; see the source.
- `c` `any`: Type and behavior are not yet reviewed; see the source.
- `ec` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDUnion.lua:84`

```lua
function RushDuel.UnionEquip(tp, c, ec)
    if c and ec and Duel.Equip(tp, ec, c) then
        local e1 = Effect.CreateEffect(ec)
        e1:SetType(EFFECT_TYPE_SINGLE)
        e1:SetCode(EFFECT_UNION_STATUS)
        e1:SetProperty(EFFECT_FLAG_CANNOT_DISABLE)
        e1:SetReset(RESET_EVENT+RESETS_STANDARD)
        ec:RegisterEffect(e1)
        return true
    end
    return false
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **3** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.UnionEquip) with `RushDuel.UnionEquip`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Lostream Shell | `120309039` | [Rush/Scripts/c120309039.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120309039.lua) | 1 |
| UMP Sky Forbia | `120306017` | [Rush/Scripts/c120306017.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306017.lua) | 1 |
| The Lauan Adventurers Are Go!! | `120306050` | [Rush/Scripts/c120306050.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306050.lua) | 2 |

## Script Examples

### Lostream Shell (`120309039`)

Source: [Rush/Scripts/c120309039.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120309039.lua)

```lua
			RD.SelectAndDoAction(HINTMSG_EQUIP,aux.NecroValleyFilter(filter2),tp,LOCATION_GRAVE,0,1,1,nil,function(sg)
				Duel.BreakEffect()
				RD.UnionEquip(tp,tc,sg:GetFirst())
			end)
		end)
```

### UMP Sky Forbia (`120306017`)

Source: [Rush/Scripts/c120306017.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306017.lua)

```lua
			local filter=RD.Filter(cm.filter,e,c)
			RD.CanSelectAndDoAction(aux.Stringid(m,2),HINTMSG_EQUIP,aux.NecroValleyFilter(filter),tp,LOCATION_GRAVE,0,1,1,nil,function(g)
				RD.UnionEquip(tp,c,g:GetFirst())
			end)
		end
```

### The Lauan Adventurers Are Go!! (`120306050`)

Source: [Rush/Scripts/c120306050.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306050.lua)

```lua
		RD.SelectAndDoAction(HINTMSG_EQUIP,aux.NecroValleyFilter(filter2),tp,LOCATION_GRAVE,0,1,max,nil,function(sg)
			local ec1,ec2=sg:GetFirst(),sg:GetNext()
			RD.UnionEquip(tp,tc,ec1)
			RD.UnionEquip(tp,tc,ec2)
		end)
```
