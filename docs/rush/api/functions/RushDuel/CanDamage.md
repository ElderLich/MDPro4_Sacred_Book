# RushDuel.CanDamage

Alias: `RD.CanDamage`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CanDamage(any desc, any player, any damage, any break_effect) -> any
```

## Description

Rush Duel helper declared in `RDAction.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
可选操作: 伤害
```

## Parameters

- `desc` `any`: Type and behavior are not yet reviewed; see the source.
- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `damage` `any`: Type and behavior are not yet reviewed; see the source.
- `break_effect` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAction.lua:616`

```lua
function RushDuel.CanDamage(desc, player, damage, break_effect)
    if damage > 0 and Duel.SelectYesNo(player, desc) then
        if break_effect then
            Duel.BreakEffect()
        end
        return Duel.Damage(1 - player, damage, REASON_EFFECT)
    end
    return 0
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **13** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CanDamage) with `RushDuel.CanDamage`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Madrhea Amelo](/examples/rush-cards/120300028) | `120300028` | [Rush/Scripts/c120300028.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300028.lua) | 1 |
| Voidvelg Divine Requiem | `120109037` | [Rush/Scripts/c120109037.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120109037.lua) | 1 |
| Necromaid Lurker | `120294044` | [Rush/Scripts/c120294044.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120294044.lua) | 1 |
| Mythical Chimera Snake | `120286006` | [Rush/Scripts/c120286006.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120286006.lua) | 1 |
| Galactica Oblivion Ark | `120277008` | [Rush/Scripts/c120277008.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120277008.lua) | 1 |
| Wicked Fire Blast of Zera | `120287013` | [Rush/Scripts/c120287013.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120287013.lua) | 1 |
| Requiem Strike Back | `120277060` | [Rush/Scripts/c120277060.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120277060.lua) | 1 |
| Micronova | `120300044` | [Rush/Scripts/c120300044.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300044.lua) | 1 |
| Attract Golem | `120271026` | [Rush/Scripts/c120271026.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120271026.lua) | 1 |
| Giant Dynamix Impact | `120274049` | [Rush/Scripts/c120274049.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120274049.lua) | 1 |
| Tamabot Boost Dragon | `120285038` | [Rush/Scripts/c120285038.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120285038.lua) | 1 |
| Dentacle the Parasitic Extraterrestrial | `120264035` | [Rush/Scripts/c120264035.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120264035.lua) | 1 |
| Summoning Sorcerer Doretheo | `120244032` | [Rush/Scripts/c120244032.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120244032.lua) | 1 |

## Script Examples

### Madrhea Amelo (`120300028`)

Source: [Rush/Scripts/c120300028.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300028.lua)

```lua
	RD.SelectAndDoAction(HINTMSG_DESTROY,cm.desfilter,tp,0,LOCATION_MZONE,1,1,nil,function(g)
		if Duel.Destroy(g,REASON_EFFECT)~=0 and g:IsExists(cm.exfilter,1,nil) then
			RD.CanDamage(aux.Stringid(m,1),tp,600)
		end
	end)
```

### Voidvelg Divine Requiem (`120109037`)

Source: [Rush/Scripts/c120109037.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120109037.lua)

```lua
		local g=Duel.GetMatchingGroup(Card.IsFaceup,tp,0,LOCATION_MZONE,nil)
		local dam=g:GetSum(Card.GetAttack)
		RD.CanDamage(aux.Stringid(m,2),tp,dam,true)
	end
end
```

### Necromaid Lurker (`120294044`)

Source: [Rush/Scripts/c120294044.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120294044.lua)

```lua
	RD.SelectAndDoAction(HINTMSG_DESTROY,nil,tp,0,LOCATION_ONFIELD,1,1,nil,function(g)
		if Duel.Destroy(g,REASON_EFFECT)~=0 then
			RD.CanDamage(aux.Stringid(m,1),tp,700,true)
		end
	end)
```
