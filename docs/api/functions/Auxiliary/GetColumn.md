# Auxiliary.GetColumn

## Signature

```lua
Auxiliary.GetColumn(Card c, [int p]) -> int
```

## Description

Return the column sequence number of card c from player's perspective, excluding the Field Zone; from left to right, columns are 0-4

## Parameters

- `c` `Card`
- `p` `int` optional - default: 0

## Returns

- `int`

## Source

- `Utilities/utility.lua:702`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **4** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.GetColumn`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Infinite Impermanence | `10045474` | [Scripts/c10045474.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10045474.lua) | 41 |
| Red Hared Hasty Horse | `19636995` | [Scripts/c19636995.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c19636995.lua) | 31 |
| Broken Line | `88086137` | [Scripts/c88086137.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88086137.lua) | 19 |
| Blasting Fuse | `99788587` | [Scripts/c99788587.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c99788587.lua) | 19 |

## Script Examples

### Infinite Impermanence (`10045474`)

Source: [Scripts/c10045474.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10045474.lua)

```lua
	local seq,fid=e:GetLabel()
	local tp=e:GetHandlerPlayer()
	return c:IsType(TYPE_SPELL+TYPE_TRAP) and aux.GetColumn(c,tp)==seq and c:GetFieldID()~=fid
end
function c10045474.disop(e,tp,eg,ep,ev,re,r,rp)
```

### Red Hared Hasty Horse (`19636995`)

Source: [Scripts/c19636995.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c19636995.lua)

```lua
end
function c19636995.desfilter(c,col)
	return col==aux.GetColumn(c)
end
function c19636995.descon(e,tp,eg,ep,ev,re,r,rp)
```

### Broken Line (`88086137`)

Source: [Scripts/c88086137.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88086137.lua)

```lua
	end
	if p==1-tp then col=4-col end
	return aux.GetColumn(c,tp)==col	and (re:IsActiveType(TYPE_MONSTER) or re:IsHasType(EFFECT_TYPE_ACTIVATE))
		and Duel.IsChainNegatable(ev)
end
```
