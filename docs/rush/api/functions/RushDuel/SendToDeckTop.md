# RushDuel.SendToDeckTop

Alias: `RD.SendToDeckTop`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.SendToDeckTop(any target, any effect, any player, any reason) -> any
```

## Description

Rush Duel helper declared in `RDAction.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
操作: 返回卡组上面 (排序)
```

## Parameters

- `target` `any`: Type and behavior are not yet reviewed; see the source.
- `effect` `any`: Type and behavior are not yet reviewed; see the source.
- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `reason` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAction.lua:386`

```lua
function RushDuel.SendToDeckTop(target, effect, player, reason)
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
    local og, ct = RushDuel.SendToDeckSort(g, SEQ_DECKTOP, REASON_EFFECT, player)
    return ct
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **27** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.SendToDeckTop) with `RushDuel.SendToDeckTop`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Major Breaking News!](/examples/rush-cards/120304060) | `120304060` | [Rush/Scripts/c120304060.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304060.lua) | 1 |
| Ether Escape | `120235062` | [Rush/Scripts/c120235062.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120235062.lua) | 1 |
| Eria the Water Spiritualist | `120301010` | [Rush/Scripts/c120301010.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120301010.lua) | 1 |
| Spice Cross Black Pepper | `120261061` | [Rush/Scripts/c120261061.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120261061.lua) | 1 |
| JAM:P Set! | `120183041` | [Rush/Scripts/c120183041.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120183041.lua) | 1 |
| Twilight Companion - Dralia | `120304068` | [Rush/Scripts/c120304068.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304068.lua) | 1 |
| Reporter Recorder | `120304010` | [Rush/Scripts/c120304010.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304010.lua) | 1 |
| Master Craftsman Kotetsu | `120238036` | [Rush/Scripts/c120238036.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120238036.lua) | 1 |
| The Nomnom Liliputian | `120309054` | [Rush/Scripts/c120309054.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120309054.lua) | 1 |
| Reporter Wars Scoopies \[R\] | `120304009` | [Rush/Scripts/c120304009.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304009.lua) | 1 |
| Unfulfilled Goblin | `120203039` | [Rush/Scripts/c120203039.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120203039.lua) | 1 |
| Alchemicalize Orb | `120272037` | [Rush/Scripts/c120272037.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120272037.lua) | 1 |
| Black Dragon's Roar | `120203053` | [Rush/Scripts/c120203053.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120203053.lua) | 1 |
| Dice Key Kuu | `120261011` | [Rush/Scripts/c120261011.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120261011.lua) | 1 |
| The Imprisoned Dragon Princess | `120306009` | [Rush/Scripts/c120306009.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120306009.lua) | 1 |
| Deep Space Impact | `120260023` | [Rush/Scripts/c120260023.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120260023.lua) | 1 |
| Sparkle the Super Assistant | `120254065` | [Rush/Scripts/c120254065.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120254065.lua) | 2 |
| Worker Warrior - Multitasking Manager | `120304028` | [Rush/Scripts/c120304028.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304028.lua) | 1 |
| Ether F Striker | `120205044` | [Rush/Scripts/c120205044.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120205044.lua) | 1 |
| Avian Spell Tactics | `120170053` | [Rush/Scripts/c120170053.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120170053.lua) | 1 |
| The Connected Liliputians | `120309053` | [Rush/Scripts/c120309053.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120309053.lua) | 1 |
| Clean Beret - Colonel Mop | `120150021` | [Rush/Scripts/c120150021.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120150021.lua) | 1 |
| Chemipet Purr | `120249009` | [Rush/Scripts/c120249009.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120249009.lua) | 1 |
| Psychic Divergence | `120140037` | [Rush/Scripts/c120140037.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120140037.lua) | 1 |
| ...and 3 more |  |  |  |

## Script Examples

### Major Breaking News! (`120304060`)

Source: [Rush/Scripts/c120304060.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304060.lua)

```lua
function cm.activate(e,tp,eg,ep,ev,re,r,rp)
	RD.SelectAndDoAction(HINTMSG_TODECK,aux.NecroValleyFilter(Card.IsAbleToDeck),tp,0,LOCATION_GRAVE,2,2,nil,function(g)
		if RD.SendToDeckTop(g,e,tp,REASON_EFFECT)~=0 then
			RD.CanSelectAndSpecialSummon(aux.Stringid(m,1),cm.spfilter,tp,LOCATION_HAND,0,1,2,nil,e,POS_FACEUP_DEFENSE,true)
		end
```

### Ether Escape (`120235062`)

Source: [Rush/Scripts/c120235062.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120235062.lua)

```lua
		and Duel.IsExistingMatchingCard(cm.exfilter,tp,LOCATION_MZONE,0,1,nil) then
		RD.CanSelectAndDoAction(aux.Stringid(m,1),HINTMSG_TODECK,cm.tdfilter,tp,0,LOCATION_ONFIELD,1,1,nil,function(g)
			RD.SendToDeckTop(g,e,tp,REASON_EFFECT)
		end)
	end
```

### Eria the Water Spiritualist (`120301010`)

Source: [Rush/Scripts/c120301010.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120301010.lua)

```lua
function cm.operation(e,tp,eg,ep,ev,re,r,rp)
	RD.SelectAndDoAction(HINTMSG_TODECK,aux.NecroValleyFilter(cm.filter),tp,0,LOCATION_GRAVE,1,1,nil,function(g)
		RD.SendToDeckTop(g,e,tp,REASON_EFFECT)
		local tc=g:GetFirst()
		local sumlimit=function(e,c)
```
