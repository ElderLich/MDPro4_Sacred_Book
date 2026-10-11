# Duel.LinkSummon

## Signature

```lua
Duel.LinkSummon(int player, Card c, Group|nil materials, [Card|nil lcard], [int minc], [int maxc]) -> void
```

## Description

Performs a rule Link Summon for player and c using an optional material group, fixed material, and min/max constraints.
Use this in effect operations after checking Card.IsLinkSummonable. The selected Link Monster's registered procedure still controls final material selection and sends materials to the GY.
The core rejects this during the Damage Step, yields while the Summon is processed, and returns no Lua value.

## Parameters

- `player` `int` - Player performing the Link Summon.
- `c` `Card` - Link Monster to Link Summon.
- `materials` `Group|nil` - Optional temporary material pool. nil uses the Link Monster's normal procedure pool.
- `lcard` `Card|nil` optional - Optional fixed material that must be included in the selected group.
- `minc` `int` optional - Runtime minimum material-card count. default: 0
- `maxc` `int` optional - Runtime maximum material-card count. default: 0

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4869`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **21** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.LinkSummon) with `Duel.LinkSummon`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [W:P Fancy Ball](/examples/cards/4993187) | `4993187` | [Scripts/c4993187.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4993187.lua) | 1 |
| Trickstar Diffusion | `63181559` | [Scripts/c63181559.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63181559.lua) | 1 |
| Link into the VRAINS! | `28827503` | [Scripts/c28827503.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28827503.lua) | 1 |
| Angello Vaalmonica | `3048768` | [Scripts/c3048768.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3048768.lua) | 1 |
| Code of Soul | `74652966` | [Scripts/c74652966.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74652966.lua) | 1 |
| Yum☆Yum☆Yummys | `56870908` | [Scripts/c56870908.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56870908.lua) | 1 |
| Salamangreat Burning Shell | `28534130` | [Scripts/c28534130.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28534130.lua) | 1 |
| Unchained Soul of Rage | `67680512` | [Scripts/c67680512.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67680512.lua) | 1 |
| Tri-Brigade Revolt | `40975243` | [Scripts/c40975243.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40975243.lua) | 1 |
| Sky Striker Special Maneuver - Lemnisgate! | `34433770` | [Scripts/c34433770.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34433770.lua) | 1 |
| Purification Power Patron | `31822037` | [Scripts/c31822037.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31822037.lua) | 1 |
| Unchained Syncretism | `93898740` | [Scripts/c93898740.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93898740.lua) | 1 |
| Unchained Soul of Anguish | `93084621` | [Scripts/c93084621.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93084621.lua) | 1 |
| Unchained Soul of Disaster | `89019964` | [Scripts/c89019964.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c89019964.lua) | 1 |
| Outburst Dragon | `87263576` | [Scripts/c87263576.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87263576.lua) | 1 |
| I:P Masquerena | `65741786` | [Scripts/c65741786.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65741786.lua) | 1 |
| Basiltrice, Familiar of the Evil Eye | `65351555` | [Scripts/c65351555.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65351555.lua) | 1 |
| Vaalmonica Creation | `98167225` | [Scripts/c98167225.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c98167225.lua) | 1 |
| Prank-Kids Plan | `15447747` | [Scripts/c15447747.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15447747.lua) | 1 |
| Evil★Twin Challenge | `98360333` | [Scripts/c98360333.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c98360333.lua) | 1 |
| World Legacy Awakens | `12989604` | [Scripts/c12989604.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12989604.lua) | 1 |

## Script Examples

### W:P Fancy Ball (`4993187`)

Source: [Scripts/c4993187.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4993187.lua)

```lua
	local tc=g:GetFirst()
	if tc then
		Duel.LinkSummon(tp,tc,nil)
	end
end
```

### Trickstar Diffusion (`63181559`)

Source: [Scripts/c63181559.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63181559.lua)

```lua
		local tc=g:GetFirst()
		if tc then
			Duel.LinkSummon(tp,tc,nil)
		end
	end
```

### Link into the VRAINS! (`28827503`)

Source: [Scripts/c28827503.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28827503.lua)

```lua
		e4:SetOperation(c28827503.effop1)
		tc:RegisterEffect(e4,true)
		Duel.LinkSummon(tp,sc,nil,tc)
	end
end
```
