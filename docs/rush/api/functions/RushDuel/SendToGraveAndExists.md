# RushDuel.SendToGraveAndExists

Alias: `RD.SendToGraveAndExists`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.SendToGraveAndExists(any target, any filter, any count, any expect) -> any
```

## Description

Rush Duel helper declared in `RDAction.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
操作: 送去墓地
```

## Parameters

- `target` `any`: Type and behavior are not yet reviewed; see the source.
- `filter` `any`: Type and behavior are not yet reviewed; see the source.
- `count` `any`: Type and behavior are not yet reviewed; see the source.
- `expect` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAction.lua:299`

```lua
function RushDuel.SendToGraveAndExists(target, filter, count, expect)
    local g = RushDuel.ToMaximunGroup(target)
    return Duel.SendtoGrave(g, REASON_EFFECT) ~= 0 and RushDuel.IsOperatedGroupExists(filter, count, expect)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **33** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.SendToGraveAndExists) with `RushDuel.SendToGraveAndExists`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Chaos Emperor Dragon - Envoy of the End](/examples/rush-cards/120305001) | `120305001` | [Rush/Scripts/c120305001.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120305001.lua) | 1 |
| [Nobody Phantom Thief](/examples/rush-cards/120244060) | `120244060` | [Rush/Scripts/c120244060.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120244060.lua) | 1 |
| [Nobody Phantom Thief](/examples/rush-cards/120273005) | `120273005` | [Rush/Scripts/c120273005.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120273005.lua) | 1 |
| [Lovely Rabbit](/examples/rush-cards/120300018) | `120300018` | [Rush/Scripts/c120300018.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120300018.lua) | 1 |
| Instant Fusion | `120305053` | [Rush/Scripts/c120305053.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120305053.lua) | 1 |
| Etraynze the Shadow Flower Ninja | `120170029` | [Rush/Scripts/c120170029.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120170029.lua) | 1 |
| Goe Goe the Rumored Ninja | `120306029` | [Rush/Scripts/c120306029.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306029.lua) | 1 |
| Hysteric Party | `120279035` | [Rush/Scripts/c120279035.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120279035.lua) | 1 |
| Critical Service | `120260022` | [Rush/Scripts/c120260022.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120260022.lua) | 1 |
| Lostream Record | `120309044` | [Rush/Scripts/c120309044.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120309044.lua) | 1 |
| Vic Viper Beginning | `120294026` | [Rush/Scripts/c120294026.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120294026.lua) | 1 |
| Lostream Stream | `120309046` | [Rush/Scripts/c120309046.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120309046.lua) | 1 |
| Legendary Scout | `120271047` | [Rush/Scripts/c120271047.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120271047.lua) | 1 |
| Neo-Spacian Aqua Dolphin | `120264017` | [Rush/Scripts/c120264017.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120264017.lua) | 1 |
| Metarion King Cobrastar | `120205039` | [Rush/Scripts/c120205039.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120205039.lua) | 1 |
| Voidalfr Heavenstar | `120300006` | [Rush/Scripts/c120300006.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120300006.lua) | 1 |
| Yoctron | `120150017` | [Rush/Scripts/c120150017.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120150017.lua) | 1 |
| Contact Dark Matter Wyvern | `120264003` | [Rush/Scripts/c120264003.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120264003.lua) | 1 |
| Descent of the Sweeping Spirit | `120228057` | [Rush/Scripts/c120228057.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120228057.lua) | 1 |
| Cyber Rush Dragon | `120231021` | [Rush/Scripts/c120231021.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120231021.lua) | 1 |
| Dian Keto the Security Master | `120170026` | [Rush/Scripts/c120170026.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120170026.lua) | 1 |
| Card 120106002 | `120106002` | [Rush/Scripts/c120106002.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120106002.lua) | 1 |
| Transam Nebula Fusion | `120272048` | [Rush/Scripts/c120272048.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120272048.lua) | 1 |
| Endless Romance Blitz | `120205034` | [Rush/Scripts/c120205034.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120205034.lua) | 1 |
| ...and 9 more |  |  |  |

## Script Examples

### Chaos Emperor Dragon - Envoy of the End (`120305001`)

Source: [Rush/Scripts/c120305001.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120305001.lua)

```lua
function cm.operation(e,tp,eg,ep,ev,re,r,rp)
	local g=Duel.GetMatchingGroup(cm.filter,tp,LOCATION_HAND+LOCATION_ONFIELD,LOCATION_HAND+LOCATION_ONFIELD,nil)
	if g:GetCount()>0 and RD.SendToGraveAndExists(g) then
		local ct=Duel.GetOperatedGroup():FilterCount(Card.IsControler,nil,1-tp)
		if ct>0 then
```

### Nobody Phantom Thief (`120244060`)

Source: [Rush/Scripts/c120244060.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120244060.lua)

```lua
		RD.SelectAndDoAction(HINTMSG_TOGRAVE,cm.filter,tp,LOCATION_HAND,0,1,99,nil,function(g)
			Duel.BreakEffect()
			if RD.SendToGraveAndExists(g) and Duel.GetFieldGroupCount(tp,LOCATION_MZONE,0)==0 then
				local e1=Effect.CreateEffect(e:GetHandler())
				e1:SetDescription(aux.Stringid(m,1))
```

### Nobody Phantom Thief (`120273005`)

Source: [Rush/Scripts/c120273005.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120273005.lua)

```lua
		RD.SelectAndDoAction(HINTMSG_TOGRAVE,cm.filter,tp,LOCATION_HAND,0,1,99,nil,function(g)
			Duel.BreakEffect()
			if RD.SendToGraveAndExists(g) and Duel.GetFieldGroupCount(tp,LOCATION_MZONE,0)==0 then
				local e1=Effect.CreateEffect(e:GetHandler())
				e1:SetDescription(aux.Stringid(m,1))
```
