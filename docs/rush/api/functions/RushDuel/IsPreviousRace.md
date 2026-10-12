# RushDuel.IsPreviousRace

Alias: `RD.IsPreviousRace`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsPreviousRace(any card, any race) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 位置变化前的种族
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `race` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:206`

```lua
function RushDuel.IsPreviousRace(card, race)
    return (card:GetPreviousRaceOnField() & race) ~= 0
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **14** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.IsPreviousRace) with `RushDuel.IsPreviousRace`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Earth Pressure Explosion | `120155058` | [Rush/Scripts/c120155058.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120155058.lua) | 1 |
| Last Day of the Pretty☆Witch | `120170046` | [Rush/Scripts/c120170046.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120170046.lua) | 1 |
| Mother's Storm | `120217062` | [Rush/Scripts/c120217062.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120217062.lua) | 1 |
| Dark Ruler Sword Swipe | `120188030` | [Rush/Scripts/c120188030.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120188030.lua) | 1 |
| RB Dragophone | `120225032` | [Rush/Scripts/c120225032.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120225032.lua) | 1 |
| Transam Alive | `120216028` | [Rush/Scripts/c120216028.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120216028.lua) | 1 |
| Breaking News! | `120199063` | [Rush/Scripts/c120199063.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120199063.lua) | 1 |
| Dark Nebula | `120235059` | [Rush/Scripts/c120235059.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120235059.lua) | 1 |
| Archfiend's Revival | `120170062` | [Rush/Scripts/c120170062.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120170062.lua) | 1 |
| Constructor Resurrection | `120151033` | [Rush/Scripts/c120151033.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120151033.lua) | 1 |
| Quantum Hole | `120150020` | [Rush/Scripts/c120150020.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120150020.lua) | 1 |
| Vengeful Dragon's Counterattack | `120110014` | [Rush/Scripts/c120110014.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120110014.lua) | 1 |
| Trumpet Charge | `120184005` | [Rush/Scripts/c120184005.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120184005.lua) | 1 |
| Psychicounter | `120183059` | [Rush/Scripts/c120183059.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120183059.lua) | 1 |

## Script Examples

### Earth Pressure Explosion (`120155058`)

Source: [Rush/Scripts/c120155058.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120155058.lua)

```lua
--Activate
function cm.confilter(c,tp,re,rp)
	return c:IsPreviousPosition(POS_ATTACK) and RD.IsPreviousRace(c,RACE_PYRO)
		and RD.IsPreviousControler(c,tp) and c:IsPreviousLocation(LOCATION_MZONE)
		and (c==Duel.GetAttackTarget()
```

### Last Day of the Pretty☆Witch (`120170046`)

Source: [Rush/Scripts/c120170046.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120170046.lua)

```lua
	RD.SelectAndDoAction(HINTMSG_DESTROY,cm.filter,tp,0,LOCATION_MZONE,1,1,nil,function(g)
		if Duel.Destroy(g,REASON_EFFECT)~=0
			and RD.IsPreviousRace(g:GetFirst(),RACE_SPELLCASTER)
			and Duel.GetFieldGroupCount(tp,0,LOCATION_MZONE)>0
			and Duel.SelectYesNo(tp,aux.Stringid(m,1)) then
```

### Mother's Storm (`120217062`)

Source: [Rush/Scripts/c120217062.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120217062.lua)

```lua
	RD.SelectAndDoAction(HINTMSG_DESTROY,cm.filter,tp,0,LOCATION_MZONE,1,1,nil,function(g)
		if Duel.Destroy(g,REASON_EFFECT)~=0
			and RD.IsPreviousRace(g:GetFirst(),RACE_MACHINE)
			and Duel.GetFieldGroupCount(tp,0,LOCATION_MZONE)>0
			and Duel.SelectYesNo(tp,aux.Stringid(m,1)) then
```
