# Duel.IsPlayerCanSendtoGrave

## Signature

```lua
Duel.IsPlayerCanSendtoGrave(int player, [Card c]) -> bool
```

## Description

Checks whether player can send c to the Graveyard.

## Parameters

- `player` `int`
- `c` `Card` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5057`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **3** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.IsPlayerCanSendtoGrave`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Evil★Twins Ki-sikil &amp; Lil-la | `62098216` | [Scripts/c62098216.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62098216.lua) | 41 |
| Dogmatikamatrix | `35569555` | [Scripts/c35569555.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35569555.lua) | 35 |
| Destructive Daruma Karma Cannon | `30748475` | [Scripts/c30748475.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30748475.lua) | 20 |

## Script Examples

### Evil★Twins Ki-sikil & Lil-la (`62098216`)

Source: [Scripts/c62098216.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62098216.lua)

```lua
	local g=Duel.GetFieldGroup(tp,0,LOCATION_ONFIELD)
	local ct=g:GetCount()-2
	if chk==0 then return Duel.IsPlayerCanSendtoGrave(1-tp) and ct>0 and g:IsExists(Card.IsAbleToGrave,1,nil,1-tp,nil) end
	Duel.SetOperationInfo(0,CATEGORY_TOGRAVE,g,ct,0,0)
end
```

### Dogmatikamatrix (`35569555`)

Source: [Scripts/c35569555.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35569555.lua)

```lua
		return c:IsType(TYPE_MONSTER) and c:IsAbleToGrave()
	else
		return Duel.IsPlayerCanSendtoGrave(tp,c)
	end
end
```

### Destructive Daruma Karma Cannon (`30748475`)

Source: [Scripts/c30748475.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30748475.lua)

```lua
	local tg=Duel.GetMatchingGroup(Card.IsFaceup,tp,LOCATION_MZONE,LOCATION_MZONE,nil)
	for p=0,1 do
		if not Duel.IsPlayerCanSendtoGrave(p) then tg:Remove(Card.IsControler,nil,p) end
	end
	if #tg>0 then
```
