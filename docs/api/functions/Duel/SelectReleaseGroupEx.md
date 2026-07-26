# Duel.SelectReleaseGroupEx

## Signature

```lua
Duel.SelectReleaseGroupEx(int player, [function|nil f], int min, int max, int reason, bool use_hand, [Card|Group|nil ex], ... any) -> Group
```

## Description

Lets player select min to max cards that can be Tributed/Released for effect purposes, optionally excluding ex and applying filter f.

## Parameters

- `player` `int`
- `f` `function|nil` optional
- `min` `int`
- `max` `int`
- `reason` `int`
- `use_hand` `bool`
- `ex` `Card|Group|nil` optional
- `...` `any`

## Returns

- `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4979`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **53** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.SelectReleaseGroupEx`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Clown Crew Malabarisme | `83232904` | [Scripts/c83232904.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c83232904.lua) | 1 |
| Tensei Ryu-Ge Anva | `56322832` | [Scripts/c56322832.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56322832.lua) | 1 |
| Abyssrhine, the Atlantean Spirit | `17080584` | [Scripts/c17080584.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17080584.lua) | 1 |
| LaSolfachord Angelia | `27993919` | [Scripts/c27993919.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27993919.lua) | 1 |
| Clown Crew Finale | `84031736` | [Scripts/c84031736.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84031736.lua) | 1 |
| Hieratic Dragon of Nebthet | `31516413` | [Scripts/c31516413.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31516413.lua) | 1 |
| Hieratic Dragon of Su | `3300267` | [Scripts/c3300267.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3300267.lua) | 1 |
| Muckraker From the Underworld | `71607202` | [Scripts/c71607202.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71607202.lua) | 1 |
| Magnificent Machine Angel | `27331568` | [Scripts/c27331568.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27331568.lua) | 1 |
| Gemini Ablation | `80758812` | [Scripts/c80758812.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80758812.lua) | 1 |
| Volcanic Queen | `63014935` | [Scripts/c63014935.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63014935.lua) | 1 |
| Kanzashi the Rikka Queen | `6284176` | [Scripts/c6284176.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6284176.lua) | 1 |
| Archfiend's Origin | `79621896` | [Scripts/c79621896.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c79621896.lua) | 1 |
| Yubel | `78371393` | [Scripts/c78371393.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78371393.lua) | 1 |
| Hieratic Seal of the Heavenly Spheres | `24361622` | [Scripts/c24361622.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24361622.lua) | 1 |
| D/D/D Dragon King Pendragon | `56619314` | [Scripts/c56619314.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56619314.lua) | 3 |
| Evoltile Pholis | `89776023` | [Scripts/c89776023.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c89776023.lua) | 1 |
| Mitsurugi Prayers | `45171524` | [Scripts/c45171524.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45171524.lua) | 1 |
| Mitsurugi Sacred Boundary | `12210097` | [Scripts/c12210097.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12210097.lua) | 1 |
| Nekroz of Valkyrus | `25857246` | [Scripts/c25857246.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25857246.lua) | 1 |
| Deception of the Sinful Spoils | `66328392` | [Scripts/c66328392.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66328392.lua) | 1 |
| Jinzo - Layered | `99666430` | [Scripts/c99666430.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c99666430.lua) | 2 |
| Magical Dimension | `28553439` | [Scripts/c28553439.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28553439.lua) | 1 |
| Nekroz of Areadbhair | `39468724` | [Scripts/c39468724.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39468724.lua) | 2 |
| ...and 29 more |  |  |  |

## Script Examples

### Clown Crew Malabarisme (`83232904`)

Source: [Scripts/c83232904.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c83232904.lua)

```lua
	if chk==0 then return aux.bfgcost(e,tp,eg,ep,ev,re,r,rp,chk) and Duel.CheckReleaseGroupEx(tp,s.cfilter,1,REASON_COST,true,nil,tp) end
	aux.bfgcost(e,tp,eg,ep,ev,re,r,rp,chk)
	local g=Duel.SelectReleaseGroupEx(tp,s.cfilter,1,1,REASON_COST,true,nil,tp)
	Duel.Release(g,REASON_COST)
end
```

### Tensei Ryu-Ge Anva (`56322832`)

Source: [Scripts/c56322832.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56322832.lua)

```lua
function s.spcost(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.CheckReleaseGroupEx(tp,s.spfilter,1,REASON_COST,true,e:GetHandler(),tp) end
	local g=Duel.SelectReleaseGroupEx(tp,s.spfilter,1,1,REASON_COST,true,e:GetHandler(),tp)
	Duel.Release(g,REASON_COST)
end
```

### Abyssrhine, the Atlantean Spirit (`17080584`)

Source: [Scripts/c17080584.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17080584.lua)

```lua
	local c=e:GetHandler()
	if chk==0 then return c:IsReleasable() and Duel.CheckReleaseGroupEx(tp,s.cfilter,1,REASON_COST,true,c,e,tp) end
	local g=Duel.SelectReleaseGroupEx(tp,s.cfilter,1,1,REASON_COST,true,c,e,tp)
	g:AddCard(c)
	Duel.Release(g,REASON_COST)
```
