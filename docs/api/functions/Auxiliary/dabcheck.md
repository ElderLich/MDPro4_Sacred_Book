# Auxiliary.dabcheck

## Signature

```lua
Auxiliary.dabcheck(Group g) -> void
```

## Description

Returns true if every card in g has a different Attribute.

## Parameters

- `g` `Group`

## Source

- `Utilities/utility.lua:1145`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **14** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.dabcheck) with `Auxiliary.dabcheck`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Spellbook of the Grand Circle](/examples/cards/11911336) | `11911336` | [Scripts/c11911336.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c11911336.lua) | 1 |
| Arms of Genex Return Zero | `61775475` | [Scripts/c61775475.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c61775475.lua) | 1 |
| Nebulus, Dragon Ruler of Mishaps | `94655777` | [Scripts/c94655777.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c94655777.lua) | 2 |
| Hyperinvoked Aeon | `33166263` | [Scripts/c33166263.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c33166263.lua) | 2 |
| Vanquish Soul Caesar Valius | `91073013` | [Scripts/c91073013.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c91073013.lua) | 2 |
| Duality | `39973386` | [Scripts/c39973386.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c39973386.lua) | 2 |
| Number 104: Masquerade Vain | `16908882` | [Scripts/c16908882.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c16908882.lua) | 2 |
| Witchcrafter Madame Rilliona | `33475154` | [Scripts/c33475154.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c33475154.lua) | 1 |
| Here There Be Dragons | `4575541` | [Scripts/c4575541.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c4575541.lua) | 1 |
| Spiritual Power Recovery Potion | `61082944` | [Scripts/c61082944.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c61082944.lua) | 1 |
| Vanquish Soul Snow Devil | `60883493` | [Scripts/c60883493.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c60883493.lua) | 1 |
| Mental Tuner | `30291086` | [Scripts/c30291086.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c30291086.lua) | 2 |
| Simorgh Onslaught | `28617139` | [Scripts/c28617139.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c28617139.lua) | 1 |
| Super Soldier Synthesis | `45948430` | [Scripts/c45948430.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c45948430.lua) | 1 |

## Script Examples

### Spellbook of the Grand Circle (`11911336`)

Source: [Scripts/c11911336.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c11911336.lua)

```lua
	if g:GetClassCount(Card.GetAttribute)<4 then return end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_ATOHAND)
	local sg=g:SelectSubGroup(tp,aux.dabcheck,false,4,4)
	if Duel.SendtoHand(sg,nil,REASON_EFFECT)>0 then
		Duel.ConfirmCards(1-tp,sg)
```

### Arms of Genex Return Zero (`61775475`)

Source: [Scripts/c61775475.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c61775475.lua)

```lua
	local g=Duel.GetMatchingGroup(s.tdfilter,tp,LOCATION_GRAVE+LOCATION_REMOVED,0,nil)
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_TODECK)
	local sg=g:SelectSubGroup(tp,aux.dabcheck,false,1,6)
	Duel.SetTargetCard(sg)
	Duel.SetOperationInfo(0,CATEGORY_TODECK,sg,sg:GetCount(),0,0)
```

### Nebulus, Dragon Ruler of Mishaps (`94655777`)

Source: [Scripts/c94655777.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c94655777.lua)

```lua
	if chk==0 then return not Duel.IsPlayerAffectedByEffect(tp,59822133)
		and Duel.GetLocationCount(tp,LOCATION_MZONE)>1
		and g:CheckSubGroup(aux.dabcheck,2,2) end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SPSUMMON)
	local g1=g:SelectSubGroup(tp,aux.dabcheck,false,2,2)
```
