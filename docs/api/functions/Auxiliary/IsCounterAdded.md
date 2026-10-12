# Auxiliary.IsCounterAdded

## Signature

```lua
Auxiliary.IsCounterAdded(Card c, int counter) -> bool
```

## Description

Returns true if counter is registered in c.counter_add_list.

## Parameters

- `c` `Card`
- `counter` `int`

## Returns

- `bool` - true if counter is registered on c.

## Source

- `Utilities/utility.lua:574`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **2** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.IsCounterAdded) with `Auxiliary.IsCounterAdded`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Battle Shogun of the Six Samurai | `74752631` | [Scripts/c74752631.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c74752631.lua) | 1 |
| Cosmic Slicer Zer'oll | `1487805` | [Scripts/c1487805.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c1487805.lua) | 1 |

## Script Examples

### Battle Shogun of the Six Samurai (`74752631`)

Source: [Scripts/c74752631.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c74752631.lua)

```lua
end
function c74752631.thfilter(c)
	return aux.IsCounterAdded(c,0x3) and c:IsAbleToHand()
end
function c74752631.thtg(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Cosmic Slicer Zer'oll (`1487805`)

Source: [Scripts/c1487805.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c1487805.lua)

```lua
end
function c1487805.thfilter(c)
	return aux.IsCounterAdded(c,0x100e) and c:IsAbleToHand()
end
function c1487805.thtg(e,tp,eg,ep,ev,re,r,rp,chk)
```
