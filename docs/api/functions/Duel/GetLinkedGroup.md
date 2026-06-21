# Duel.GetLinkedGroup

## Signature

```lua
Duel.GetLinkedGroup(int player, int s_range, int o_range) -> Group
```

## Description

Return the group of linked cards in s_range and o_range zones from player's perspective \[as long as the last two parameters are not 0, they become LOCATION_MZONE\]
NOTE: The original description includes a question mark (?), indicating potential uncertainty or incomplete information; translated as written

## Parameters

- `player` `int`
- `s_range` `int`
- `o_range` `int`

## Returns

- `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4940`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **6** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.GetLinkedGroup`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Borrelcode Dragon | `67288539` | [Scripts/c67288539.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67288539.lua) | 53 |
| Pitknight Filly | `25919316` | [Scripts/c25919316.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25919316.lua) | 43 |
| Crusadia Draco | `54525057` | [Scripts/c54525057.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54525057.lua) | 36 |
| Crusadia Reclusia | `55241609` | [Scripts/c55241609.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55241609.lua) | 34 |
| Voltester | `18585765` | [Scripts/c18585765.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18585765.lua) | 33 |
| Crusadia Krawler | `55838342` | [Scripts/c55838342.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55838342.lua) | 30 |

## Script Examples

### Borrelcode Dragon (`67288539`)

Source: [Scripts/c67288539.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67288539.lua)

```lua
function c67288539.immcon(e)
	local tp=e:GetHandlerPlayer()
	local lg1=Duel.GetLinkedGroup(tp,1,1)
	local lg2=Duel.GetLinkedGroup(1-tp,1,1)
	lg1:Merge(lg2)
```

### Pitknight Filly (`25919316`)

Source: [Scripts/c25919316.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25919316.lua)

```lua
end
function s.atkcon(e,tp,eg,ep,ev,re,r,rp)
	local lg1=Duel.GetLinkedGroup(tp,1,1)
	local lg2=Duel.GetLinkedGroup(1-tp,1,1)
	lg1:Merge(lg2)
```

### Crusadia Draco (`54525057`)

Source: [Scripts/c54525057.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54525057.lua)

```lua
end
function c54525057.thcon(e,tp,eg,ep,ev,re,r,rp)
	local lg1=Duel.GetLinkedGroup(tp,1,1)
	local lg2=Duel.GetLinkedGroup(1-tp,1,1)
	lg1:Merge(lg2)
```
