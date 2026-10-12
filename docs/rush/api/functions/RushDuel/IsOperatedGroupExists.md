# RushDuel.IsOperatedGroupExists

Alias: `RD.IsOperatedGroupExists`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsOperatedGroupExists(any filter, any count, any expect) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
额外条件: 最后的操作是否包含某种卡
```

## Parameters

- `filter` `any`: Type and behavior are not yet reviewed; see the source.
- `count` `any`: Type and behavior are not yet reviewed; see the source.
- `expect` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:422`

```lua
function RushDuel.IsOperatedGroupExists(filter, count, expect)
    return filter == nil or Duel.GetOperatedGroup():IsExists(filter, count, expect)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **17** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.IsOperatedGroupExists) with `RushDuel.IsOperatedGroupExists`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Abyssal Dragon Lord Abyss Poseidra \[L\]](/examples/rush-cards/120239013) | `120239013` | [Rush/Scripts/c120239013.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120239013.lua) | 1 |
| [Curse of the Magiclad Dragon](/examples/rush-cards/120304061) | `120304061` | [Rush/Scripts/c120304061.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120304061.lua) | 1 |
| [Star Protector Recapture](/examples/rush-cards/120306063) | `120306063` | [Rush/Scripts/c120306063.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306063.lua) | 1 |
| Celeb Rose Warlock | `120254046` | [Rush/Scripts/c120254046.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120254046.lua) | 1 |
| Machine Inspector | `120257057` | [Rush/Scripts/c120257057.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120257057.lua) | 1 |
| Constructor Sentry Dragline | `120247042` | [Rush/Scripts/c120247042.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120247042.lua) | 1 |
| Celeb Rose Enchanter | `120254050` | [Rush/Scripts/c120254050.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120254050.lua) | 1 |
| Sevens Road Witch | `120115001` | [Rush/Scripts/c120115001.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120115001.lua) | 1 |
| Frenzied Panda of the Bamboo Forest | `120294028` | [Rush/Scripts/c120294028.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120294028.lua) | 1 |
| Spice the Special Noodle Ninja Rich Broth | `120300036` | [Rush/Scripts/c120300036.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120300036.lua) | 1 |
| Specter of Heaven's Beginning | `120249035` | [Rush/Scripts/c120249035.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120249035.lua) | 1 |
| Cat Claw Girl | `120235016` | [Rush/Scripts/c120235016.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120235016.lua) | 1 |
| Draconic Fruits | `120294046` | [Rush/Scripts/c120294046.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120294046.lua) | 1 |
| Shield in the Right Hand | `120246048` | [Rush/Scripts/c120246048.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120246048.lua) | 1 |
| Descent of the Sweeping Spirit | `120228057` | [Rush/Scripts/c120228057.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120228057.lua) | 1 |
| Volcano Black Dragon | `120283041` | [Rush/Scripts/c120283041.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120283041.lua) | 1 |
| Space Resonance | `120260019` | [Rush/Scripts/c120260019.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120260019.lua) | 1 |

## Script Examples

### Abyssal Dragon Lord Abyss Poseidra [L] (`120239013`)

Source: [Rush/Scripts/c120239013.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120239013.lua)

```lua
	if chk==0 then return g:GetCount()>0 end
	RD.SendToDeckBottom(g,e,tp,REASON_COST)
	if RD.IsOperatedGroupExists(cm.exfilter,3,nil) then
		e:SetValue(1)
	else
```

### Curse of the Magiclad Dragon (`120304061`)

Source: [Rush/Scripts/c120304061.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120304061.lua)

```lua
		if Duel.SendtoGrave(g,REASON_EFFECT)~=0 then
			if RD.CanSelectAndSpecialSummon(aux.Stringid(m,1),aux.NecroValleyFilter(cm.spfilter),tp,LOCATION_GRAVE,0,1,2,nil,e,POS_FACEUP_DEFENSE,true)~=0
				and RD.IsOperatedGroupExists(cm.exfilter,1,nil) then
				local filter=RD.Filter(cm.posfilter,e,tp)
				RD.CanSelectAndDoAction(aux.Stringid(m,2),HINTMSG_SET,filter,tp,0,LOCATION_MZONE,1,1,nil,function(sg)
```

### Star Protector Recapture (`120306063`)

Source: [Rush/Scripts/c120306063.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306063.lua)

```lua
	RD.SelectAndDoAction(HINTMSG_DESTROY,nil,tp,0,LOCATION_ONFIELD,1,1,nil,function(g)
		if Duel.Destroy(g,REASON_EFFECT)~=0
			and RD.IsOperatedGroupExists(cm.exfilter,1,nil)
			and RD.CanSelectAndSpecialSummon(aux.Stringid(m,1),aux.NecroValleyFilter(cm.spfilter),tp,LOCATION_GRAVE,0,1,1,nil,e,POS_FACEUP)~=0 then
			local tc=Duel.GetOperatedGroup():GetFirst()
```
