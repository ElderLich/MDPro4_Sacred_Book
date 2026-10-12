# Duel.SwapSequence

## Signature

```lua
Duel.SwapSequence(Card c1, Card c2) -> void
```

## Description

Swaps the Monster Zone sequences of c1 and c2 when both are controlled by the same player, both are affected by the current reason effect, and both are in the Monster Zone.
The core raises move events for the swapped cards when the swap occurs.

## Parameters

- `c1` `Card`
- `c2` `Card`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4885`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **7** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.SwapSequence) with `Duel.SwapSequence`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Arktos XII - Chronochasm Vaylantz | `50687050` | [Scripts/c50687050.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c50687050.lua) | 1 |
| Elfnote Tinia | `59581480` | [Scripts/c59581480.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c59581480.lua) | 1 |
| Elfnote Lucina | `13597785` | [Scripts/c13597785.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c13597785.lua) | 1 |
| Elfnote Fortuna | `85976588` | [Scripts/c85976588.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c85976588.lua) | 1 |
| Appliancer Dryer Drake | `3507053` | [Scripts/c3507053.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c3507053.lua) | 1 |
| World Legacy's Nightmare | `25163979` | [Scripts/c25163979.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c25163979.lua) | 1 |
| Castle Link | `22198672` | [Scripts/c22198672.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c22198672.lua) | 1 |

## Script Examples

### Arktos XII - Chronochasm Vaylantz (`50687050`)

Source: [Scripts/c50687050.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c50687050.lua)

```lua
		local tc1=sg:GetFirst()
		local tc2=sg:GetNext()
		Duel.SwapSequence(tc1,tc2)
	end
end
```

### Elfnote Tinia (`59581480`)

Source: [Scripts/c59581480.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c59581480.lua)

```lua
	if g:GetCount()==1 then
		local tc=g:GetFirst()
		Duel.SwapSequence(c,tc)
		if c:GetSequence()==cs then return end
		if Duel.IsExistingMatchingCard(Card.IsAbleToRemove,tp,0,LOCATION_HAND,1,nil)
```

### Elfnote Lucina (`13597785`)

Source: [Scripts/c13597785.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c13597785.lua)

```lua
	if g:GetCount()==1 then
		local tc=g:GetFirst()
		Duel.SwapSequence(c,tc)
		if c:GetSequence()==cs then return end
		if Duel.IsExistingMatchingCard(s.rthfilter,tp,0,LOCATION_MZONE,1,nil)
```
