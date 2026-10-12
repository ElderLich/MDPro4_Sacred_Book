# Auxiliary.GetAttributeCount

## Signature

```lua
Auxiliary.GetAttributeCount(Group g) -> void
```

## Description

Returns how many different Attributes are represented among the cards in g; an empty group returns 0.

## Parameters

- `g` `Group`

## Source

- `Utilities/utility.lua:587`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **9** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.GetAttributeCount) with `Auxiliary.GetAttributeCount`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Elemental HERO Sunrise | `22908820` | [Scripts/c22908820.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c22908820.lua) | 1 |
| Possessed Partnerships | `65046521` | [Scripts/c65046521.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c65046521.lua) | 1 |
| Charmer Quartet in Bloom | `27519978` | [Scripts/c27519978.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c27519978.lua) | 1 |
| Ancient Warriors Saga - Borrowing of Arrows | `33609093` | [Scripts/c33609093.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c33609093.lua) | 1 |
| Pressured Planet Wraitsoth | `71832012` | [Scripts/c71832012.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c71832012.lua) | 1 |
| Elemental HERO Shining Neos Wingman | `56733747` | [Scripts/c56733747.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c56733747.lua) | 1 |
| Ancient Warriors Saga - Sun-Liu Alliance | `58116537` | [Scripts/c58116537.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c58116537.lua) | 1 |
| Dark Doriado | `62312469` | [Scripts/c62312469.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c62312469.lua) | 1 |
| Awakening of the Possessed | `62256492` | [Scripts/c62256492.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c62256492.lua) | 1 |

## Script Examples

### Elemental HERO Sunrise (`22908820`)

Source: [Scripts/c22908820.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c22908820.lua)

```lua
function c22908820.val(e,c)
	local g=Duel.GetMatchingGroup(c22908820.atkfilter,e:GetHandlerPlayer(),LOCATION_MZONE,0,nil)
	return aux.GetAttributeCount(g)*200
end
function c22908820.descon(e,tp,eg,ep,ev,re,r,rp)
```

### Possessed Partnerships (`65046521`)

Source: [Scripts/c65046521.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c65046521.lua)

```lua
	local mg=Duel.GetMatchingGroup(Card.IsFaceup,tp,LOCATION_MZONE,0,nil)
	local g=Duel.GetMatchingGroup(Card.IsFaceup,tp,LOCATION_ONFIELD,LOCATION_ONFIELD,aux.ExceptThisCard(e))
	if aux.GetAttributeCount(mg)>=2 and g:GetCount()>0 and Duel.SelectYesNo(tp,aux.Stringid(65046521,1)) then
		Duel.BreakEffect()
		Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_DESTROY)
```

### Charmer Quartet in Bloom (`27519978`)

Source: [Scripts/c27519978.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c27519978.lua)

```lua
function s.atkval(e,c)
	local g=Duel.GetMatchingGroup(s.atkfilter,e:GetHandlerPlayer(),LOCATION_MZONE,LOCATION_MZONE,nil)
	return aux.GetAttributeCount(g)*300
end
function s.spcon(e,tp,eg,ep,ev,re,r,rp)
```
