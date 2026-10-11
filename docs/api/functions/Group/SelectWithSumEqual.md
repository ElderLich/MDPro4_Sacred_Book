# Group.SelectWithSumEqual

## Signature

```lua
Group.SelectWithSumEqual(Group g, int player, function f, int acc, int min, int max, [... any]) -> Group|nil
```

## Description

Lets player select cards from g whose f-sum equals acc using between min and max cards.
Cards previously set with Duel.SetSelectedCard are forced into the sum, removed from the selectable pool, cleared afterward, and are not included in the returned Group.

## Parameters

- `g` `Group`
- `player` `int`
- `f` `function`
- `acc` `int`
- `min` `int`
- `max` `int`
- `...` `any` optional

## Returns

- `Group|nil` - Selected optional cards, or nil for invalid player.

## Source

- `D:\Programs\GitHub\ygopro-core\libgroup.cpp:921`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **19** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Group.SelectWithSumEqual) with `Group.SelectWithSumEqual`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Prompthorn | `50548657` | [Scripts/c50548657.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50548657.lua) | 1 |
| Blackwing - Gofu the Vague Shadow | `9929398` | [Scripts/c9929398.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9929398.lua) | 1 |
| Rescue Ferret | `56343672` | [Scripts/c56343672.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56343672.lua) | 1 |
| Benghalancer the Resurgent | `73345237` | [Scripts/c73345237.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c73345237.lua) | 1 |
| Blackwing - Vata the Emblem of Wandering | `71187462` | [Scripts/c71187462.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71187462.lua) | 1 |
| Starliege Seyfert | `15381421` | [Scripts/c15381421.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15381421.lua) | 1 |
| Variety Comes Out | `65196094` | [Scripts/c65196094.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65196094.lua) | 1 |
| Block Dragon | `94689206` | [Scripts/c94689206.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c94689206.lua) | 1 |
| Gordian Slicer | `66236707` | [Scripts/c66236707.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66236707.lua) | 1 |
| Luminous Dragon Ritual | `34834619` | [Scripts/c34834619.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34834619.lua) | 1 |
| Spacetime Transcendence | `39041729` | [Scripts/c39041729.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39041729.lua) | 1 |
| Crop Circles | `24082387` | [Scripts/c24082387.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24082387.lua) | 1 |
| Necroid Synchro | `26194151` | [Scripts/c26194151.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c26194151.lua) | 1 |
| Ancient Gear Factory | `30435145` | [Scripts/c30435145.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30435145.lua) | 1 |
| King's Consonance | `24590232` | [Scripts/c24590232.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24590232.lua) | 1 |
| Stardust Shimmer | `89181369` | [Scripts/c89181369.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c89181369.lua) | 1 |
| Void Feast | `31548814` | [Scripts/c31548814.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31548814.lua) | 1 |
| The Puppet Magic of Dark Ruler | `40703393` | [Scripts/c40703393.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40703393.lua) | 1 |
| Tokusano Shinkyojin | `50357013` | [Scripts/c50357013.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50357013.lua) | 1 |

## Script Examples

### Prompthorn (`50548657`)

Source: [Scripts/c50548657.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50548657.lua)

```lua
	if ft<=0 or g:GetCount()==0 then return end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SPSUMMON)
	local sg=g:SelectWithSumEqual(tp,Card.GetLevel,e:GetLabel(),1,ft)
	if sg:GetCount()>0 then
		local fid=e:GetHandler():GetFieldID()
```

### Blackwing - Gofu the Vague Shadow (`9929398`)

Source: [Scripts/c9929398.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9929398.lua)

```lua
	local rg=Duel.GetMatchingGroup(c9929398.cfilter,tp,LOCATION_MZONE,0,e:GetHandler())
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_REMOVE)
	local g2=rg:SelectWithSumEqual(tp,Card.GetLevel,rlv,ct,63)
	g2:AddCard(e:GetHandler())
	Duel.Remove(g2,POS_FACEUP,REASON_COST)
```

### Rescue Ferret (`56343672`)

Source: [Scripts/c56343672.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56343672.lua)

```lua
		local fid=c:GetFieldID()
		Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SPSUMMON)
		local sg=g:SelectWithSumEqual(tp,Card.GetLevel,6,1,ct)
		local tc=sg:GetFirst()
		while tc do
```
