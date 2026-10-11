# Auxiliary.GetColumn

## Signature

```lua
Auxiliary.GetColumn(Card c, [int p]) -> int
```

## Description

Returns c's column index from player p's viewpoint, or NULL_VALUE when c has no field column.
The local helper maps ordinary Monster Zones and Spell & Trap Zones to columns 0-4; Extra Monster Zone sequences 5 and 6 map to columns 1 and 3.

## Parameters

- `c` `Card` - Card whose field column is checked.
- `p` `int` optional - Viewpoint player. Defaults to 0.

## Returns

- `int` - Column index from p's viewpoint, or NULL_VALUE if c has no field column.

## Source

- `Utilities/utility.lua:705`

## Guided Examples

Learn how to use this function in context:

- [Field Zones And Sequences](/learn/field-zones-and-sequences)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **4** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.GetColumn) with `Auxiliary.GetColumn`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Infinite Impermanence | `10045474` | [Scripts/c10045474.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10045474.lua) | 1 |
| Red Hared Hasty Horse | `19636995` | [Scripts/c19636995.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c19636995.lua) | 2 |
| Broken Line | `88086137` | [Scripts/c88086137.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88086137.lua) | 1 |
| Blasting Fuse | `99788587` | [Scripts/c99788587.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c99788587.lua) | 2 |

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
