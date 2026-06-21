# Auxiliary.dlvcheck

## Signature

```lua
Auxiliary.dlvcheck(Group g) -> void
```

## Description

Returns true if every card in g has a different Level.

## Parameters

- `g` `Group`

## Source

- `Utilities/utility.lua:1130`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **11** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.dlvcheck`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Gouki Sheik Ogre | `7382007` | [Scripts/c7382007.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7382007.lua) | 59 |
| Astrolasma Urania | `18738846` | [Scripts/c18738846.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18738846.lua) | 55 |
| Dogmatikaturgy | `42158279` | [Scripts/c42158279.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42158279.lua) | 50 |
| Junk Speeder | `77075360` | [Scripts/c77075360.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77075360.lua) | 49 |
| Bloom Harmonist the Melodious Composer | `34974462` | [Scripts/c34974462.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34974462.lua) | 46 |
| Royal Straight Slasher | `11020863` | [Scripts/c11020863.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11020863.lua) | 46 |
| Message in a Bottle | `97433739` | [Scripts/c97433739.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97433739.lua) | 43 |
| Indulged Darklord | `82773292` | [Scripts/c82773292.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82773292.lua) | 42 |
| Cybernetic Overflow | `82428674` | [Scripts/c82428674.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82428674.lua) | 37 |
| Resonance Device | `26864586` | [Scripts/c26864586.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c26864586.lua) | 29 |
| Gouki Re-Match | `62376646` | [Scripts/c62376646.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62376646.lua) | 28 |

## Script Examples

### Gouki Sheik Ogre (`7382007`)

Source: [Scripts/c7382007.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7382007.lua)

```lua
	if g:GetCount()==0 then return end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SPSUMMON)
	local sg=g:SelectSubGroup(tp,aux.dlvcheck,false,1,ft)
	if Duel.SpecialSummon(sg,0,tp,tp,false,false,POS_FACEUP)~=0 then
		for tc in aux.Next(sg) do
```

### Astrolasma Urania (`18738846`)

Source: [Scripts/c18738846.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18738846.lua)

```lua
	local g=Duel.GetMatchingGroup(s.cfilter,tp,LOCATION_HAND,0,nil)
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_CONFIRM)
	aux.GCheckAdditional=aux.dlvcheck
	local sg=g:SelectSubGroup(tp,aux.TRUE,false,1,ct)
	aux.GCheckAdditional=nil
```

### Dogmatikaturgy (`42158279`)

Source: [Scripts/c42158279.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42158279.lua)

```lua
end
function c42158279.fselect(g)
	return aux.dlvcheck(g) and g:IsExists(c42158279.fcheck,1,nil,g)
end
function c42158279.fcheck(c,g)
```
