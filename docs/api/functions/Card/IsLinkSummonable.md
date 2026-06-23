# Card.IsLinkSummonable

## Signature

```lua
Card.IsLinkSummonable(Card c, Group|nil materials, [Card|nil lcard], [int minc], [int maxc]) -> bool
```

## Description

Checks whether Link Monster c can be Link Summoned by the current reason player.
Optional materials, lcard, minc, and maxc restrict the Link Material pool and material count used by the core check.
Use this in effect target and operation branches before calling Duel.LinkSummon. minc and maxc default to 0 when omitted, leaving the registered procedure's own count rules in control.
The core rejects this check during the Damage Step.

## Parameters

- `c` `Card` - Link Monster being tested.
- `materials` `Group|nil` - Optional temporary material pool. nil lets the registered procedure collect its normal pool.
- `lcard` `Card|nil` optional - Optional fixed material that the final selected group must include.
- `minc` `int` optional - Runtime minimum material-card count. default: 0
- `maxc` `int` optional - Runtime maximum material-card count. default: 0

## Returns

- `bool` - true if c has a legal Link Summon under the supplied temporary limits.

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3578`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **20** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.IsLinkSummonable`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [W:P Fancy Ball](/examples/cards/4993187) | `4993187` | [Scripts/c4993187.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4993187.lua) | 61 |
| [Trickstar Diffusion](/examples/cards/63181559) | `63181559` | [Scripts/c63181559.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63181559.lua) | 61 |
| Link into the VRAINS! | `28827503` | [Scripts/c28827503.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28827503.lua) | 55 |
| Angello Vaalmonica | `3048768` | [Scripts/c3048768.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3048768.lua) | 54 |
| Code of Soul | `74652966` | [Scripts/c74652966.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74652966.lua) | 50 |
| Yum☆Yum☆Yummys | `56870908` | [Scripts/c56870908.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56870908.lua) | 49 |
| Salamangreat Burning Shell | `28534130` | [Scripts/c28534130.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28534130.lua) | 48 |
| Unchained Soul of Rage | `67680512` | [Scripts/c67680512.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67680512.lua) | 44 |
| Tri-Brigade Revolt | `40975243` | [Scripts/c40975243.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40975243.lua) | 44 |
| Sky Striker Special Maneuver - Lemnisgate! | `34433770` | [Scripts/c34433770.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34433770.lua) | 43 |
| Power Patron Envoy of Pure Prayers | `31822037` | [Scripts/c31822037.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31822037.lua) | 43 |
| Unchained Soul of Anguish | `93084621` | [Scripts/c93084621.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93084621.lua) | 40 |
| Unchained Soul of Disaster | `89019964` | [Scripts/c89019964.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c89019964.lua) | 40 |
| Outburst Dragon | `87263576` | [Scripts/c87263576.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87263576.lua) | 40 |
| I:P Masquerena | `65741786` | [Scripts/c65741786.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65741786.lua) | 39 |
| Basiltrice, Familiar of the Evil Eye | `65351555` | [Scripts/c65351555.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65351555.lua) | 37 |
| Vaalmonica Creation | `98167225` | [Scripts/c98167225.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c98167225.lua) | 36 |
| Prank-Kids Plan | `15447747` | [Scripts/c15447747.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15447747.lua) | 32 |
| Evil★Twin Challenge | `98360333` | [Scripts/c98360333.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c98360333.lua) | 30 |
| World Legacy Awakens | `12989604` | [Scripts/c12989604.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12989604.lua) | 15 |

## Script Examples

### W:P Fancy Ball (`4993187`)

Source: [Scripts/c4993187.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4993187.lua)

```lua
end
function s.lkfilter(c)
	return c:IsLinkSummonable(nil)
end
function s.mattg(e,c)
```

### Trickstar Diffusion (`63181559`)

Source: [Scripts/c63181559.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63181559.lua)

```lua
end
function s.filter(c)
	return c:IsLinkSummonable(nil) and c:IsSetCard(0xfb)
end
function s.target(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Link into the VRAINS! (`28827503`)

Source: [Scripts/c28827503.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28827503.lua)

```lua
end
function c28827503.lkfilter(c,mc)
	return c:IsLinkSummonable(nil,mc)
end
function c28827503.spfilter(c,e,tp)
```
