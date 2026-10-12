# RushDuel.RevealDeckTopAndCanSelect

Alias: `RD.RevealDeckTopAndCanSelect`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.RevealDeckTopAndCanSelect(any player, any count, any desc, any hint, any filter, any min, any max, ... any) -> any
```

## Description

Rush Duel helper declared in `RDAction.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
操作: 翻开卡组并可以选择卡
```

## Parameters

- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `count` `any`: Type and behavior are not yet reviewed; see the source.
- `desc` `any`: Type and behavior are not yet reviewed; see the source.
- `hint` `any`: Type and behavior are not yet reviewed; see the source.
- `filter` `any`: Type and behavior are not yet reviewed; see the source.
- `min` `any`: Type and behavior are not yet reviewed; see the source.
- `max` `any`: Type and behavior are not yet reviewed; see the source.
- `...` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAction.lua:442`

```lua
function RushDuel.RevealDeckTopAndCanSelect(player, count, desc, hint, filter, min, max, ...)
    Duel.ConfirmDecktop(player, count)
    local g = Duel.GetDecktopGroup(player, count)
    local mg = g:Filter(filter, nil, ...)
    if #mg >= min then
        local sg = RushDuel.CanSelect(desc, hint, player, mg, nil, min, max)
        if sg and #sg > 0 then
            g:Sub(sg)
            return sg, g
        end
    end
    return Group.CreateGroup(), g
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **51** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.RevealDeckTopAndCanSelect) with `RushDuel.RevealDeckTopAndCanSelect`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Soleil, the Fairy of Skysavior](/examples/rush-cards/120235020) | `120235020` | [Rush/Scripts/c120235020.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120235020.lua) | 1 |
| Abysslayer Quintiamat | `120257021` | [Rush/Scripts/c120257021.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120257021.lua) | 1 |
| Rurigra the Eternal | `120285028` | [Rush/Scripts/c120285028.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120285028.lua) | 1 |
| Cornetlass the Music Princess | `120287066` | [Rush/Scripts/c120287066.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120287066.lua) | 1 |
| Rising HERO Argent | `120263010` | [Rush/Scripts/c120263010.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120263010.lua) | 1 |
| Lostream Record | `120309044` | [Rush/Scripts/c120309044.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120309044.lua) | 1 |
| Lovely Ange | `120272026` | [Rush/Scripts/c120272026.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120272026.lua) | 1 |
| Voidvelg Whiterider | `120109060` | [Rush/Scripts/c120109060.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120109060.lua) | 1 |
| Hybridrive Orbuster | `120264007` | [Rush/Scripts/c120264007.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120264007.lua) | 1 |
| Memory of Sunlit | `120300051` | [Rush/Scripts/c120300051.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120300051.lua) | 1 |
| Scissor Hercules | `120298038` | [Rush/Scripts/c120298038.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120298038.lua) | 1 |
| Summoner Monk | `120307009` | [Rush/Scripts/c120307009.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120307009.lua) | 1 |
| Fist the Star Protector's Roaring Gauntlet | `120306011` | [Rush/Scripts/c120306011.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306011.lua) | 1 |
| Leave it to the Sparkhearts! | `120298021` | [Rush/Scripts/c120298021.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120298021.lua) | 1 |
| Weaksauce Brassdes | `120304066` | [Rush/Scripts/c120304066.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120304066.lua) | 1 |
| Imaginary Arc Actor | `120271037` | [Rush/Scripts/c120271037.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120271037.lua) | 1 |
| Kibatsu the Cutting Edge Deity | `120246052` | [Rush/Scripts/c120246052.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120246052.lua) | 1 |
| Encounter of the Stars | `120305025` | [Rush/Scripts/c120305025.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120305025.lua) | 1 |
| Dice Key Mekuru | `120261010` | [Rush/Scripts/c120261010.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120261010.lua) | 1 |
| Dark Magician's Curtain | `120238012` | [Rush/Scripts/c120238012.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120238012.lua) | 1 |
| Meteor Drake | `120253028` | [Rush/Scripts/c120253028.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120253028.lua) | 1 |
| Necromaid Order | `120294051` | [Rush/Scripts/c120294051.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120294051.lua) | 1 |
| Evasive Chaos Ninjutsu Art of Goshinichu | `120277054` | [Rush/Scripts/c120277054.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120277054.lua) | 1 |
| Mercissus the Planetairy | `120293053` | [Rush/Scripts/c120293053.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120293053.lua) | 1 |
| ...and 27 more |  |  |  |

## Script Examples

### Soleil, the Fairy of Skysavior (`120235020`)

Source: [Rush/Scripts/c120235020.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120235020.lua)

```lua
		if Duel.GetFieldGroupCount(tp,LOCATION_DECK,0)<4 then return end
		Duel.BreakEffect()
		local sg,g=RD.RevealDeckTopAndCanSelect(tp,4,aux.Stringid(m,1),HINTMSG_ATOHAND,cm.thfilter,1,1)
		if sg:GetCount()>0 then
			Duel.DisableShuffleCheck()
```

### Abysslayer Quintiamat (`120257021`)

Source: [Rush/Scripts/c120257021.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120257021.lua)

```lua
function cm.operation(e,tp,eg,ep,ev,re,r,rp)
	if RD.Draw()~=0 and Duel.GetFieldGroupCount(tp,LOCATION_DECK,0)>4 and Duel.SelectYesNo(tp,aux.Stringid(m,1)) then
		local sg,g=RD.RevealDeckTopAndCanSelect(tp,5,aux.Stringid(m,2),HINTMSG_ATOHAND,cm.thfilter,1,3)
		if sg:GetCount()>0 then
			Duel.DisableShuffleCheck()
```

### Rurigra the Eternal (`120285028`)

Source: [Rush/Scripts/c120285028.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120285028.lua)

```lua
		if RD.SendToDeckBottom(g,e,tp,REASON_EFFECT)~=0
			and Duel.GetFieldGroupCount(tp,LOCATION_DECK,0)>3 then
			local sg,lg=RD.RevealDeckTopAndCanSelect(tp,4,aux.Stringid(m,1),HINTMSG_ATOHAND,cm.thfilter,1,1)
			if sg:GetCount()>0 then
				Duel.DisableShuffleCheck()
```
