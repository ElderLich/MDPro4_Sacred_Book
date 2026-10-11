# Card.GetMutualLinkedGroup

## Signature

```lua
Card.GetMutualLinkedGroup(Card c) -> Group
```

## Description

Returns the Group of cards mutually linked with c.

## Parameters

- `c` `Card`

## Returns

- `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3473`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **3** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.GetMutualLinkedGroup) with `Card.GetMutualLinkedGroup`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Zero Extra Link | `60162470` | [Scripts/c60162470.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60162470.lua) | 1 |
| V-LAN Hydra | `13536606` | [Scripts/c13536606.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13536606.lua) | 1 |
| Akashic Magician | `28776350` | [Scripts/c28776350.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28776350.lua) | 2 |

## Script Examples

### Zero Extra Link (`60162470`)

Source: [Scripts/c60162470.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60162470.lua)

```lua
	local lg=Duel.GetMatchingGroup(c60162470.lkfilter,tp,LOCATION_MZONE,LOCATION_MZONE,nil)
	for tc in aux.Next(lg) do
		tg:Merge(tc:GetMutualLinkedGroup())
	end
	if chkc then return chkc:IsLocation(LOCATION_MZONE) and chkc:IsControler(tp) and c60162470.filter(chkc,tg) end
```

### V-LAN Hydra (`13536606`)

Source: [Scripts/c13536606.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13536606.lua)

```lua
function c13536606.tktg(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
	local c=e:GetHandler()
	local lg=c:GetMutualLinkedGroup()
	if chkc then return chkc:IsLocation(LOCATION_MZONE) and c13536606.rfilter(chkc,tp,lg) end
	if chk==0 then return Duel.IsExistingTarget(c13536606.rfilter,tp,LOCATION_MZONE,LOCATION_MZONE,1,nil,tp,lg)
```

### Akashic Magician (`28776350`)

Source: [Scripts/c28776350.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28776350.lua)

```lua
	if chk==0 then
		local c=e:GetHandler()
		local lg=c:GetMutualLinkedGroup()
		local ct=lg:GetSum(Card.GetLink)
		if ct<=0 or not Duel.IsPlayerCanDiscardDeck(tp,ct) then return false end
```
