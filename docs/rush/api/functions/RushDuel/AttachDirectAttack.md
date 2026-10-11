# RushDuel.AttachDirectAttack

Alias: `RD.AttachDirectAttack`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AttachDirectAttack(any e, any card, any desc, any reset, any forced) -> any
```

## Description

Rush Duel helper declared in `RDAttach.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
赋予: 直接攻击
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `desc` `any`: Type and behavior are not yet reviewed; see the source.
- `reset` `any`: Type and behavior are not yet reviewed; see the source.
- `forced` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAttach.lua:18`

```lua
function RushDuel.AttachDirectAttack(e, card, desc, reset, forced)
    return RushDuel.CreateSingleEffect(e, desc, card, EFFECT_DIRECT_ATTACK, nil, reset, forced)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **21** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.AttachDirectAttack) with `RushDuel.AttachDirectAttack`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| OuTerverSe Direct Driver | `120109056` | [Rush/Scripts/c120109056.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120109056.lua) | 1 |
| UMP Sky Forbia | `120306017` | [Rush/Scripts/c120306017.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120306017.lua) | 1 |
| Beginning Hiyashi the Sonic Noodle Ninja | `120300035` | [Rush/Scripts/c120300035.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300035.lua) | 1 |
| Doushin Kaika the Shadow Flower Full Moon | `120228037` | [Rush/Scripts/c120228037.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120228037.lua) | 1 |
| Jinzo #7.7 | `120257026` | [Rush/Scripts/c120257026.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120257026.lua) | 1 |
| Shining Shamaness | `120254082` | [Rush/Scripts/c120254082.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120254082.lua) | 1 |
| Gaia, Conqueror of Champions | `120249046` | [Rush/Scripts/c120249046.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120249046.lua) | 1 |
| Cat's Eye | `120150028` | [Rush/Scripts/c120150028.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120150028.lua) | 1 |
| Kimeruler the Dark Raider | `120140001` | [Rush/Scripts/c120140001.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120140001.lua) | 1 |
| Lovely Shoot | `120260048` | [Rush/Scripts/c120260048.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120260048.lua) | 1 |
| Elemental HERO Mariner | `120272047` | [Rush/Scripts/c120272047.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120272047.lua) | 1 |
| Shining Shaman | `120105009` | [Rush/Scripts/c120105009.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120105009.lua) | 1 |
| Hydro Cannon Big Bluefin | `120130032` | [Rush/Scripts/c120130032.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120130032.lua) | 1 |
| Hazy Strike Dragon Miragiastar F | `120205033` | [Rush/Scripts/c120205033.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120205033.lua) | 1 |
| Digracheon the Skysavior Radiaknight | `120301036` | [Rush/Scripts/c120301036.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120301036.lua) | 1 |
| Burst Bunny | `120264037` | [Rush/Scripts/c120264037.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120264037.lua) | 1 |
| Telepathic Agent | `120140030` | [Rush/Scripts/c120140030.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120140030.lua) | 1 |
| Alligator's Sword Dragon | `120206001` | [Rush/Scripts/c120206001.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120206001.lua) | 1 |
| Cyber Tutu | `120102004` | [Rush/Scripts/c120102004.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120102004.lua) | 1 |
| Kimeterasu the Divine Ruler | `120246040` | [Rush/Scripts/c120246040.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120246040.lua) | 1 |
| Direct Dive Dragon | `120109015` | [Rush/Scripts/c120109015.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120109015.lua) | 1 |

## Script Examples

### OuTerverSe Direct Driver (`120109056`)

Source: [Rush/Scripts/c120109056.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120109056.lua)

```lua
				Duel.BreakEffect()
				g:ForEach(function(tc)
					RD.AttachDirectAttack(e,tc,aux.Stringid(m,3),RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
				end)
				RD.CreateLimitAttackCountEffect(e,aux.Stringid(m,4),2,tp,1,0,RESET_PHASE+PHASE_END)
```

### UMP Sky Forbia (`120306017`)

Source: [Rush/Scripts/c120306017.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120306017.lua)

```lua
	local c=e:GetHandler()
	if c:IsFaceup() and c:IsRelateToEffect(e) then
		RD.AttachDirectAttack(e,c,aux.Stringid(m,1),RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
		if Duel.GetLocationCount(tp,LOCATION_SZONE)>0 then
			local filter=RD.Filter(cm.filter,e,c)
```

### Beginning Hiyashi the Sonic Noodle Ninja (`120300035`)

Source: [Rush/Scripts/c120300035.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300035.lua)

```lua
	local c=e:GetHandler()
	if c:IsFaceup() and c:IsRelateToEffect(e) then
		RD.AttachDirectAttack(e,c,aux.Stringid(m,1),RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
		local posfilter=RD.Filter(cm.posfilter,e,tp)
		RD.CanSelectAndDoAction(aux.Stringid(m,2),HINTMSG_POSCHANGE,posfilter,tp,0,LOCATION_MZONE,1,1,nil,function(g)
```
