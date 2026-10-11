# RushDuel.SelectGroupAndDoAction

Alias: `RD.SelectGroupAndDoAction`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.SelectGroupAndDoAction(any hint, any filter, any check, any tp, any s_range, any o_range, any min, any max, any expect, any action) -> any
```

## Description

Rush Duel helper declared in `RDAction.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
操作: 选择子卡片组
```

## Parameters

- `hint` `any`: Type and behavior are not yet reviewed; see the source.
- `filter` `any`: Type and behavior are not yet reviewed; see the source.
- `check` `any`: Type and behavior are not yet reviewed; see the source.
- `tp` `any`: Type and behavior are not yet reviewed; see the source.
- `s_range` `any`: Type and behavior are not yet reviewed; see the source.
- `o_range` `any`: Type and behavior are not yet reviewed; see the source.
- `min` `any`: Type and behavior are not yet reviewed; see the source.
- `max` `any`: Type and behavior are not yet reviewed; see the source.
- `expect` `any`: Type and behavior are not yet reviewed; see the source.
- `action` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAction.lua:112`

```lua
function RushDuel.SelectGroupAndDoAction(hint, filter, check, tp, s_range, o_range, min, max, expect, action)
    local hint_selection = RushDuel._private_is_include_public(s_range, o_range)
    return RushDuel._private_action_select_group(hint, filter, check, tp, s_range, o_range, min, max, expect, hint_selection, false, action)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **40** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.SelectGroupAndDoAction) with `RushDuel.SelectGroupAndDoAction`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Lufer the Symbol of the Devils](/examples/rush-cards/120309059) | `120309059` | [Rush/Scripts/c120309059.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120309059.lua) | 1 |
| [Analyze Phlogiston](/examples/rush-cards/120226001) | `120226001` | [Rush/Scripts/c120226001.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120226001.lua) | 1 |
| [Planet Aegis](/examples/rush-cards/120297006) | `120297006` | [Rush/Scripts/c120297006.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120297006.lua) | 1 |
| [Rising Protect](/examples/rush-cards/120304055) | `120304055` | [Rush/Scripts/c120304055.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304055.lua) | 1 |
| [Tubardiche the Music Princess](/examples/rush-cards/120247025) | `120247025` | [Rush/Scripts/c120247025.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120247025.lua) | 1 |
| [Spiritualization Training](/examples/rush-cards/120301020) | `120301020` | [Rush/Scripts/c120301020.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120301020.lua) | 1 |
| [Animagica Majesty](/examples/rush-cards/120277063) | `120277063` | [Rush/Scripts/c120277063.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120277063.lua) | 1 |
| Darkness Jointech Tyrant | `120257018` | [Rush/Scripts/c120257018.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120257018.lua) | 1 |
| The Dragiastar | `120235035` | [Rush/Scripts/c120235035.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120235035.lua) | 1 |
| Excutie Lumière | `120231031` | [Rush/Scripts/c120231031.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120231031.lua) | 1 |
| Sportsdragon Defender | `120130019` | [Rush/Scripts/c120130019.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120130019.lua) | 1 |
| Cyber Tactical Dragon | `120244044` | [Rush/Scripts/c120244044.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120244044.lua) | 1 |
| Spice Cross Black Pepper | `120261061` | [Rush/Scripts/c120261061.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120261061.lua) | 1 |
| Ring of Storms | `120235055` | [Rush/Scripts/c120235055.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120235055.lua) | 1 |
| The Ultimate Flag | `120294019` | [Rush/Scripts/c120294019.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120294019.lua) | 1 |
| Prime Roast Beef Horseman | `120205042` | [Rush/Scripts/c120205042.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120205042.lua) | 1 |
| Shadowforce Explosion | `120300042` | [Rush/Scripts/c120300042.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300042.lua) | 1 |
| Vortex Chaos Shooter | `120277006` | [Rush/Scripts/c120277006.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120277006.lua) | 1 |
| Dark Matter Requiem Omega | `120264040` | [Rush/Scripts/c120264040.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120264040.lua) | 1 |
| Triangle Reborn | `120155051` | [Rush/Scripts/c120155051.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120155051.lua) | 1 |
| Explosive Destructor Wyrm Dangerous Bakhamut | `120247038` | [Rush/Scripts/c120247038.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120247038.lua) | 1 |
| Animagica Trader | `120277026` | [Rush/Scripts/c120277026.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120277026.lua) | 1 |
| Destructor Detonator Heavy Contractor | `120247039` | [Rush/Scripts/c120247039.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120247039.lua) | 1 |
| Tail Swipe | `120277059` | [Rush/Scripts/c120277059.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120277059.lua) | 1 |
| ...and 16 more |  |  |  |

## Script Examples

### Lufer the Symbol of the Devils (`120309059`)

Source: [Rush/Scripts/c120309059.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120309059.lua)

```lua
end
function cm.activate(e,tp,eg,ep,ev,re,r,rp)
	RD.SelectGroupAndDoAction(aux.Stringid(m,1),cm.filter,cm.check,tp,LOCATION_MZONE,0,2,2,nil,function(g)
		local reset=RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END
		g:ForEach(function(tc)
```

### Analyze Phlogiston (`120226001`)

Source: [Rush/Scripts/c120226001.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120226001.lua)

```lua
	local lv=g:GetSum(Card.GetLevel,nil)
	local check=RD.Check(cm.check,lv)
	RD.SelectGroupAndDoAction(HINTMSG_TODECK,aux.NecroValleyFilter(cm.filter),check,tp,LOCATION_GRAVE,0,3,3,nil,function(sg)
		if RD.SendToDeckAndExists(sg,e,tp,REASON_EFFECT) then
			Duel.BreakEffect()
```

### Planet Aegis (`120297006`)

Source: [Rush/Scripts/c120297006.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120297006.lua)

```lua
end
function cm.operation(e,tp,eg,ep,ev,re,r,rp)
	RD.SelectGroupAndDoAction(aux.Stringid(m,1),cm.filter,cm.check,tp,LOCATION_ONFIELD,0,1,2,nil,function(g)
		g:ForEach(function(tc)
			local e1=Effect.CreateEffect(e:GetHandler())
```
