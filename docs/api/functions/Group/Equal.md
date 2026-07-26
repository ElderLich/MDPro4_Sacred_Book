# Group.Equal

## Signature

```lua
Group.Equal(Group g1, Group g2) -> bool
```

## Description

Checks whether g1 and g2 contain exactly the same cards in the same internal order.

## Parameters

- `g1` `Group`
- `g2` `Group`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libgroup.cpp:931`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Group.Equal`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Pole Position | `73578229` | [Scripts/c73578229.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c73578229.lua) | 1 |

## Script Examples

### Pole Position (`73578229`)

Source: [Scripts/c73578229.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c73578229.lua)

```lua
	if g:GetCount()>0 then
		local ag=g:GetMaxGroup(Card.GetAttack)
		if ag:Equal(preg) then return end
		preg:Clear()
		preg:Merge(ag)
```
